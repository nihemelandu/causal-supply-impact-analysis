# Logistics Causal Inference Data Dictionary

## Project Overview
**Purpose**: Assess the causal impact of transitioning from in-house logistics to a third-party logistics (3PL) network with algorithmic carrier selection on cost, delivery time, and customer satisfaction.

**Analysis Period**: January 1, 2024 - June 30, 2024  
**Treatment Date**: April 1, 2024 (Q2 start)  
**Unit of Analysis**: Individual shipments  
**Sample Size**: ~9,000 shipments

---

## Variable Definitions

### Core Variables

| Variable | Type | Description | Values/Range | Role |
|----------|------|-------------|--------------|------|
| `shipment_id` | String | Unique identifier for each shipment | SHIP_XXXXXX | Unit ID |
| `date` | Date | Date when shipment was processed | 2024-01-01 to 2024-06-30 | Time |
| `treatment_period` | Boolean | Indicates if shipment occurred after treatment | 0 = Pre-treatment<br>1 = Post-treatment | Treatment Period |
| `logistics_system` | Boolean | Type of logistics system used | 0 = In-house<br>1 = 3PL + algorithmic | Treatment Variable |

### Outcome Variables

| Variable | Type | Description | Values/Range | Notes |
|----------|------|-------------|--------------|-------|
| `cost_per_shipment` | Decimal(10,2) | Total cost to ship one package | $5.00 - $50.00 | Primary outcome |
| `delivery_time_hours` | Integer | Hours from shipment to delivery | 12 - 120 hours | Primary outcome |
| `customer_satisfaction` | Decimal(3,1) | Customer satisfaction rating | 1.0 - 10.0 scale | Primary outcome |

### Shipment Characteristics (Confounders)

| Variable | Type | Description | Values/Range | Impact |
|----------|------|-------------|--------------|--------|
| `package_weight` | Decimal(8,2) | Weight of package in pounds | 0.1 - 50.0 lbs | Affects cost & delivery time |
| `package_size` | Decimal(10,3) | Volume of package in cubic feet | 0.1 - 20.0 ft³ | Affects cost & delivery time |
| `service_level` | String | Shipping service tier | 'standard', 'express' | Affects all outcomes |
| `destination_distance` | Integer | Distance to destination in miles | 10 - 2,000 miles | Major cost & time driver |
| `order_value` | Decimal(10,2) | Total value of order | $10.00 - $1,000.00 | Influences service priority |

### Temporal Controls (Confounders)

| Variable | Type | Description | Values/Range | Impact |
|----------|------|-------------|--------------|--------|
| `day_of_week` | Integer | Day of week (Monday=1) | 1-7 | Weekend delays |
| `month` | Integer | Month of year | 1-12 | Seasonal patterns |
| `is_holiday` | Boolean | Holiday indicator | 0 = Regular day<br>1 = Holiday | Service disruptions |
| `is_peak_season` | Boolean | Peak shipping season | 0 = Regular<br>1 = Peak (Q4/holidays) | Capacity constraints |

### Business Context (Confounders)

| Variable | Type | Description | Values/Range | Impact |
|----------|------|-------------|--------------|--------|
| `customer_type` | String | Type of customer | 'B2B', 'B2C' | Service expectations |
| `product_category` | String | Category of shipped product | 'Electronics', 'Clothing', 'Books', 'Home', 'Sports' | Handling requirements |
| `monthly_shipment_volume` | Integer | Total shipments in that month | 1,200 - 2,500 | **Key confounder**: Volume drives treatment decision and economies of scale |
| `business_growth_rate` | Decimal(5,2) | Monthly business growth rate | 0.03 - 0.17 (3%-17%) | **Key confounder**: Growth triggers treatment |

### External Factors (Confounders)

| Variable | Type | Description | Values/Range | Impact |
|----------|------|-------------|--------------|--------|
| `fuel_price` | Decimal(6,3) | Fuel price per gallon on ship date | $2.00 - $5.00 | Affects shipping costs |
| `weather_disruptions` | Boolean | Weather-related delays | 0 = Clear<br>1 = Weather issues | Delivery delays |

---

## Variable Roles in Causal Analysis

### 🎯 **Treatment Variables**
- `logistics_system` - Main treatment of interest

### 📊 **Outcome Variables** 
- `cost_per_shipment` - Expected decrease of $3.00
- `delivery_time_hours` - Expected decrease of 12 hours  
- `customer_satisfaction` - Expected increase of 0.8 points

### ⚠️ **Critical Confounders** (Must Control For)
- `monthly_shipment_volume` - Creates backdoor path: Treatment ← Volume → Outcomes
- `business_growth_rate` - Creates backdoor path: Treatment ← Growth → Volume → Outcomes  
- `is_peak_season` - Creates backdoor path: Treatment ← Peak Season → Outcomes

### 🎛️ **Control Variables** (For Precision)
- Shipment characteristics (weight, size, distance, service level)
- Temporal controls (day of week, holidays)
- External factors (fuel price, weather)
- Business context (customer type, product category)

### 🚫 **Variables to Avoid** (Colliders)
- `delivery_performance_rating` - Caused by both treatment and outcomes
- `customer_complaint_filed` - Result of treatment and outcome performance
- `management_attention_flag` - Consequence of treatment and outcomes

---

## Data Quality Notes

### Missing Values
- All core variables are required (no missing values)
- Outcome variables may have rare missing values for failed deliveries
- External factors interpolated for weekends/holidays

### Data Validation Rules
- `cost_per_shipment` > 0
- `delivery_time_hours` ≥ 12 (minimum processing time)
- `customer_satisfaction` between 1.0 and 10.0
- `treatment_period` and `logistics_system` must be consistent

### Known Limitations
- Customer satisfaction based on post-delivery surveys (response bias possible)
- Weather disruptions simplified to binary indicator
- Fuel prices averaged daily (not shipment-specific)

---

## Causal Identification Strategy

### Methods Used
1. **Interrupted Time Series (ITS)** - Exploits sharp treatment cutoff at April 1, 2024
2. **Difference-in-Differences (DiD)** - Uses synthetic comparison groups
3. **Synthetic Control** - Creates counterfactual using pre-treatment patterns

### Key Assumptions
1. **No unmeasured confounders** - All backdoor paths controlled
2. **Sharp treatment cutoff** - No gradual rollout or anticipation effects  
3. **Stable unit treatment** - No spillover between shipments
4. **Parallel trends** - Pre-treatment trends would continue absent treatment

### Expected Treatment Effects (True Values)
- Cost reduction: $3.00 per shipment (15% decrease)
- Delivery time improvement: 12 hours (20% decrease)
- Satisfaction increase: 0.8 points (11% improvement)

---

## Usage Guidelines

### For Analysis
1. Always control for critical confounders: `monthly_shipment_volume`, `business_growth_rate`, `is_peak_season`
2. Include shipment characteristics for precision
3. Never control for collider variables
4. Use robust standard errors clustered by date

### For Interpretation
- Treatment effects represent the causal impact of switching to 3PL + algorithmic selection
- Control for confounders when estimating treatment effects
- Raw pre/post comparisons will be biased upward due to business growth confounding

---

**Data Dictionary Version**: 1.0  
**Last Updated**: July 24, 2025  
**Contact**: Data Science Team
