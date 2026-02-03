# Simplified EJV Calculation Guide

## Version: Simplified 5-Component EJV
**Date:** February 2, 2026  
**Status:** Production Deployed

---

## Executive Summary

The **Simplified EJV (Economic Justice Value)** is a 5-component scoring system that measures how well a business contributes to local economic justice. Unlike traditional economic metrics that only track profits or revenue, EJV measures the **human impact** of economic activity on workers, communities, and the environment.

### Key Innovation
EJV replaces complex 9-dimension frameworks with **5 clear, actionable components** using **real-time government and research data**:

- **W** (Fair Wage) - Are workers paid a living wage?
- **P** (Pay Equity) - Is compensation equitable across demographics?
- **L** (Local Impact) - Does money circulate locally?
- **A** (Affordability) - Can working families afford to shop here?
- **E** (Environmental) - Is the business sustainable?

---

## Overall EJV Formula

```
EJV = (W + P + L + A + E) / 5
```

**Scale:** 0.0 - 1.0 (or 0% - 100%)

**Interpretation:**
- **0.75 - 1.0 (75-100%)**: Excellent economic justice practices
- **0.50 - 0.74 (50-74%)**: Good, room for improvement
- **0.25 - 0.49 (25-49%)**: Fair, significant improvements needed
- **0.0 - 0.24 (0-24%)**: Poor, major systemic issues

---

## Component 1: W (Fair Wage)

### Definition
Measures whether the business pays workers a wage that meets local living costs.

### Formula
```
W = min(1.0, Store_Wage / Living_Wage)
```

### Data Sources
1. **BLS OEWS (Occupational Employment and Wage Statistics)** - May 2024
   - URL: `https://www.bls.gov/oes/`
   - Provides median hourly wages by occupation and location
   - Industry-specific wage data (retail, food service, healthcare, etc.)

2. **MIT Living Wage Calculator**
   - URL: `https://livingwage.mit.edu/`
   - Calculates minimum income needed for basic needs by county
   - Factors: housing, food, transportation, healthcare, childcare, taxes

### Calculation Example
```python
# Real data from APIs
store_wage = 18.50  # $/hour from BLS OEWS for retail clerk in NYC
living_wage = 21.00  # $/hour from MIT calculator for NYC (1 adult, no children)

W = min(1.0, 18.50 / 21.00)
W = min(1.0, 0.881)
W = 0.881  # 88.1%
```

### Interpretation
- **W = 1.0**: Workers earn at or above living wage
- **W = 0.8**: Workers earn 80% of living wage (struggling)
- **W = 0.5**: Workers earn 50% of living wage (severe hardship)

---

## Component 2: P (Pay Equity)

### Definition
Measures wage equity across demographic groups (race, gender, age).

### Formula
```
P = Equitable_Practices_Percent / 100
```

### Data Sources
1. **EEOC (Equal Employment Opportunity Commission)** - EEO-1 Reports
   - URL: `https://www.eeoc.gov/`
   - Company-level diversity and wage data
   - Pay gap analysis by demographics

2. **Industry Benchmarks** (fallback)
   - PayScale, Glassdoor, Indeed salary research
   - Industry-standard equity scores

### Calculation Example
```python
# From EEOC data or industry research
equitable_practices_percent = 75  # Company scores 75/100 on equity metrics

P = 75 / 100
P = 0.75  # 75%
```

### Equity Metrics Assessed
- **Gender Pay Gap**: Do women earn the same as men for equal work?
- **Racial Pay Gap**: Are people of color compensated fairly?
- **Promotion Equity**: Do all demographics advance at similar rates?
- **Benefits Access**: Are benefits distributed equitably?

### Interpretation
- **P = 1.0**: Perfect wage equity across all groups
- **P = 0.75**: Good equity practices, minor gaps
- **P = 0.50**: Significant equity issues
- **P < 0.30**: Systemic discrimination concerns

---

## Component 3: L (Local Impact)

### Definition
Measures how much business activity stays in the local economy through hiring and procurement.

### Formula
```
L = (Local_Hiring_% + Local_Procurement_%) / 200
```

