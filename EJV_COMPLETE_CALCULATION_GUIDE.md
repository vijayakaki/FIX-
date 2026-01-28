# Complete EJV Calculation Guide
## All Versions with Data Sources

**Last Updated:** January 26, 2026  
**Document Type:** Comprehensive Reference

---

## Table of Contents

1. [EJV v1: Traditional Economic Justice Value](#ejv-v1-traditional-economic-justice-value)
2. [EJV v2: Justice-Weighted Local Impact](#ejv-v2-justice-weighted-local-impact)
3. [EJV v3: Systemic Power Analysis](#ejv-v3-systemic-power-analysis)
4. [EJV v4: Decomposed Flows + Community Capacity](#ejv-v4-decomposed-flows--community-capacity)
5. [EJV v4.1: Decomposed Local Capture + Financing-Aware](#ejv-v41-decomposed-local-capture--financing-aware)
6. [EJV v4.2: Participation & Agency Amplification](#ejv-v42-participation--agency-amplification)
7. [Version Comparison Matrix](#version-comparison-matrix)
8. [Consolidated Data Sources](#consolidated-data-sources)

---

# EJV v1: Traditional Economic Justice Value

**Status:** Fully Implemented  
**Purpose:** Simple 0-100 composite scoring system

## Formula

```
EJV v1 = Wage Score + Hiring Score + Community Score + Participation Score
Range: 0-100 points (each component 0-25 points)
```

## Components

### 1. Wage Score (0-25 points)

**Formula:**
```python
living_wage = (median_income / 2080 hours) × 0.35
wage_score = min(25, (avg_wage / living_wage) × 25)
```

**Data Sources:**
- **Average Wage**: BLS OEWS (Occupation Employment and Wage Statistics), May 2024
  - URL: https://www.bls.gov/oes/
  - Update: Annual
  - Reliability: ±5%
- **Median Income**: US Census Bureau ACS 2022 (5-year estimates)
  - URL: https://api.census.gov/data/2022/acs/acs5
  - Variable: B19013_001E
  - Geography: Census tract
  - Reliability: ±3% margin of error

### 2. Hiring Score (0-25 points)

**Formula:**
```python
hiring_score = min(25, local_hire_pct × 25 × (1 + svi))
# where svi = Social Vulnerability Index (default 0.7)
```

**Data Sources:**
- **Local Hire Percentage**: Calculated from:
  - **Census LODES** (Worker residence vs. workplace flows)
    - URL: https://lehd.ces.census.gov/data/
    - Update: Annual, 2021 most recent
  - **BLS LAUS** (Unemployment affects local hiring)
    - URL: https://www.bls.gov/lau/
    - Formula: +0-20% bonus based on unemployment
- **SVI**: CDC/ATSDR Social Vulnerability Index
  - URL: https://www.atsdr.cdc.gov/placeandhealth/svi/
  - Update: Every 10 years (2020 Census-based)

### 3. Community Score (0-25 points)

**Formula:**
```python
community_score = min(25, (community_spending / daily_payroll) × 25)
```

**Data Sources:**
- **Employee Count**: BLS QCEW (Quarterly Census of Employment and Wages)
  - URL: https://www.bls.gov/cew/
  - Update: Quarterly
  - Lag: 5-6 months
- **Wages**: BLS OEWS (see above)
- **Community Spending**: Self-reported or estimated
  - Ideal: CSR reports, 990 forms, annual reports
  - Estimated: 0.5-25% of payroll

### 4. Participation Score (0-25 points)

**Formula:**
```python
participation_score = min(25, (active_employees / benchmark) × 25)
# benchmark = 25 (default)
```

**Data Sources:**
- **Employee Count**: BLS QCEW
- **Industry Benchmarks**: 
  - BLS Industries at a Glance: https://www.bls.gov/iag/
  - Economic Census: https://www.census.gov/programs-surveys/economic-census.html
  - County Business Patterns: https://www.census.gov/programs-surveys/cbp.html

## Example Calculation

**Supermarket in Manhattan (ZIP 10001)**

**Data Inputs:**
- Median Income: $106,509 [Census ACS]
- Average Wage: $15.02/hour [BLS OEWS]
- Local Hire: 82% [Calculated from LODES + unemployment]
- Active Employees: 48 [BLS QCEW]
- Community Spending: $288.48/day [Estimated]

**Calculation:**
```
Living Wage = ($106,509 / 2,080) × 0.35 = $17.92/hour

Wage Score = min(25, ($15.02 / $17.92) × 25) = 20.95
Hiring Score = min(25, 0.82 × 25 × 1.7) = 25.00 (capped)
Community Score = min(25, ($288.48 / $5,769.60) × 25) = 1.25
Participation Score = min(25, (48 / 25) × 25) = 25.00 (capped)

EJV v1 = 20.95 + 25.00 + 1.25 + 25.00 = 72.20 / 100
```

**API Endpoint:** `/api/ejv/<store_id>`

---

# EJV v2: Justice-Weighted Local Impact

**Status:** Fully Implemented  
**Purpose:** Dollar-based justice-weighted impact measurement

## Formula

```
EJV v2 = (P × LC) × (JS_ZIP / 100)

Where:
- P = Purchase Amount ($)
- LC = Local Capture (0-1)
- JS_ZIP = Justice Score for ZIP (0-100, from 9 dimensions)
```

## Nine Dimensions

1. **AES** - Access to Essential Services (Community Score)
2. **ART** - Access to Resources & Technology (Wage Score)
3. **HWI** - Health, Wellness & Inclusion (Hiring Score)
4. **PSR** - Public Service Representation (Community Score)
5. **CAI** - Cultural Awareness & Inclusivity (Participation Score)
6. **JCE** - Job Creation/Economic Empowerment (Hiring Score)
7. **FSI** - Financial Support & Investment (Wage Score)
8. **CED** - Community Engagement & Development (Avg of Community + Participation)
9. **ESD** - Education & Skill Development (Hiring Score)

## ZIP Need Modifier (NM)

**Applied to 3 dimensions: AES, ART, HWI**

**Formula:**
```python
unemployment_factor = min(unemployment_rate / 10.0, 1.0)
income_factor = max(0, 1 - (median_income / 75000))

base_modifier = 0.80 + (0.30 × ((unemployment_factor + income_factor) / 2))

NM_AES = base_modifier × 1.05  # Higher weight for essential services
NM_HWI = base_modifier × 1.03  # Health in high-need areas
NM_ART = base_modifier × 1.02  # Technology access

# Clamped to range [0.80, 1.10]
```

## Data Sources

### Government Data (100% of v2)

#### 1. Bureau of Labor Statistics (BLS)

**A. OEWS (Wages)**
- URL: https://www.bls.gov/oes/
- Version: May 2024
- Update: Annual
- Coverage: All occupations, national/state/metro
- Reliability: ±5%
- API: https://www.bls.gov/developers/ (500 queries/day with registration)

**B. LAUS (Unemployment)**
- URL: https://www.bls.gov/lau/
- Update: Monthly
- Latest: December 2025
- Lag: ~1 month
- Reliability: ±0.2 percentage points
- Geographic: County, metro, state

**C. QCEW (Employment)**
- URL: https://www.bls.gov/cew/
- Update: Quarterly
- Latest: Q4 2025
- Lag: 5-6 months
- Coverage: 97% of civilian employment

#### 2. U.S. Census Bureau

**A. American Community Survey (ACS)**
- URL: https://www.census.gov/programs-surveys/acs/
- API: https://api.census.gov/data/2022/acs/acs5
- Version: 2022 5-year estimates (2018-2022)
- Update: Annual
- Key Variables:
  - B19013_001E: Median household income
- Reliability: ±3% margin of error
- Geography: Census tract level
- API Key: Free at https://api.census.gov/data/key_signup.html
- Rate Limit: Unlimited with key

**B. LODES (Worker Flows)**
- URL: https://lehd.ces.census.gov/data/
- Version: 2021
- Update: Annual
- Lag: 18-24 months
- Use: Worker residence vs. workplace
- Coverage: Block-level flows

**C. TIGER/Line (Geography)**
- URL: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
- Use: ZIP to census tract mapping
- Update: Annual

### Calculation Pipeline

```
Input: Store ID + ZIP Code
    ↓
1. Geographic Mapping
   ZIP → Census Tract (TIGER/Line)
   ZIP → County (for BLS LAUS)
   ZIP → Metro Area (for BLS OEWS)
    ↓
2. API Calls (Parallel)
   Census ACS: Median income
   BLS LAUS: Unemployment rate
   BLS OEWS: Wage data by occupation
    ↓
3. Calculations
   Living wage from median income
   Local hire % from unemployment + patterns
   Need modifiers from unemployment + income
   Dimension scores from wages + hiring + estimates
    ↓
4. Justice Score
   Apply NM to AES, ART, HWI
   Average all 9 adjusted dimensions
   Scale to 0-100
    ↓
5. EJV v2
   Multiply purchase × local_capture × (justice_score / 100)
```

## Example Calculation

**$100 Purchase at Manhattan Supermarket**

**Data:**
- Purchase: $100
- Local Capture: 82% [Calculated]
- Median Income: $106,509 [Census ACS]
- Unemployment: 3.1% [BLS LAUS]

**Step 1: Base Dimensions**
```
AES (Community): 0.036
ART (Wage): 1.000
HWI (Hiring): 1.000
PSR (Community): 0.036
CAI (Participation): 1.000
JCE (Hiring): 1.000
FSI (Wage): 1.000
CED (Avg): 0.518
ESD (Hiring): 1.000
```

**Step 2: Need Modifiers**
```
unemployment_factor = 3.1 / 10.0 = 0.31
income_factor = max(0, 1 - (106509 / 75000)) = 0

base_modifier = 0.80 + (0.30 × 0.155) = 0.847

NM_AES = 0.847 × 1.05 = 0.889 (clamped to 0.889)
NM_ART = 0.847 × 1.02 = 0.864
NM_HWI = 0.847 × 1.03 = 0.872
```

**Step 3: Adjusted Dimensions**
```
AES: 0.036 × 0.889 = 0.032
ART: 1.000 × 0.864 = 0.864
HWI: 1.000 × 0.872 = 0.872
PSR: 0.036 (unchanged)
CAI: 1.000 (unchanged)
JCE: 1.000 (unchanged)
FSI: 1.000 (unchanged)
CED: 0.518 (unchanged)
ESD: 1.000 (unchanged)
```

**Step 4: Justice Score**
```
JS_ZIP = (0.032 + 0.864 + 0.872 + 0.036 + 1.000 + 1.000 + 1.000 + 0.518 + 1.000) / 9 × 100
       = 6.322 / 9 × 100
       = 70.2
```

**Step 5: EJV v2**
```
EJV v2 = ($100 × 0.82) × (70.2 / 100)
       = $82.00 × 0.702
       = $57.56
```

**Interpretation:** For every $100 spent, $57.56 creates justice-weighted local economic impact.

**API Endpoint:** `/api/ejv-v2/<store_id>`

---

# EJV v3: Systemic Power Analysis

**Status:** Conceptual Framework (Not Implemented)  
**Purpose:** Analyze power dynamics and systemic equity

## Formula

```
EJV v3 = Base Economic Impact × Power Equity Factor (PEF)

PEF = (Ownership Equity × 0.35) + 
      (Decision Participation × 0.25) + 
      (Voice & Agency × 0.20) + 
      (Barrier Removal × 0.15) + 
      (Power Redistribution × 0.05)

PEF Multiplier = 0.5 + (PEF × 1.5)
Range: 0.5 - 2.0
```

## Five Power Dimensions

### 1. Ownership Equity (35%)

**Measures:** Who owns the business and how ownership affects economic justice

**Scoring:**
- Worker Cooperative: 1.00
- Community Ownership: 0.95
- ESOP (Employee Stock): 0.85
- Local Family Business: 0.75
- Impact Investor: 0.65
- Regional Corporation: 0.50
- National Corporation: 0.35
- Private Equity: 0.25
- Multinational Corp: 0.20

**Data Sources:**
- State business registration records
- SEC EDGAR (public companies): https://www.sec.gov/edgar
- Cooperative registries: National Cooperative Business Association
- B Corp directory: https://www.bcorporation.net/
- DOL ESOP database

### 2. Decision Participation (25%)

**Measures:** Who has meaningful input in business decisions

**Scoring:**
- Consensus Democracy: 1.00
- Worker Self-Management: 0.95
- Board with Worker Seats: 0.80
- Advisory Committees: 0.65
- Open Door Policy: 0.50
- Management Hierarchy: 0.35
- Absentee Control: 0.20

**Data Sources:**
- Governance documents
- Board composition records
- Union contracts
- Worker survey data
- Meeting minutes (if public)

### 3. Voice & Agency (20%)

**Measures:** Actual ability to exercise power and influence outcomes

**Scoring:**
- Union Contract: 1.00
- Worker Board Seats: 0.90
- Community Advisory Board: 0.75
- Regular Town Halls: 0.60
- Feedback Systems: 0.45
- Informal Networks: 0.30
- No Voice Mechanisms: 0.10

**Data Sources:**
- Union contracts and CBA documents
- Grievance procedure records
- Worker surveys
- Collective bargaining agreements
- Retaliation protection policies

### 4. Barrier Removal (15%)

**Measures:** Active efforts to remove systemic barriers

**Scoring by Action:**
- Living Wage Guarantee: 0.95
- Ban the Box: 0.90
- Healthcare Day One: 0.90
- On-Site Childcare: 0.85
- Flexible Scheduling: 0.80
- Language Access: 0.75
- Skills Training: 0.70
- Transportation Support: 0.65

**Data Sources:**
- HR policies and employee handbooks
- Job postings and requirements
- Benefits documentation
- Accommodation records
- Training program enrollment

### 5. Power Redistribution (5%)

**Measures:** Active transfer of economic power

**Scoring:**
- Profit Sharing (All Workers): 1.00
- Employee Ownership (Broad): 0.95
- Community Wealth Building: 0.85
- Supplier Diversity Program: 0.75
- Preferential Hiring: 0.70
- Local Reinvestment: 0.60
- No Redistribution: 0.10

**Data Sources:**
- Profit-sharing plans
- ESOP documents
- Supplier diversity reports
- Community investment records
- Equity distribution records

## Example Calculation

**Worker Cooperative vs. National Chain**

**Worker Cooperative Cafe:**
```
Base Impact (v2): $67.50

Power Analysis:
- Ownership: 1.00 × 0.35 = 0.350
- Decision: 0.95 × 0.25 = 0.238
- Voice: 0.90 × 0.20 = 0.180
- Barriers: 0.89 × 0.15 = 0.134
- Redistribution: 0.88 × 0.05 = 0.044

PEF = 0.946
PEF Multiplier = 0.5 + (0.946 × 1.5) = 1.919

EJV v3 = $67.50 × 1.919 = $129.53
```

**National Chain Cafe:**
```
Base Impact (v2): $45.20

Power Analysis:
- Ownership: 0.35 × 0.35 = 0.123
- Decision: 0.35 × 0.25 = 0.088
- Voice: 0.40 × 0.20 = 0.080
- Barriers: 0.25 × 0.15 = 0.038
- Redistribution: 0.15 × 0.05 = 0.008

PEF = 0.337
PEF Multiplier = 0.5 + (0.337 × 1.5) = 1.006

EJV v3 = $45.20 × 1.006 = $45.47
```

**Ratio:** Worker coop creates **2.85× more** justice-weighted value when accounting for power structures.

**API Endpoint:** Not yet implemented

---

# EJV v4: Decomposed Flows + Community Capacity

**Status:** Conceptual Framework (v4.1 and v4.2 implemented)  
**Purpose:** Comprehensive flow decomposition with capacity building

## Formula

```
EJV v4 = (Purchase Amount × LC_aggregate) × (1 + Capacity Score)

Where:
LC_aggregate = (LC_wages × 0.35) + (LC_suppliers × 0.25) + (LC_taxes × 0.15) + 
               (LC_financing × 0.15) + (LC_ownership × 0.10)

Capacity Score = (Skills × 0.30) + (Infrastructure × 0.25) + 
                 (Networks × 0.25) + (Institutional × 0.20)
```

## Five Flow Components

### 1. LC_wages (35%)
Percentage of wages paid to workers living in local area

**Typical Ranges:**
- Large corporation: 0.40-0.50
- National chain: 0.50-0.60
- Regional chain: 0.60-0.70
- Local small business: 0.75-0.85
- Worker cooperative: 0.90-0.95

**Data Sources:** BLS OEWS, Census LODES, BLS LAUS

### 2. LC_suppliers (25%)
Percentage of procurement from local suppliers

**Typical Ranges:**
- Large corporation: 0.15-0.25
- National chain: 0.25-0.35
- Regional chain: 0.35-0.50
- Local small business: 0.60-0.70
- Local cooperative: 0.75-0.85

**Data Sources:** BEA Regional Accounts, Economic Census, industry research

### 3. LC_taxes (15%)
Percentage of taxes paid to local/state vs. federal

**Typical Range:** 0.60-0.90 for all types

**Data Sources:** BEA Government Finances, Census Government Finances, state/local tax codes

### 4. LC_financing (15%)
Percentage of interest paid to local lenders

**Ranges by Lender:**
- CDFI: 0.90-0.95
- Credit Union: 0.80-0.90
- Community Bank: 0.70-0.80
- Regional Bank: 0.40-0.60
- National Bank: 0.20-0.30
- Private Equity: 0.05-0.15

**Data Sources:** FDIC, NCUA, CDFI Fund

### 5. LC_ownership (10%)
Percentage of profits retained locally

**Ranges by Type:**
- Worker Cooperative: 0.95-1.00
- Local Sole Proprietor: 0.85-0.95
- Local Partnership: 0.75-0.85
- ESOP: 0.60-0.80
- Regional Corp: 0.25-0.40
- National Corp: 0.10-0.20
- Multinational: 0.05-0.10

**Data Sources:** Business registrations, SEC EDGAR, cooperative registries

## Four Capacity Dimensions

### 1. Skills Development (30%)

**Measures:** Human capital building

**Indicators:**
- Apprenticeships and structured training
- On-the-job training hours
- Education subsidies
- Mentorship programs
- Skill certifications earned

**Formula:**
```
Skills Score = (workers_in_training / total_workers) × 
               (avg_training_hours / 100) × 
               (advancement_rate)
```

**Data Sources:** Training records, DOL Apprenticeship.gov, certification data

### 2. Infrastructure Investment (25%)

**Measures:** Physical/digital infrastructure built

**Indicators:**
- Facility improvements (public-accessible)
- Technology infrastructure
- Transportation improvements
- Public spaces created
- Accessibility upgrades

**Formula:**
```
Infrastructure Score = community_accessible_investments / total_capital_expenditures
```

**Data Sources:** Capital expenditure records, public benefit documentation

### 3. Network Building (25%)

**Measures:** Social and economic connections

**Indicators:**
- Local supplier relationships
- Community partnerships
- Business-to-business connections
- Civic engagement
- Information sharing

**Formula:**
```
Network Score = (active_partnerships) × (interaction_frequency) × (reciprocity_index)
```

**Data Sources:** Partnership records, collaboration agreements, chamber participation

### 4. Institutional Strength (20%)

**Measures:** Long-term community institutions

**Indicators:**
- Organizational support (donations)
- Leadership development
- Governance participation
- Policy advocacy
- Crisis resilience contribution

**Formula:**
```
Institutional Score = (org_investment / revenue) + 
                      (leaders_developed / workforce) + 
                      (governance_hours / leadership_hours)
```

**Data Sources:** CSR reports, 990 forms, board service records

## Example Calculation

**Worker Cooperative: $100 Purchase**

**Flow Analysis:**
```
LC_wages: 0.95 × 0.35 = 0.333
LC_suppliers: 0.80 × 0.25 = 0.200
LC_taxes: 0.90 × 0.15 = 0.135
LC_financing: 0.95 × 0.15 = 0.143
LC_ownership: 1.00 × 0.10 = 0.100

LC_aggregate = 0.911
```

**Capacity Building:**
```
Skills: 0.576 × 0.30 = 0.173
Infrastructure: 0.25 × 0.25 = 0.063
Networks: 0.85 × 0.25 = 0.213
Institutional: 0.225 × 0.20 = 0.045

Capacity Score = 0.494
```

**EJV v4:**
```
EJV v4 = ($100 × 0.911) × (1 + 0.494)
       = $91.10 × 1.494
       = $136.10
```

**API Endpoint:** Not yet implemented (use v4.1 or v4.2)

---

# EJV v4.1: Decomposed Local Capture + Financing-Aware

**Status:** Fully Implemented  
**Purpose:** Directional estimation of local value retention vs. leakage

## Formula

```
ELVR = P × LC_aggregate
EVL = P - ELVR

Where:
LC_aggregate = (LC_wages × 0.35) + (LC_suppliers × 0.25) + (LC_taxes × 0.15) + 
               (LC_financing × 0.15) + (LC_ownership × 0.10)
```

## Five Local Capture Components

Same as v4 base, but without capacity building dimension.

### Component Defaults by Business Type

```python
LOCAL_CAPTURE_DEFAULTS = {
    "worker_cooperative": {
        "lc_wages": 0.95,
        "lc_suppliers": 0.80,
        "lc_taxes": 0.90,
        "lc_financing": 0.95,
        "lc_ownership": 1.00
    },
    "local_small_business": {
        "lc_wages": 0.80,
        "lc_suppliers": 0.65,
        "lc_taxes": 0.80,
        "lc_financing": 0.70,
        "lc_ownership": 0.90
    },
    "regional_chain": {
        "lc_wages": 0.60,
        "lc_suppliers": 0.40,
        "lc_taxes": 0.70,
        "lc_financing": 0.50,
        "lc_ownership": 0.30
    },
    "national_chain": {
        "lc_wages": 0.50,
        "lc_suppliers": 0.25,
        "lc_taxes": 0.65,
        "lc_financing": 0.30,
        "lc_ownership": 0.10
    },
    "large_corporation": {
        "lc_wages": 0.40,
        "lc_suppliers": 0.15,
        "lc_taxes": 0.60,
        "lc_financing": 0.20,
        "lc_ownership": 0.05
    }
}
```

## Financing-Aware Calculation

**Time-value of interest over loan life:**

```python
# Calculate total interest
monthly_rate = apr / 12
monthly_payment = financed_amount * (
    monthly_rate * (1 + monthly_rate)**months
) / ((1 + monthly_rate)**months - 1)
total_interest = (monthly_payment * months) - financed_amount

# Apply LC_financing
local_interest_retained = total_interest * lc_financing
```

## Data Sources

### Component-Specific Sources

| Component | Primary Source | Reliability | Update Frequency |
|-----------|----------------|-------------|------------------|
| **LC_wages** | BLS OEWS + Census LODES | ±10% | Annual |
| **LC_suppliers** | BEA Regional + Industry research | ±25% | Varies |
| **LC_taxes** | BEA Gov Finances + Tax codes | ±5% | Annual |
| **LC_financing** | FDIC + NCUA + lender type | ±15% | Quarterly |
| **LC_ownership** | Business registrations + SEC | ±20% | Varies |

**Detailed sources same as v4 base framework**

## Example Calculation

**Local Small Business: $100 Purchase**

**Flow Components:**
```
LC_wages: 0.80 × 0.35 = 0.280
LC_suppliers: 0.65 × 0.25 = 0.163
LC_taxes: 0.80 × 0.15 = 0.120
LC_financing: 0.70 × 0.15 = 0.105
LC_ownership: 0.90 × 0.10 = 0.090

LC_aggregate = 0.758
```

**ELVR Calculation:**
```
ELVR = $100 × 0.758 = $75.80
EVL = $100 - $75.80 = $24.20

Retention: 75.8%
Leakage: 24.2%
```

**With Financing (5.5% APR, 12 months, $20 down):**
```
Financed: $80
Total Interest: $1.88
Local Interest (70%): $1.32

Total ELVR = $75.80 + $1.32 = $77.12
Total EVL = $100 + $1.88 - $77.12 = $24.76
```

**API Endpoint:** `/api/ejv-v4.1/<store_id>`

---

# EJV v4.2: Participation & Agency Amplification

**Status:** Fully Implemented  
**Purpose:** Amplify local value through verified participation

## Formula

```
ELVR v4.2 = ELVR v4.1 × PAF

Where:
PAF = 1.0 + Σ(participation contributions)
Range: 1.0 - 1.25 (max 25% amplification)
```

## Participation Amplification Factor (PAF)

**Five Participation Pathways:**

### 1. Mentoring (Weight: 0.08)

**Formula:**
```python
intensity = min(hours_per_week / 10.0, 1.0)
verification = 1.2 if verified else 1.0
duration = min(duration_months / 12.0, 1.0)

contribution = 0.08 × intensity × verification × duration
```

**Maximum contribution:** 0.08 × 1.0 × 1.2 × 1.0 = 0.096 (~10% of total PAF)

**Data Sources:**
- School district MOUs
- Workforce development programs
- VolunteerMatch verification: https://www.volunteermatch.org/
- Program attendance logs
- Completion certificates

### 2. Volunteering (Weight: 0.06)

**Formula:**
```python
intensity = min(hours_per_week / 10.0, 1.0)
verification = 1.2 if verified else 1.0
duration = min(duration_months / 12.0, 1.0)

contribution = 0.06 × intensity × verification × duration
```

**Data Sources:**
- Volunteer management platforms (Galaxy Digital, Track It Forward)
- Nonprofit 501(c)(3) confirmation letters
- Service hour logs
- IRS EIN verification

### 3. Sponsorship (Weight: 0.05)

**Formula:**
```python
base_contribution = 0.05
verification = 1.2 if verified else 1.0

contribution = base_contribution × verification
```

**Data Sources:**
- Sponsorship agreements/contracts
- Bank statements and receipts
- Event programs listing sponsors
- Tax documentation (1099, charitable receipts)

### 4. Apprenticeships (Weight: 0.04)

**Formula:**
```python
base_contribution = 0.04
program_quality = 1.5 if DOL_registered else 1.0
verification = 1.2 if verified else 1.0

contribution = base_contribution × program_quality × verification
```

**Data Sources:**
- DOL Registered Apprenticeship: https://www.apprenticeship.gov/
- Program registration numbers
- Apprenticeship agreements
- Training hour logs
- Industry certifications

### 5. Community Organizing (Weight: 0.02)

**Formula:**
```python
intensity = min(hours_per_month / 20.0, 1.0)
verification = 1.2 if verified else 1.0
duration = min(duration_months / 12.0, 1.0)

contribution = 0.02 × intensity × verification × duration
```

**Data Sources:**
- Union membership verification
- NLRB election filings
- Tenant association records
- Organizing committee participation
- Campaign documentation

## Verification Standards

### Gold Standard (1.2× multiplier)
- Official program registration (DOL apprenticeship)
- Financial records (sponsorship payments)
- Third-party platform verification (VolunteerMatch)
- Government records (NLRB filings)

### Silver Standard (1.0× multiplier)
- Organization confirmation letter
- Signed time logs from supervisor
- Partnership agreements
- Event documentation

### Bronze Standard (0.8× multiplier, temporary)
- Self-reported with some documentation
- Pending verification (max 30 days)

### No Verification (0× multiplier)
- Self-reported only
- Does not contribute to PAF

## Example Calculation

**Local Small Business with Participation**

**Base v4.1:**
```
ELVR v4.1 = $75.75
```

**Participation Data:**
```
Mentoring: 5 hrs/week, 12 months, verified
  Contribution = 0.08 × 0.5 × 1.2 × 1.0 = 0.048

Volunteering: 3 hrs/week, 6 months, verified
  Contribution = 0.06 × 0.3 × 1.2 × 0.5 = 0.011

Sponsorship: $5,000, verified
  Contribution = 0.05 × 1.2 = 0.060

Total PAF Contribution = 0.048 + 0.011 + 0.060 = 0.119
```

**PAF Calculation:**
```
PAF = 1.0 + 0.119 = 1.119
```

**Amplified ELVR:**
```
ELVR v4.2 = $75.75 × 1.119 = $84.76
```

**Interpretation:** Participation actions increase local value retention by 11.9%, from $75.75 to $84.76.

## Data Privacy

**Privacy Protections:**
- Individual names anonymized
- Aggregate participation only
- Encrypted document storage
- GDPR/CCPA compliant
- User controls data sharing

**Data Retention:**
- Active participation: Duration + 1 year
- Verification documents: 7 years (audit requirement)
- Historical: Aggregated only

**API Endpoint:** `/api/ejv-v4.2/<store_id>` (POST)

---

# Version Comparison Matrix

| Feature | v1 | v2 | v3 | v4 | v4.1 | v4.2 |
|---------|----|----|----|----|------|------|
| **Output Type** | Score (0-100) | Dollars | Dollars | Value + Capacity | Dollars (ELVR/EVL) | Amplified Dollars |
| **Components** | 4 outcomes | 9 dimensions | 5 power factors | 5 flows + 4 capacity | 5 flows | 5 flows + PAF |
| **Equity Weighting** | SVI only | ZIP need modifiers | Power structure | Capacity building | Via v2 baseline | Via v4.1 base |
| **Implementation** | ✅ Complete | ✅ Complete | ⏳ Conceptual | ⏳ Conceptual | ✅ Complete | ✅ Complete |
| **Data Sources** | BLS + Census | Government only | Survey intensive | Extensive | Gov + estimates | v4.1 + participation |
| **Complexity** | Low | Medium | High | Very High | Medium-High | Medium-High |
| **Primary Use Case** | Quick compare | Budget planning | Power analysis | Research | LOCATOR advanced | ENABLE only |
| **API Available** | ✅ Yes | ✅ Yes | ❌ No | ❌ No | ✅ Yes | ✅ Yes |
| **Government Data %** | 80% | 100% | 30% | 60% | 70% | 70% + verified |
| **Update Frequency** | Annual | Annual | As needed | As needed | Annual | Real-time |
| **Reliability** | High | Very High | Medium | High | Medium-High | Medium-High |

---

# Consolidated Data Sources

## Government Data Sources

### Bureau of Labor Statistics (BLS)

**1. OEWS - Occupational Employment and Wage Statistics**
- URL: https://www.bls.gov/oes/
- Version: May 2024
- Update: Annual (May release)
- Use: Wage data (all versions)
- Coverage: All occupations, national/state/metro areas
- Reliability: ±5%
- API: https://www.bls.gov/developers/
- Rate Limit: 500/day with registration

**2. LAUS - Local Area Unemployment Statistics**
- URL: https://www.bls.gov/lau/
- Update: Monthly
- Lag: 1 month
- Use: Unemployment rates (v1, v2, v4.1)
- Geography: County, metro, state
- Reliability: ±0.2 percentage points

**3. QCEW - Quarterly Census of Employment and Wages**
- URL: https://www.bls.gov/cew/
- Update: Quarterly
- Lag: 5-6 months
- Use: Employment counts (all versions)
- Coverage: 97% of civilian employment

**4. Industries at a Glance**
- URL: https://www.bls.gov/iag/
- Update: Monthly
- Use: Industry benchmarks (v1, v4.1)

### U.S. Census Bureau

**1. American Community Survey (ACS)**
- URL: https://www.census.gov/programs-surveys/acs/
- API: https://api.census.gov/data/2022/acs/acs5
- Version: 2022 5-year estimates
- Update: Annual
- Use: Median income (all versions)
- Key Variable: B19013_001E (Median household income)
- Geography: Census tract level
- Reliability: ±3% margin of error
- API Key: Free registration
- Rate Limit: Unlimited with key

**2. LODES - LEHD Origin-Destination Employment Statistics**
- URL: https://lehd.ces.census.gov/data/
- Version: 2021
- Update: Annual
- Lag: 18-24 months
- Use: Worker residence/workplace flows (all versions)
- Coverage: Block-level employment flows
- Format: CSV files by state

**3. TIGER/Line Shapefiles**
- URL: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
- Update: Annual
- Use: Geographic mapping (ZIP to tract)

**4. Economic Census**
- URL: https://www.census.gov/programs-surveys/economic-census.html
- Frequency: Every 5 years (2022 most recent)
- Use: Industry benchmarks (v1, v4.1)

**5. County Business Patterns**
- URL: https://www.census.gov/programs-surveys/cbp.html
- Update: Annual
- Use: Employment patterns (v1, v4.1)

### Bureau of Economic Analysis (BEA)

**1. Regional Accounts**
- URL: https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas
- Update: Annual
- Use: Supply chain patterns (v4, v4.1)
- Measures: Input-output tables, procurement

**2. Government Finances**
- URL: https://www.bea.gov/data/income-saving/state-and-local-government-finances
- Update: Annual
- Use: Tax revenue distribution (v4, v4.1)

### Other Government Sources

**1. CDC/ATSDR - Social Vulnerability Index**
- URL: https://www.atsdr.cdc.gov/placeandhealth/svi/
- Version: 2020 (Census-based)
- Update: Every 10 years
- Use: SVI adjustment (v1)
- Geography: Census tract
- Range: 0-1 (higher = more vulnerable)

**2. FDIC - Bank Data**
- URL: https://www.fdic.gov/analysis/bank-find/
- Update: Quarterly
- Use: Lender classification (v4, v4.1)
- Coverage: All FDIC-insured banks

**3. NCUA - Credit Union Data**
- URL: https://www.ncua.gov/analysis/credit-union-corporate-call-report-data
- Update: Quarterly
- Use: Credit union classification (v4, v4.1)

**4. CDFI Fund**
- URL: https://www.cdfifund.gov/
- Use: Community lender directory (v4, v4.1)

**5. DOL Apprenticeship.gov**
- URL: https://www.apprenticeship.gov/
- Update: Real-time
- Use: Registered apprenticeship verification (v4.2)

**6. SEC EDGAR**
- URL: https://www.sec.gov/edgar
- Update: Real-time
- Use: Public company ownership (v3, v4, v4.1)

**7. NLRB - National Labor Relations Board**
- URL: https://www.nlrb.gov/
- Use: Union election records (v3, v4.2)

## Non-Government Data Sources

### Industry Research

**1. National Cooperative Business Association**
- Use: Cooperative registries (v3, v4, v4.1)

**2. B Corporation Directory**
- URL: https://www.bcorporation.net/
- Use: B Corp certification (v3, v4, v4.1)

**3. Industry Supply Chain Studies**
- Sources: Academic research, CSR reports, trade associations
- Use: Supplier localization estimates (v4, v4.1)
- Reliability: ±25%

### Verification Platforms

**1. VolunteerMatch**
- URL: https://www.volunteermatch.org/
- Use: Volunteer hour verification (v4.2)
- Verification: Automated API

**2. Galaxy Digital**
- Use: Volunteer tracking system (v4.2)

**3. Track It Forward**
- Use: Volunteer hours with verification (v4.2)

### Business Records

**1. Self-Reported Data**
- Payroll records
- Community spending documentation
- Training program enrollment
- Partnership agreements
- Sponsorship contracts

**Reliability:**
- High for financial records (auditable)
- Medium for operational data
- Low for self-assessed metrics

## Data Quality Summary

| Data Type | Source | Reliability | Update Frequency | Geographic Level |
|-----------|--------|-------------|------------------|------------------|
| **Wages** | BLS OEWS | ±5% | Annual | Metro area |
| **Median Income** | Census ACS | ±3% | Annual (5-yr) | Census tract |
| **Unemployment** | BLS LAUS | ±0.2pp | Monthly | County |
| **Employment** | BLS QCEW | ±2% | Quarterly | County |
| **Worker Flows** | Census LODES | High | Annual | Block |
| **Supply Chain** | BEA + Industry | ±25% | Varies | Regional |
| **Tax Distribution** | BEA + Codes | ±5% | Annual | State/local |
| **Lender Type** | FDIC/NCUA | ±15% | Quarterly | Institution |
| **Ownership** | Registrations | ±20% | Varies | Business |
| **Participation** | Verified records | ±5-10% | Real-time | Individual |

## API Access Summary

| API | Rate Limit (Free) | Rate Limit (Registered) | Cost |
|-----|-------------------|------------------------|------|
| **Census ACS** | 500/day | Unlimited | Free |
| **BLS** | 25/day | 500/day | Free |
| **LODES** | No limit (bulk) | No limit | Free |
| **FDIC** | 1000/day | 1000/day | Free |

## Citation Format

**For Academic/Research Use:**

```
Bureau of Labor Statistics. (2024). Occupational Employment and Wage 
Statistics (OEWS), May 2024. U.S. Department of Labor. 
https://www.bls.gov/oes/

U.S. Census Bureau. (2022). American Community Survey 5-Year Estimates, 
2018-2022. https://www.census.gov/programs-surveys/acs/

U.S. Census Bureau, Center for Economic Studies. (2021). Longitudinal 
Employer-Household Dynamics (LEHD) Origin-Destination Employment 
Statistics (LODES). https://lehd.ces.census.gov/data/

Bureau of Economic Analysis. (2024). Regional Economic Accounts. 
https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas

All data accessed: January 2026
```

---

## Document Information

**Version:** 1.0  
**Last Updated:** January 26, 2026  
**Maintained By:** EJV Development Team  
**Purpose:** Comprehensive reference for all EJV calculations and data sources

**Related API Endpoints:**
- `/api/ejv/<store_id>` - v1 (Traditional score)
- `/api/ejv-v2/<store_id>` - v2 (Justice-weighted)
- `/api/ejv-v4.1/<store_id>` - v4.1 (Decomposed flows)
- `/api/ejv-v4.2/<store_id>` - v4.2 (Participation amplification)

**Application URL:** https://fix-app-three.vercel.app

---

**END OF DOCUMENT**
