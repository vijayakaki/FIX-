# EJV v4.2 Calculation Guide
## Participation & Agency Amplification

**Version:** 4.2  
**Last Updated:** January 23, 2026  
**Architecture:** v2 (baseline) → v4.1 (decomposed flows) → v4.2 (participation amplification)

---

## Core Formula

```
ELVR v4.2 = ELVR v4.1 × PAF
```

**Where:**
- **ELVR v4.1** = Estimated Local Value Retained (decomposed flows from v4.1)
- **PAF** = Participation Amplification Factor (1.0 to 1.25)
- **ELVR v4.2** = Amplified local value retained through verified participation

---

## Canonical Definition

EJV v4.2 amplifies the decomposed local value flows from v4.1 by recognizing verified participation pathways—such as mentoring, volunteering, sponsorship, and apprenticeships—that multiply community benefit through civic engagement and agency.

**In Simple Terms:** v4.2 takes the estimated local value retained from v4.1's decomposed flows and amplifies it through verified participation actions that strengthen community agency.

---

## Architecture Overview

### Version Flow:
1. **EJV v2**: Government-only baseline (9 dimensions)
   - Used in LOCATOR for objective comparison
   - No estimates or third-party data

2. **EJV v4.1**: Decomposed Local Capture + Financing-Aware
   - Breaks transaction into 5 components: wages, suppliers, taxes, financing, ownership
   - Time-aware for financing (interest over loan life)
   - Produces ELVR (retained) and EVL (leakage)
   - Uses v2 for justice weighting
   - **Used in LOCATOR as optional advanced view**

3. **EJV v4.2**: Participation & Agency Amplification
   - Applies PAF multiplier to v4.1's ELVR
   - Requires verified participation evidence
   - **Used ONLY in ENABLE workflow**
   - Never shown in LOCATOR

---

## Step-by-Step Calculation

### Step 1: Calculate Base Decomposed Flows (v4.1)

v4.1 decomposes the transaction into local capture components:

```
ELVR = P × ΣLCᵢ
```

#### Five Components (LCᵢ):

| Component | Weight | Description | Range |
|-----------|--------|-------------|-------|
| **LC_wages** | 35% | % of wages to local workers | 40-95% |
| **LC_suppliers** | 25% | % from local suppliers | 15-80% |
| **LC_taxes** | 15% | % taxes paid locally | 60-90% |
| **LC_financing** | 15% | % financing costs local | 20-95% |
| **LC_ownership** | 10% | % local ownership | 5-100% |

**Aggregate Local Capture:**
```
LC_aggregate = (LC_wages × 0.35) + (LC_suppliers × 0.25) + (LC_taxes × 0.15) + 
               (LC_financing × 0.15) + (LC_ownership × 0.10)
```

#### Example (Local Small Business):
```
Purchase: $100
Business Type: local_small_business

Component Values:
- LC_wages: 0.80 (80%)
- LC_suppliers: 0.65 (65%)
- LC_taxes: 0.80 (80%)
- LC_financing: 0.70 (70%)
- LC_ownership: 0.90 (90%)

LC_aggregate = (0.80 × 0.35) + (0.65 × 0.25) + (0.80 × 0.15) + (0.70 × 0.15) + (0.90 × 0.10)
             = 0.28 + 0.1625 + 0.12 + 0.105 + 0.09
             = 0.7575 (75.75%)

ELVR v4.1 = $100 × 0.7575 = $75.75
EVL = $100 - $75.75 = $24.25
```

---

### Step 2: Calculate Participation Amplification Factor (PAF)

PAF ranges from **1.0** (no participation) to **1.25** (maximum verified engagement)

#### Participation Types & Weights:

| Type | Base Weight | Description | Unit |
|------|-------------|-------------|------|
| **Mentoring** | 0.08 (8%) | Youth, workforce, entrepreneurship | hours/week |
| **Volunteering** | 0.06 (6%) | Time, skills, governance | hours/week |
| **Sponsorship** | 0.05 (5%) | Community orgs, sports, events | annual commitment |
| **Apprenticeship** | 0.04 (4%) | Workforce development programs | positions offered |
| **Facilities** | 0.02 (2%) | Space, resources, infrastructure | availability |

#### PAF Calculation Formula:

For each participation activity:

```
Contribution = Base_Weight × Intensity × Verification_Multiplier × Duration_Factor
```

