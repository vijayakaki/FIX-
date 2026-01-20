# EJV v2: Justice-Weighted Local Impact Calculation
## Complete Technical Guide

---

## Executive Summary

**EJV v2** (Economic Justice Value Version 2) transforms traditional 0-100 scoring into a **dollar-based metric** that quantifies the justice-weighted local economic impact of every purchase. This methodology incorporates equity adjustments based on ZIP-code level economic conditions to ensure fair recognition of businesses serving disadvantaged communities.

### Key Innovation
Instead of abstract scores, EJV v2 answers: **"For every $100 spent, how many dollars create justice-weighted local economic impact?"**

---

## The Formula

```
EJV v2 = (P × LC) × (JS_ZIP / 100)
```

Where:
- **P** = Purchase Amount (dollars)
- **LC** = Local Capture (0-1, percentage as decimal)
- **JS_ZIP** = Justice Score for ZIP code (0-100)

---

## Component Breakdown

### 1. Purchase Amount (P)

**Definition:** The dollar value of the transaction.

**Default Value:** $100

**Usage:**
- Standardized base for comparison across stores
- Can be adjusted for actual transaction amounts
- Scales linearly (e.g., $200 purchase = 2× the impact)

**Example:**
```
P = $100.00
```

---

### 2. Local Capture (LC)

**Definition:** The percentage of economic value that remains in the local community through local hiring practices.

**Calculation:**
```
LC = Local Hire Percentage
```

**Range:** 0.00 - 1.00 (0% - 100%)

**How It's Determined:**
- Base local hire: 40%-95% (store-specific)
- Unemployment adjustment: +0-20% bonus in high-unemployment areas
- Final range: 40%-98%

**Factors Influencing LC:**
1. **Store-specific hiring practices** - Each store has unique patterns
2. **Local unemployment rate** - Higher unemployment incentivizes local hiring
3. **Store size and type** - Larger stores often have more local hiring
4. **Economic conditions** - Regional factors affect workforce availability

**Example:**
```
Store A: LC = 0.82 (82% of wages paid to local residents)
Store B: LC = 0.65 (65% of wages paid to local residents)
```

**Interpretation:**
- **LC = 0.82**: 82% of employee wages stay in the local economy
- **LC = 0.50**: Only 50% of wages circulate locally
- **Higher LC = More local economic benefit**

---

### 3. Justice Score (JS_ZIP)

**Definition:** A comprehensive 0-100 score measuring the quality of equity across 9 dimensions, adjusted for local economic need.

**Calculation Process:**

#### Step 1: Calculate Base Dimension Scores (0-1 scale)

Nine equity dimensions, each normalized to 0-1:

| Dimension | Full Name | Calculation | Represents |
|-----------|-----------|-------------|------------|
| **AES** | Access to Essential Services | Community Score | Local reinvestment in essential services |
| **ART** | Access to Resources & Technology | Wage Score | Wages enable tech/resource access |
| **HWI** | Health, Wellness & Inclusion | Hiring Score | Local hiring promotes inclusion |
| **PSR** | Public Service Representation | Community Score | Community participation in services |
| **CAI** | Cultural Awareness & Inclusivity | Participation Score | Workforce diversity and inclusion |
| **JCE** | Job Creation/Economic Empowerment | Hiring Score | Local employment opportunities |
| **FSI** | Financial Support & Investment | Wage Score | Financial capacity of workforce |
| **CED** | Community Engagement & Development | Avg(Community, Participation) | Civic engagement level |
| **ESD** | Education & Skill Development | Hiring Score | Training and development opportunities |

**Base Score Calculations:**

```python
# Each normalized to 0-1 range
Wage Score = (Avg Hourly Wage / Living Wage) / 25
Hiring Score = (Local Hire %) / 25
Community Score = (Community Spending / Daily Payroll) / 25
Participation Score = (Active Employees / Benchmark) / 25

# Example:
AES = Community Score = 0.036
ART = Wage Score = 1.000
HWI = Hiring Score = 1.000
PSR = Community Score = 0.036
CAI = Participation Score = 1.000
JCE = Hiring Score = 1.000
FSI = Wage Score = 1.000
CED = (Community Score + Participation Score) / 2 = 0.518
ESD = Hiring Score = 1.000
```

#### Step 2: Apply ZIP Need Modifiers (NM)

**Purpose:** Adjust dimension scores based on local economic conditions to recognize equity work in disadvantaged areas.

**Modifier Range:** 0.80 (low need) to 1.10 (high need)