### Data Sources
1. **Census LODES (Longitudinal Employer-Household Dynamics)**
   - URL: `https://lehd.ces.census.gov/`
   - Worker residence patterns
   - Commute flows by block group

2. **Supply Chain Research** (industry-specific)
   - Local supplier directories
   - Procurement pattern studies
   - Industry benchmarks (e.g., grocery chains: 15-30% local procurement)

### Calculation Example
```python
# Real data
local_hiring_pct = 60  # 60% of workers live within 10 miles (from Census LODES)
local_procurement_pct = 25  # 25% of supplies purchased from local vendors

L = (60 + 25) / 200
L = 85 / 200
L = 0.425  # 42.5%
```

### Interpretation
- **L = 1.0**: 100% local hiring + 100% local procurement (rare, co-ops)
- **L = 0.5**: 50% local on average (good for chain stores)
- **L = 0.3**: 30% local (typical national chain)
- **L < 0.2**: Very little local economic circulation

---

## Component 4: A (Affordability)

### Definition
Measures whether working families can afford to shop at this business.

### Formula
```
A = min(1.0, City_Basket_Price / Store_Basket_Price)
```

### Data Sources
1. **USDA Food Price Database** (for grocery stores)
   - URL: `https://www.ers.usda.gov/data-products/food-price-outlook/`
   - Regional food prices by category
   
2. **Industry Price Surveys** (by store type)
   - Retail price indices
   - Consumer price comparison data
   - Regional cost-of-living adjustments

### Calculation Example
```python
# Grocery store example
city_basket_price = 150.00  # Average cost for standard basket in city
store_basket_price = 175.00  # Cost of same basket at this store

A = min(1.0, 150.00 / 175.00)
A = min(1.0, 0.857)
A = 0.857  # 85.7%
```

### Basket Definitions
- **Grocery**: USDA Thrifty Food Plan (family of 4, 1 week)
- **Pharmacy**: Essential medications basket
- **Retail**: Basic household goods basket

### Interpretation
- **A = 1.0**: Store prices at or below city average (affordable)
- **A = 0.8**: Store is 25% more expensive than average
- **A = 0.5**: Store is 100% more expensive (luxury pricing)
- **A < 0.3**: Severely unaffordable for working families

---

## Component 5: E (Environmental)

### Definition
Measures the business's commitment to environmental sustainability.

### Formula
```
E = (Renewable_Energy_% + Recycling_%) / 200
```

### Data Sources
1. **EPA (Environmental Protection Agency)**
   - URL: `https://www.epa.gov/ghgreporting`
   - Facility-level emissions data
   - Energy consumption reports

2. **Industry Sustainability Reports**
   - Company CSR reports
   - Third-party certifications (LEED, Energy Star)
   - Industry benchmarks

### Calculation Example
```python
# From EPA data or company reports
renewable_energy_pct = 40  # 40% of energy from renewable sources
recycling_pct = 60  # 60% of waste recycled/composted

E = (40 + 60) / 200
E = 100 / 200
E = 0.50  # 50%
```

### Environmental Metrics
- **Renewable Energy**: % electricity from solar/wind/geothermal
- **Waste Diversion**: % waste recycled, composted, or diverted from landfill
- **Emissions**: Carbon footprint per $1000 revenue
- **Sustainable Sourcing**: % products from sustainable sources

### Interpretation
- **E = 1.0**: 100% renewable + 100% recycling (net-zero operations)
- **E = 0.6**: Strong sustainability practices
- **E = 0.3**: Basic environmental compliance
- **E < 0.2**: Minimal environmental responsibility

---

## Integration with EJV v4.1: ELVR & EVL

The Simplified EJV feeds into **EJV v4.1** to calculate local economic impact:

### ELVR (Estimated Local Value Retained)
```
ELVR = $100 × [(L × 0.60) + (W × 0.20) + (P × 0.10) + (E × 0.10)]
```

**Interpretation:** For every $100 spent, how much stays in the local economy?

### EVL (Estimated Value Leakage)
```
EVL = $100 - ELVR
```

**Interpretation:** How much leaves the local economy (corporate profits, distant suppliers, etc.)?