**Calculation Factors:**

**1. Intensity:** Hours per week normalized to 0-1 scale
```
Intensity = min(hours_per_week / 10.0, 1.0)
```
- 0 hours = 0.0
- 5 hours = 0.5
- 10+ hours = 1.0 (capped)

**2. Verification Multiplier:**
- Unverified = 1.0
- Verified by community partner = 1.2 (+20% bonus)

**3. Duration Factor:** Sustained engagement over time
```
Duration_Factor = min(months / 12.0, 1.0)
```
- 1 month = 0.083
- 6 months = 0.5
- 12+ months = 1.0 (maximum)

#### Final PAF:
```
PAF = 1.0 + min(Sum_of_All_Contributions, 0.25)
```
**Capped at 1.25 to prevent gaming.**

---

## Complete Worked Example

### Scenario:
Local coffee shop in Manhattan (ZIP 10001) with active community participation

### Input Data:

**Transaction:**
- Purchase Amount: $100
- Business Type: local_small_business

**v4.1 Decomposed Local Capture (Defaults):**
- LC_wages: 0.80 (80%)
- LC_suppliers: 0.65 (65%)
- LC_taxes: 0.80 (80%)
- LC_financing: 0.70 (70%)
- LC_ownership: 0.90 (90%)

**Participation Data:**
```json
{
  "mentoring": {
    "hours": 2,
    "verified": true,
    "duration_months": 12
  },
  "volunteering": {
    "hours": 4,
    "verified": false,
    "duration_months": 6
  }
}
```

---

### Detailed Calculation Steps:

#### 1. Calculate v4.1 Base (ELVR):
```
LC_aggregate = (0.80 × 0.35) + (0.65 × 0.25) + (0.80 × 0.15) + (0.70 × 0.15) + (0.90 × 0.10)
             = 0.28 + 0.1625 + 0.12 + 0.105 + 0.09
             = 0.7575

ELVR v4.1 = $100 × 0.7575 = $75.75
EVL = $100 - $75.75 = $24.25
Retention: 75.75%
```

#### 2. Calculate PAF:

**Mentoring Contribution:**
```
Base Weight: 0.08
Intensity: 2 hours / 10 = 0.2
Verification: 1.2 (verified by partner)
Duration: 12 months / 12 = 1.0

Contribution = 0.08 × 0.2 × 1.2 × 1.0 
             = 0.0192
```

**Volunteering Contribution:**
```
Base Weight: 0.06
Intensity: 4 hours / 10 = 0.4
Verification: 1.0 (not verified)
Duration: 6 months / 12 = 0.5

Contribution = 0.06 × 0.4 × 1.0 × 0.5 
             = 0.012
```

**Total Contribution:**
```
Total = 0.0192 + 0.012 
      = 0.0312
```

**PAF:**
```
PAF = 1.0 + min(0.0312, 0.25) 
    = 1.0 + 0.0312
    = 1.0312
    
Rounded: 1.031
```

#### 3. Calculate ELVR v4.2:
```
ELVR v4.2 = ELVR v4.1 × PAF
          = $75.75 × 1.031
          = $78.10
```

---

### Results Summary:

| Metric | Value |
|--------|-------|
| Base ELVR (v4.1) | $75.75 |
| Base EVL (v4.1) | $24.25 |
| Base Retention % | 75.75% |
| Participation Amplification Factor | 1.031 |
| **ELVR v4.2 (Amplified)** | **$78.10** |
| Amplification Value | $2.35 |
| Amplification Percentage | 3.1% |

**Interpretation:**  
"For $100 spent with 2 participation pathways (2 hrs/week mentoring + 4 hrs/week volunteering), the estimated local value retained increases to **$78.10** (from $75.75 base). Participation adds **$2.35** (3.1%) through civic engagement, strengthening community agency and multiplying local benefit."

---

## Multiple Scenarios Comparison

### Scenario A: No Participation
```
Input: No participation activities
PAF = 1.0
ELVR v4.2 = $75.75 × 1.0 = $75.75

Interpretation: Base decomposed flows only, no participation amplification
```

### Scenario B: Light Participation
```
Input: 
- Mentoring: 1 hr/week, 3 months, unverified

Calculation:
Contribution = 0.08 × (1/10) × 1.0 × (3/12)
             = 0.08 × 0.1 × 1.0 × 0.25
             = 0.002

PAF = 1.0 + 0.002 = 1.002
EJV v4.2 = $57.89 × 1.002 = $58.01

Amplification: $0.12 (0.2%)
```