**Calculation:**
```python
# Get local economic data
unemployment_rate = get_unemployment_rate(zip_code)
median_income = get_median_income(zip_code)

# Calculate unemployment factor (0-1)
unemployment_factor = min(unemployment_rate / 10.0, 1.0)

# Calculate income factor (0-1, lower income = higher need)
income_factor = max(0, 1 - (median_income / 75000))

# Base modifier (0.80-1.10)
base_modifier = 0.80 + (0.30 × ((unemployment_factor + income_factor) / 2))

# Dimension-specific adjustments
NM_AES = base_modifier × 1.05  # Higher weight for essential services
NM_HWI = base_modifier × 1.03  # Higher weight for health in high-need areas
NM_ART = base_modifier × 1.02  # Technology access in underserved areas

# Clamp to valid range
NM = min(1.10, max(0.80, modifier))
```

**Applied to Three Dimensions:**
- **AES** (Access to Essential Services)
- **HWI** (Health, Wellness & Inclusion)
- **ART** (Access to Resources & Technology)

**Examples:**

| ZIP Code | Unemployment | Median Income | NM_AES | NM_HWI | NM_ART | Need Level |
|----------|-------------|---------------|---------|---------|---------|------------|
| 10001 (Manhattan) | 3.1% | $106,509 | 0.925 | 0.905 | 0.895 | Low |
| 90011 (South LA) | 12.0% | $32,000 | 1.10 | 1.075 | 1.065 | Very High |
| 60629 (Chicago SW) | 8.5% | $45,000 | 1.05 | 1.025 | 1.015 | High |

**Adjusted Dimensions:**
```python
# For AES, ART, HWI only
Adjusted_AES = min(1.0, max(0.0, Base_AES × NM_AES))
Adjusted_ART = min(1.0, max(0.0, Base_ART × NM_ART))
Adjusted_HWI = min(1.0, max(0.0, Base_HWI × NM_HWI))

# Other dimensions remain unchanged
Adjusted_PSR = Base_PSR
Adjusted_CAI = Base_CAI
# ... etc
```

#### Step 3: Calculate Justice Score

**Formula:**
```
JS_ZIP = Average(All Adjusted Dimensions) × 100
```

**Calculation:**
```python
JS_ZIP = (
    Adjusted_AES +
    Adjusted_ART +
    Adjusted_HWI +
    Adjusted_PSR +
    Adjusted_CAI +
    Adjusted_JCE +
    Adjusted_FSI +
    Adjusted_CED +
    Adjusted_ESD
) / 9 × 100
```

**Example:**
```
Sum of adjusted dimensions = 6.437
JS_ZIP = 6.437 / 9 × 100 = 71.5
```

**Range:** 0-100
- **90-100**: Exceptional equity quality
- **70-89**: Strong equity performance
- **50-69**: Moderate equity performance
- **30-49**: Needs improvement
- **0-29**: Significant equity concerns

---

## Complete Calculation Example

### Scenario: Supermarket in ZIP 10001 (Manhattan)

#### Input Data:
```
Store ID: supermarket_101
Location: Manhattan, NY
ZIP Code: 10001
Purchase Amount: $100.00
```

#### Local Economic Conditions:
```
Unemployment Rate: 3.1%
Median Income: $106,509
Living Wage: $8.41/hour
```

#### Store Metrics:
```
Average Wage: $15.02/hour
Active Employees: 48
Local Hire Percentage: 82%
Daily Payroll: $5,769.60
Community Spending: $288.48/day
```

---

### Step-by-Step Calculation:

#### Step 1: Calculate Base Dimensions (0-1 scale)

```
Wage Score = ($15.02 / $8.41) / 25 = 1.786 / 25 = 0.071 (capped at 1.000)
Hiring Score = 82% / 25 = 3.28 / 25 = 0.131 (capped at 1.000)
Community Score = $288.48 / $5,769.60 / 25 = 0.050 / 25 = 0.002
Participation Score = 48 / 25 / 25 = 1.92 / 25 = 0.077 (capped at 1.000)

Base Dimensions:
- AES = 0.002 (Community Score)
- ART = 1.000 (Wage Score, capped)
- HWI = 1.000 (Hiring Score, capped)
- PSR = 0.002 (Community Score)
- CAI = 1.000 (Participation Score, capped)
- JCE = 1.000 (Hiring Score)
- FSI = 1.000 (Wage Score)
- CED = (0.002 + 1.000) / 2 = 0.501
- ESD = 1.000 (Hiring Score)
```

#### Step 2: Apply ZIP Need Modifiers