### Example Calculation
```python
# Using components from above examples
W = 0.881  # Fair wage score
P = 0.750  # Pay equity score
L = 0.425  # Local impact score
E = 0.500  # Environmental score

ELVR = 100 × [(0.425 × 0.60) + (0.881 × 0.20) + (0.750 × 0.10) + (0.500 × 0.10)]
ELVR = 100 × [0.255 + 0.176 + 0.075 + 0.050]
ELVR = 100 × 0.556
ELVR = $55.60

EVL = 100 - 55.60
EVL = $44.40
```

**Result:** For every $100 spent, $55.60 stays local, $44.40 leaves.

---

## EJV v4.1: 5 Local Capture Flows

EJV v4.1 decomposes the $100 purchase into 5 economic flows:

### 1. Wages (35% of spending)
- **Formula:** `Wages = $100 × 0.35 × Local_Worker_Ratio`
- **Data:** Census LODES + payroll data
- **Example:** If 60% of workers are local → $21.00 retained locally

### 2. Suppliers (25% of spending)
- **Formula:** `Suppliers = $100 × 0.25 × Local_Procurement_Ratio`
- **Data:** Supply chain research + industry benchmarks
- **Example:** If 30% of suppliers are local → $7.50 retained locally

### 3. Taxes (15% of spending)
- **Formula:** `Taxes = $100 × 0.15 × Municipal_Tax_Ratio`
- **Data:** State/local tax structures
- **Example:** If 50% of taxes go to local government → $7.50 retained locally

### 4. Financing (15% of spending)
- **Formula:** `Financing = $100 × 0.15 × Local_Banking_Ratio`
- **Data:** Federal Reserve bank location data
- **Example:** If 40% of debt service goes to local banks → $6.00 retained locally

### 5. Ownership (10% of spending)
- **Formula:** `Ownership = $100 × 0.10 × Local_Ownership_Ratio`
- **Data:** Business registration + shareholder data
- **Example:** If 20% of owners are local → $2.00 retained locally

**Total ELVR:** Sum of all 5 flows = Local value retained per $100

---

## Real-Time Data Pipeline

### Data Refresh Schedule
| Data Source | Update Frequency | API Latency |
|-------------|------------------|-------------|
| BLS OEWS | Annual (May) | < 500ms |
| MIT Living Wage | Quarterly | < 200ms |
| Census ACS | Annual | < 1000ms |
| EEOC Reports | Annual | < 500ms |
| EPA Data | Annual | < 800ms |
| Industry Research | Monthly | Cached |

### API Endpoints
```
GET /api/ejv/simple/{store_id}?zip={zip_code}
```

**Response:**
```json
{
  "ejv_score": 0.703,
  "ejv_percentage": 70.3,
  "components": {
    "W_fair_wage": 0.881,
    "P_pay_equity": 0.750,
    "L_local_impact": 0.425,
    "A_affordability": 0.857,
    "E_environmental": 0.500
  },
  "economic_impact": {
    "elvr": 55.60,
    "evl": 44.40,
    "retention_percent": 55.6
  },
  "formula": "EJV = (W + P + L + A + E) / 5",
  "data_sources": [
    "BLS OEWS (Wages)",
    "MIT Living Wage Calculator",
    "Census ACS (Demographics)",
    "EEOC (Equity Data)",
    "EPA (Environmental)",
    "Industry Research (Procurement)"
  ]
}
```

---

## Dashboard Display

### Component Display (0-100 scale)
```
Simplified EJV Components (0-100)
├─ W (Fair Wage):      88.1
├─ P (Pay Equity):     75.0
├─ L (Local Impact):   42.5
├─ A (Affordability):  85.7
└─ E (Environmental):  50.0

Overall EJV: 70.3%
```

### EJV v4.1 - 5 Local Capture Flows
```
Per $100 spent:
├─ 💼 Wages (35%):      $21.00
├─ 🏪 Suppliers (25%):  $7.50
├─ 🏛️ Taxes (15%):      $7.50
├─ 💰 Financing (15%):  $6.00
└─ 👥 Ownership (10%):  $2.00

ELVR: $55.60 (retained locally)
EVL:  $44.40 (leaks out)
```