### Scenario C: Moderate Participation
```
Input:
- Mentoring: 5 hrs/week, 12 months, verified
- Sponsorship: Annual commitment, verified

Calculation:
Mentoring: 0.08 × 0.5 × 1.2 × 1.0 = 0.048
Sponsorship: 0.05 × 1.0 × 1.2 × 1.0 = 0.060
Total = 0.108

PAF = 1.0 + 0.108 = 1.108
ELVR v4.2 = $75.75 × 1.108 = $83.93

Amplification: $8.18 (10.8%)
```

### Scenario D: Maximum Participation
```
Input: All 5 pathways, 10+ hrs each, verified, 12+ months

Calculation:
Mentoring:      0.08 × 1.0 × 1.2 × 1.0 = 0.096
Volunteering:   0.06 × 1.0 × 1.2 × 1.0 = 0.072
Sponsorship:    0.05 × 1.0 × 1.2 × 1.0 = 0.060
Apprenticeship: 0.04 × 1.0 × 1.2 × 1.0 = 0.048
Facilities:     0.02 × 1.0 × 1.2 × 1.0 = 0.024

Total = 0.300 → CAPPED at 0.25

PAF = 1.0 + 0.25 = 1.25 (maximum)
ELVR v4.2 = $75.75 × 1.25 = $94.69

Amplification: $18.94 (25%)
```

---

## Key Design Principles

### 1. v4.2 Builds on v4.1 Decomposed Flows
- **v4.1** decomposes transactions into 5 local capture components
- **v4.2** amplifies the ELVR through verified participation
- **Never** mixes v4.2 with v2; always v2 → v4.1 → v4.2

### 2. PAF is Bounded
- **Minimum:** 1.0 (no participation)
- **Maximum:** 1.25 (25% amplification)
- **Purpose:** Prevents infinite scaling or gaming the system

### 3. Verification Matters
- **Unverified activities:** Full base weight (multiplier = 1.0)
- **Verified activities:** +20% bonus (multiplier = 1.2)
- **Purpose:** Encourages credible reporting and community partnerships

### 4. Duration Rewards Commitment
- **Short-term (<3 months):** Minimal impact (0-25% of full weight)
- **Medium-term (6 months):** Half weight (50%)
- **Long-term (12+ months):** Full weight (100%)
- **Purpose:** Recognizes sustained engagement over one-time actions

### 4. Intensity Scaled Realistically
- **10 hours/week:** 100% intensity (realistic maximum)
- **5 hours/week:** 50% intensity
- **1 hour/week:** 10% intensity
- **Purpose:** Prevents unrealistic hour claims, normalizes different participation types

### 5. Multiple Pathways Compound
- Activities from different categories add together
- Each pathway contributes independently
- Total still capped at PAF = 1.25
- **Purpose:** Rewards diverse engagement strategies

---

## What PAF Does NOT Do

### ❌ Does NOT Monetize Hours as Dollars
- 2 hours of volunteering ≠ $20 added
- PAF amplifies existing money flows, doesn't create new dollars
- Participation strengthens impact, doesn't replace it

### ❌ Does NOT Override Economic Reality
- Base economic impact must exist first
- You can't have PAF without base EJV v4.1
- Participation enhances money flows, not substitute them

### ❌ Does NOT Allow Unlimited Growth
- Hard cap at PAF = 1.25 (25% maximum boost)
- Multiple pathways compound but hit ceiling
- Prevents gaming through excessive reporting

### ❌ Does NOT Moralize Participation
- PAF = 1.0 is valid and neutral
- No judgment on non-participants
- Measures amplification, not worthiness

### ❌ Does NOT Create Direct Dollar Equivalencies
- "Volunteer hour = $X" is NOT how this works
- PAF reflects how participation strengthens economic conversion
- It's about effectiveness multipliers, not substitution

---

## Verification Methods

### Human-in-the-Loop Verification

**Three Tiers of Credibility:**

**1. Self-Reported (Multiplier = 1.0)**
- User provides participation data
- No external verification
- Still counts toward PAF but without bonus

**2. Evidence-Based (Multiplier = 1.1)**
- User uploads documentation
- Photos, certificates, timesheets
- Light verification without third-party

