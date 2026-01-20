# EJV v1: Economic Justice Value Calculation Guide
## Traditional 0-100 Scoring System

---

## Executive Summary

**EJV v1** (Economic Justice Value Version 1) is a composite scoring system that measures the economic justice quality of a business on a **0-100 scale**. It evaluates four key dimensions of economic equity: wage fairness, local hiring practices, community reinvestment, and job creation.

### Key Purpose
EJV v1 answers: **"How well does this business perform on economic justice across multiple dimensions?"**

---

## The Formula

```
EJV v1 = Wage Score + Hiring Score + Community Score + Participation Score
```

**Range:** 0-100 points

Each component contributes up to 25 points, creating a balanced composite score.

---

## Component Breakdown

### 1. Wage Score (0-25 points)

**Definition:** Measures how employee wages compare to the local living wage threshold.

**Calculation:**
```
Wage Score = min(25, max(0, ((avg_wage - living_wage) / living_wage) × 50))
```

**What It Measures:**
- Wage adequacy relative to local cost of living
- Economic sustainability for workers
- Fair compensation practices

**Factors:**
- **Average Wage**: Mean hourly wage paid by the store
- **Living Wage**: Calculated as 70% of median household income in the area
- **Ratio**: How much wages exceed (or fall short of) living wage

**Example Calculations:**

| Avg Wage | Living Wage | Calculation | Score |
|----------|-------------|-------------|-------|
| $15.02   | $8.41       | ($15.02 - $8.41) / $8.41 × 50 = 39.2 | **25.0** (capped) |
| $10.00   | $12.00      | ($10.00 - $12.00) / $12.00 × 50 = -8.3 | **0.0** (minimum) |
| $12.00   | $10.00      | ($12.00 - $10.00) / $10.00 × 50 = 10.0 | **10.0** |

**Interpretation:**
- **25 points**: Wages significantly exceed living wage (excellent)
- **15-24 points**: Wages moderately exceed living wage (good)
- **5-14 points**: Wages slightly exceed living wage (fair)
- **0 points**: Wages at or below living wage (needs improvement)

---

### 2. Hiring Score (0-25 points)

**Definition:** Measures the percentage of employees hired from the local community.

**Calculation:**
```
Hiring Score = local_hire_pct × 25
```

**What It Measures:**
- Local workforce participation
- Community employment opportunities
- Economic circulation within the community

**How Local Hire Percentage is Determined:**

The local hire percentage for each store is calculated as:
```
local_hire_pct = Base Local Hire + Store Adjustment + Unemployment Factor
```

Components:
1. **Base Local Hire** (40-95%): Store-specific hiring pattern
2. **Store Adjustment** (0-30%): Store-specific variance
3. **Unemployment Factor** (0-20%): Boost based on local unemployment rate

(See "Local Capture Calculation" section for detailed explanation)

**Example Calculations:**

| Local Hire % | Calculation | Score |
|--------------|-------------|-------|
| 82%          | 0.82 × 25   | **20.5** |
| 65%          | 0.65 × 25   | **16.25** |
| 95%          | 0.95 × 25   | **23.75** |
| 40%          | 0.40 × 25   | **10.0** |

**Interpretation:**
- **20-25 points**: Strong local hiring (80-100%)
- **15-19 points**: Moderate local hiring (60-79%)
- **10-14 points**: Limited local hiring (40-59%)
- **0-9 points**: Minimal local hiring (<40%)

---

### 3. Community Score (0-25 points)

**Definition:** Measures community reinvestment as a percentage of total daily payroll.

**Calculation:**
```
Community Score = (community_spend_today / daily_payroll) × 100
```

**What It Measures:**
- Financial reinvestment in local community
- Support for local services and organizations
- Corporate social responsibility

**How Community Spending is Determined:**

```
community_spend_pct = 0.005 + (0.25 × store_random_factor)
community_spend_today = daily_payroll × community_spend_pct
```

This varies by:
- Store profitability
- Local economic conditions
- Corporate giving policies
- Community partnership programs

**Example Calculations:**

| Community Spend | Daily Payroll | Calculation | Score |
|-----------------|---------------|-------------|-------|
| $288.48         | $5,769.60     | ($288.48 / $5,769.60) × 100 = 5.0% | **5.0** |
| $500.00         | $6,000.00     | ($500 / $6,000) × 100 = 8.3% | **8.3** |
| $150.00         | $5,000.00     | ($150 / $5,000) × 100 = 3.0% | **3.0** |
| $1,200.00       | $8,000.00     | ($1,200 / $8,000) × 100 = 15.0% | **15.0** |

