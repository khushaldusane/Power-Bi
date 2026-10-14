# Telco Customer Churn Analysis
### Customer Churn Prediction & Revenue Risk Analytics | Power BI Dashboard

---

## 📌 Overview

An end-to-end churn analytics project built on the IBM Telco Customer Churn dataset. The project identifies churn drivers through statistical analysis, scores customers by risk tier, and delivers AI-generated retention playbooks — all surfaced in an interactive Power BI dashboard.

---

## 🎯 Business Problem

A telecom company with **7,043 customers** and **$456K/month in MRR** is losing **26.5% of its customers annually**. That translates to **$139K/month in churned revenue** and a further **$140K/month at risk** from high-probability churners still active. This project answers three questions:

1. **Who is churning?** — Statistical profiling of churned vs. retained customers  
2. **Why are they churning?** — Feature-level driver analysis via chi-squared tests and logistic regression  
3. **What should we do?** — Segment-level retention playbooks with estimated revenue impact

---

## 📊 Key Metrics

| Metric | Value |
|---|---|
| Total Customers | 7,043 |
| Churn Rate | 26.5% |
| Total MRR | $456.1K / month |
| Churned MRR | $139.1K / month |
| Expected MRR at Risk | $140.0K / month |

---

## 🔍 Key Findings

### Top Churn Drivers (Categorical — Chi-Squared + Cramér's V)

| Feature | Cramér's V | Highest-Risk Category |
|---|---|---|
| Contract Type | 0.41 | Month-to-month (42.7% churn) |
| Online Security | 0.35 | No security add-on (41.8% churn) |
| Tech Support | 0.34 | No tech support (41.6% churn) |
| Internet Service | 0.32 | Fiber Optic (41.9% churn) |
| Payment Method | 0.30 | Electronic check (45.3% churn) |

**Gender and PhoneService were not statistically significant** (p > 0.05).

### Top Churn Drivers (Logistic Regression — Odds Ratios)

**Increases churn risk:**
- Fiber Optic internet → **3.43x** higher odds of churning
- Streaming Movies (Yes) → **1.65x**
- Multiple Lines (Yes) → **1.51x**
- Paperless Billing (Yes) → **1.49x**
- Electronic Check payment → **1.41x**

**Protective factors (reduces churn risk):**
- No internet service → **0.26x** (74% lower odds)
- Two-year contract → **0.27x** (73% lower odds)
- Longer tenure (standardized) → **0.46x**
- One-year contract → **0.48x**
- Online Security add-on → **0.74x**

### Model Slice Evaluation

| Segment | Test Size | Actual Churn | Predicted | ROC-AUC |
|---|---|---|---|---|
| Month-to-month contracts | 572 | 42.5% | 41.5% | 0.755 |
| Two-year contracts | 256 | 2.0% | 2.8% | 0.802 |
| Fiber Optic customers | 441 | 41.5% | 41.6% | 0.799 |
| Senior Citizens | 161 | 44.1% | 40.0% | 0.796 |
| Non-senior Citizens | 896 | 23.4% | 23.1% | 0.844 |

---

## 🤖 AI-Generated Customer Segments & Retention Playbooks

### Segment A — High-Risk Month-to-Month Broadband ⚠️ CRITICAL
- **Churn Rate:** 44.8% | **Avg ARPU:** $70.42/mo | **Avg Tenure:** 17.1 months
- **Root Cause:** Month-to-month contract exposure + Fiber Optic price sensitivity + Electronic check billing without security/support add-ons
- **Playbook:** (1) Offer $10/mo incentive to convert to 1-year contract + AutoPay; (2) Bundle 6-month complimentary Online Security & Tech Support; (3) Trigger Day-30 onboarding call
- **Expected Annual Savings (25% lift):** $342,846

### Segment B — Loyal Multi-Service Power Users ✅ HIGH-VALUE CORE
- **Churn Rate:** 11.8% | **Avg ARPU:** $86.87/mo | **Avg Tenure:** 57.4 months
- **Root Cause:** Protected by 1–2 year contracts and deep ecosystem lock-in (avg 4.1 add-on services)
- **Playbook:** (1) Enroll in VIP Loyalty Tier; (2) Automated contract renewal 45 days before expiry; (3) Avoid margin-diluting promotional discounts
- **Expected Annual Savings (25% lift):** $70,536

### Segment C — Early-Tenure Phone-Only Utility
- **Churn Rate:** 14.3% | **Avg ARPU:** $20.41/mo | **Expected MRR Loss:** $1,993/mo
- **Playbook:** (1) Maintain zero-touch digital servicing; (2) Test low-cost DSL bundle upgrades
- **Expected Annual Savings (25% lift):** $5,978

### Segment D — Loyal Phone-Only Long-Timers ✅ STABLE
- **Churn Rate:** 1.0% | **Avg ARPU:** $21.72/mo | **Expected MRR Loss:** $192/mo
- **Playbook:** (1) Maintain zero-touch digital servicing; (2) Test low-cost DSL bundle upgrades
- **Expected Annual Savings (25% lift):** $575

---

## 🗂️ Project Structure

```
Telco Churn/
│
├── telco churn.pbix              # Power BI dashboard (main deliverable)
│
├── data/
│   ├── telco_churn.csv           # Raw dataset — 7,043 customers, 21 features
│   ├── categorical_associations.csv  # Chi-squared stats + Cramér's V for all categorical features
│   ├── odds_ratios.csv           # Logistic regression coefficients and odds ratios (95% CI)
│   ├── slice_evaluation.csv      # Model performance by customer segment (ROC-AUC, F1)
│   └── ai_narratives.csv         # AI-generated executive diagnosis + retention playbooks per segment
│
└── README.md                     # This file
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Power BI | Interactive dashboard, KPI cards, risk segmentation visuals |
| Python (pandas, scipy, statsmodels) | Statistical analysis — chi-squared tests, logistic regression |
| Scikit-learn | Model training and evaluation (ROC-AUC, F1) |
| Claude API | AI-generated executive diagnostics and retention playbooks |
| IBM Telco Dataset | Source data (7,043 customers, 21 features) |

---

## 🚀 Dashboard Features

- **Executive Overview** — Churn rate, Total MRR, Churned MRR, MRR at Risk
- **Churn Analysis** — Breakdown by payment method, internet service, tenure band, and contract type
- **Feature Analysis** — Cramér's V and odds ratio visualizations for key churn drivers
- **Risk Segmentation** — Customers classified into Low / Medium / High risk tiers
- **Model Performance** — Actual vs. predicted churn rates, ROC-AUC by segment
- **AI Retention Insights** — Segment-specific diagnosis, root cause, and recommended playbooks with revenue impact

---

## 📈 Dataset

**Source:** IBM Sample Data — Telco Customer Churn  
**Rows:** 7,043 customers  
**Features:** 21 (demographics, service subscriptions, billing, churn label)

Key columns: `customerID`, `gender`, `SeniorCitizen`, `Partner`, `Dependents`, `tenure`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`, `Churn`

---

## 🔮 Future Enhancements

- [ ] Real-time churn prediction via API integration
- [ ] Customer Lifetime Value (CLV) modeling
- [ ] Automated retention campaign triggers
- [ ] Advanced model explainability (SHAP values)
- [ ] Model performance monitoring and drift detection

---

## 👤 Author

**Khushal Dusane**  
Aspiring Data Analyst | SQL · Python · Power BI · Excel  
📍 Pune, India  

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/khushaldusane)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/khushaldusane)
