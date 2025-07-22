# 3PL Network Impact Analysis System
*Causal Inference Framework for Supply Chain Intervention Assessment*

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![DoWhy](https://img.shields.io/badge/DoWhy-causal--inference-red.svg)](https://github.com/microsoft/dowhy)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🎯 Project Overview
A comprehensive causal inference system designed to measure the true impact of supply chain interventions on operational performance. The system quantifies the causal effects of the Q2 regional 3PL network deployment and algorithmic carrier selection on shipment costs, delivery times, and customer satisfaction through robust quasi-experimental methods.

📘 For a detailed breakdown of the problem definition, scoping process, stakeholder requirements, and full project methodology see the [Methodology Document](docs/methodology.md)

---

## 📊 Business Impact
- **6% reduction** in per-shipment costs validated through causal analysis  
- **12-hour improvement** in average delivery times  
- **0.8-point increase** in customer satisfaction scores  
- **Statistically validated** intervention effects with 95% confidence intervals  
- Clear **ROI justification** for supply chain investments

---

## 🔧 Technical Stack
- **Languages**: Python 3.8+, SQL, R (optional)  
- **Causal Inference**: DoWhy, CausalImpact  
- **Statistical Libraries**: scipy, statsmodels  
- **Data Processing**: pandas, numpy  
- **ML Libraries**: scikit-learn, XGBoost (for synthetic control)  
- **Visualization**: matplotlib, seaborn, plotly  
- **Workflow Automation**: Python data pipelines  
- **Testing**: pytest  

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
Shipment and logistics data (pre/post intervention)
Customer satisfaction survey data
Regional and temporal identifiers
```

### Installation
```bash
# Clone the repo
git clone https://github.com/username/3pl-impact-analysis.git
cd 3pl-impact-analysis

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run test suite
pytest tests/

# Verify setup
python -c "import src; print('Setup OK')"
```

---

## 🔍 Key Features

### 1. Difference-in-Differences Analysis  
- **Method**: Exploits temporal and regional variation  
- **Assumptions**: Parallel trends validation with event studies  
- **Robustness**: Multiple specification checks and placebo tests  
- **Output**: Treatment effect estimates with confidence intervals

### 2. Synthetic Control Method  
- **Approach**: Constructs artificial counterfactual units  
- **Donor Pool**: Non-treated regions/time periods  
- **Validation**: In-space and in-time placebo tests  
- **Output**: Visual and statistical evidence of intervention impact

### 3. Interrupted Time Series  
- **Framework**: Structural break analysis in time series  
- **Controls**: Seasonal adjustment and trend modeling  
- **Diagnostics**: Residual analysis and autocorrelation tests  
- **Output**: Level and trend change estimates

### 4. Causal Validation Framework  
- **Tools**: DoWhy identification and estimation  
- **Sensitivity**: Robustness to unobserved confounding  
- **Cross-validation**: Multiple estimator comparison  
- **Output**: Causal effect validation and uncertainty quantification

---

## 📈 Results

### Problem Resolution
- Isolated true causal impact of 3PL network changes from confounding factors  
- Quantified intervention effects on all three key business metrics  
- Provided statistical validation for supply chain investment decisions  
- Established framework for future intervention assessments

### Causal Analysis Performance
- **Cost Impact**: 6% reduction (p<0.05, CI: [4.2%, 7.8%])  
- **Delivery Time**: 12-hour improvement (p<0.01, CI: [9.5h, 14.5h])  
- **Customer Satisfaction**: +0.8 points (p<0.05, CI: [0.5, 1.1])  
- **Robustness**: Consistent effects across all three causal methods

---

## 🗂️ Repository Structure

```
3pl-impact-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── shipments/
│   │   ├── costs/
│   │   └── satisfaction/
│   ├── processed/
│   └── synthetic/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_descriptive_analysis.ipynb
│   ├── 03_difference_in_differences.ipynb
│   ├── 04_synthetic_control.ipynb
│   ├── 05_interrupted_time_series.ipynb
│   ├── 06_causal_validation.ipynb
│   └── 07_results_synthesis.ipynb
├── src/
│   ├── data/
│   │   ├── loader.py
│   │   ├── preprocessor.py
│   │   └── validator.py
│   ├── causal/
│   │   ├── diff_in_diff.py
│   │   ├── synthetic_control.py
│   │   ├── time_series.py
│   │   └── validation.py
│   ├── analysis/
│   │   ├── descriptive.py
│   │   ├── diagnostics.py
│   │   └── robustness.py
│   ├── visualization/
│   │   ├── plotting.py
│   │   └── reporting.py
│   └── utils/
│       ├── config.py
│       └── helpers.py
├── tests/
│   ├── test_causal_methods.py
│   ├── test_data_processing.py
│   ├── test_validation.py
│   └── test_utils.py
├── results/
│   ├── figures/
│   ├── tables/
│   ├── models/
│   └── reports/
└── docs/
    ├── methodology.md
    ├── data_dictionary.md
    ├── causal_assumptions.md
    └── causal_DAG.md
```

---

## 🔬 Methodology
### Causal Inference DAG
📘 Expand to view causal DAG [causal_DAG](docs/causal_DAG.md)

### Causal Inference Pipeline
1. **Data Preparation**: Clean and structure pre/post intervention data  
2. **Exploratory Analysis**: Identify trends and potential confounders  
3. **Assumption Testing**: Validate parallel trends and other identifying assumptions  
4. **Multiple Estimation**: Apply DiD, synthetic control, and ITS methods  
5. **Robustness Checks**: Placebo tests, sensitivity analysis, specification tests  
6. **Effect Synthesis**: Combine results across methods with uncertainty quantification

### Approach to Causal Identification
- **Quasi-Experimental Design**: Leverage natural variation in treatment timing/geography  
- **Multiple Methods**: Cross-validate results across complementary approaches  
- **Assumption Validation**: Rigorous testing of identifying assumptions  
- **Sensitivity Analysis**: Assess robustness to potential violations

---

## 📓 Usage Examples

### Run Difference-in-Differences Analysis
```python
from src.causal.diff_in_diff import DifferenceInDifferences
from src.data.loader import load_shipment_data

# Load data
df = load_shipment_data('data/processed/shipments_panel.csv')

# Run DiD analysis
did_model = DifferenceInDifferences(
    outcome='cost_per_shipment',
    treatment='post_3pl_rollout',
    unit_id='region_id',
    time_id='month'
)
results = did_model.fit(df)
print(results.summary())
```

### Synthetic Control Method
```python
from src.causal.synthetic_control import SyntheticControl

# Initialize synthetic control
sc_model = SyntheticControl(
    outcome='delivery_time_hours',
    treated_unit='region_A',
    intervention_time='2025-04-01'
)
sc_results = sc_model.fit(df)
sc_model.plot_results()
```

### Comprehensive Causal Validation
```python
from src.causal.validation import CausalValidator

validator = CausalValidator(methods=['did', 'synthetic_control', 'its'])
validation_results = validator.run_all_methods(df)
validator.generate_report('results/reports/causal_validation.html')
```

---

## 🧪 Testing
```bash
# Run all tests
pytest tests/ -v

# Test causal methods specifically
pytest tests/test_causal_methods.py -v

# Check coverage
pytest --cov=src --cov-report=html
```

---

## 📊 Data Requirements
- **Shipment Records**: Cost, delivery times, timestamps, regional identifiers  
- **Treatment Assignment**: 3PL rollout dates by region/facility  
- **Customer Satisfaction**: Survey responses linked to shipment periods  
- **Control Variables**: Seasonal indicators, regional characteristics, volume metrics

*Note: Synthetic data samples available in `data/synthetic/` for testing.*

---

## 🔄 Maintenance & Monitoring
- **Quarterly Updates**: Refresh analysis with new data  
- **Assumption Monitoring**: Validate parallel trends as new data arrives  
- **Effect Stability**: Monitor treatment effect consistency over time  
- **Method Validation**: Periodic comparison of causal estimation approaches

---

## 📋 Reporting & Interpretation

### Key Outputs
- **Executive Summary**: High-level findings with business implications  
- **Technical Report**: Detailed methodology and statistical results  
- **Visual Dashboard**: Interactive plots showing treatment effects over time  
- **Robustness Documentation**: Evidence for causal claim validity

### Statistical Interpretation
- **Effect Sizes**: Practical significance beyond statistical significance  
- **Confidence Intervals**: Uncertainty quantification for business planning  
- **Sensitivity Bounds**: Robustness to potential unobserved confounding  

---

## 🤝 Contributing
1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/causal-method-xyz`)  
3. Add tests for new causal methods or validation techniques  
4. Commit changes (`git commit -m 'Add causal method xyz'`)  
5. Push your branch (`git push origin feature/causal-method-xyz`)  
6. Open a Pull Request with clear description of methodology

---

## 📚 References & Further Reading
- Angrist, J.D. & Pischke, J.S. (2009). *Mostly Harmless Econometrics*
- Imbens, G.W. & Rubin, D.B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*
- Abadie, A. (2021). "Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects"

---

## 🏷️ Tags
`causal-inference` `difference-in-differences` `synthetic-control` `supply-chain-analytics` `quasi-experimental` `python` `econometrics` `dowhy` `impact-evaluation`