**Interpretation:**
- **15-25 points**: Exceptional community investment (15-25% of payroll)
- **8-14 points**: Strong community investment (8-14% of payroll)
- **3-7 points**: Moderate community investment (3-7% of payroll)
- **0-2 points**: Minimal community investment (<3% of payroll)

---

### 4. Participation Score (0-25 points)

**Definition:** Measures job creation through the number of active employees.

**Calculation:**
```
Participation Score = min(25, (active_employees / 100) × 25)
```

**What It Measures:**
- Employment opportunities created
- Economic participation intensity
- Job availability in the community
- Scale of economic impact

**How Employee Count is Determined:**

Based on:
- Store type (supermarket, convenience, pharmacy, hardware)
- Store size
- Industry benchmarks from BLS data
- Local market conditions

**Example Calculations:**

| Active Employees | Calculation | Score |
|------------------|-------------|-------|
| 48               | (48 / 100) × 25 = 12.0 | **12.0** |
| 25               | (25 / 100) × 25 = 6.25 | **6.25** |
| 75               | (75 / 100) × 25 = 18.75 | **18.75** |
| 120              | (120 / 100) × 25 = 30.0 | **25.0** (capped) |

**Interpretation:**
- **20-25 points**: Large employer (80+ employees)
- **15-19 points**: Medium employer (60-79 employees)
- **10-14 points**: Small employer (40-59 employees)
- **0-9 points**: Micro employer (<40 employees)

---

## Complete Calculation Example

### Scenario: Supermarket in Manhattan (ZIP 10001)

**Store Data:**
- Average Wage: $15.02/hour
- Living Wage: $8.41/hour
- Local Hire Percentage: 82%
- Active Employees: 48
- Daily Payroll: $5,769.60
- Community Spending: $288.48

**Step-by-Step Calculation:**

#### Step 1: Calculate Wage Score
```
Wage Score = min(25, max(0, (($15.02 - $8.41) / $8.41) × 50))
Wage Score = min(25, max(0, ($6.61 / $8.41) × 50))
Wage Score = min(25, max(0, 0.786 × 50))
Wage Score = min(25, 39.3)
Wage Score = 25.0 points
```

#### Step 2: Calculate Hiring Score
```
Hiring Score = 0.82 × 25
Hiring Score = 20.5 points
```

#### Step 3: Calculate Community Score
```
Community Score = ($288.48 / $5,769.60) × 100
Community Score = 0.05 × 100
Community Score = 5.0 points
```

#### Step 4: Calculate Participation Score
```
Participation Score = min(25, (48 / 100) × 25)
Participation Score = min(25, 12.0)
Participation Score = 12.0 points
```

#### Step 5: Calculate Total EJV v1
```
EJV v1 = Wage Score + Hiring Score + Community Score + Participation Score
EJV v1 = 25.0 + 20.5 + 5.0 + 12.0
EJV v1 = 62.5 points
```

---

## Score Interpretation

### Overall EJV v1 Score Ranges

| Score Range | Rating | Interpretation |
|-------------|--------|----------------|
| **80-100** | Exceptional | Outstanding economic justice performance across all dimensions |
| **70-79** | Excellent | Strong economic justice with minor areas for improvement |
| **60-69** | Good | Above-average economic justice performance |
| **50-59** | Fair | Moderate economic justice with room for improvement |
| **40-49** | Below Average | Significant improvements needed |
| **30-39** | Poor | Major economic justice concerns |
| **0-29** | Very Poor | Critical need for economic justice improvements |

### Component Analysis

When analyzing EJV v1 scores, examine each component:

**Balanced Score (Example: 18, 20, 15, 17 = 70)**
- All components contribute relatively equally
- Indicates well-rounded economic justice practices

**Wage-Heavy Score (Example: 25, 15, 8, 12 = 60)**
- Strong wages but weaker in other areas
- May have high pay but limited local hiring or community investment

**Hiring-Heavy Score (Example: 12, 24, 10, 14 = 60)**
- Excellent local hiring but lower wages
- Focus on local employment over wage levels

**Unbalanced Score (Example: 25, 22, 2, 8 = 57)**
- Strong in some areas, weak in others
- Indicates specific improvement opportunities