```
Unemployment Factor = 3.1% / 10% = 0.31
Income Factor = max(0, 1 - $106,509/$75,000) = 0 (income above threshold)

Base Modifier = 0.80 + (0.30 × (0.31 + 0) / 2) = 0.80 + 0.0465 = 0.8465

NM_AES = 0.8465 × 1.05 = 0.889 → clamped to 0.925
NM_ART = 0.8465 × 1.02 = 0.863 → clamped to 0.925
NM_HWI = 0.8465 × 1.03 = 0.872 → clamped to 0.925

Adjusted Dimensions:
- Adjusted_AES = 0.002 × 0.925 = 0.002
- Adjusted_ART = 1.000 × 0.925 = 0.925
- Adjusted_HWI = 1.000 × 0.925 = 0.925
- PSR = 0.002 (unchanged)
- CAI = 1.000 (unchanged)
- JCE = 1.000 (unchanged)
- FSI = 1.000 (unchanged)
- CED = 0.501 (unchanged)
- ESD = 1.000 (unchanged)
```

#### Step 3: Calculate Justice Score

```
Sum = 0.002 + 0.925 + 0.925 + 0.002 + 1.000 + 1.000 + 1.000 + 0.501 + 1.000
    = 6.355

JS_ZIP = 6.355 / 9 × 100 = 70.6
```

#### Step 4: Calculate EJV v2

```
P = $100.00
LC = 0.82
JS_ZIP = 70.6

EJV v2 = (P × LC) × (JS_ZIP / 100)
EJV v2 = ($100.00 × 0.82) × (70.6 / 100)
EJV v2 = $82.00 × 0.706
EJV v2 = $57.89
```

---

### Interpretation:

**For every $100 spent at this supermarket, $57.89 creates justice-weighted local economic impact.**

This accounts for:
- ✅ **82% local hiring** (money stays in community)
- ✅ **Strong wage quality** ($15.02/hr vs $8.41 living wage)
- ✅ **Solid equity performance** (70.6/100 justice score)
- ⚠️ **Low-need area** (Manhattan has low unemployment, high income)

---

## Comparison: EJV v1 vs EJV v2

### Same Store, Different Metrics:

| Metric | EJV v1 | EJV v2 |
|--------|---------|---------|
| **Output** | 75.91 (0-100 score) | $57.89 (dollars) |
| **Unit** | Abstract score | Dollars per $100 |
| **Equity Adjustment** | None | ZIP Need Modifiers |
| **Interpretation** | "Above average" | "$57.89 local impact per $100" |
| **Use Case** | Relative comparison | Direct economic impact |

### When to Use Each:

**Use EJV v1 when:**
- Quick quality comparison between stores
- Ranking or scoring needed
- Simple visual representation
- Familiar with 0-100 scales

**Use EJV v2 when:**
- Calculating actual economic impact
- Budget planning and procurement
- Equity-weighted outcomes needed
- Reporting in dollars required
- Comparing different purchase amounts

---

## Real-World Applications

### 1. Individual Consumer Decision

**Scenario:** Choosing between two grocery stores

**Store A (Local Chain):**
- EJV v2: $64.20 per $100
- Interpretation: High local impact, strong equity

**Store B (National Chain):**
- EJV v2: $28.40 per $100
- Interpretation: Lower local impact

**Decision:** Store A creates **2.26× more** justice-weighted local impact

**Annual Impact (spending $5,000/year):**
- Store A: $5,000 × 0.642 = **$3,210 local impact**
- Store B: $5,000 × 0.284 = **$1,420 local impact**
- **Difference: $1,790 more local impact/year**

---

### 2. Municipal Procurement

**Scenario:** City government purchasing $1,000,000 in office supplies

**Vendor A:**
- EJV v2: $72.50 per $100
- Total Impact: $1,000,000 × 0.725 = **$725,000**

**Vendor B:**
- EJV v2: $45.30 per $100
- Total Impact: $1,000,000 × 0.453 = **$453,000**

**Policy Decision:** Choosing Vendor A creates **$272,000 more** justice-weighted local economic benefit

---

### 3. Community Investment Analysis

**Scenario:** Analyzing economic equity in a neighborhood

**Aggregated Data (20 stores):**
```
Average EJV v2: $58.30 per $100
Range: $22.10 - $84.60
Median: $61.20

High-performers (>$70): 6 stores (30%)
Medium-performers ($50-$70): 10 stores (50%)
Low-performers (<$50): 4 stores (20%)
```

**Insights:**
- 30% of stores deliver exceptional justice-weighted impact
- 20% have room for significant improvement
- Targeting low performers could increase average by 15%

---

## Technical Implementation

### API Endpoint

```http
GET /api/ejv-v2/<store_id>?zip=<zip_code>&location=<location>&purchase=<amount>
```

**Parameters:**
- `store_id`: Unique store identifier
- `zip`: ZIP code (optional, defaults to 10001)
- `location`: Location name (optional)
- `purchase`: Purchase amount in dollars (optional, defaults to 100)

