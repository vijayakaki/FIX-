# FIX$ Application - Complete Documentation
## Economic Justice Value (EJV) Calculation System - Full Technical Reference

**Last Updated:** January 30, 2026  
**Version:** 4.2 (includes v2 baseline, v4.1 decomposed flows, v4.2 participation amplification)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Application Architecture](#application-architecture)
3. [Data Sources](#data-sources)
4. [EJV Version Overview](#ejv-version-overview)
5. [Score Components (4 Core Scores)](#score-components-4-core-scores)
6. [EJV v2: 9 Justice Dimensions](#ejv-v2-9-justice-dimensions)
7. [EJV v4.1: 5 Decomposed Components](#ejv-v41-5-decomposed-components)
8. [EJV v4.2: Participation Amplification](#ejv-v42-participation-amplification)
9. [Integration Across Pages](#integration-across-pages)
10. [Complete Calculation Flow](#complete-calculation-flow)
11. [API Endpoints](#api-endpoints)
12. [Frontend Implementation](#frontend-implementation)

---

## Executive Summary

The FIX$ application is a comprehensive Economic Justice Value (EJV) calculation engine that measures and compares the local economic impact of businesses across multiple dimensions. The system uses real government data combined with economic modeling to provide actionable insights for consumers, businesses, and policymakers.

### Key Features:
- **Multi-version EJV calculations** (v2, v4.1, v4.2) for different use cases
- **Real-time data integration** from government sources (BLS, Census)
- **4 core score components** that measure fundamental economic impacts
- **9 justice dimensions** that capture equity and community benefit
- **5 decomposed flow components** that track where money goes
- **Participation amplification** that rewards civic engagement
- **Geographic comparison** tools for location-based decisions
- **User dashboard** for tracking personal impact

---

## Application Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                     FIX$ Application                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Frontend (index.html)                                      │
│  ├── Landing Page (Module Selection)                       │
│  ├── User Dashboard (Personal Impact Tracking)             │
│  ├── Locator (Search & Compare Stores)                     │
│  ├── Compare (Side-by-Side Analysis)                       │
│  └── Optimize (Future: Route Planning)                     │
│                                                             │
│  Backend (app.py / api/index.py)                           │
│  ├── EJV Calculation Engine                                │
│  ├── Data Integration (BLS, Census)                        │
│  ├── Store Analysis                                        │
│  └── User Management                                        │
│                                                             │
│  Database (database.py)                                     │
│  ├── User Accounts                                          │
│  ├── Sessions                                               │
│  └── Purchase History                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘

External Data Sources:
├── Bureau of Labor Statistics (BLS) OEWS
├── U.S. Census ACS
├── OpenStreetMap (OSM)
└── Nominatim Geocoding
```

### Technology Stack

**Frontend:**
- Pure HTML5, CSS3, JavaScript (ES6+)
- Leaflet.js for interactive maps
- No heavy frameworks for maximum portability

**Backend:**
- Python 3.9+
- Flask web framework
- SQLite database
- Requests library for API calls

**Data Sources:**
- Bureau of Labor Statistics (BLS) OEWS API
- U.S. Census Bureau ACS API
- OpenStreetMap Overpass API
- Nominatim Geocoding Service

---

## Data Sources

### 1. Bureau of Labor Statistics (BLS) - Occupational Employment and Wage Statistics (OEWS)

**Purpose:** Provides real wage data for different occupations and industries

**Data Used:**
- Median hourly wages by occupation (SOC codes)
- Industry-specific wage rates (NAICS codes)
- Updated: May 2024 (most recent publication)

**Example SOC Codes Used:**
- `41-2031`: Retail Salespersons ($15.02/hr)
- `53-7064`: Packers and Packagers, Hand ($17.02/hr)
- `29-2052`: Pharmacy Technicians ($18.79/hr)
- `35-3031`: Waiters and Waitresses ($15.15/hr)
- `35-3023`: Fast Food Workers ($14.33/hr)

**API Endpoint:** `https://www.bls.gov/oes/current/oes_nat.htm`

**Integration:** Used in `get_bls_wage_data()` function in app.py

---

### 2. U.S. Census Bureau - American Community Survey (ACS)

**Purpose:** Provides demographic and economic data at ZIP code level

**Data Used:**
- Unemployment rate by ZIP code
- Median household income by ZIP code
- Updated: 2022 5-Year Estimates

**API Endpoint:** `https://api.census.gov/data/2022/acs/acs5/profile`

**Query Parameters:**
- `DP03_0005PE`: Unemployment rate (percentage)
- `DP03_0062E`: Median household income (dollars)

**Integration:** Used in `get_local_economic_indicators()` function in app.py

**Example Response:**
```json
{
  "unemployment_rate": 5.2,
  "median_income": 62500
}
```

---

### 3. OpenStreetMap (OSM) - Overpass API

**Purpose:** Provides store location data and business attributes

**Data Used:**
- Store names and addresses
- Business types (shop, amenity tags)
- Geographic coordinates (lat/lon)
- Contact information (websites, phones)

**API Endpoint:** `https://overpass-api.de/api/interpreter`

**Query Types:**
- Shop nodes (shop=supermarket, shop=convenience, etc.)
- Amenity nodes (amenity=restaurant, amenity=pharmacy, etc.)

**Integration:** Used via `/api/overpass` endpoint in backend

---

### 4. Industry Research Data (Embedded in Code)

**Purpose:** Provides typical business metrics when real-time data unavailable

**Data Used:**
- Average employees per establishment by NAICS code
- Typical supply chain patterns by business type
- Tax structure estimates by jurisdiction
- Financing patterns by business size

**Sources:**
- BLS Business Employment Dynamics
- Economic Census reports
- Industry association reports
- Academic research studies

**Integration:** Stored in `INDUSTRY_EMPLOYMENT` and related constants in app.py

---

## EJV Version Overview

The FIX$ application implements three versions of EJV calculations, each serving different purposes:

### Version Comparison Table

| Version | Purpose | Input Data | Output Metric | Use Case |
|---------|---------|------------|---------------|----------|
| **EJV v2** | Justice-weighted baseline | Government data only | 9 dimensions (0-100%) | Objective comparison, LOCATOR |
| **EJV v4.1** | Decomposed local flows | Gov data + estimates | ELVR ($), EVL ($) | Detailed analysis, LOCATOR advanced |
| **EJV v4.2** | Participation amplified | v4.1 + verified actions | Amplified ELVR ($) | ENGAGE workflow only |

### When Each Version Is Used

**EJV v2 (9 Dimensions Baseline):**
- Primary display in LOCATOR module
- Used as "justice score" component in v4.1
- Always calculated first as foundation
- No estimates, government data only

**EJV v4.1 (Decomposed Flows):**
- Called by `/api/ejv-v4.1/<store_id>` endpoint
- Returns ELVR (Estimated Local Value Retained)
- Returns EVL (Estimated Value Leakage)
- Includes v2 baseline in response
- Optional advanced view in LOCATOR

**EJV v4.2 (Participation Amplification):**
- Only used in ENGAGE workflow
- Never shown in LOCATOR
- Requires verified participation data
- Applies PAF multiplier to v4.1 ELVR

---

## Score Components (4 Core Scores)

The foundation of all EJV calculations rests on four core score components. Each component measures a fundamental aspect of economic justice and is scored from 0 to 25 points.

### 1. Wage Score (0-25 points)

**What It Measures:** How well the business pays its employees relative to the local cost of living

**Formula:**
```python
def wage_score(avg_wage, living_wage):
    return min(25, (avg_wage / living_wage) * 25)
```

**Inputs:**
- `avg_wage`: Average hourly wage paid by the business (from BLS + store variance)
- `living_wage`: Living wage for the area (calculated from median income)

**Living Wage Calculation:**
```python
def living_wage(median_income):
    return (median_income / 2080) * 0.35
```
- 2080 = working hours per year (40 hrs/week × 52 weeks)
- 0.35 = 35% of median income hourly rate

**Example:**
```
Store: Walmart Supercenter
Median Income: $60,000
Living Wage: ($60,000 / 2080) * 0.35 = $10.10/hr
Avg Wage (from BLS + variance): $16.50/hr
Wage Score: min(25, ($16.50 / $10.10) * 25) = 25.00
```

**Interpretation:**
- 25 points: Pays 100%+ of living wage (excellent)
- 20 points: Pays 80% of living wage (good)
- 15 points: Pays 60% of living wage (fair)
- <10 points: Pays <40% of living wage (poor)

**Data Sources:**
1. **Base Wage:** BLS OEWS May 2024 by SOC code
2. **Store Variance:** ±35% based on store_id hash (simulates individual store differences)
3. **Median Income:** Census ACS 2022 by ZIP code

---

### 2. Hiring Score (0-25 points)

**What It Measures:** Percentage of employees hired from the local community, adjusted for social vulnerability

**Formula:**
```python
def hiring_score(local_hire_pct, svi=0.7):
    return min(25, local_hire_pct * 25 * (1 + svi))
```

**Inputs:**
- `local_hire_pct`: Percentage of employees living locally (0.0-1.0)
- `svi`: Social Vulnerability Index (default 0.7, representing typical community needs)

**Local Hire Percentage Calculation:**
```python
# Base: 40%-95% (store-specific)
base_local_hire = 0.40 + (0.55 * random_seed(store_id))

# Unemployment bonus: +0-20%
unemployment_factor = min(unemployment_rate / 10.0, 0.20)

# Final calculation
local_hire_pct = min(0.98, base_local_hire + unemployment_factor)
```

**Example:**
```
Store: Target
Base Local Hire: 65%
Unemployment Rate: 8.0%
Unemployment Factor: 8.0 / 10.0 = 0.80 → +16%
Local Hire %: 65% + 16% = 81%
SVI: 0.7
Hiring Score: min(25, 0.81 * 25 * (1 + 0.7)) = 25.00
```

**Interpretation:**
- 25 points: 85%+ local hiring with high SVI (excellent)
- 20 points: 70%+ local hiring (good)
- 15 points: 55%+ local hiring (fair)
- <10 points: <40% local hiring (poor)

**Data Sources:**
1. **Base Pattern:** Store-specific seed generates consistent pattern
2. **Unemployment Rate:** Census ACS 2022 by ZIP code (DP03_0005PE)
3. **SVI:** Social Vulnerability Index (currently fixed at 0.7)

---

### 3. Community Score (0-25 points)

**What It Measures:** How much the business reinvests in local community services and infrastructure

**Formula:**
```python
def community_score(community_spend, payroll):
    return min(25, (community_spend / payroll) * 25)
```

**Inputs:**
- `community_spend`: Daily spending on community programs, donations, local services
- `payroll`: Daily total payroll

**Community Spend Calculation:**
```python
# Based on store profitability and local conditions
base_community_ratio = 0.05  # 5% of payroll baseline
community_spend = daily_payroll * base_community_ratio * (1 + store_variance)
```

**Typical Ratios by Business Type:**
- Local cooperatives: 8-12% of payroll
- Local small businesses: 5-8% of payroll
- Regional chains: 3-5% of payroll
- National chains: 1-3% of payroll
- Large corporations: 0.5-2% of payroll

**Example:**
```
Store: Local Food Co-op
Daily Payroll: $3,200
Community Spend Ratio: 9%
Community Spend: $3,200 * 0.09 = $288
Community Score: min(25, ($288 / $3,200) * 25) = 22.50
```

**Interpretation:**
- 25 points: Spends 100%+ of payroll on community (exceptional)
- 20 points: Spends 80%+ of payroll on community (excellent)
- 15 points: Spends 60%+ of payroll on community (good)
- <10 points: Spends <40% of payroll on community (fair/poor)

**Data Sources:**
1. **Base Ratio:** Industry research and store type
2. **Store Variance:** Simulates individual store community commitment
3. **Payroll Data:** Calculated from BLS wages × employee count

---

### 4. Participation Score (0-25 points)

**What It Measures:** Scale of workforce participation and employment opportunities provided

**Formula:**
```python
def participation_score(active_employees, benchmark=25):
    return min(25, (active_employees / benchmark) * 25)
```

**Inputs:**
- `active_employees`: Number of employees at the store
- `benchmark`: Reference size (25 employees = typical community impact)

**Active Employees Calculation:**
```python
# From industry data + store variance
base_employees = INDUSTRY_EMPLOYMENT[naics_code]['avg_employees']
variance = (random_seed(store_id) - 0.5) * 1.20  # ±60%
active_employees = int(base_employees * (1 + variance))
active_employees = max(3, active_employees)  # Minimum 3 employees
```

**Industry Averages (from BLS Business Employment Dynamics):**
- Supermarkets: 48 employees
- Warehouse Clubs: 72 employees
- Convenience Stores: 9 employees
- Pharmacies: 21 employees
- Restaurants: 17 employees
- Clothing Stores: 14 employees
- Department Stores: 58 employees

**Example:**
```
Store: Kroger Supermarket
Industry Average: 48 employees
Store Variance: +25%
Active Employees: 48 * 1.25 = 60
Benchmark: 25
Participation Score: min(25, (60 / 25) * 25) = 25.00
```

**Interpretation:**
- 25 points: 25+ employees (maximum community participation)
- 20 points: 20 employees (good participation)
- 15 points: 15 employees (fair participation)
- <10 points: <10 employees (limited participation)

**Data Sources:**
1. **Industry Averages:** BLS Business Employment Dynamics
2. **Store Variance:** Simulates store-specific size differences
3. **NAICS Code:** Derived from store type/category

---

### Score Components Summary

**Total Possible Score: 100 points (25 per component)**

**Typical Score Distributions:**
- Local cooperatives/small businesses: 75-95 points
- Regional chains: 60-80 points
- National chains: 50-70 points
- Large corporations: 40-60 points

**How Scores Are Used:**

1. **EJV v2 (9 Dimensions):** Scores are normalized to 0-1 and mapped to dimensions
2. **EJV v4.1 (Decomposed Flows):** Scores inform local capture estimates
3. **Dashboard Display:** Shown as individual components (0-25 each)
4. **Justice Score:** Average of all adjusted dimension scores × 100

---

## EJV v2: 9 Justice Dimensions

EJV v2 transforms the 4 core scores into 9 comprehensive justice dimensions, adjusted for local economic conditions to ensure fair comparison across different communities.

### Architecture

```
4 Core Scores → 9 Justice Dimensions → ZIP Need Modifier → Justice Score (0-100)
```

### The 9 Dimensions

#### 1. AES - Access to Essential Services

**Definition:** Local reinvestment in essential community services and infrastructure

**Calculation:**
```python
dimensions["AES"] = community_score / 25  # Normalized 0-1
```

**What It Captures:**
- Community programs funding
- Local infrastructure support
- Essential services access
- Public service investment

**ZIP Need Modifier Applied:** Yes (×0.80 to ×1.10)
- Higher modifier in underserved areas
- Recognizes greater need for essential services
- Formula: `NM_AES = base_modifier × 1.05`

**Example:**
```
Community Score: 18.5 / 25
Base Dimension: 0.74 (74%)
ZIP Unemployment: 9.0%
ZIP Median Income: $45,000
Need Modifier: 1.06 (high need area)
Adjusted AES: 0.74 × 1.06 = 0.78 (78%)
```

---

#### 2. ART - Access to Resources & Technology

**Definition:** Wage levels that enable access to technology, education, and resources

**Calculation:**
```python
dimensions["ART"] = wage_score / 25  # Normalized 0-1
```

**What It Captures:**
- Wage adequacy for tech access
- Educational resource affordability
- Digital divide mitigation
- Resource accessibility

**ZIP Need Modifier Applied:** Yes (×0.80 to ×1.10)
- Higher in areas with lower tech access
- Formula: `NM_ART = base_modifier × 1.02`

**Example:**
```
Wage Score: 22.0 / 25
Base Dimension: 0.88 (88%)
Need Modifier: 0.95 (higher income area)
Adjusted ART: 0.88 × 0.95 = 0.84 (84%)
```

---

#### 3. HWI - Health, Wellness & Inclusion

**Definition:** Local hiring practices that promote community health and inclusion

**Calculation:**
```python
dimensions["HWI"] = hiring_score / 25  # Normalized 0-1
```

**What It Captures:**
- Local employment opportunities
- Community health outcomes
- Social inclusion metrics
- Workforce diversity

**ZIP Need Modifier Applied:** Yes (×0.80 to ×1.10)
- Higher in high-unemployment areas
- Formula: `NM_HWI = base_modifier × 1.03`

**Example:**
```
Hiring Score: 20.5 / 25
Base Dimension: 0.82 (82%)
Need Modifier: 1.08 (high unemployment)
Adjusted HWI: 0.82 × 1.08 = 0.89 (89%)
```

---

#### 4. PSR - Public Service Representation

**Definition:** Business participation in public services and civic life

**Calculation:**
```python
dimensions["PSR"] = community_score / 25  # Normalized 0-1
```

**What It Captures:**
- Civic engagement
- Public service support
- Government collaboration
- Community representation

**ZIP Need Modifier Applied:** No (uses base score)

**Example:**
```
Community Score: 16.0 / 25
Dimension: 0.64 (64%)
```

---

#### 5. CAI - Cultural Awareness & Inclusivity

**Definition:** Workforce diversity and cultural competence

**Calculation:**
```python
dimensions["CAI"] = participation_score / 25  # Normalized 0-1
```

**What It Captures:**
- Cultural diversity in hiring
- Inclusive workplace practices
- Community cultural engagement
- Multilingual services

**ZIP Need Modifier Applied:** No (uses base score)

**Example:**
```
Participation Score: 19.0 / 25
Dimension: 0.76 (76%)
```

---

#### 6. JCE - Job Creation/Economic Empowerment

**Definition:** Local employment opportunities and economic mobility

**Calculation:**
```python
dimensions["JCE"] = hiring_score / 25  # Normalized 0-1
```

**What It Captures:**
- Job creation rate
- Local employment access
- Economic mobility opportunities
- Workforce development

**ZIP Need Modifier Applied:** No (uses base score)

**Example:**
```
Hiring Score: 21.0 / 25
Dimension: 0.84 (84%)
```

---

#### 7. FSI - Financial Support & Investment

**Definition:** Wage and financial investment in local economy

**Calculation:**
```python
dimensions["FSI"] = wage_score / 25  # Normalized 0-1
```

**What It Captures:**
- Financial stability for workers
- Local economic investment
- Savings capability
- Financial security

**ZIP Need Modifier Applied:** No (uses base score)

**Example:**
```
Wage Score: 23.5 / 25
Dimension: 0.94 (94%)
```

---

#### 8. CED - Community Engagement & Development

**Definition:** Combined community investment and workforce participation

**Calculation:**
```python
dimensions["CED"] = (community_score + participation_score) / 50  # Average, normalized 0-1
```

**What It Captures:**
- Community development programs
- Workforce engagement
- Local partnerships
- Development initiatives

**ZIP Need Modifier Applied:** No (uses base scores)

**Example:**
```
Community Score: 17.0 / 25
Participation Score: 20.0 / 25
Dimension: (17.0 + 20.0) / 50 = 0.74 (74%)
```

---

#### 9. ESD - Education & Skill Development

**Definition:** Investment in workforce education and skill building

**Calculation:**
```python
dimensions["ESD"] = hiring_score / 25  # Normalized 0-1
```

**What It Captures:**
- Training programs
- Educational partnerships
- Skill development opportunities
- Career advancement paths

**ZIP Need Modifier Applied:** No (uses base score)

**Example:**
```
Hiring Score: 18.5 / 25
Dimension: 0.74 (74%)
```

---

### Justice Score Calculation

**Formula:**
```python
# Calculate average of all 9 adjusted dimensions
justice_score_zip = sum(adjusted_dimensions.values()) / 9 * 100
```

**Steps:**
1. Calculate 4 core scores (0-25 each)
2. Map to 9 dimensions (normalize to 0-1)
3. Apply ZIP need modifiers to AES, ART, HWI
4. Calculate average of all 9 dimensions
5. Multiply by 100 to get 0-100 scale

**Example:**
```
Adjusted Dimensions:
  AES: 0.78
  ART: 0.84
  HWI: 0.89
  PSR: 0.64
  CAI: 0.76
  JCE: 0.84
  FSI: 0.94
  CED: 0.74
  ESD: 0.74

Average: (0.78 + 0.84 + 0.89 + 0.64 + 0.76 + 0.84 + 0.94 + 0.74 + 0.74) / 9 = 0.797

Justice Score: 0.797 × 100 = 79.7
```

---

### ZIP Need Modifier Formula

**Purpose:** Adjust scores based on local economic conditions to ensure fair comparison

**Formula:**
```python
def get_zip_need_modifier(zip_code, dimension):
    unemployment_factor = min(unemployment_rate / 10.0, 1.0)
    income_factor = max(0, 1 - (median_income / 75000))
    base_modifier = 0.80 + (0.30 * ((unemployment_factor + income_factor) / 2))
    
    if dimension == "AES":
        modifier = base_modifier * 1.05
    elif dimension == "HWI":
        modifier = base_modifier * 1.03
    elif dimension == "ART":
        modifier = base_modifier * 1.02
    else:
        modifier = base_modifier
    
    return round(min(1.10, max(0.80, modifier)), 2)
```

**Range:** 0.80 (low need) to 1.10 (high need)

**Example Calculations:**

**High Need Area (Rural Mississippi):**
```
Unemployment: 12.5%
Median Income: $35,000
unemployment_factor: 1.0 (capped)
income_factor: 1.0 - (35000/75000) = 0.53
base_modifier: 0.80 + (0.30 × ((1.0 + 0.53)/2)) = 1.03

NM_AES: 1.03 × 1.05 = 1.08
NM_HWI: 1.03 × 1.03 = 1.06
NM_ART: 1.03 × 1.02 = 1.05
```

**Low Need Area (Silicon Valley):**
```
Unemployment: 3.2%
Median Income: $120,000
unemployment_factor: 0.32
income_factor: 0 (capped at 0)
base_modifier: 0.80 + (0.30 × ((0.32 + 0)/2)) = 0.85

NM_AES: 0.85 × 1.05 = 0.89
NM_HWI: 0.85 × 1.03 = 0.88
NM_ART: 0.85 × 1.02 = 0.87
```

---

### EJV v2 Complete Formula

```
EJV v2 = (P × LC) × (JS_ZIP / 100)

Where:
  P = Purchase Amount ($)
  LC = Local Capture (local_hire_pct)
  JS_ZIP = Justice Score (0-100, from 9 adjusted dimensions)
```

**Example Complete Calculation:**

```
Store: Whole Foods Market
ZIP: 90210 (Beverly Hills)
Purchase: $100

Step 1: Calculate 4 Core Scores
  Wage Score: 22.5 / 25
  Hiring Score: 18.0 / 25
  Community Score: 16.5 / 25
  Participation Score: 20.0 / 25

Step 2: Map to 9 Dimensions
  AES: 16.5/25 = 0.66
  ART: 22.5/25 = 0.90
  HWI: 18.0/25 = 0.72
  PSR: 16.5/25 = 0.66
  CAI: 20.0/25 = 0.80
  JCE: 18.0/25 = 0.72
  FSI: 22.5/25 = 0.90
  CED: (16.5+20.0)/50 = 0.73
  ESD: 18.0/25 = 0.72

Step 3: Get ZIP Need Modifiers
  Unemployment: 4.5%
  Median Income: $85,000
  NM_AES: 0.87
  NM_ART: 0.85
  NM_HWI: 0.86

Step 4: Apply Need Modifiers
  AES: 0.66 × 0.87 = 0.57
  ART: 0.90 × 0.85 = 0.77
  HWI: 0.72 × 0.86 = 0.62
  (others unchanged)

Step 5: Calculate Justice Score
  Average: (0.57 + 0.77 + 0.62 + 0.66 + 0.80 + 0.72 + 0.90 + 0.73 + 0.72) / 9 = 0.721
  JS_ZIP: 0.721 × 100 = 72.1

Step 6: Calculate EJV v2
  Local Capture: 0.68 (68% local hiring)
  EJV v2: ($100 × 0.68) × (72.1/100)
  EJV v2: $68.00 × 0.721 = $49.03

Interpretation: For every $100 spent, $49.03 creates justice-weighted local impact
```

---

## EJV v4.1: 5 Decomposed Components

EJV v4.1 breaks down transactions into five measurable components that track where money flows in the local economy. This provides a detailed picture of economic leakage vs retention.

### Architecture

```
Purchase Amount ($) → 5 Components → Weighted Sum → ELVR (retained) & EVL (leaked)
                                    ↓
                         Includes EJV v2 as Justice Weighting
```

### Core Formula

```
ELVR = P × LC_aggregate
EVL = P - ELVR

LC_aggregate = (LC_wages × 0.35) + (LC_suppliers × 0.25) + (LC_taxes × 0.15) + 
               (LC_financing × 0.15) + (LC_ownership × 0.10)
```

**Where:**
- **ELVR** = Estimated Local Value Retained ($)
- **EVL** = Estimated Value Leakage ($)
- **P** = Purchase Amount ($)
- **LC_aggregate** = Aggregate Local Capture (0-1)
- **LC_X** = Local Capture for component X (0-1)

---

### Component 1: LC_wages (35% weight)

**Definition:** Percentage of wage payments that go to workers living locally

**Formula:**
```python
def calculate_lc_wages(store_id, business_type, zip_code):
    # Get local hiring percentage from EJV v2 calculation
    local_hire_pct = get_local_hire_pct(store_id, zip_code)
    return local_hire_pct
```

**Typical Ranges by Business Type:**

| Business Type | LC_wages Range | Example |
|---------------|----------------|---------|
| Worker Cooperative | 90-95% | Local bike shop co-op: 93% |
| Local Small Business | 75-85% | Family restaurant: 80% |
| Regional Chain | 60-70% | Regional grocer: 65% |
| National Chain | 50-60% | Walmart: 55% |
| Large Corporation | 40-50% | Amazon warehouse: 45% |

**Factors Affecting LC_wages:**
1. **Commute patterns:** Workers living near store vs commuting
2. **Labor market:** Local unemployment rate affects local hiring
3. **Store size:** Larger stores draw from wider area
4. **Wage levels:** Higher wages attract workers from farther away

**Calculation Example:**
```
Store: Target (national chain)
ZIP: 10001 (Manhattan)
Base Local Hire: 55% (national chain pattern)
Unemployment Rate: 6.2%
Unemployment Bonus: 6.2/10 = 0.62 → +12.4%
LC_wages: 55% + 12.4% = 67.4%

Contribution to ELVR:
67.4% × 35% weight = 23.6% of purchase
```

---

### Component 2: LC_suppliers (25% weight)

**Definition:** Percentage of procurement and supplies sourced from local suppliers

**Formula:**
```python
def calculate_lc_suppliers(business_type):
    supplier_percentages = {
        "worker_cooperative": 0.80,      # 75-85%
        "local_small_business": 0.68,    # 60-75%
        "regional_chain": 0.45,          # 35-55%
        "national_chain": 0.30,          # 25-35%
        "large_corporation": 0.20        # 15-25%
    }
    
    base = supplier_percentages.get(business_type, 0.30)
    variance = (random_seed(store_id) - 0.5) * 0.20  # ±10%
    return max(0.15, min(0.85, base + variance))
```

**Typical Ranges by Business Type:**

| Business Type | LC_suppliers Range | Explanation |
|---------------|-------------------|-------------|
| Worker Cooperative | 75-85% | Prioritize local sourcing, community focus |
| Local Small Business | 60-75% | Mix of local & regional, relationship-based |
| Regional Chain | 35-55% | Some regional, mostly centralized |
| National Chain | 25-35% | Centralized procurement, economies of scale |
| Large Corporation | 15-25% | Global supply chains, maximum efficiency |

**Factors Affecting LC_suppliers:**
1. **Supply chain structure:** Centralized vs distributed
2. **Product type:** Fresh vs packaged goods
3. **Local supplier availability:** Urban vs rural differences
4. **Business philosophy:** Value-driven vs cost-driven

**Calculation Example:**
```
Store: Local Bakery
Business Type: local_small_business
Base LC_suppliers: 68%
Store Variance: +5%
LC_suppliers: 73%

Contribution to ELVR:
73% × 25% weight = 18.25% of purchase
```

---

### Component 3: LC_taxes (15% weight)

**Definition:** Percentage of taxes paid to local/state jurisdictions vs federal

**Formula:**
```python
def calculate_lc_taxes(business_type, zip_code):
    # Sales tax: 90-100% local/state
    sales_tax_local = 0.95
    
    # Property tax: 100% local
    property_tax_local = 1.00
    
    # Business tax: varies by structure
    business_tax_local = {
        "worker_cooperative": 0.80,
        "local_small_business": 0.75,
        "regional_chain": 0.70,
        "national_chain": 0.65,
        "large_corporation": 0.60
    }.get(business_type, 0.70)
    
    # Weighted average
    lc_taxes = (sales_tax_local * 0.50 + 
                property_tax_local * 0.30 + 
                business_tax_local * 0.20)
    
    return lc_taxes
```

**Tax Breakdown:**
- **Sales Tax:** 90-100% stays local/state (varies by state)
- **Property Tax:** 100% stays local (funds schools, services)
- **Business Income Tax:** 60-80% local/state vs federal
- **Payroll Tax:** Mostly federal (Social Security, Medicare)

**Typical Ranges:**

| Business Type | LC_taxes Range | Explanation |
|---------------|----------------|-------------|
| All Types | 75-85% | Sales & property taxes are mostly local |
| High Property | 80-90% | More property = more local tax |
| High Profit | 65-75% | More federal income tax |

**Calculation Example:**
```
Store: CVS Pharmacy
Business Type: national_chain
Sales Tax Local: 95%
Property Tax Local: 100%
Business Tax Local: 65%
LC_taxes: (0.95×0.50) + (1.00×0.30) + (0.65×0.20) = 0.605 + 0.300 + 0.130 = 80.5%

Contribution to ELVR:
80.5% × 15% weight = 12.08% of purchase
```

---

### Component 4: LC_financing (15% weight)

**Definition:** Percentage of financing costs (interest, fees) paid to local lenders

**Formula:**
```python
def calculate_lc_financing(business_type, apr=None, loan_term_months=None):
    financing_percentages = {
        "worker_cooperative": 0.85,      # Credit unions, local banks
        "local_small_business": 0.70,    # Mix of local & regional banks
        "regional_chain": 0.45,          # Regional banks, some national
        "national_chain": 0.30,          # National banks
        "large_corporation": 0.20        # Wall Street, global finance
    }
    
    base = financing_percentages.get(business_type, 0.40)
    
    # If APR provided, calculate time-weighted financing
    if apr and loan_term_months:
        # Calculate total interest over loan life
        # More interest = more financing leakage
        pass
    
    return base
```

**Typical Ranges by Business Type:**

| Business Type | LC_financing Range | Typical Lenders |
|---------------|-------------------|-----------------|
| Worker Cooperative | 80-90% | Local credit unions, community banks |
| Local Small Business | 65-75% | Local banks, SBA loans |
| Regional Chain | 40-50% | Regional banks |
| National Chain | 25-35% | National banks, bond markets |
| Large Corporation | 15-25% | Wall Street, global finance |

**Time-Aware Financing (Optional):**
When loan terms are provided, calculate cumulative interest:
```
Example: $100 purchase, 6% APR, 12 months
Monthly payment: $8.61
Total paid: $103.32
Total interest: $3.32
Interest as % of purchase: 3.32%

If financed by local bank (LC_financing = 70%):
Local financing retained: $3.32 × 70% = $2.32
```

**Calculation Example:**
```
Store: Local Hardware Store
Business Type: local_small_business
LC_financing: 70%

Contribution to ELVR:
70% × 15% weight = 10.5% of purchase
```

---

### Component 5: LC_ownership (10% weight)

**Definition:** Percentage of profit/dividends distributed to local owners vs external shareholders

**Formula:**
```python
def calculate_lc_ownership(business_type):
    ownership_percentages = {
        "worker_cooperative": 0.95,      # Workers are local owners
        "local_small_business": 0.85,    # Owner lives locally
        "regional_chain": 0.40,          # Mix of local/regional owners
        "national_chain": 0.15,          # Mostly external shareholders
        "large_corporation": 0.05        # Global shareholders
    }
    
    base = ownership_percentages.get(business_type, 0.30)
    variance = (random_seed(store_id) - 0.5) * 0.15  # ±7.5%
    return max(0.05, min(1.00, base + variance))
```

**Typical Ranges by Business Type:**

| Business Type | LC_ownership Range | Explanation |
|---------------|-------------------|-------------|
| Worker Cooperative | 90-100% | Worker-owners live locally |
| Local Small Business | 80-90% | Owner(s) live in community |
| Regional Chain | 35-45% | Some local franchisees/shareholders |
| National Chain | 10-20% | Mostly external shareholders |
| Large Corporation | 0-10% | Global institutional investors |

**Ownership Structures:**
- **Sole Proprietor:** 100% local if owner local
- **Partnership:** Percentage based on partner residency
- **Franchise:** 40-60% local (franchisee), 40-60% corporate
- **Publicly Traded:** 0-15% local (most shareholders external)
- **Worker Co-op:** 90-100% local (worker-owners)

**Calculation Example:**
```
Store: Starbucks
Business Type: large_corporation
LC_ownership: 8%

Contribution to ELVR:
8% × 10% weight = 0.8% of purchase
```

---

### LC_aggregate Calculation

**Formula:**
```python
LC_aggregate = (LC_wages × 0.35) + 
               (LC_suppliers × 0.25) + 
               (LC_taxes × 0.15) + 
               (LC_financing × 0.15) + 
               (LC_ownership × 0.10)
```

**Complete Example:**

```
Store: Whole Foods Market
Business Type: large_corporation (owned by Amazon)
Purchase: $100

Component Calculations:
1. LC_wages: 52% (national chain, adjusted for local unemployment)
2. LC_suppliers: 28% (mostly centralized procurement)
3. LC_taxes: 78% (sales + property mostly local)
4. LC_financing: 22% (corporate bonds, Wall Street)
5. LC_ownership: 6% (Amazon shareholders global)

LC_aggregate Calculation:
= (0.52 × 0.35) + (0.28 × 0.25) + (0.78 × 0.15) + (0.22 × 0.15) + (0.06 × 0.10)
= 0.182 + 0.070 + 0.117 + 0.033 + 0.006
= 0.408 (40.8%)

ELVR: $100 × 0.408 = $40.80
EVL: $100 - $40.80 = $59.20

Interpretation:
- $40.80 stays in local economy (40.8%)
- $59.20 leaves local economy (59.2%)
```

---

### Complete EJV v4.1 Output

**API Response Structure:**
```json
{
  "store_id": "store_12345",
  "business_type": "large_corporation",
  "purchase_amount": 100.00,
  "elvr": 40.80,
  "evl": 59.20,
  "retention_percentage": 40.8,
  "local_capture_components": {
    "lc_wages": 0.52,
    "lc_suppliers": 0.28,
    "lc_taxes": 0.78,
    "lc_financing": 0.22,
    "lc_ownership": 0.06,
    "lc_aggregate": 0.408
  },
  "component_contributions": {
    "wages": 18.20,
    "suppliers": 7.00,
    "taxes": 11.70,
    "financing": 3.30,
    "ownership": 0.60
  },
  "ejv_v2_baseline": {
    "EJV": 72.5,
    "justice_score_zip": 72.5,
    "dimensions": {...}
  }
}
```

---

### Business Type Comparison

**$100 Purchase Across Business Types:**

| Business Type | ELVR | EVL | Retention % |
|---------------|------|-----|-------------|
| Worker Cooperative | $87.50 | $12.50 | 87.5% |
| Local Small Business | $73.25 | $26.75 | 73.3% |
| Regional Chain | $57.40 | $42.60 | 57.4% |
| National Chain | $44.80 | $55.20 | 44.8% |
| Large Corporation | $35.20 | $64.80 | 35.2% |

**Breakdown by Component (National Chain Example):**

| Component | Weight | Local % | Contribution | Amount |
|-----------|--------|---------|--------------|--------|
| Wages | 35% | 55% | 19.25% | $19.25 |
| Suppliers | 25% | 30% | 7.50% | $7.50 |
| Taxes | 15% | 75% | 11.25% | $11.25 |
| Financing | 15% | 30% | 4.50% | $4.50 |
| Ownership | 10% | 15% | 1.50% | $1.50 |
| **Total** | **100%** | - | **44.00%** | **$44.00** |

---

## EJV v4.2: Participation Amplification

EJV v4.2 builds on v4.1 by applying a Participation Amplification Factor (PAF) that rewards businesses for verified civic engagement through five participation pathways.

### Architecture

```
EJV v4.1 (ELVR) → PAF (1.0-1.25) → EJV v4.2 (Amplified ELVR)
                   ↑
         5 Participation Pathways
```

### Core Formula

```
ELVR v4.2 = ELVR v4.1 × PAF

PAF = 1.0 + min(Σ(pathway_contributions), 0.25)
```

**Where:**
- **ELVR v4.1** = Base local value retained from decomposed flows
- **PAF** = Participation Amplification Factor (1.0 to 1.25)
- **ELVR v4.2** = Amplified local value through participation

**PAF Range:**
- **1.00** = No participation (neutral, no amplification)
- **1.10** = Moderate participation (10% amplification)
- **1.20** = Strong participation (20% amplification)
- **1.25** = Maximum participation (25% amplification, all 5 pathways active)

---

### The 5 Participation Pathways

#### Pathway 1: Mentoring (8% weight)

**Definition:** Youth, workforce, or entrepreneurship mentoring programs

**Parameters:**
- `hours`: Hours per week committed to mentoring
- `verified`: Boolean - Is this verified by third party?
- `duration_months`: How many months sustained?

**Calculation:**
```python
base_weight = 0.08  # 8% of PAF
intensity = min(hours / 10.0, 1.0)  # Normalize to 0-1
verification_multiplier = 1.2 if verified else 1.0
duration_factor = min(duration_months / 12.0, 1.0)

contribution = base_weight × intensity × verification_multiplier × duration_factor
```

**Example:**
```
Program: Youth Career Mentoring
Hours/week: 3
Verified: Yes (by local school district)
Duration: 12 months

intensity: 3 / 10 = 0.30
verification: 1.2
duration: 12 / 12 = 1.00

contribution: 0.08 × 0.30 × 1.2 × 1.00 = 0.0288 (2.88%)
```

**Best Practices:**
- Partner with schools, community colleges
- Verified programs carry 20% bonus
- Sustained effort (12+ months) maximizes impact

---

#### Pathway 2: Volunteering (6% weight)

**Definition:** Employee time volunteering, skills-based service, board participation

**Parameters:**
- `hours`: Hours per week of volunteer time
- `verified`: Boolean - Verified by nonprofit?
- `duration_months`: Duration of commitment

**Calculation:**
```python
base_weight = 0.06  # 6% of PAF
intensity = min(hours / 10.0, 1.0)
verification_multiplier = 1.2 if verified else 1.0
duration_factor = min(duration_months / 12.0, 1.0)

contribution = base_weight × intensity × verification_multiplier × duration_factor
```

**Example:**
```
Program: Food Bank Volunteering
Hours/week: 4
Verified: Yes (by food bank)
Duration: 12 months

intensity: 4 / 10 = 0.40
verification: 1.2
duration: 12 / 12 = 1.00

contribution: 0.06 × 0.40 × 1.2 × 1.00 = 0.0288 (2.88%)
```

**Types of Volunteering:**
- Skills-based (accounting, legal, IT)
- Direct service (food bank, shelter)
- Board service (nonprofit governance)
- Pro bono professional services

---

#### Pathway 3: Community Sponsorship (5% weight)

**Definition:** Sponsoring youth sports, community orgs, local events

**Parameters:**
- `annual_commitment`: Annual financial or in-kind commitment
- `verified`: Boolean - Verified by recipient?
- `duration_months`: Length of commitment

**Calculation:**
```python
base_weight = 0.05  # 5% of PAF
intensity = min(annual_commitment / 10000, 1.0)  # $10k = max
verification_multiplier = 1.2 if verified else 1.0
duration_factor = min(duration_months / 12.0, 1.0)

contribution = base_weight × intensity × verification_multiplier × duration_factor
```

**Example:**
```
Sponsorship: Little League Team
Annual Commitment: $5,000 + uniforms
Verified: Yes (by league)
Duration: 24 months (2 years)

intensity: 5000 / 10000 = 0.50
verification: 1.2
duration: 24 / 12 = 1.00 (capped)

contribution: 0.05 × 0.50 × 1.2 × 1.00 = 0.0300 (3.00%)
```

**Sponsorship Examples:**
- Youth sports teams
- Community festivals
- Arts organizations
- Educational programs

---

#### Pathway 4: Apprenticeships & Training (4% weight)

**Definition:** Structured workforce development, paid apprenticeships, training programs

**Parameters:**
- `positions`: Number of apprenticeship/trainee positions
- `verified`: Boolean - Verified by program?
- `duration_months`: Program duration

**Calculation:**
```python
base_weight = 0.04  # 4% of PAF
intensity = min(positions / 5.0, 1.0)  # 5 positions = max
verification_multiplier = 1.2 if verified else 1.0
duration_factor = min(duration_months / 12.0, 1.0)

contribution = base_weight × intensity × verification_multiplier × duration_factor
```

**Example:**
```
Program: Paid Internship Program
Positions: 3 interns
Verified: Yes (by department of labor)
Duration: 10 months

intensity: 3 / 5 = 0.60
verification: 1.2
duration: 10 / 12 = 0.83

contribution: 0.04 × 0.60 × 1.2 × 0.83 = 0.0239 (2.39%)
```

**Program Types:**
- Registered apprenticeships
- Paid internships
- Job training partnerships
- On-the-job training

---

#### Pathway 5: Community Facilities Support (2% weight)

**Definition:** Providing space, resources, or infrastructure for community use

**Parameters:**
- `availability`: Hours per week facility available
- `verified`: Boolean - Verified by users?
- `duration_months`: Length of commitment

**Calculation:**
```python
base_weight = 0.02  # 2% of PAF
intensity = min(availability / 20.0, 1.0)  # 20 hrs/week = max
verification_multiplier = 1.2 if verified else 1.0
duration_factor = min(duration_months / 12.0, 1.0)

contribution = base_weight × intensity × verification_multiplier × duration_factor
```

**Example:**
```
Program: Community Meeting Room
Availability: 15 hrs/week
Verified: No (self-reported)
Duration: 12 months

intensity: 15 / 20 = 0.75
verification: 1.0
duration: 12 / 12 = 1.00

contribution: 0.02 × 0.75 × 1.0 × 1.00 = 0.0150 (1.50%)
```

**Facilities Examples:**
- Meeting spaces
- Parking lots for events
- Equipment lending
- Wifi access for community

---

### PAF Calculation Example

**Complete Participation Profile:**

```
Business: Local Bike Shop Cooperative

Pathway 1 - Mentoring:
  Program: Youth cycling safety education
  Hours/week: 3
  Verified: Yes
  Duration: 12 months
  Contribution: 0.0288 (2.88%)

Pathway 2 - Volunteering:
  Program: Trail maintenance volunteers
  Hours/week: 2
  Verified: Yes
  Duration: 12 months
  Contribution: 0.0144 (1.44%)

Pathway 3 - Sponsorship:
  Sponsorship: High school cycling team
  Commitment: $3,000/year
  Verified: Yes
  Duration: 12 months
  Contribution: 0.0180 (1.80%)

Pathway 4 - Apprenticeships:
  Program: Bike mechanic apprenticeship
  Positions: 2
  Verified: Yes
  Duration: 10 months
  Contribution: 0.0192 (1.92%)

Pathway 5 - Facilities:
  Support: Bike repair space for community
  Hours: 8/week
  Verified: No
  Duration: 12 months
  Contribution: 0.0080 (0.80%)

Total Contribution: 0.0884 (8.84%)
PAF: 1.0 + 0.0884 = 1.0884 (≈1.09)
```

---

### Complete EJV v4.2 Calculation

**Example:**

```
Store: Local Bike Shop
Business Type: worker_cooperative
Purchase: $100

Step 1: Calculate EJV v4.1
  LC_aggregate: 0.875 (87.5%)
  ELVR v4.1: $100 × 0.875 = $87.50

Step 2: Calculate PAF
  5 active pathways (see above)
  Total contribution: 8.84%
  PAF: 1.0884

Step 3: Calculate EJV v4.2
  ELVR v4.2: $87.50 × 1.0884 = $95.24
  Amplification Value: $95.24 - $87.50 = $7.74

Step 4: Interpret
  Base local retention: $87.50 (87.5%)
  Participation adds: $7.74 (8.84%)
  Total amplified: $95.24 (95.24%)
  
  "For $100 spent with comprehensive civic engagement, 
   $95.24 creates justice-weighted community impact."
```

---

### Maximum Participation Example

**All 5 Pathways at Maximum:**

```
Pathway 1 - Mentoring: 10 hrs/week, verified, 12 months
  Contribution: 0.08 × 1.0 × 1.2 × 1.0 = 0.0960 (9.60%)

Pathway 2 - Volunteering: 10 hrs/week, verified, 12 months
  Contribution: 0.06 × 1.0 × 1.2 × 1.0 = 0.0720 (7.20%)

Pathway 3 - Sponsorship: $10k/year, verified, 12 months
  Contribution: 0.05 × 1.0 × 1.2 × 1.0 = 0.0600 (6.00%)

Pathway 4 - Apprenticeships: 5 positions, verified, 12 months
  Contribution: 0.04 × 1.0 × 1.2 × 1.0 = 0.0480 (4.80%)

Pathway 5 - Facilities: 20 hrs/week, verified, 12 months
  Contribution: 0.02 × 1.0 × 1.2 × 1.0 = 0.0240 (2.40%)

Total: 0.3000 (30.00%)
Capped at: 0.25 (25.00%)
PAF: 1.25 (maximum amplification)
```

---

### Participation vs No Participation

**Comparison for Same Store:**

| Scenario | ELVR v4.1 | PAF | ELVR v4.2 | Amplification |
|----------|-----------|-----|-----------|---------------|
| No Participation | $75.00 | 1.00 | $75.00 | $0.00 (0%) |
| Moderate (2 pathways) | $75.00 | 1.08 | $81.00 | $6.00 (8%) |
| Strong (4 pathways) | $75.00 | 1.18 | $88.50 | $13.50 (18%) |
| Maximum (5 pathways) | $75.00 | 1.25 | $93.75 | $18.75 (25%) |

**Key Insight:** Participation can increase local impact by up to 25%, regardless of business size or type. This rewards civic engagement and community agency.

---

## Integration Across Pages

The FIX$ application uses different EJV versions strategically across its four main modules.

### 1. User Dashboard

**Purpose:** Personal impact tracking and civic engagement

**EJV Versions Used:**
- **v2**: Shows justice dimensions for awareness
- **v4.2**: Primary metric (with participation amplification)

**Data Displayed:**
- Total EJV v4.2 from all purchases
- Breakdown by store
- Participation score
- Civic actions log
- Impact over time graphs

**API Calls:**
```javascript
// When user logs purchase
POST /api/user/purchase
{
  "storeName": "Local Co-op",
  "amount": 45.00,
  "category": "Groceries",
  "date": "2026-01-30"
}

// Response includes EJV v4.2 with participation
{
  "ejv_v42": 38.50,
  "elvr_base": 35.00,
  "paf": 1.10,
  "participation_bonus": 3.50
}
```

**How Participation Is Tracked:**
- User logs civic actions (volunteering, mentoring, etc.)
- Points accumulate into participation score
- PAF calculated from logged actions
- Applied to all purchases for amplification

---

### 2. Locator Module

**Purpose:** Search, discover, and compare stores in a geographic area

**EJV Versions Used:**
- **v2**: Primary display (objective, government data only)
- **v4.1**: Advanced view (optional, detailed breakdown)

**Why v2 for Primary Display:**
- Based only on government data (BLS, Census)
- No estimates or third-party data needed
- Fair comparison across all businesses
- Justice dimensions provide comprehensive view

**Data Displayed:**
- Map with stores color-coded by EJV v2
- Right dashboard showing:
  - EJV v2 baseline (9 dimensions)
  - EJV v4.1 advanced (5 components, ELVR/EVL)
  - 4 core scores
  - Justice score
  - Local retention/leakage percentages

**API Calls:**
```javascript
// Search for stores
POST /api/overpass
{
  "lat": 34.7304,
  "lon": -86.5861,
  "radius": 5000,
  "shop_type": "supermarket"
}

// Calculate EJV for each store
GET /api/ejv-v4.1/<store_id>?zip=35801

// Response includes both v2 and v4.1
{
  "elvr": 65.50,
  "evl": 34.50,
  "retention_percentage": 65.5,
  "ejv_v2_baseline": {
    "EJV": 72.5,
    "dimensions": {...},
    "wage_score": 18.5,
    "hiring_score": 20.0,
    "community_score": 16.5,
    "participation_score": 17.5
  },
  "local_capture_components": {...}
}
```

**User Flow:**
1. Enter ZIP code or address
2. Select store category
3. View results on map
4. Hover over store → see EJV v2 score
5. Click store → open right dashboard
6. View detailed breakdown (v2 + v4.1)
7. Click "Add to Compare" → save for comparison

---

### 3. Compare Module

**Purpose:** Side-by-side comparison of two stores

**EJV Versions Used:**
- **v4.1**: Primary (detailed flow comparison)
- **v2**: Secondary (justice dimensions)

**Why v4.1 for Comparison:**
- Shows exactly where money flows
- ELVR vs EVL is tangible ($)
- Component breakdown reveals differences
- Helps users understand tradeoffs

**Data Displayed:**
- Side-by-side cards for Store A and Store B
- ELVR and EVL for each
- 5-component breakdown comparison
- Justice dimensions comparison
- Difference calculation
- Recommendation based on highest ELVR

**API Calls:**
```javascript
// Load Store A
GET /api/ejv-v4.1/<store_a_id>?zip=35801

// Load Store B  
GET /api/ejv-v4.1/<store_b_id>?zip=35801

// Both return full v4.1 + v2 data
```

**Comparison Display Example:**
```
Store A: Whole Foods          Store B: Local Co-op
ELVR: $47.25 (47.3%)         ELVR: $82.50 (82.5%)
EVL: $52.75 (52.7%)          EVL: $17.50 (17.5%)

Component Breakdown:
Wages: $19.25 vs $28.00 ✓
Suppliers: $7.50 vs $17.00 ✓
Taxes: $11.70 vs $13.50 ✓
Financing: $6.30 vs $15.00 ✓
Ownership: $2.50 vs $9.00 ✓

Winner: Store B (Local Co-op)
+$35.25 more local impact (+74.6%)
```

**User Flow:**
1. Navigate to Compare module
2. Select Store A from dropdown (current search or purchase history)
3. Select Store B from dropdown
4. Click "Compare Stores"
5. View side-by-side breakdown
6. See which store has higher ELVR
7. Make informed decision

---

### 4. Optimize Module (Future)

**Purpose:** Route optimization for multiple errands

**EJV Versions Planned:**
- **v4.1**: Calculate total ELVR for route
- **v2**: Factor in justice scores

**Planned Features:**
- Input multiple shopping needs
- Find optimal route that maximizes ELVR
- Consider: distance, time, ELVR, justice score
- Suggest alternative stores with higher EJV

**Not Yet Implemented**

---

### Cross-Module Data Flow

```
┌─────────────────────────────────────────────────────────┐
│                     User Dashboard                       │
│  - Logs purchases                                        │
│  - Logs civic actions                                    │
│  - Calculates PAF from actions                           │
└────────────────┬───────────────────────────────────────┘
                 │ Stores purchase history
                 ↓
┌─────────────────────────────────────────────────────────┐
│                   Locator Module                         │
│  - Search for stores                                     │
│  - Display on map with EJV v2                            │
│  - Show detailed v4.1 in dashboard                       │
└────────────────┬───────────────────────────────────────┘
                 │ Stores search results in
                 │ window.lastSearchResults
                 ↓
┌─────────────────────────────────────────────────────────┐
│                  Compare Module                          │
│  - Loads from search results or purchase history        │
│  - Side-by-side EJV v4.1 comparison                      │
│  - Helps user choose best option                         │
└────────────────┬───────────────────────────────────────┘
                 │ User makes decision
                 │ Logs purchase
                 ↓
          Back to User Dashboard
```

---

### Data Caching Strategy

**ejvCache Object:**
```javascript
// Global cache prevents redundant API calls
ejvCache = {
  "store_12345": {
    "data": {...full EJV v4.1 response...},
    "timestamp": "2026-01-30T14:30:00Z"
  }
}
```

**When Cache Is Used:**
- Hovering over same store multiple times
- Switching between modules
- Returning to previously viewed store
- Compare module loading stores

**When Cache Is Cleared:**
- New search in Locator (clears for fresh results)
- User explicitly refreshes
- Session timeout

**Benefits:**
- Faster UI responsiveness
- Reduced API load
- Better user experience
- Consistent data within session

---

## Complete Calculation Flow

### End-to-End Example: $100 Purchase at Target

**Step 1: Store Identification**
```
Store Name: Target
OSM ID: way/123456789
Location: 2500 University Dr, Huntsville, AL 35801
ZIP: 35801
Business Type: national_chain (derived from chain detection)
```

**Step 2: Get Local Economic Data**
```
API Call: Census ACS 2022
ZIP: 35801

Response:
  Unemployment Rate: 5.8%
  Median Income: $58,500
  
Calculate Living Wage:
  Living Wage = ($58,500 / 2080) * 0.35
  Living Wage = $9.86/hr
```

**Step 3: Get Wage Data**
```
API Call: BLS OEWS May 2024
SOC Code: 41-2031 (Retail Salespersons)

Response:
  Base Wage: $15.02/hr
  
Apply Store Variance:
  Store Hash: hash("way/123456789") mod 100 = 47
  Variance: (47/100 - 0.5) * 0.70 = -0.049
  Adjusted Wage: $15.02 * (1 - 0.049) = $14.28/hr
```

**Step 4: Calculate 4 Core Scores**
```
1. Wage Score:
   Score = min(25, ($14.28 / $9.86) * 25)
   Score = min(25, 36.20)
   Score = 25.00

2. Hiring Score:
   Base Local Hire: 55% (national chain pattern)
   Unemployment Bonus: (5.8/10.0) * 0.20 = 0.116 → +11.6%
   Local Hire %: 55% + 11.6% = 66.6%
   Score = min(25, 0.666 * 25 * (1 + 0.7))
   Score = min(25, 28.31)
   Score = 25.00

3. Community Score:
   Daily Payroll: 45 employees × $14.28 × 8hr = $5,140.80
   Community Ratio: 2.5% (national chain)
   Community Spend: $5,140.80 * 0.025 = $128.52
   Score = min(25, ($128.52 / $5,140.80) * 25)
   Score = min(25, 0.625)
   Score = 0.625 × 25 = 15.63

4. Participation Score:
   Employees: 45
   Benchmark: 25
   Score = min(25, (45/25) * 25)
   Score = 25.00
```

**Step 5: Map to 9 Dimensions (EJV v2)**
```
Dimensions (normalized 0-1):
  AES: 15.63/25 = 0.625
  ART: 25.00/25 = 1.000
  HWI: 25.00/25 = 1.000
  PSR: 15.63/25 = 0.625
  CAI: 25.00/25 = 1.000
  JCE: 25.00/25 = 1.000
  FSI: 25.00/25 = 1.000
  CED: (15.63+25.00)/50 = 0.813
  ESD: 25.00/25 = 1.000
```

**Step 6: Apply ZIP Need Modifiers**
```
Calculate Base Modifier:
  unemployment_factor = 5.8/10.0 = 0.58
  income_factor = max(0, 1 - (58500/75000)) = 0.22
  base_modifier = 0.80 + (0.30 * ((0.58 + 0.22)/2))
  base_modifier = 0.80 + (0.30 * 0.40) = 0.92

Apply to Dimensions:
  NM_AES = 0.92 * 1.05 = 0.97
  NM_ART = 0.92 * 1.02 = 0.94
  NM_HWI = 0.92 * 1.03 = 0.95

Adjusted Dimensions:
  AES: 0.625 * 0.97 = 0.606
  ART: 1.000 * 0.94 = 0.940
  HWI: 1.000 * 0.95 = 0.950
  (others unchanged)
```

**Step 7: Calculate Justice Score**
```
Average of 9 Adjusted Dimensions:
  (0.606 + 0.940 + 0.950 + 0.625 + 1.000 + 1.000 + 1.000 + 0.813 + 1.000) / 9
  = 7.934 / 9
  = 0.881

Justice Score (0-100):
  JS_ZIP = 0.881 * 100 = 88.1
```

**Step 8: Calculate EJV v2**
```
Formula: EJV v2 = (P × LC) × (JS_ZIP / 100)

Purchase: $100
Local Capture: 0.666 (from hiring score calculation)
Justice Score: 88.1

EJV v2 = ($100 × 0.666) × (88.1/100)
EJV v2 = $66.60 × 0.881
EJV v2 = $58.68

Interpretation: Of $100 spent, $58.68 creates justice-weighted local impact
```

**Step 9: Calculate EJV v4.1 (Decomposed Flows)**
```
Business Type: national_chain

Component Calculations:
1. LC_wages: 0.666 (from step 4)
2. LC_suppliers: 0.30 (national chain, centralized procurement)
3. LC_taxes: 0.75 (sales + property mostly local)
4. LC_financing: 0.28 (national banks)
5. LC_ownership: 0.12 (publicly traded, global shareholders)

LC_aggregate:
  = (0.666 × 0.35) + (0.30 × 0.25) + (0.75 × 0.15) + (0.28 × 0.15) + (0.12 × 0.10)
  = 0.2331 + 0.075 + 0.1125 + 0.042 + 0.012
  = 0.4746 (47.46%)

ELVR: $100 × 0.4746 = $47.46
EVL: $100 - $47.46 = $52.54

Component Contributions:
  Wages: $23.31
  Suppliers: $7.50
  Taxes: $11.25
  Financing: $4.20
  Ownership: $1.20
```

**Step 10: Calculate EJV v4.2 (with Participation)**
```
Assume User Has Logged Participation:
  Pathway 1 (Mentoring): 0.020 (2.0%)
  Pathway 2 (Volunteering): 0.015 (1.5%)
  Total: 0.035 (3.5%)

PAF: 1.0 + 0.035 = 1.035

ELVR v4.2: $47.46 × 1.035 = $49.12
Amplification: $49.12 - $47.46 = $1.66

Interpretation: User's civic participation added $1.66 (3.5%) to local impact
```

**Final Summary:**
```
$100 Purchase at Target (Huntsville, AL)

EJV Metrics:
  EJV v2: $58.68 (justice-weighted baseline)
  EJV v4.1 ELVR: $47.46 (local retained)
  EJV v4.1 EVL: $52.54 (external leakage)
  EJV v4.2 ELVR: $49.12 (with participation)

Justice Dimensions (9):
  AES: 60.6% | ART: 94.0% | HWI: 95.0%
  PSR: 62.5% | CAI: 100% | JCE: 100%
  FSI: 100% | CED: 81.3% | ESD: 100%
  Average: 88.1%

Core Scores (4):
  Wage: 25.00 / 25
  Hiring: 25.00 / 25
  Community: 15.63 / 25
  Participation: 25.00 / 25
  Total: 90.63 / 100

Local Capture Components (5):
  Wages: 66.6% → $23.31
  Suppliers: 30.0% → $7.50
  Taxes: 75.0% → $11.25
  Financing: 28.0% → $4.20
  Ownership: 12.0% → $1.20
  Aggregate: 47.46% → $47.46

Data Sources:
  - BLS OEWS May 2024 (wages)
  - Census ACS 2022 (demographics)
  - OSM (store data)
  - Industry research (business patterns)
```

---

## API Endpoints

### Base URL
```
Development: http://localhost:5000
Production: https://fixapp.vercel.app
```

### Authentication Endpoints

#### POST /api/register
Register a new user account

**Request:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure123",
  "full_name": "John Doe"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User registered successfully",
  "user_id": 42
}
```

---

#### POST /api/login
Login to existing account

**Request:**
```json
{
  "username": "john_doe",
  "password": "secure123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Login successful",
  "session_token": "abc123xyz...",
  "user": {
    "id": 42,
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe"
  },
  "expires_at": "2026-02-06T14:30:00Z"
}
```

---

#### POST /api/logout
Logout and invalidate session

**Request:**
```json
{
  "session_token": "abc123xyz..."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Logout successful"
}
```

---

### EJV Calculation Endpoints

#### GET /api/ejv-v4.1/<store_id>
Get complete EJV v4.1 analysis (includes v2 baseline)

**Parameters:**
- `store_id`: Store identifier (OSM ID or custom)
- `zip`: ZIP code (query param, optional, default: 10001)
- `location`: Location name (query param, optional)
- `purchase`: Purchase amount (query param, optional, default: 100.00)
- `business_type`: Business type override (query param, optional)

**Example:**
```
GET /api/ejv-v4.1/way123456789?zip=35801&purchase=100&business_type=national_chain
```

**Response:**
```json
{
  "store_id": "way123456789",
  "location": "Huntsville, AL",
  "zip_code": "35801",
  "ejv_version": "4.1",
  "purchase_amount": 100.00,
  "elvr": 47.46,
  "evl": 52.54,
  "retention_percentage": 47.5,
  "business_type": "national_chain",
  "local_capture_components": {
    "lc_wages": 0.666,
    "lc_suppliers": 0.30,
    "lc_taxes": 0.75,
    "lc_financing": 0.28,
    "lc_ownership": 0.12,
    "lc_aggregate": 0.4746
  },
  "component_contributions": {
    "wages": 23.31,
    "suppliers": 7.50,
    "taxes": 11.25,
    "financing": 4.20,
    "ownership": 1.20
  },
  "ejv_v2_baseline": {
    "EJV": 88.1,
    "justice_score_zip": 88.1,
    "wage_score": 25.00,
    "hiring_score": 25.00,
    "community_score": 15.63,
    "participation_score": 25.00,
    "dimensions": {
      "AES": 0.625,
      "ART": 1.000,
      "HWI": 1.000,
      "PSR": 0.625,
      "CAI": 1.000,
      "JCE": 1.000,
      "FSI": 1.000,
      "CED": 0.813,
      "ESD": 1.000
    },
    "adjusted_dimensions": {
      "AES": 0.606,
      "ART": 0.940,
      "HWI": 0.950,
      "PSR": 0.625,
      "CAI": 1.000,
      "JCE": 1.000,
      "FSI": 1.000,
      "CED": 0.813,
      "ESD": 1.000
    },
    "zip_modifiers": {
      "AES": 0.97,
      "ART": 0.94,
      "HWI": 0.95
    },
    "unemployment_rate": 5.8,
    "median_income": 58500,
    "living_wage": 9.86
  }
}
```

---

#### POST /api/ejv-v4.2/<store_id>
Get EJV v4.2 with participation amplification

**Request:**
```json
{
  "zip": "35801",
  "location": "Huntsville, AL",
  "purchase": 100.00,
  "business_type": "national_chain",
  "participation": {
    "mentoring": {
      "hours": 3,
      "verified": true,
      "duration_months": 12
    },
    "volunteering": {
      "hours": 2,
      "verified": true,
      "duration_months": 12
    }
  }
}
```

**Response:**
```json
{
  "store_id": "way123456789",
  "location": "Huntsville, AL",
  "zip_code": "35801",
  "version": "4.2",
  "ejv_v42": {
    "elvr_amplified": 49.12,
    "elvr_base": 47.46,
    "amplification_factor": 1.035,
    "amplification_value": 1.66,
    "retention_percentage": 49.1,
    "formula": "ELVR v4.2 = $47.46 × 1.035 = $49.12"
  },
  "participation": {
    "active_pathways": 2,
    "paf": 1.035,
    "paf_range": "1.0 - 1.25",
    "activities": [
      {
        "type": "Mentoring",
        "hours": 3,
        "verified": true,
        "duration_months": 12,
        "weight": 0.08
      },
      {
        "type": "Volunteering",
        "hours": 2,
        "verified": true,
        "duration_months": 12,
        "weight": 0.06
      }
    ]
  },
  "base_v41_metrics": {
    "purchase_amount": 100.00,
    "elvr": 47.46,
    "evl": 52.54,
    "local_capture_components": {...},
    "ejv_v2_baseline": {...}
  },
  "interpretation": {
    "message": "For $100 spent with 2 participation pathway(s), ELVR increases to $49.12 (from $47.46 base).",
    "amplification_effect": "Participation adds $1.66 (3.5%) through civic engagement.",
    "sustainability": "Participation pathways strengthen community agency and multiply local economic benefit."
  }
}
```

---

### Store Search Endpoints

#### POST /api/overpass
Search for stores using OpenStreetMap Overpass API

**Request:**
```json
{
  "lat": 34.7304,
  "lon": -86.5861,
  "radius": 5000,
  "shop_type": "supermarket"
}
```

**Response:**
```json
{
  "elements": [
    {
      "type": "node",
      "id": 123456789,
      "lat": 34.7285,
      "lon": -86.5834,
      "tags": {
        "name": "Kroger",
        "shop": "supermarket",
        "addr:street": "University Dr",
        "addr:city": "Huntsville",
        "addr:state": "AL",
        "addr:postcode": "35801"
      }
    }
  ]
}
```

---

### Help & Documentation Endpoints

#### GET /api/ejv-v2/help
Get detailed help documentation for EJV v2

#### GET /api/ejv-v4.1/help
Get detailed help documentation for EJV v4.1

#### GET /api/ejv-v4.2/help
Get detailed help documentation for EJV v4.2

**Response Format:**
```json
{
  "version": "4.1",
  "title": "EJV v4.1: Decomposed Local Capture + Financing-Aware",
  "description": "...",
  "formula": "...",
  "components": [...],
  "examples": [...]
}
```

---

## Frontend Implementation

### Key JavaScript Functions

#### calculateEJV(storeId, storeName, showDashboard)
Main function to calculate and cache EJV data

**Flow:**
1. Check ejvCache for existing data
2. If not cached, call API `/api/ejv-v4.1/<storeId>`
3. Parse response and extract ELVR, EVL, v2 baseline
4. Store in ejvCache and allStoresEJV array
5. If showDashboard=true, update right dashboard
6. Return cached data

---

#### updateRightDashboard(data, storeName)
Updates the right-side EJV dashboard

**What It Displays:**
- Store name and location
- EJV v2 baseline score
- EJV v4.1 ELVR and EVL
- Wealth retained/leaked percentages
- 4 core score components
- 9 justice dimensions
- Formula and data sources

**Data Flow:**
```javascript
updateRightDashboard(data, "Target") {
  // Extract values
  elvr = data.elvr
  ejvV2 = data.ejv_v2_baseline.EJV
  
  // Update displays
  document.getElementById('ejvV2Display').textContent = ejvV2
  document.getElementById('ejvV41Display').textContent = '$' + elvr
  document.getElementById('wageScore').textContent = data.wage_score
  // ... etc
}
```

---

#### displayStores(stores)
Main function to display search results on map

**Flow:**
1. Clear existing markers
2. Save stores to window.lastSearchResults
3. For each store:
   - Create Leaflet marker with icon
   - Add to map
   - Create popup with basic info
   - Store in markers array
4. Calculate EJV for each store (async)
5. Update marker colors based on EJV

---

#### populateCompareSelects()
Populate dropdowns in Compare module

**Data Sources:**
1. `window.lastSearchResults` - Most recent search results
2. `localStorage('fixAppUserData')` - Purchase history

**Flow:**
1. Clear existing options
2. Create "Current Search Results" optgroup from window.lastSearchResults
3. Create "Your Purchases" optgroup from localStorage
4. Populate both Store A and Store B dropdowns

---

### Local Storage Structure

```javascript
localStorage.setItem('fixAppUserData', JSON.stringify({
  username: "john_doe",
  email: "john@example.com",
  purchases: [
    {
      storeName: "Kroger",
      amount: 85.50,
      category: "Groceries",
      date: "2026-01-28",
      ejv: 68.5,
      elvr: 62.00
    }
  ],
  civicActions: [
    {
      type: "volunteering",
      description: "Food bank volunteer",
      hours: 4,
      date: "2026-01-25",
      points: 10,
      verified: true
    }
  ],
  totalEJV: 1250.00,
  totalSpent: 2100.00
}))
```

---

### Decision Mode Toggle

```javascript
let decisionMode = 'locate'; // 'locate', 'compare', 'engage'

function setDecisionMode(mode) {
  decisionMode = mode;
  
  if (mode === 'engage') {
    // Show EJV v4.2 with participation
    showParticipationPanel();
    enableParticipationTracking();
  } else {
    // Show EJV v2 + v4.1
    hideParticipationPanel();
  }
}
```

---

## Conclusion

The FIX$ application provides a comprehensive, data-driven approach to measuring economic justice in local commerce. By combining government data sources (BLS, Census) with sophisticated economic modeling, it delivers actionable insights for consumers, businesses, and policymakers.

**Key Achievements:**
- ✅ Multi-version EJV calculations for different use cases
- ✅ Real-time government data integration
- ✅ 4 core scores, 9 justice dimensions, 5 decomposed components
- ✅ Participation amplification rewards civic engagement
- ✅ Geographic comparison and analysis tools
- ✅ User-friendly interface with interactive maps
- ✅ Comprehensive API for external integration

**Future Enhancements:**
- Route optimization module
- Verified business participation database
- Historical trend analysis
- Community impact reports
- Policy recommendation engine
- Mobile application

---


