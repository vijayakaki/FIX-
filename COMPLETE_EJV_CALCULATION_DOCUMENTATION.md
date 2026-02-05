# Complete EJV Calculation Documentation
**Version:** February 3, 2026  
**Status:** Production Implementation

---

## Table of Contents
1. [Overview](#overview)
2. [Simplified EJV (Justice Score)](#simplified-ejv-justice-score)
3. [EJV 4.1 (Local Capture Flow)](#ejv-41-local-capture-flow)
4. [ELVR & EVL (Value Retention/Leakage)](#elvr--evl-value-retentionleakage)
5. [Store-Specific Variance](#store-specific-variance)
6. [Data Sources](#data-sources)
7. [API Endpoints](#api-endpoints)
8. [UI Display](#ui-display)

---

## Overview

The FIX$ application uses **two complementary EJV methodologies** that measure different aspects of economic activity:

| Metric | Purpose | Output | Used For |
|--------|---------|--------|----------|
| **Simplified EJV** | Measures economic justice quality | 0-100% score | Justice/equity rating |
| **EJV 4.1** | Tracks local money flow | 0-100% retention | ELVR/EVL calculation |

**Key Principle:** 
- **Simplified EJV** → "How just/equitable is this business?"
- **EJV 4.1** → "Where does the money go?"

---

## Simplified EJV (Justice Score)

### Purpose
Measures how well a business contributes to economic justice across 5 dimensions.

### Formula
```
Simplified EJV = (W + P + L + A + E) / 5
```

### Components (Each scored 0-1)

#### **W - Fair Wage (0-1)**
```
W = min(1.0, Store_Wage / Living_Wage)
```
- **Measures:** Whether workers earn a living wage
- **Data Sources:** 
  - BLS OEWS (Occupational Employment & Wage Statistics)
  - MIT Living Wage Calculator
- **Variance:** ±10% per store

**Example:**
```
Store wage: $18.50/hr
Living wage: $21.00/hr
W = min(1.0, 18.50/21.00) = 0.881 (88.1%)
```

---

#### **P - Pay Equity (0-1)**
```
P = Equitable_Practices_Percent / 100
```
- **Measures:** Wage equity across demographics (race, gender, age)
- **Data Sources:**
  - EEOC (Equal Employment Opportunity Commission)
  - Industry equity benchmarks
- **Variance:** ±12% per store

**Baseline by Business Type:**
- National chain: 55%
- Local business: 65% (+15% equity bonus)
- Worker cooperative: 95%

---

#### **L - Local Impact (0-1)**
```
L = (Local_Hiring_% + Local_Procurement_%) / 200
```
- **Measures:** Economic circulation through hiring and procurement
- **Data Sources:**
  - Census LODES (worker residence patterns)
  - Supply chain research
- **Variance:** 
  - Local hiring: ±5%
  - Local procurement: ±15%

**Example:**
```
Local hiring: 60%
Local procurement: 25%
L = (60 + 25) / 200 = 0.425 (42.5%)
```

---

#### **A - Affordability (0-1)**
```
A = min(1.0, City_Basket_Price / Store_Basket_Price)
```
- **Measures:** Whether working families can afford to shop here
- **Data Sources:**
  - USDA Food Price Database
  - Industry price surveys
- **Variance:** ±8% per store

**Example:**
```
City average: $150
Store price: $175
A = min(1.0, 150/175) = 0.857 (85.7%)
```

---

#### **E - Environmental (0-1)**
```
E = (Renewable_Energy_% + Recycling_%) / 200
```
- **Measures:** Environmental sustainability practices
- **Data Sources:**
  - EPA (Environmental Protection Agency)
  - Company sustainability reports
- **Variance:** ±15% for both metrics

**Example:**
```
Renewable energy: 40%
Recycling: 60%
E = (40 + 60) / 200 = 0.50 (50%)
```

---

### Simplified EJV Score

**Final Calculation:**
```
Simplified EJV = (0.881 + 0.750 + 0.425 + 0.857 + 0.500) / 5
                = 3.413 / 5
                = 0.683 (68.3%)
```

**Interpretation:**
- **75-100%**: Excellent economic justice practices
- **50-74%**: Good, room for improvement
- **25-49%**: Fair, significant improvements needed
- **0-24%**: Poor, major systemic issues

---

## EJV 4.1 (Local Capture Flow)

### Purpose
Tracks how much money stays in vs. leaves the local economy by decomposing transactions into 5 measurable flows.

### Formula
```
LC_aggregate = (LC_wages × 0.35) + 
               (LC_suppliers × 0.25) + 
               (LC_taxes × 0.15) + 
               (LC_financing × 0.15) + 
               (LC_ownership × 0.10)
```

### Components (Each 0-1, representing % retained locally)

#### **1. LC_wages (35% weight)**
**Definition:** Percentage of employees who live locally

**Calculation:**
```python
# From Census LODES worker flow data
base_local_hire = 0.65 + unemployment_factor  # 65-85% range

# Apply business size multiplier
# Local businesses: 1.15× (hire more locally)
# Chains: 0.85× (hire less locally)
lc_wages = base_local_hire × size_multiplier × store_variance
```

**Variance:** ±5% per store

**Typical Ranges:**
- Large corporation: 40-50%
- National chain: 50-60%
- Regional chain: 60-70%
- Local small business: 75-85%
- Worker cooperative: 90-95%

**Data Sources:**
- Census LODES (Longitudinal Employer-Household Dynamics)
- BLS OEWS (wage levels)
- Local unemployment data

---

#### **2. LC_suppliers (25% weight)**
**Definition:** Percentage of procurement from local suppliers

**Calculation:**
```python
# Industry baseline
base_procurement = {
    "supermarket": 25%,
    "warehouse_club": 15%,
    "local_small_business": 60%
}

# Apply business size multiplier
# Local businesses: 1.30× (source more locally)
# Chains: 0.60× (centralized procurement)
lc_suppliers = base_procurement × size_multiplier × store_variance
```

**Variance:** ±15% per store

**Typical Ranges:**
- Large corporation: 15-25%
- National chain: 25-35%
- Regional chain: 35-50%
- Local small business: 60-70%
- Local cooperative: 75-85%

**Data Sources:**
- BEA Regional Accounts
- Economic Census
- Supply chain research

---

#### **3. LC_taxes (15% weight)**
**Definition:** Percentage of taxes paid to local/state vs federal

**Calculation:**
```python
base_tax_retention = 0.75  # 75% baseline (sales tax, property tax local)

# Small store-specific variation
lc_taxes = base_tax_retention × store_variance  # ±5%
```

**Variance:** ±5% per store

**Typical Range:** 70-90% for all business types
- Sales tax: State/local
- Property tax: Local
- Business taxes: State/local
- Income tax: Federal (leakage)

**Data Sources:**
- State/local tax codes
- BEA government finances
- Census government revenue data

---

#### **4. LC_financing (15% weight)**
**Definition:** Percentage of debt service/interest to local lenders

**Calculation:**
```python
financing_baseline = {
    "national_chain": 0.25,      # Global/national lenders
    "regional_chain": 0.50,      # Mix
    "local_independent": 0.70    # Local banks/credit unions
}

lc_financing = financing_baseline[business_type] × store_variance
```

**Variance:** ±10% per store

**Typical Ranges:**
- Large corporation: 20-30%
- National chain: 30-40%
- Regional chain: 45-55%
- Local small business: 65-75%
- Local cooperative: 85-95%

**Data Sources:**
- FDIC branch data
- NCUA credit union data
- Loan origination patterns

---

#### **5. LC_ownership (10% weight)**
**Definition:** Percentage of ownership held by local residents

**Calculation:**
```python
ownership_baseline = {
    "national_chain": 0.10,      # Distributed shareholders
    "regional_chain": 0.30,      # Some regional ownership
    "local_independent": 0.90    # Local owner(s)
}

lc_ownership = ownership_baseline[business_type] × store_variance
```

**Variance:** ±8% per store

**Typical Ranges:**
- Public corporation: 5-15%
- National franchise: 20-40%
- Regional chain: 25-35%
- Local franchise: 60-80%
- Local independent: 85-95%
- Worker cooperative: 100%

**Data Sources:**
- Business registration data
- Ownership structure (when disclosed)
- Industry research

---

### EJV 4.1 LC_aggregate Calculation

**Example: Local Coffee Shop**

| Component | Value | Weight | Contribution |
|-----------|-------|--------|--------------|
| LC_wages | 0.80 | 35% | 0.80 × 0.35 = 0.280 |
| LC_suppliers | 0.65 | 25% | 0.65 × 0.25 = 0.163 |
| LC_taxes | 0.78 | 15% | 0.78 × 0.15 = 0.117 |
| LC_financing | 0.70 | 15% | 0.70 × 0.15 = 0.105 |
| LC_ownership | 0.90 | 10% | 0.90 × 0.10 = 0.090 |
| **LC_aggregate** | | | **0.755 (75.5%)** |

**Interpretation:**
- For every $100 spent, **$75.50 stays local**, **$24.50 leaks out**

---

## ELVR & EVL (Value Retention/Leakage)

### Relationship to EJV 4.1

**ELVR and EVL are derived from EJV 4.1's LC_aggregate**, NOT from Simplified EJV.

### Formulas

```
ELVR = Purchase_Amount × LC_aggregate
EVL = Purchase_Amount - ELVR

Retention_% = LC_aggregate × 100
Leakage_% = (1 - LC_aggregate) × 100
```

### Example

**Purchase:** $100  
**LC_aggregate:** 0.755 (from EJV 4.1 calculation above)

```
ELVR = $100 × 0.755 = $75.50
EVL = $100 - $75.50 = $24.50

Retention_% = 75.5%
Leakage_% = 24.5%
```

### Why EJV 4.1 (not Simplified EJV) for ELVR/EVL?

**Conceptual Alignment:**

| Methodology | Measures | Purpose |
|-------------|----------|---------|
| **EJV 4.1** | Money flows (where dollars go) | Track economic circulation → ELVR/EVL |
| **Simplified EJV** | Justice quality (how fair/equitable) | Rate business practices → Justice score |

**EJV 4.1 components directly map to money flow:**
- LC_wages → Worker wages staying local
- LC_suppliers → Procurement dollars staying local
- LC_taxes → Tax revenue to local government
- LC_financing → Interest payments to local banks
- LC_ownership → Profits to local owners

**Simplified EJV components measure different things:**
- W → Wage adequacy (vs living wage) ≠ local retention
- P → Pay equity ≠ local retention
- A → Affordability ≠ local retention
- E → Environmental practices ≠ local retention

**Conclusion:** ELVR/EVL should use EJV 4.1 because it's designed to track money flows.

---

## Store-Specific Variance

### Purpose
Create realistic store-to-store differences while maintaining deterministic consistency (same store = same values).

### Implementation

**Method:** Hash-based deterministic variation
```python
store_id_hash = hash(str(store_id) + "_component") % 10000
variation_factor = min_value + (store_id_hash / 10000) * range
component_value = base_value × variation_factor
```

**Key Properties:**
1. **Deterministic:** Same store_id always produces same variation
2. **Unique:** Different stores get different variations
3. **Independent:** Each metric uses different hash suffix
4. **Bounded:** Variations stay within realistic ranges

### Variance Ranges by Component

| Component | Variance Range | Why? |
|-----------|----------------|------|
| **Simplified EJV:** | | |
| W - Wages | ±10% | Wage variations within industry |
| W - Employee count | ±10% | Staffing level differences |
| P - Pay equity | ±12% | Practice variations |
| L - Local hiring | ±5% | Relatively stable |
| L - Procurement | ±15% | Supply chain flexibility |
| A - Basket pricing | ±8% | Pricing strategy |
| E - Renewable energy | ±15% | Investment levels vary |
| E - Recycling | ±15% | Program maturity varies |
| **EJV 4.1:** | | |
| LC_wages | ±5% | From payroll (already varied) |
| LC_suppliers | ±15% | From procurement (already varied) |
| LC_taxes | ±5% | Relatively uniform |
| LC_financing | ±10% | Lender relationships vary |
| LC_ownership | ±8% | Ownership structures vary |

### Example: Two Publix Stores in Same ZIP

**Store A (hash: 3421):**
- LC_wages: 0.56 (56%)
- LC_suppliers: 0.28 (28%)
- LC_aggregate: 0.524 (52.4%)

**Store B (hash: 7834):**
- LC_wages: 0.59 (59%)
- LC_suppliers: 0.32 (32%)
- LC_aggregate: 0.556 (55.6%)

**Different but consistent** - Store A always gets same values, Store B always gets its values.

---

## Data Sources

### Government/Official Data

| Source | What It Provides | Update Frequency | Used For |
|--------|------------------|------------------|----------|
| **BLS OEWS** | Median wages by occupation/location | Annual (May) | W (Fair Wage) |
| **MIT Living Wage** | Cost of living by county | Quarterly | W (Fair Wage) |
| **Census LODES** | Worker residence/commute patterns | Annual | L, LC_wages |
| **Census ACS** | Demographics, median income | Annual | Economic context |
| **BLS LAUS** | Unemployment rates | Monthly | Local hiring factors |
| **EEOC** | Pay equity data | Annual | P (Pay Equity) |
| **EPA** | Environmental data | Annual | E (Environmental) |
| **BEA Regional** | Supply chain patterns | Annual | LC_suppliers |
| **FDIC/NCUA** | Bank/credit union locations | Quarterly | LC_financing |

### Industry Research

| Source | What It Provides | Used For |
|--------|------------------|----------|
| **Supply Chain Studies** | Procurement patterns by industry | LC_suppliers |
| **Civic Economics** | Local multiplier research | Business size factors |
| **USDA Food Prices** | Regional food costs | A (Affordability) |
| **Company ESG Reports** | Environmental practices | E (Environmental) |
| **PayScale/Glassdoor** | Equity benchmarks | P (Pay Equity) |

### Fallback/Modeling

When real data unavailable, use:
- Industry baseline averages
- Business type standards
- Economic modeling estimates
- Clearly labeled as estimates

---

## API Endpoints

### 1. Simplified EJV + EJV 4.1 (Combined)

```
GET /api/ejv/simple/<store_id>?zip=<zip>&name=<name>
```

**Returns:**
```json
{
  "ejv_score": 0.683,
  "ejv_percentage": 68.3,
  "components": {
    "W_fair_wage": 0.881,
    "P_pay_equity": 0.750,
    "L_local_impact": 0.425,
    "A_affordability": 0.857,
    "E_environmental": 0.500
  },
  "economic_impact": {
    "elvr": 75.50,
    "evl": 24.50,
    "retention_percent": 75.5
  },
  "ejv_v41": {
    "ejv_version": "4.1",
    "local_capture_components": {
      "lc_wages": 0.800,
      "lc_suppliers": 0.650,
      "lc_taxes": 0.780,
      "lc_financing": 0.700,
      "lc_ownership": 0.900,
      "lc_aggregate": 0.755
    },
    "elvr": 75.50,
    "evl": 24.50,
    "retention_percentage": 75.5
  }
}
```

### 2. EJV 4.1 Only

```
GET /api/ejv/v4.1/<store_id>?zip=<zip>&name=<name>&purchase=<amount>
```

**Returns:**
```json
{
  "ejv_version": "4.1",
  "local_capture_components": {
    "lc_wages": 0.800,
    "lc_suppliers": 0.650,
    "lc_taxes": 0.780,
    "lc_financing": 0.700,
    "lc_ownership": 0.900,
    "lc_aggregate": 0.755
  },
  "purchase_amount": 100,
  "elvr": 75.50,
  "evl": 24.50,
  "retention_percentage": 75.5,
  "leakage_percentage": 24.5,
  "weights": {
    "wages": 0.35,
    "suppliers": 0.25,
    "taxes": 0.15,
    "financing": 0.15,
    "ownership": 0.10
  },
  "formula": "LC_aggregate = (LC_wages × 0.35) + (LC_suppliers × 0.25) + (LC_taxes × 0.15) + (LC_financing × 0.15) + (LC_ownership × 0.10)"
}
```

### 3. Help Documentation

```
GET /api/ejv/simple/help
```

Returns detailed explanation of Simplified EJV methodology.

---

## UI Display

### Main Dashboard

```
┌─────────────────────────────────────┐
│  Publix                              │
│  Unknown                             │
├─────────────────────────────────────┤
│                                      │
│  61.90               $52.41         │
│  SIMPLIFIED EJV      EJV v4.1 (%)   │
│  (W,P,L,A,E)        (LC_aggregate)  │
│                                      │
├─────────────────────────────────────┤
│                                      │
│  52.4%               47.6%          │
│  Estimated Local     Estimated      │
│  Retention (%)       Leakage (%)    │
│  (from EJV 4.1)      (from EJV 4.1) │
│                                      │
└─────────────────────────────────────┘
```

### Simplified EJV Components (0-100)
- W (Fair Wage): 88.1
- P (Pay Equity): 75.0
- L (Local Impact): 42.5
- A (Affordability): 85.7
- E (Environmental): 50.0

### EJV v4.1 - 5 Local Capture Flows (per $100)
- 💼 Wages (35%): $28.00
- 🏪 Suppliers (25%): $16.25
- 🏛️ Taxes (15%): $11.70
- 🏦 Financing (15%): $10.50
- 👥 Ownership (10%): $9.00

**Note:** ELVR % and EJV 4.1 % show the **same value** because ELVR is derived from EJV 4.1's LC_aggregate.

---

## Summary

### Two Metrics, Two Purposes

| | Simplified EJV | EJV 4.1 |
|---|----------------|---------|
| **Question** | How just is this business? | Where does money flow? |
| **Components** | W, P, L, A, E | LC_wages, suppliers, taxes, financing, ownership |
| **Output** | Justice score (0-100%) | Retention rate (0-100%) |
| **Used For** | Rating business practices | Calculating ELVR/EVL |
| **Variance** | Each component ±5-15% | Each component ±5-15% |

### Data Flow

```
1. User searches for store
2. API calculates:
   a. Simplified EJV (justice score)
   b. EJV 4.1 (local capture)
3. ELVR/EVL derived from EJV 4.1 LC_aggregate
4. UI displays:
   - Simplified EJV: 68.3%
   - EJV 4.1: 75.5% (same as ELVR %)
   - ELVR: 75.5%
   - EVL: 24.5%
```

### Key Insight

**They measure different things but are complementary:**
- A business can score high on Simplified EJV (fair wages, good equity) but low on EJV 4.1 (money leaks to national HQ)
- A business can score low on Simplified EJV (low wages) but high on EJV 4.1 (locally owned, local suppliers)

**Together they provide complete picture:**
- **Simplified EJV** → Quality of economic justice
- **EJV 4.1** → Quantity of local economic retention

---

## Implementation Status

✅ **Implemented:** Both Simplified EJV and EJV 4.1 with proper variance  
✅ **Deployed:** Vercel production (https://fix-app-three.vercel.app)  
✅ **API:** Both `/api/ejv/simple/<store_id>` and `/api/ejv/v4.1/<store_id>`  
✅ **UI:** Displays both metrics with proper labeling  
✅ **ELVR/EVL:** Derived from EJV 4.1 LC_aggregate  

**Last Updated:** February 3, 2026  
**Commit:** 0e44d86
