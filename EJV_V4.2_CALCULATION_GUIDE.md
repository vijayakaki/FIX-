# EJV v4.2 Calculation Guide
## Agency-Enabled Economic Justice Value

**Version:** 4.2  
**Last Updated:** January 22, 2026

---

## Core Formula

```
EJV v4.2 = Community EJV v4.1 × PAF
```

**Where:**
- **Community EJV v4.1** = Base justice-weighted local impact
- **PAF** = Participation Amplification Factor (1.0 to 1.25)

---

## Canonical Definition

EJV v4.2 quantifies the justice-weighted community impact of economic activity by combining decomposed, time-aware local value flows with explicit participation pathways—such as mentoring, volunteering, and community investment—that amplify long-term equity outcomes.

**In Simple Terms:** EJV v4.2 turns impact measurement into impact participation by recognizing that time, skills, and civic engagement strengthen how economic activity translates into lasting community benefit.

---

## Step-by-Step Calculation

### Step 1: Calculate Base Community Impact (v4.1)

Starting from EJV v2 (current implementation):

```
Community EJV = (Purchase Amount × Local Capture) × (Justice Score / 100)
```

#### Components:

**1. Purchase Amount (P):** Transaction value (e.g., $100)

**2. Local Capture (LC):** Percentage of money staying local through hiring
- Range: 40-98% depending on store
- Formula: `local_hire_percentage + unemployment_adjustment`
- Higher unemployment = higher LC adjustment (+0-20%)

**3. Justice Score (JS_ZIP):** 0-100 composite across 9 dimensions
- Each dimension normalized to 0-1 scale
- ZIP Need Modifiers applied to 3 dimensions (AES, ART, HWI)
- Average all 9 dimensions × 100

#### Example:
```
Purchase: $100
Local Capture: 82% (0.82)
Justice Score: 70.6

Base EJV v4.1 = ($100 × 0.82) × (70.6/100)
              = $82 × 0.706
              = $57.89
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
Local supermarket in Manhattan (ZIP 10001) with active participation

### Input Data:

**Transaction:**
- Purchase Amount: $100

**Base Metrics:**
- Local Hire: 82%
- Justice Score: 70.6
- Unemployment: 3.1%
- Median Income: $106,509

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

#### 1. Base EJV v4.1:
```
Community EJV v4.1 = $100 × 0.82 × 0.706 
                   = $82 × 0.706
                   = $57.89
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

#### 3. Calculate EJV v4.2:
```
EJV v4.2 = Base Impact × PAF
         = $57.89 × 1.031
         = $59.68
```

---

### Results Summary:

| Metric | Value |
|--------|-------|
| Base Impact (v4.1) | $57.89 |
| Participation Amplification Factor | 1.031 |
| **EJV v4.2 Community Impact** | **$59.68** |
| Amplification Value | $1.79 |
| Amplification Percentage | 3.1% |

**Interpretation:**  
"For $100 spent with 2 participation pathways (2 hrs/week mentoring + 4 hrs/week volunteering), this creates **$59.68** in justice-weighted community impact. Participation adds **$1.79** (3.1%) through civic engagement, strengthening how economic activity translates into lasting community benefit."

---

## Multiple Scenarios Comparison

### Scenario A: No Participation
```
Input: No participation activities
PAF = 1.0
EJV v4.2 = $57.89 × 1.0 = $57.89

Interpretation: Base impact only, no amplification
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
EJV v4.2 = $57.89 × 1.108 = $64.14

Amplification: $6.25 (10.8%)
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
EJV v4.2 = $57.89 × 1.25 = $72.36

Amplification: $14.47 (25%)
```

---

## Key Design Principles

### 1. PAF is Bounded
- **Minimum:** 1.0 (no participation)
- **Maximum:** 1.25 (25% amplification)
- **Purpose:** Prevents infinite scaling or gaming the system

### 2. Verification Matters
- **Unverified activities:** Full base weight (multiplier = 1.0)
- **Verified activities:** +20% bonus (multiplier = 1.2)
- **Purpose:** Encourages credible reporting and community partnerships

### 3. Duration Rewards Commitment
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

## Key Insight

**EJV v4.2 = Economic Activity × Participation Agency**

It measures not just what money does, but how people strengthen what money can accomplish. Participation pathways turn EJV from "impact measurement" into "impact participation."

---

## Documentation

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
