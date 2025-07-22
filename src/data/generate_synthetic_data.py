# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 06:45:40 2025

@author: ngozi


Goal: Realistic synthetic data for your shipments, customers, 
      and carriers tables, with Q2 rollout dynamics and plausible distributions.

Purpose: To prototype and test your causal analysis pipeline before using real 
         production data. The confounding patterns implemented are realistic 
         and will properly test whether the causal analysis can recover 
         the true treatment effects.
         
✅ 1. Define Business Logic & Assumptions
This ensures the synthetic data reflects real-world patterns:
"""

import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import numpy as np

fake = Faker()
random.seed(42)
np.random.seed(42)

# Parameters
NUM_CUSTOMERS = 120
NUM_CARRIERS = 15
NUM_SHIPMENTS = 800

# Generate customers with quality characteristics that create confounding
customers_data = []
for i in range(1, NUM_CUSTOMERS + 1):
    # Customer quality score affects both treatment access and baseline outcomes
    customer_quality = np.random.beta(2, 5)  # Most customers average, some high-value
    
    # High-value customers are more likely to be enterprise and in certain regions
    if customer_quality > 0.8:
        segment = 'enterprise'
        region_probs = [0.4, 0.3, 0.2, 0.1]  # Concentrated in East/West
    elif customer_quality > 0.5:
        segment = 'repeat'  
        region_probs = [0.3, 0.3, 0.2, 0.2]
    else:
        segment = 'new'
        region_probs = [0.25, 0.25, 0.25, 0.25]  # Evenly distributed
    
    customers_data.append({
        "customer_id": f"CUST_{i:04d}",
        "customer_name": fake.company(),
        "customer_region": np.random.choice(["East", "West", "North", "South"], p=region_probs),
        "customer_segment": segment,
        "customer_quality_score": customer_quality,  # Hidden confounder
        "signup_date": fake.date_between(start_date='-2y', end_date='today')
    })

customers = pd.DataFrame(customers_data)
customers.to_csv("customers.csv", index=False)

# Generate carriers with varying capabilities
carriers_data = []
for i in range(1, NUM_CARRIERS + 1):
    # Carrier capability affects both selection probability and outcomes
    carrier_capability = np.random.beta(3, 2)  # Most carriers decent, some excellent
    
    carriers_data.append({
        "carrier_id": f"CARR_{i:03d}",
        "carrier_name": fake.company(),
        "carrier_region": random.choice(["East", "West", "North", "South"]),
        "is_3pl_partner": i <= 8,  # First 8 are 3PL partners
        "service_level": random.choice(["standard", "express", "overnight"]),
        "carrier_capability_score": carrier_capability,  # Hidden confounder
    })

carriers = pd.DataFrame(carriers_data)
carriers.to_csv("carriers.csv", index=False)

def get_treatment_probability(shipment_date, customer, rollout_date):
    """
    Realistic treatment assignment with confounding:
    - High-value customers get priority access
    - Gradual rollout over time
    - Some pre-rollout leakage for VIP customers
    """
    days_since_rollout = (shipment_date - rollout_date).days
    
    # Base probability depends on customer quality (CONFOUNDING!)
    if customer['customer_segment'] == 'enterprise':
        base_prob = 0.8
    elif customer['customer_segment'] == 'repeat':
        base_prob = 0.6  
    else:
        base_prob = 0.4
    
    if days_since_rollout < 0:
        # Pre-rollout: VIP early access creates confounding
        early_access_prob = 0.15 if customer['customer_quality_score'] > 0.7 else 0.02
        return early_access_prob
    else:
        # Post-rollout: gradual ramp-up, higher for better customers
        ramp_progress = min(days_since_rollout / 90, 1.0)  # 90-day full rollout
        return base_prob * ramp_progress

def select_carrier(customer, is_algorithmic, carriers_df):
    """
    Carrier selection with realistic bias:
    - Algorithmic selection prefers 3PL but also considers capability
    - Manual selection has quality bias (good customers get good carriers)
    """
    if is_algorithmic:
        # Algorithmic: prefers 3PL partners with high capability
        eligible_3pl = carriers_df[carriers_df['is_3pl_partner'] == True]
        if len(eligible_3pl) > 0 and random.random() < 0.75:
            # Weight by capability within 3PL partners
            weights = eligible_3pl['carrier_capability_score'].values
            weights = weights / weights.sum()
            return eligible_3pl.sample(1, weights=weights).iloc[0]
    
    # Manual selection: biased toward good carriers for good customers (CONFOUNDING!)
    if customer['customer_quality_score'] > 0.6:
        # High-value customers get better carriers even in manual selection
        weights = carriers_df['carrier_capability_score'].values ** 2  # Square to amplify differences
    else:
        weights = np.ones(len(carriers_df))  # Random for regular customers
    
    weights = weights / weights.sum()
    return carriers_df.sample(1, weights=weights).iloc[0]

def calculate_performance_metrics(carrier, customer, shipment_date, is_algorithmic, start_date):
    """
    Performance with realistic confounding patterns:
    - Customer and carrier quality affect baseline performance
    - Time trends independent of treatment
    - Treatment effect exists but is confounded
    """
    
    # Time trend: general operational improvements (independent of treatment)
    days_from_start = (shipment_date - start_date).days
    time_trend_factor = 1 - (days_from_start * 0.0008)  # 0.08% daily improvement
    
    # Baseline performance depends on carrier and customer quality (CONFOUNDING!)
    carrier_effect = 1 - (carrier['carrier_capability_score'] * 0.2)  # Up to 20% improvement
    customer_effect = 1 - (customer['customer_quality_score'] * 0.15)  # Up to 15% improvement
    
    # Service level base effects
    service_multipliers = {
        'standard': {'time': 1.0, 'cost': 1.0},
        'express': {'time': 0.7, 'cost': 1.4}, 
        'overnight': {'time': 0.4, 'cost': 2.2}
    }
    service_mult = service_multipliers.get(carrier['service_level'], service_multipliers['standard'])
    
    # TRUE TREATMENT EFFECT (what we want to recover)
    treatment_effect = {'time': 0.85, 'cost': 0.88, 'satisfaction_boost': 0.4}  # 15% time, 12% cost, +0.4 satisfaction
    
    if is_algorithmic and carrier['is_3pl_partner']:
        time_factor = treatment_effect['time']
        cost_factor = treatment_effect['cost'] 
        satisfaction_boost = treatment_effect['satisfaction_boost']
    else:
        time_factor = 1.0
        cost_factor = 1.0
        satisfaction_boost = 0.0
    
    # Calculate delivery time
    base_delivery_time = 48  # hours
    delivery_time = (base_delivery_time * 
                    service_mult['time'] * 
                    carrier_effect * 
                    customer_effect * 
                    time_trend_factor * 
                    time_factor *
                    np.random.normal(1.0, 0.15))
    delivery_time = max(6, delivery_time)
    
    # Calculate cost  
    base_cost = 25  # USD
    cost = (base_cost * 
           service_mult['cost'] * 
           (2 - carrier_effect) *  # Higher capability = higher cost (realistic!)
           cost_factor *
           np.random.normal(1.0, 0.2))
    cost = max(5, cost)
    
    # On-time delivery probability
    on_time_base = 0.7
    on_time_base += carrier['carrier_capability_score'] * 0.2  # Better carriers more reliable
    on_time_base += customer['customer_quality_score'] * 0.1   # Better customers get priority
    if is_algorithmic and carrier['is_3pl_partner']:
        on_time_base += 0.15  # Treatment effect
    
    delivered_on_time = random.random() < min(on_time_base, 0.95)
    
    # Customer satisfaction
    base_satisfaction = 2.8
    base_satisfaction += carrier['carrier_capability_score'] * 0.8
    base_satisfaction += customer['customer_quality_score'] * 0.5
    base_satisfaction += satisfaction_boost  # Treatment effect
    if delivered_on_time:
        base_satisfaction += 0.6
    if customer['customer_segment'] == 'enterprise':
        base_satisfaction -= 0.2  # Higher expectations
    
    satisfaction = np.clip(np.random.normal(base_satisfaction, 0.7), 1, 5)
    
    return {
        'delivery_time_hours': round(delivery_time, 1),
        'cost_usd': round(cost, 2),
        'delivered_on_time': delivered_on_time,
        'customer_satisfaction': round(satisfaction, 1)
    }

# Generate shipments with realistic confounding
shipment_rows = []
start_date = datetime(2024, 1, 1)
rollout_date = datetime(2024, 4, 1)

for i in range(1, NUM_SHIPMENTS + 1):
    # Select customer (this matters for confounding!)
    customer = customers.sample(1).iloc[0]
    
    # Generate shipment date with business seasonality
    base_day = random.randint(0, 180)  # Jan–Jun 2024
    
    # Business seasonality: higher volume in Q1 (Jan-Mar) and Q2 (Apr-Jun)
    if base_day < 90:  # Q1: higher volume
        seasonal_adjustment = random.randint(-10, 5)
    else:  # Q2: steady volume  
        seasonal_adjustment = random.randint(-5, 10)
    
    final_day = max(0, min(179, base_day + seasonal_adjustment))
    shipment_date = start_date + timedelta(days=final_day)
    
    # Avoid weekends for business customers
    if (customer['customer_segment'] in ['repeat', 'enterprise'] and 
        shipment_date.weekday() >= 5 and random.random() < 0.7):
        # Move to next Monday
        days_to_add = 7 - shipment_date.weekday()
        shipment_date += timedelta(days=days_to_add)
    
    # Treatment assignment (CONFOUNDED by customer quality!)
    treatment_prob = get_treatment_probability(shipment_date, customer, rollout_date)
    is_algorithmic = random.random() < treatment_prob
    
    # Carrier selection (also confounded!)
    carrier = select_carrier(customer, is_algorithmic, carriers)
    
    # Determine selection method for tracking
    if shipment_date >= rollout_date and is_algorithmic:
        selection_method = 'algorithmic'
    else:
        selection_method = 'manual'
    
    # Calculate metrics (with all confounding patterns)
    metrics = calculate_performance_metrics(carrier, customer, shipment_date, is_algorithmic, start_date)
    
    # Survey response (biased - more responses when problems occur)
    response_prob = 0.25  # Base response rate
    if not metrics['delivered_on_time']:
        response_prob = 0.45  # Higher when delivery issues
    if customer['customer_segment'] == 'enterprise':
        response_prob *= 1.3  # Enterprise customers respond more
    
    has_survey_response = random.random() < response_prob
    
    shipment_rows.append({
        "shipment_id": f"SHIP_{i:05d}",
        "customer_id": customer["customer_id"],
        "carrier_id": carrier["carrier_id"],
        "shipment_date": shipment_date.date(),
        "delivery_time_hours": metrics['delivery_time_hours'],
        "cost_usd": metrics['cost_usd'],
        "delivered_on_time": metrics['delivered_on_time'],
        "carrier_selection_method": selection_method,
        "customer_satisfaction": metrics['customer_satisfaction'] if has_survey_response else None,
        "survey_date": (shipment_date + timedelta(days=random.randint(1, 4))).date() if has_survey_response else None,
        "is_post_rollout": shipment_date >= rollout_date,
        "is_algorithmic_selection": is_algorithmic
    })

shipments = pd.DataFrame(shipment_rows)

#Save to CSV
shipments.to_csv("shipments.csv", index=False)

# Merge with customer and carrier data for analysis
shipments_full = (shipments
                 .merge(customers, on='customer_id')
                 .merge(carriers, on='carrier_id'))

print("=== CONFOUNDING ASSESSMENT ===")
print("\n1. Treatment Assignment Bias:")
treatment_by_segment = (shipments_full.groupby(['customer_segment', 'is_post_rollout'])
                       ['is_algorithmic_selection'].mean().round(3))
print(treatment_by_segment)

print("\n2. Carrier Quality Bias:")
carrier_quality_by_method = (shipments_full.groupby('carrier_selection_method')
                           ['carrier_capability_score'].mean().round(3))
print(carrier_quality_by_method)

print("\n3. Customer Quality Bias:")  
customer_quality_by_treatment = (shipments_full.groupby('is_algorithmic_selection')
                                ['customer_quality_score'].mean().round(3))
print(customer_quality_by_treatment)

print("\n4. Naive vs True Treatment Effects:")
print("(Naive comparison - confounded)")
naive_comparison = (shipments_full.groupby('is_algorithmic_selection')
                   [['delivery_time_hours', 'cost_usd', 'customer_satisfaction']]
                   .mean().round(2))
print(naive_comparison)

print("\n5. Survey Response Bias:")
survey_response_by_performance = (shipments_full.groupby('delivered_on_time')
                                 ['customer_satisfaction'].count())
print(f"Survey responses - On time: {survey_response_by_performance.get(True, 0)}, Late: {survey_response_by_performance.get(False, 0)}")

print(f"\nTotal shipments: {len(shipments)}")
print(f"With algorithmic selection: {shipments['is_algorithmic_selection'].sum()}")
print(f"Survey responses: {shipments['customer_satisfaction'].notna().sum()}")

print("\n=== TRUE TREATMENT PARAMETERS ===")
print("Time improvement: 15% (factor = 0.85)")
print("Cost improvement: 12% (factor = 0.88)") 
print("Satisfaction boost: +0.4 points")
print("\nNote: Naive estimates will be biased due to confounding!")
print("Use causal methods (IV, DiD, Matching) to recover true effects.")