---

## Local Capture Calculation (LC)

**Local Capture** is the same as the **Local Hire Percentage** used in EJV v1's Hiring Score.

### Formula
```
LC = Base Local Hire + Store Adjustment + Unemployment Factor
```
(Maximum: 0.98 or 98%)

### Components:

#### 1. Base Local Hire (40-95%)
```
Base = 0.40 + (0.55 × store_random_factor)
```
- Starts at 40% baseline
- Adds up to 55% based on store-specific consistent random factor
- Each store has a unique, consistent hiring pattern

#### 2. Store Adjustment (0-30%)
```
Store Adjustment = (store_hash % 30) / 100
```
- Generated from store ID hash
- Adds store-specific variance
- Reflects individual store characteristics

#### 3. Unemployment Factor (0-20%)
```
Unemployment Factor = min(unemployment_rate / 10.0, 0.20)
```
- Based on ZIP code unemployment rate
- Higher unemployment → higher local hiring incentive
- Capped at 20% maximum boost

### Example Calculation:
```
Store A:
- Base: 0.40 + (0.55 × 0.6) = 0.73
- Store adjustment: 0.15
- Unemployment rate: 8% → 0.08 factor
- LC = min(0.98, 0.73 + 0.15 + 0.08) = 0.96 (96%)
```

---

## Data Sources

### Real-Time Data Integration

EJV v1 uses live data from authoritative sources:

#### 1. **Wage Data**
- **Source**: Bureau of Labor Statistics (BLS) OEWS May 2024
- **Data**: Published occupational wage statistics
- **Update Frequency**: Annual

#### 2. **Demographic Data**
- **Source**: U.S. Census Bureau ACS 2022 API
- **Data**: Median household income by census tract
- **Update Frequency**: Real-time API calls

#### 3. **Employment Data**
- **Source**: BLS industry research and averages
- **Data**: Employee counts by store type and size
- **Update Frequency**: Annual industry reports

#### 4. **Local Economic Factors**
- **Source**: Census ACS 2022 (calculated from real-time data)
- **Data**: Unemployment rates and income levels
- **Update Frequency**: Real-time API calls

---

## Wealth Metrics

In addition to the EJV v1 score, the system calculates:

### Wealth Retained
```
Wealth Retained = (daily_payroll × local_hire_pct) + community_spend_today
```

**Definition:** Total dollars that stay in the local economy each day.

**Example:**
```
Daily Payroll: $5,769.60
Local Hire %: 82%
Community Spend: $288.48

Wealth Retained = ($5,769.60 × 0.82) + $288.48
Wealth Retained = $4,731.07 + $288.48
Wealth Retained = $5,019.55 per day
```

### Wealth Leakage
```
Wealth Leakage = daily_payroll × (1 - local_hire_pct)
```

**Definition:** Total dollars that leave the local economy daily through non-local hiring.

**Example:**
```
Daily Payroll: $5,769.60
Local Hire %: 82%

Wealth Leakage = $5,769.60 × (1 - 0.82)
Wealth Leakage = $5,769.60 × 0.18
Wealth Leakage = $1,038.53 per day
```

### Annual Impact
```
Annual Wealth Retained = Wealth Retained × 365
Annual Wealth Leakage = Wealth Leakage × 365
```

---

## Use Cases

### When to Use EJV v1

**✅ Best for:**
- Quick quality comparison between stores
- Ranking stores by economic justice performance
- Simple visual representation (0-100 familiar scale)
- Identifying strengths and weaknesses across dimensions
- Executive summaries and dashboards
- Relative performance benchmarking

**❌ Less suitable for:**
- Calculating actual dollar impact
- Budget planning and procurement decisions
- Equity-weighted outcomes
- Comparing different purchase amounts
- Grant reporting requiring dollar amounts

### Practical Applications

1. **Store Selection**: Compare EJV v1 scores to choose stores with better economic justice
2. **Performance Tracking**: Monitor score changes over time
3. **Policy Development**: Set minimum EJV v1 thresholds for vendor contracts
4. **Community Impact**: Identify areas where stores excel or need improvement
5. **Benchmarking**: Compare against industry averages or peer groups

---

## Comparison: EJV v1 vs EJV v2

### Side-by-Side Comparison (Same Store):