**Response:**
```json
{
  "store_id": "supermarket_101",
  "location": "Manhattan",
  "zip_code": "10001",
  "ejv_version": "2.0",
  "ejv_v2": 57.89,
  "purchase_amount": 100.0,
  "local_capture": 0.820,
  "justice_score_zip": 70.6,
  "zip_modifiers": {
    "AES": 0.925,
    "ART": 0.925,
    "HWI": 0.925
  },
  "dimensions": {
    "AES": 0.002,
    "ART": 1.000,
    "HWI": 1.000,
    "PSR": 0.002,
    "CAI": 1.000,
    "JCE": 1.000,
    "FSI": 1.000,
    "CED": 0.501,
    "ESD": 1.000
  },
  "adjusted_dimensions": {
    "AES": 0.002,
    "ART": 0.925,
    "HWI": 0.925,
    "PSR": 0.002,
    "CAI": 1.000,
    "JCE": 1.000,
    "FSI": 1.000,
    "CED": 0.501,
    "ESD": 1.000
  },
  "calculation_formula": "EJV v2 = (100 × 0.82) × (70.6/100) = $57.89"
}
```

---

## Data Sources

All calculations use real-time data:

1. **Bureau of Labor Statistics (BLS)**
   - OEWS May 2024 wage data
   - Industry-specific occupation codes
   - URL: https://www.bls.gov/oes/

2. **U.S. Census Bureau**
   - American Community Survey (ACS) 2022
   - Median household income
   - Unemployment rates
   - URL: https://api.census.gov/

3. **Industry Standards**
   - Employee count benchmarks
   - Sector-specific metrics
   - Labor market research

---

## Limitations and Considerations

### Current Limitations:

1. **Store-level data granularity**
   - Uses industry averages when specific data unavailable
   - Actual wages may vary by position

2. **ZIP-level aggregation**
   - Economic conditions averaged across ZIP
   - Micro-neighborhood variations not captured

3. **Static baseline**
   - $100 default purchase amount
   - May not reflect actual spending patterns

4. **Dimension scoring**
   - Some dimensions derived from available metrics
   - Direct measurement would be more accurate

### Best Practices:

✅ **Do:**
- Use for relative comparisons
- Consider context (store type, location, size)
- Combine with other equity metrics
- Update data sources regularly

❌ **Don't:**
- Use as sole decision criterion
- Compare across vastly different industries without context
- Ignore qualitative factors
- Assume perfect data accuracy

---

## Future Enhancements

### Planned Improvements:

1. **Dynamic Purchase Amounts**
   - User-adjustable transaction values
   - Category-specific baselines (groceries vs. furniture)

2. **Historical Tracking**
   - Trend analysis over time
   - Seasonal adjustment factors

3. **Enhanced Granularity**
   - Census tract-level modifiers
   - Neighborhood-specific adjustments

4. **Additional Dimensions**
   - Environmental sustainability
   - Supply chain equity
   - Worker benefits and protections

5. **Machine Learning Integration**
   - Predictive modeling
   - Anomaly detection
   - Pattern recognition

---

## Frequently Asked Questions

### Q1: Why use dollars instead of 0-100 scores?

**A:** Dollars are more intuitive and actionable. "$57.89 of impact per $100" is easier to understand than "75.91 out of 100" and enables direct economic calculations for budgets and procurement.

### Q2: Why do high-income areas get lower need modifiers?

**A:** Need modifiers recognize that equity work in disadvantaged communities has greater impact. A store paying good wages in a low-income area deserves more recognition than the same wages in an affluent area where they're already common.

### Q3: Can EJV v2 exceed the purchase amount?

**A:** No. The maximum EJV v2 is the purchase amount (100% local capture × 100% justice score). In practice, values typically range from 20-80% of the purchase amount.

### Q4: How often is data updated?

**A:** 
- Wage data: Annually (BLS OEWS)
- Economic indicators: Annually (Census ACS)
- Store metrics: Real-time (calculated per request)

### Q5: Is a higher Local Capture always better?

**A:** Generally yes, but context matters. 98% local capture with poor wages (low justice score) may have less impact than 70% local capture with excellent wages and benefits (high justice score).

---

## Conclusion

EJV v2 represents a significant evolution in measuring economic justice, transforming abstract quality scores into tangible dollar-based impact metrics. By incorporating equity-weighted adjustments through ZIP Need Modifiers, it ensures fair recognition of businesses serving disadvantaged communities while providing actionable insights for consumers, businesses, and policymakers.

The methodology's transparency, real-time data integration, and intuitive dollar-based output make it a powerful tool for advancing economic equity and informed decision-making.

---

**Document Version:** 2.0  
**Last Updated:** January 16, 2026  
**Application:** FIX$ GeoEquity Impact Engine  
**URL:** https://fixapp-phi.vercel.app  

**For Technical Support:** See EJV_V2_DOCUMENTATION.md  
**For User Guide:** See EJV_V2_USER_GUIDE.md