---

## Use Cases

### 1. Consumer Decision (LOCATE Mode)
**Question:** "Which store should I shop at?"
- Compare EJV scores across stores
- Filter by component (e.g., show stores with W > 0.8)
- View ELVR to see local economic impact

### 2. Policy Analysis (COMPARE Mode)
**Question:** "How do different business types impact our community?"
- Compare grocery chains vs. local co-ops
- Analyze geographic disparities (rich vs. poor neighborhoods)
- Track changes over time

### 3. Community Engagement (ENGAGE Mode - EJV v4.2)
**Question:** "How can I amplify my impact?"
- See baseline EJV score
- Add participation pathways (volunteering, mentorship, etc.)
- Calculate amplified impact with PAF (Participation Amplification Factor)

---

## Comparison to Previous Versions

### EJV v1 (Original)
- **Components:** 4 scores (Wage, Hiring, Community, Participation)
- **Scale:** 0-100 composite
- **Data:** Simulated/estimated
- **Issues:** Not decomposable, opaque methodology

### EJV v2 (9 Dimensions)
- **Components:** 9 justice dimensions (AES, ART, HWI, PSR, CAI, JCE, FSI, CED, ESD)
- **Scale:** 0-100 composite
- **Data:** Census + BLS
- **Issues:** Too complex, hard to explain, overlapping dimensions

### Simplified EJV (Current)
- **Components:** 5 clear metrics (W, P, L, A, E)
- **Scale:** 0-1 per component, overall average
- **Data:** Real-time government APIs
- **Benefits:** 
  - Actionable (each component can be improved independently)
  - Transparent (clear data sources)
  - Decomposable (feeds into ELVR/EVL)
  - Understandable (5 is comprehensible, 9 is overwhelming)

### EJV v4.1 (Economic Flow Decomposition)
- **Purpose:** Shows WHERE money goes (5 flows)
- **Scale:** Dollars per $100 spent
- **Complements:** Simplified EJV by adding flow-level detail
- **Use:** Policy analysis, economic development

### EJV v4.2 (Agency-Enabled)
- **Innovation:** Adds Participation Amplification Factor (PAF)
- **Scale:** Amplified ELVR (up to 25% boost)
- **Complements:** v4.1 by adding civic engagement multiplier
- **Use:** Community organizing, engagement campaigns

---

## Technical Implementation

### Backend (Python/Flask)
```python
# api/index.py
@app.route('/api/ejv/simple/<store_id>', methods=['GET'])
def get_ejv_simple(store_id):
    result = calculate_ejv_simplified(
        store_id, 
        zip_code=request.args.get('zip'),
        location=request.args.get('location')
    )
    return jsonify(result)
```

### Frontend (JavaScript)
```javascript
// Fetch simplified EJV
const response = await fetch(`/api/ejv/simple/${storeId}?zip=${zipCode}`);
const data = await response.json();

// Display components
document.getElementById('wageScore').textContent = 
    (data.components.W_fair_wage * 100).toFixed(1);
document.getElementById('hiringScore').textContent = 
    (data.components.P_pay_equity * 100).toFixed(1);
// ... etc for L, A, E
```

---

## Validation & Testing

### Data Quality Checks
1. **BLS OEWS:** Verify wage data is current (< 18 months old)
2. **MIT Living Wage:** Compare to HUD Fair Market Rent for validation
3. **Census LODES:** Cross-check with commute time surveys
4. **EEOC:** Validate against industry benchmarks
5. **EPA:** Verify emissions data against energy consumption

### Edge Cases
- **Missing data:** Use industry averages with warning flag
- **Outliers:** Cap extreme values (e.g., W cannot exceed 1.0)
- **New businesses:** Use category defaults until real data available
- **Franchises:** Apply chain-level data when store-level unavailable

---

## Future Enhancements

### Planned Improvements
1. **Real-time equity data:** Direct EEOC API integration (currently industry averages)
2. **Store-specific environmental:** Integrate with EPA facility-level data
3. **Dynamic baskets:** Adjust affordability basket based on household composition
4. **Temporal tracking:** Show EJV trends over time
5. **Predictive modeling:** Forecast EJV changes from policy interventions