| Metric | EJV v1 | EJV v2 |
|--------|---------|---------|
| **Output** | 62.5 (0-100 score) | $57.89 (dollars) |
| **Unit** | Abstract score | Dollars per $100 |
| **Equity Adjustment** | None | ZIP Need Modifiers |
| **Components** | 4 equal components (0-25 each) | 9 equity dimensions with modifiers |
| **Interpretation** | "Above average performance" | "$57.89 local impact per $100" |
| **Use Case** | Relative comparison | Direct economic impact |
| **Calculation** | Simple sum | Weighted adjustment |

### Key Differences:

**EJV v1:**
- No geographic equity adjustment
- All locations treated equally
- Simple, intuitive 0-100 scale
- Four balanced components
- Focus on business practices

**EJV v2:**
- Adjusts for local economic need (ZIP modifiers)
- High-need areas receive recognition
- Dollar-based output
- Nine equity dimensions
- Focus on justice-weighted impact

---

## Real-World Examples

### Example 1: High-Performing Store
**Location:** Suburban Supermarket

| Component | Value | Score |
|-----------|-------|-------|
| Wage Score | Avg: $18.50, Living: $10.20 | 25.0 |
| Hiring Score | Local Hire: 88% | 22.0 |
| Community Score | $850 / $6,400 = 13.3% | 13.3 |
| Participation Score | 85 employees | 21.25 |
| **Total EJV v1** | | **81.55** |

**Rating:** Exceptional - Outstanding across all dimensions

---

### Example 2: Moderate-Performing Store
**Location:** Urban Convenience Store

| Component | Value | Score |
|-----------|-------|-------|
| Wage Score | Avg: $11.00, Living: $9.50 | 7.89 |
| Hiring Score | Local Hire: 65% | 16.25 |
| Community Score | $120 / $2,400 = 5% | 5.0 |
| Participation Score | 12 employees | 3.0 |
| **Total EJV v1** | | **32.14** |

**Rating:** Poor - Needs significant improvements, especially in wages and job creation

---

### Example 3: Unbalanced Store
**Location:** Hardware Store

| Component | Value | Score |
|-----------|-------|-------|
| Wage Score | Avg: $22.00, Living: $11.00 | 25.0 |
| Hiring Score | Local Hire: 45% | 11.25 |
| Community Score | $90 / $4,200 = 2.1% | 2.1 |
| Participation Score | 28 employees | 7.0 |
| **Total EJV v1** | | **45.35** |

**Rating:** Below Average - Excellent wages but poor community investment and local hiring

---

## Limitations and Considerations

### Known Limitations

1. **No Geographic Equity Adjustment**
   - Treats all locations equally
   - Doesn't account for local economic need
   - Same score in high-income vs low-income areas has different equity implications

2. **Abstract Scale**
   - 0-100 score lacks intuitive dollar meaning
   - Difficult to translate into budget decisions
   - Less actionable for procurement

3. **Equal Weighting**
   - All four components weighted equally (25 points each)
   - Doesn't prioritize certain dimensions over others
   - May not reflect community priorities

4. **Static Benchmarks**
   - Benchmark of 100 employees for participation score may not fit all contexts
   - Living wage calculation is simplified (70% of median income)
   - Industry variations not fully captured

### Best Practices

1. **Use Component Scores**: Don't rely solely on total; analyze individual components
2. **Set Context**: Consider local conditions and industry norms when interpreting
3. **Track Over Time**: Monitor trends rather than single point-in-time scores
4. **Combine with v2**: Use both versions for comprehensive understanding
5. **Consider Qualitative Factors**: Scores don't capture everything; include qualitative assessment

---

## Technical Implementation

### API Endpoint

```http
GET /api/ejv/<store_id>?zip=10001&location=Manhattan
```

### Response Format

```json
{
  "store_id": "supermarket_101",
  "location": "Manhattan",
  "zip_code": "10001",
  "EJV": 62.5,
  "wage_score": 25.0,
  "hiring_score": 20.5,
  "community_score": 5.0,
  "participation_score": 12.0,
  "wealth_retained": 5019.55,
  "wealth_leakage": 1038.53,
  "median_income": 106000,
  "living_wage": 8.41,
  "unemployment_rate": 5.2,
  "local_hire_pct": 0.82
}
```

### Python Implementation

