# Problem Definition & Scoping

## 1.1 Original Business Problem Statement

**Stakeholder:** VP of Operations  
**Date:** 07/18/2025  
**Urgency:** High — Critical operational and financial impact

**Original Problem Description:**  
> "In Q2, the company deployed a new regional third-party logistics (3PL) network and introduced algorithmic carrier selection to improve delivery performance and reduce costs. We seek to measure the causal impact of this rollout on cost per shipment, average delivery time, and customer satisfaction."

## 1.2 Problem Decomposition

The problem encompasses multiple interconnected outcomes that need to be analyzed and prioritized:

### A. Cost Efficiency  
- **Core Problem:** High per-shipment costs impacting profitability  
- **Impact:** Operational expenses that can be optimized  
- **Measurable Aspect:** Average cost incurred per shipment before and after intervention

### B. Delivery Performance  
- **Core Problem:** Delivery speed and reliability affect customer experience  
- **Impact:** Timeliness can drive customer satisfaction and retention  
- **Measurable Aspect:** Average delivery time (hours), on-time delivery rate

### C. Customer Satisfaction  
- **Core Problem:** Customer perceptions influenced by delivery experience  
- **Impact:** Satisfaction scores affect repeat business and brand reputation  
- **Measurable Aspect:** Customer satisfaction score (CSAT) or related survey metrics

## 1.3 Problem Prioritization

Based on business impact and data availability:

| Priority | Area                 | Reason                                                       |
|----------|----------------------|--------------------------------------------------------------|
| 1        | Delivery Performance | Key driver of customer satisfaction and operational success  |
| 2        | Cost Efficiency      | Direct impact on operational costs and profit margins        |
| 3        | Customer Satisfaction| Ultimate downstream metric reflecting overall intervention   |

## 1.4 Focused Problem Statement

**Primary Focus:** Quantify the causal impact of the new regional 3PL network and algorithmic carrier selection on shipment costs, delivery times, and customer satisfaction.

**Specific Problem Definition:**  
"Assess whether and to what extent the Q2 rollout of the new 3PL network and routing algorithms caused reductions in average per-shipment costs, improvements in delivery speed, and increases in customer satisfaction scores."

## 1.5 Success Criteria

**Primary Success Metrics:**  
- **Cost Reduction:** Statistically significant reduction in per-shipment cost (target: ≥5%)  
- **Delivery Speed Improvement:** Meaningful reduction in average delivery time (target: ≥10 hours faster)  
- **Customer Satisfaction Increase:** Detectable positive lift in CSAT scores (target: ≥0.5 points increase)

**Secondary Success Metrics:**  
- **Consistency:** Sustained improvements over at least 3 months post-intervention  
- **Statistical Validation:** Robust causal inference results validated with multiple methods  
- **Stakeholder Confidence:** Approval from Operations and Customer Experience teams

## 1.6 Scope Definition

### ✅ In Scope  
- Evaluation of shipments affected by the new 3PL network and algorithmic carrier selection  
- Analysis of shipment cost components as recorded in internal logistics and finance systems  
- Delivery performance measured by timestamped shipping and delivery records  
- Customer satisfaction measured via post-delivery surveys or aggregated CSAT data  

### 🚫 Out of Scope  
- Changes in product pricing or assortment  
- Upstream supplier or vendor operations unrelated to shipping  
- Non-shipment related customer service interactions  
- External market factors not captured in available data (e.g., weather, strikes)

## 1.7 Assumptions & Constraints

**Assumptions:**  
- Accurate and consistent shipment cost and delivery time data before and after Q2  
- Sufficient customer satisfaction data linked to shipment records  
- Intervention rollout timing and affected regions clearly documented  

**Constraints:**  
- Potential confounding factors (seasonality, promotions) may impact outcomes  
- Limited granularity on shipment-level cost breakdowns  
- Adoption timing may vary by geography or customer segment  

## 1.8 Stakeholder Alignment

**Primary Stakeholders:**  
- VP of Operations (Problem owner)  
- Logistics and Supply Chain Managers  
- Customer Experience Team  
- Data Science and Analytics Team  

**Success Validation Process:**  
- Data availability and quality assessment by Week 2  
- Interim findings shared by Week 6  
- Final causal impact report delivered by Week 12  

**Communication Plan:**  
- Weekly progress updates to Operations VP  
- Bi-weekly review meetings with Logistics and Customer Experience leads  

---
## 1.9 Problem Translation to DS/ML Task

### A. Task Classification
**Task Type:** Causal Inference / Treatment Effect Estimation

**Formal Problem Statement:**
- **Treatment Variable (T):** Binary indicator for implementation of new 3PL network + algorithmic carrier selection at time T_intervention
- **Outcome Variables (Y):** 
  - Y₁: Cost per shipment (continuous, USD)
  - Y₂: Delivery time (continuous, hours)  
  - Y₃: Customer satisfaction score (continuous, rating scale)
- **Units:** Individual shipments or aggregated time-region units
- **Time Dimension:** Pre-intervention (Q1 and earlier) vs. Post-intervention (Q2 onwards)

### B. Causal Inference Framework
**Fundamental Causal Question:** What would the outcomes have been in the absence of the intervention?

**Identification Strategy:**
- **Primary Challenge:** Estimating counterfactual outcomes Y₀ᵢ for treated units
- **Confounding Sources:** Seasonality, market conditions, concurrent operational changes, regional heterogeneity
- **Temporal Structure:** Exploit before/after variation with robust time trend modeling

### C. Technical Approach
**Statistical Framework:**
- **Quasi-Experimental Design** rather than pure predictive modeling
- **Multiple Estimator Approach** for robustness and sensitivity analysis:
  1. **Difference-in-Differences (DiD):** Leverage parallel trends assumption across regions/time
  2. **Synthetic Control Method:** Construct artificial counterfactual using donor pool
  3. **Interrupted Time Series (ITS):** Model structural breaks in time series
- **Validation Framework:** Cross-validation using causal inference diagnostics

### D. Key Methodological Distinctions
**Explanatory vs. Predictive Modeling:**
- **Objective:** Unbiased causal effect estimation rather than forecast accuracy
- **Model Selection:** Prioritize interpretability and causal identification over predictive performance
- **Evaluation Metrics:** Statistical significance, effect size, robustness checks vs. RMSE/MAE
- **Assumptions:** Focus on causal assumptions (parallel trends, no spillovers) vs. distributional assumptions

**Treatment of Confounding:**
- **Observed Confounders:** Control for measurable factors (seasonality, regional characteristics)
- **Unobserved Confounders:** Leverage quasi-experimental variation and sensitivity analysis
- **Time-Varying Confounders:** Use flexible time trend modeling and event study designs

### E. Success Criteria Translation
**Statistical Success Metrics:**
- **Effect Size:** Economically meaningful treatment effects (>5% cost reduction, >10-hour delivery improvement)
- **Statistical Significance:** p-values <0.05 with robust standard errors
- **Robustness:** Consistent results across multiple causal methods
- **Assumption Validation:** Pass diagnostic tests for parallel trends and other identifying assumptions

**Model Validation Approach:**
- **Placebo Tests:** Test for effects in pre-treatment periods
- **Sensitivity Analysis:** Assess robustness to unobserved confounding
- **Cross-Method Validation:** Compare results across DiD, synthetic control, and ITS

---

*This section will be updated as new information or constraints arise during the project lifecycle.*