**3. Partner-Verified (Multiplier = 1.2)**
- Community organization confirms
- Nonprofit, school, government agency
- Full 20% verification bonus

### Time-Bounded Decay

- Participation data expires after 12 months
- Must be renewed to maintain PAF
- Encourages sustained, current engagement
- Prevents stale claims

### Purpose

Keeps v4.2 credible and SBIR-safe while enabling honest participation tracking without creating excessive bureaucracy.

---

## API Usage

### Endpoint
```
POST /api/ejv-v4.2/<store_id>
```

### Request Body
```json
{
  "zip": "10001",
  "location": "Manhattan, NY",
  "purchase": 100.0,
  "participation": {
    "mentoring": {
      "hours": 2,
      "verified": true,
      "duration_months": 12
    },
    "volunteering": {
      "hours": 4,
      "verified": false,
      "duration_months": 6
    }
  }
}
```

### Response Structure
```json
{
  "store_id": "supermarket_10001",
  "location": "Manhattan, NY",
  "zip_code": "10001",
  "version": "4.2",
  "ejv_v42": {
    "community_impact": 59.68,
    "base_impact_v41": 57.89,
    "amplification_factor": 1.031,
    "amplification_value": 1.79,
    "formula": "EJV v4.2 = $57.89 × 1.031 = $59.68"
  },
  "participation": {
    "active_pathways": 2,
    "paf": 1.031,
    "paf_range": "1.0 - 1.25",
    "activities": [
      {
        "type": "Mentoring",
        "hours": 2,
        "verified": true,
        "duration_months": 12,
        "weight": 0.08
      },
      {
        "type": "Volunteering",
        "hours": 4,
        "verified": false,
        "duration_months": 6,
        "weight": 0.06
      }
    ]
  },
  "base_metrics": {
    "purchase_amount": 100.0,
    "local_capture": 0.82,
    "justice_score": 70.6,
    "unemployment_rate": 3.1,
    "median_income": 106509
  },
  "interpretation": {
    "message": "For $100 spent with 2 participation pathway(s), this creates $59.68 in justice-weighted community impact.",
    "amplification_effect": "Participation adds $1.79 (3.1%) through civic engagement.",
    "sustainability": "Participation pathways strengthen how economic activity translates into lasting community benefit."
  }
}
```

---

## New Questions v4.2 Can Answer

1. **How does mentoring amplify the impact of local spending?**
   - Track mentoring hours and see PAF increase
   - Measure dollar amplification per hour of mentoring

2. **Does sponsorship make a large purchase less extractive over time?**
   - Compare EJV v4.2 with/without sponsorship
   - Quantify community benefit from civic engagement

3. **Can businesses earn higher impact without price increases?**
   - Yes, through participation pathways
   - Increase community value by 0-25% through PAF

4. **How do civic actions compound economic flows?**
   - Multiple pathways add together
   - See total PAF from diverse engagement

5. **What participation level creates 10% more community value?**
   - Target PAF = 1.10
   - Calculate required hours/verification/duration

---

## Evolution Timeline

| Version | Key Addition | Formula Impact |
|---------|--------------|----------------|
| **v2** | Local impact × need | Justice-weighted scoring |
| **v3** | Systemic power | Power dynamics analysis |
| **v4** | Decomposed flows + capacity | Time-aware financing |
| **v4.1** | Personal/community split | Dual impact streams |
| **v4.2** | Participation & agency | PAF multiplier (1.0-1.25) |

---

## Data Sources

### Economic Data (Base v4.1)
- **BLS OEWS:** Real wage data (May 2024)
- **US Census ACS:** ZIP-level demographics (2022)
- **Industry Research:** Employment averages by NAICS

### Participation Data (New in v4.2)
- **Self-Reported:** User input with evidence
- **Partner-Verified:** Community organizations
- **Time-Bounded:** 12-month validity window

---

## Implementation Notes

### For Developers

**PAF Calculation Function:**
```python
def calculate_paf(participation_data):
    if not participation_data:
        return 1.0
    
    total_contribution = 0.0
    
    for activity_type, activity_data in participation_data.items():
        base_weight = PARTICIPATION_TYPES[activity_type]["weight"]
        intensity = min(activity_data.get("hours", 1) / 10.0, 1.0)
        verification = 1.2 if activity_data.get("verified") else 1.0
        duration = min(activity_data.get("duration_months", 1) / 12.0, 1.0)
        
        contribution = base_weight * intensity * verification * duration
        total_contribution += contribution
    
    paf = 1.0 + min(total_contribution, 0.25)
    return round(paf, 3)
```