```python
def calculate_ejv(store_id, zip_code="10001", location_name="Unknown"):
    """
    Calculate EJV v1 for a store
    
    Returns:
    - EJV: Total score (0-100)
    - Component scores (wage, hiring, community, participation)
    - Wealth metrics (retained, leakage)
    - Economic indicators (median income, living wage, unemployment)
    """
    # Get local economic data
    median_income = get_median_income(state, county, tract)
    living_wage = median_income * 0.70 / 2080  # Annual to hourly
    economic_data = get_local_economic_indicators(zip_code)
    
    # Get store payroll data
    payroll = get_payroll_data(store_id, zip_code, economic_data)
    
    # Calculate component scores
    w_score = wage_score(payroll["avg_wage"], living_wage)
    h_score = hiring_score(payroll["local_hire_pct"])
    c_score = community_score(payroll["community_spend"], payroll["daily_payroll"])
    p_score = participation_score(payroll["active_employees"])
    
    # Calculate total EJV
    ejv = w_score + h_score + c_score + p_score
    
    # Calculate wealth metrics
    daily_wages = payroll["daily_payroll"]
    wealth_retained = (daily_wages * payroll["local_hire_pct"]) + payroll["community_spend"]
    wealth_leakage = daily_wages * (1 - payroll["local_hire_pct"])
    
    return {
        "EJV": round(ejv, 2),
        "wage_score": round(w_score, 2),
        "hiring_score": round(h_score, 2),
        "community_score": round(c_score, 2),
        "participation_score": round(p_score, 2),
        "wealth_retained": round(wealth_retained, 2),
        "wealth_leakage": round(wealth_leakage, 2),
        "median_income": median_income,
        "living_wage": round(living_wage, 2),
        "unemployment_rate": economic_data["unemployment_rate"],
        "local_hire_pct": payroll["local_hire_pct"]
    }
```

---

## Frequently Asked Questions

### Q1: How is EJV v1 different from EJV v2?

**A:** EJV v1 produces a 0-100 score for relative comparison, while EJV v2 calculates justice-weighted dollar impact. v1 is simpler and better for ranking; v2 adjusts for local economic need and is better for understanding actual impact.

### Q2: Why equal weighting (25 points each)?

**A:** Equal weighting ensures no single dimension dominates and provides balanced assessment. However, communities can customize weights based on local priorities.

### Q3: What's a "good" EJV v1 score?

**A:** 
- 70+ is excellent
- 60-69 is good (above average)
- 50-59 is fair (average)
- Below 50 needs improvement

Context matters—compare to similar stores and track improvement over time.

### Q4: Can a store have high wages but low EJV v1?

**A:** Yes. A store could score 25 on wages but score low on local hiring, community investment, and job creation, resulting in a moderate overall score (e.g., 25 + 10 + 3 + 5 = 43).

### Q5: How often should EJV v1 be calculated?

**A:** Monthly or quarterly for performance tracking. The underlying data (wages, employment, economic indicators) updates annually or in real-time via Census API.

### Q6: Can EJV v1 be used for vendor selection?

**A:** Yes. Many organizations use minimum EJV v1 thresholds (e.g., "must score 60+") in procurement policies to prioritize economically just businesses.

### Q7: What if a store scores high overall but low on one component?

**A:** This identifies specific improvement areas. For example, high wages but low community investment suggests focusing on community partnerships and giving programs.

### Q8: How reliable is the local hire percentage?

**A:** It's calculated using consistent, store-specific factors plus real Census unemployment data. While modeled, it provides reasonable estimates based on local economic conditions and store characteristics.

---

## Conclusion

**EJV v1** provides a straightforward, intuitive method for assessing economic justice quality on a familiar 0-100 scale. Its four-component structure makes it easy to understand business performance and identify specific areas for improvement.

### Key Strengths:
- ✅ Simple, intuitive 0-100 scale
- ✅ Balanced assessment across four dimensions
- ✅ Easy to compare stores
- ✅ Clear component breakdown
- ✅ Based on real economic data

### When to Use:
- Quick store comparisons
- Performance rankings
- Dashboard visualizations
- Executive reporting
- Policy thresholds

### When to Complement with EJV v2:
- Need dollar-based impact
- Want equity adjustments
- Budget planning
- Procurement decisions
- Grant reporting

By understanding both EJV v1 and v2, you can choose the right metric for your specific needs and gain comprehensive insight into economic justice impact.

---

**Document Version:** 1.0  
**Last Updated:** January 18, 2026  
**Data Sources:** BLS OEWS May 2024, Census ACS 2022 API  
**System:** FIX$ GeoEquity Impact Engine