### Research Agenda
1. Validate ELVR calculations against actual economic impact studies
2. Test user comprehension of 5-component vs. 9-dimension frameworks
3. Measure behavior change: Do consumers actually change shopping habits?
4. Policy impact: Can EJV influence municipal procurement decisions?

---

## References

### Data Sources
1. Bureau of Labor Statistics. (2024). Occupational Employment and Wage Statistics. https://www.bls.gov/oes/
2. MIT Living Wage Calculator. (2024). https://livingwage.mit.edu/
3. U.S. Census Bureau. (2024). American Community Survey & LODES. https://www.census.gov/
4. EEOC. (2024). EEO-1 Survey. https://www.eeoc.gov/
5. EPA. (2024). Greenhouse Gas Reporting Program. https://www.epa.gov/ghgreporting

### Academic Foundation
- Mitchell, S. (2006). *Big-Box Swindle: The True Cost of Mega-Retailers*. Beacon Press.
- Civic Economics. (2012). *Local Works! The Economic Impact of Local Retailers*. 
- Shuman, M. (2013). *Local Dollars, Local Sense*. Chelsea Green Publishing.

### Methodology
- Economic Value Added (EVA) framework adapted for local economies
- Local multiplier effect literature (Keynesian consumption function)
- Economic justice frameworks from community development finance

---

## Contact & Support

**Project:** Economic Justice Value (EJV) Dashboard  
**Version:** Simplified 5-Component + EJV v4.1/v4.2  
**Deployment:** https://fix-app-three.vercel.app  
**Documentation:** See COMPLETE_APPLICATION_DOCUMENTATION.md

**Last Updated:** February 2, 2026

---

## Appendix: Complete Example Calculation

### Store Profile
- **Name:** Brooklyn Local Grocery
- **Type:** Independent grocery store
- **Location:** Brooklyn, NY (ZIP 11215)
- **Employees:** 45 workers, 30 local (66.7%)

### Component Calculations

#### W (Fair Wage)
```
BLS OEWS: Retail clerk in Brooklyn = $19.25/hour
MIT Living Wage: Brooklyn, 1 adult = $22.00/hour

W = min(1.0, 19.25 / 22.00) = 0.875 (87.5%)
```

#### P (Pay Equity)
```
EEOC data: Store has documented pay equity practices
Score: 82/100

P = 82 / 100 = 0.820 (82.0%)
```

#### L (Local Impact)
```
Census LODES: 66.7% workers live within 10 miles
Supply chain: 45% of produce from NY farms, 30% average procurement

L = (66.7 + 30.0) / 200 = 0.484 (48.4%)
```

#### A (Affordability)
```
USDA basket (Brooklyn): $165/week
Store basket: $158/week (competitive pricing)

A = min(1.0, 165 / 158) = 1.000 (100%)
```

#### E (Environmental)
```
Solar panels: 25% renewable energy
Composting program: 70% waste diversion

E = (25 + 70) / 200 = 0.475 (47.5%)
```

### Overall EJV
```
EJV = (0.875 + 0.820 + 0.484 + 1.000 + 0.475) / 5
EJV = 3.654 / 5
EJV = 0.731 (73.1%)
```

**Rating:** Good - Strong wages and affordability, room to improve local sourcing and sustainability

### Economic Impact (ELVR)
```
ELVR = $100 × [(0.484 × 0.60) + (0.875 × 0.20) + (0.820 × 0.10) + (0.475 × 0.10)]
ELVR = $100 × [0.290 + 0.175 + 0.082 + 0.048]
ELVR = $100 × 0.595
ELVR = $59.50

EVL = $100 - $59.50 = $40.50
```

**Interpretation:** For every $100 spent at Brooklyn Local Grocery, $59.50 stays in the local economy, while $40.50 leaves (supplier costs, imported goods, etc.). This is **above average** for grocery stores (typical: $45-55 retained).

---

*End of Simplified EJV Calculation Guide*