### For Users

**Quick PAF Estimator:**
- Each hour/week of verified mentoring ≈ +0.96% PAF per year
- Each hour/week of verified volunteering ≈ +0.72% PAF per year
- Verified annual sponsorship ≈ +6% PAF
- Maximum possible PAF = 1.25 (25% boost)

---

## Workflow & Version Usage

### LOCATOR Workflow
**Purpose:** Objective comparison using government data

**Versions Used:**
1. **EJV v2** (Default): Government-only baseline (9 dimensions)
   - Always shown for all businesses
   - Repeatable, transparent, reviewer-safe
   
2. **EJV v4.1** (Optional Advanced): Decomposed flows + financing
   - Toggle: "Show Advanced Impact (v4.1)"
   - Adds ELVR/EVL breakdown
   - Shows estimated retention vs leakage

**Never Show v4.2 in LOCATOR**

### ENABLE Workflow
**Purpose:** Agency & participation tracking

**Version Used:**
- **EJV v4.2 ONLY**: Participation amplification
  - Requires verified actions
  - Human-in-the-loop checks
  - Time-bound uplift (decays unless renewed)

### Data Flow
```
LOCATOR → Selected business + transaction → ENABLE
         ↓                                    ↓
    v2 + v4.1 metrics                  Apply v4.2 (PAF)
         ↓                                    ↓
    Objective baseline              Participation uplift
```

---

## API Usage

### v4.1 Endpoint (Decomposed Flows)
```bash
POST /api/ejv-v4.1/coffee_shop_10001
Content-Type: application/json

{
  "zip": "10001",
  "location": "Manhattan Coffee Shop",
  "purchase": 100,
  "business_type": "local_small_business",
  "local_hire_pct": 0.85,
  "supplier_local_pct": 0.70,
  "apr": 5.5,
  "loan_term_months": 12,
  "down_payment": 20
}
```

**Response:**
```json
{
  "elvr": 76.50,
  "evl": 23.50,
  "retention_percentage": 76.5,
  "local_capture_components": {
    "lc_wages": 0.85,
    "lc_suppliers": 0.70,
    "lc_taxes": 0.80,
    "lc_financing": 0.70,
    "lc_ownership": 0.90,
    "lc_aggregate": 0.785
  },
  "ejv_v2_baseline": { ... }
}
```

### v4.2 Endpoint (Participation Amplification)
```bash
POST /api/ejv-v4.2/coffee_shop_10001
Content-Type: application/json

{
  "zip": "10001",
  "location": "Manhattan Coffee Shop",
  "purchase": 100,
  "business_type": "local_small_business",
  "participation": {
    "mentoring": {
      "hours": 2,
      "verified": true,
      "duration_months": 12
    },
    "volunteering": {
      "hours": 4,
      "verified": false,
      "duration_months": 6
    }
  }
}
```

**Response:**
```json
{
  "version": "4.2",
  "ejv_v42": {
    "elvr_amplified": 78.10,
    "elvr_base": 75.75,
    "amplification_factor": 1.031,
    "amplification_value": 2.35,
    "retention_percentage": 78.1
  },
  "participation": {
    "paf": 1.031,
    "paf_range": "1.0 - 1.25",
    "activities": [ ... ]
  },
  "base_v41_metrics": { ... }
}
```

---

## Key Insight

**EJV v4.2 = Economic Activity × Participation Agency**

It measures not just what money does, but how people strengthen what money can accomplish. Participation pathways turn EJV from "impact measurement" into "impact participation."

---

## Documentation

**Version Guide:**
- EJV v2: Baseline (9 dimensions, government data)
- EJV v4.1: Decomposed flows (ELVR/EVL, financing-aware)
- EJV v4.2: Participation amplification (PAF multiplier)

**API Help Endpoint:**
```
GET /api/ejv-v4.2/help
```

**Live Application:**
https://fix-app-three.vercel.app

**Source Code:**
https://github.com/[your-repo]/FIX$APP

---

**Last Updated:** January 22, 2026  
**Version:** 4.2  
**Author:** FIX$ GeoEquity Impact Engine
