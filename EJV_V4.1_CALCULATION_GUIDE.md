# EJV v4.1 Calculation Guide
## Decomposed Local Capture + Financing-Aware

**Version:** 4.1  
**Last Updated:** January 23, 2026  
**Purpose:** Directional estimation of local value retention vs leakage

---

## Core Formula

```
ELVR = P × ΣLCᵢ
EVL = P - ELVR
```

**Where:**
- **P** = Purchase Amount ($)
- **LCᵢ** = Local Capture components (wages, suppliers, taxes, financing, ownership)
- **ELVR** = Estimated Local Value Retained ($)
- **EVL** = Estimated Value Leakage ($)

---

## Canonical Definition

EJV v4.1 provides a **directional estimate** of how much transaction value is retained locally versus leaked out, by decomposing the purchase into five measurable components: wages, suppliers, taxes, financing, and ownership.

**Important:** This is an **estimate** based on public data and economic modeling, not audited financial flow.

---

## Five Local Capture Components

### 1. LC_wages (Weight: 35%)
**Definition:** Percentage of wages paid to workers living in the local area

**Factors:**
- Local hiring practices
- Commute patterns
- ZIP-level employment data

**Typical Ranges:**
- Large corporation: 40-50%
- National chain: 50-60%
- Regional chain: 60-70%
- Local small business: 75-85%
- Worker cooperative: 90-95%

**Data Sources:**
- BLS OEWS (wage levels)
- Census LODES (worker flows)
- Payroll data when available

---

### 2. LC_suppliers (Weight: 25%)
**Definition:** Percentage of procurement/inputs sourced from local suppliers

**Factors:**
- Supply chain structure
- Industry vertical integration
- Regional supplier availability

**Typical Ranges:**
- Large corporation: 15-25% (centralized procurement)
- National chain: 25-35%
- Regional chain: 35-50%
- Local small business: 60-70%
- Local cooperative: 75-85%

**Data Sources:**
- Industry supply chain research
- BEA regional accounts
- Business survey data (when available)

---

### 3. LC_taxes (Weight: 15%)
**Definition:** Percentage of taxes paid to local/state jurisdiction vs federal

**Factors:**
- Sales tax (state/local)
- Property tax (local)
- Business taxes (state/local)
- Federal income tax (leakage)

**Typical Ranges:**
- All business types: 60-90%
- Higher for property-intensive businesses
- Lower for high-profit margin businesses

**Data Sources:**
- State/local tax codes
- BEA government finances
- Census government revenue data

---

### 4. LC_financing (Weight: 15%)
**Definition:** Percentage of interest/financing costs retained locally

**Factors:**
- Bank/lender location (local vs national)
- Credit union vs bank
- Community development financing
- Owner-financed vs external debt

**Typical Ranges:**
- Large corporation: 20-30% (national/global lenders)
- National chain: 30-40%
- Regional chain: 45-55%
- Local small business: 65-75% (local banks)
- Local cooperative: 85-95% (credit unions, local lenders)

**Data Sources:**
- FDIC branch data
- NCUA credit union data
- Loan origination data (when available)

**Time-Aware Component:**
If purchase is financed, calculate interest over loan life:
```
Monthly Rate = APR / 12 / 100
Monthly Payment = Principal × (r(1+r)^n) / ((1+r)^n - 1)
Total Interest = (Monthly Payment × n) - Principal
Local Interest = Total Interest × LC_financing
```

---

### 5. LC_ownership (Weight: 10%)
**Definition:** Percentage of ownership held by local residents/entities

**Factors:**
- Sole proprietor (local)
- Partnership structure
- Corporation (public vs private)
- Geographic distribution of shareholders

**Typical Ranges:**
- Public corporation: 5-15%
- National chain franchise: 20-40%
- Regional chain: 25-35%
- Local franchise: 60-80%
- Local independent: 85-95%
- Worker cooperative: 100%

**Data Sources:**
- Business registration data
- Ownership structure (when disclosed)
- Industry research

---

## Aggregate Local Capture Formula

```
LC_aggregate = (LC_wages × 0.35) + 
               (LC_suppliers × 0.25) + 
               (LC_taxes × 0.15) + 
               (LC_financing × 0.15) + 
               (LC_ownership × 0.10)
```

**Why These Weights?**
- **Wages (35%)**: Largest direct local economic impact
- **Suppliers (25%)**: Significant multiplier effect
- **Taxes (15%)**: Public goods/services funding
- **Financing (15%)**: Long-term wealth building
- **Ownership (10%)**: Profit retention and control

---

## Complete Worked Example

### Scenario: Local Coffee Shop

**Transaction:**
- Purchase: $100
- Business Type: local_small_business
- ZIP: 10001 (Manhattan)

**Step 1: Determine Local Capture Components**

Using defaults for local_small_business:

| Component | Value | Reasoning |
|-----------|-------|-----------|
| LC_wages | 0.80 | 80% of employees live within commuting distance |
| LC_suppliers | 0.65 | Mix of local (produce, baked goods) and regional (coffee beans) |
| LC_taxes | 0.80 | NY state/local sales tax + property tax |
| LC_financing | 0.70 | Loan from local credit union |
| LC_ownership | 0.90 | Owner lives in NYC |

**Step 2: Calculate Aggregate Local Capture**

```
LC_aggregate = (0.80 × 0.35) + (0.65 × 0.25) + (0.80 × 0.15) + (0.70 × 0.15) + (0.90 × 0.10)

Components:
  Wages:      0.80 × 0.35 = 0.280
  Suppliers:  0.65 × 0.25 = 0.1625
  Taxes:      0.80 × 0.15 = 0.120
  Financing:  0.70 × 0.15 = 0.105
  Ownership:  0.90 × 0.10 = 0.090
  
LC_aggregate = 0.7575 (75.75%)
```

**Step 3: Calculate ELVR and EVL**

```
ELVR = $100 × 0.7575 = $75.75
EVL = $100 - $75.75 = $24.25

Retention Rate: 75.75%
Leakage Rate: 24.25%
```

**Step 4: Add Financing (Optional)**

If financed at 5.5% APR for 12 months with $20 down:

```
Financed Amount: $100 - $20 = $80
Monthly Rate: 5.5% / 12 = 0.458%
Monthly Payment: $6.82
Total Paid: $6.82 × 12 = $81.88
Total Interest: $81.88 - $80 = $1.88
Local Interest: $1.88 × 0.70 = $1.32

Updated ELVR: $75.75 + $1.32 = $77.07
Total Transaction Value: $100 + $1.88 = $101.88
EVL: $101.88 - $77.07 = $24.81
```

---

## Comparison by Business Type

### $100 Purchase Comparison

| Business Type | LC_agg | ELVR | EVL | Retention % |
|---------------|--------|------|-----|-------------|
| Worker Cooperative | 0.920 | $92.00 | $8.00 | 92.0% |
| B-Corp | 0.800 | $80.00 | $20.00 | 80.0% |
| Local Small Business | 0.758 | $75.75 | $24.25 | 75.8% |
| Regional Chain | 0.520 | $52.00 | $48.00 | 52.0% |
| National Chain | 0.400 | $40.00 | $60.00 | 40.0% |
| Large Corporation | 0.280 | $28.00 | $72.00 | 28.0% |

**Key Insight:** Local businesses retain 2-3x more value locally than large corporations.

---

## EJV v2 Integration

**v4.1 Uses v2 for Justice Weighting:**

EJV v4.1 builds on v2's 9-dimension justice framework:
1. AES - Access to Essential Services
2. ART - Access to Resources & Technology
3. HWI - Health, Wellness & Inclusion
4. PSR - Public Service Representation
5. CAI - Cultural Awareness & Inclusivity
6. JCE - Job Creation/Economic Empowerment
7. FSI - Financial Support & Investment
8. CED - Community Engagement & Development
9. ESD - Education & Skill Development

**v4.1 Response Includes v2 Baseline:**
```json
{
  "elvr": 75.75,
  "evl": 24.25,
  "local_capture_components": { ... },
  "ejv_v2_baseline": {
    "EJV": 67.2,
    "justice_score": 72.4,
    "dimensions": { ... }
  }
}
```

This allows users to see both:
- **v2**: Relative justice-weighted score (0-100)
- **v4.1**: Dollar-based retention/leakage estimate

---

## Terminology & Disclaimers

### Use These Terms:
✅ "Estimated Local Value Retained"
✅ "Estimated Value Leakage"
✅ "Directional retention analysis"
✅ "Model-based estimates"

### Avoid These Terms:
❌ "Actual wealth retained"
❌ "Measured leakage"
❌ "Verified capital flow"
❌ "Audited financial data"

### Required Disclaimer:
> "Estimates based on public data and economic modeling. Not audited financial measures."

---

## API Usage

### Request Example:

```bash
POST /api/ejv-v4.1/coffee_shop_10001
Content-Type: application/json

{
  "zip": "10001",
  "location": "Manhattan Coffee Shop",
  "purchase": 100,
  "business_type": "local_small_business",
  
  // Optional: Override defaults with actual data
  "local_hire_pct": 0.85,
  "supplier_local_pct": 0.70,
  "tax_local_pct": 0.82,
  "financing_local_pct": 0.75,
  "ownership_local_pct": 0.95,
  
  // Optional: Financing parameters
  "apr": 5.5,
  "loan_term_months": 12,
  "down_payment": 20
}
```

### Response Example:

```json
{
  "store_id": "coffee_shop_10001",
  "location": "Manhattan Coffee Shop",
  "zip_code": "10001",
  "ejv_version": "4.1",
  
  "elvr": 77.07,
  "evl": 24.81,
  "retention_percentage": 75.6,
  "leakage_percentage": 24.4,
  
  "purchase_amount": 100,
  "down_payment": 20,
  
  "local_capture_components": {
    "lc_wages": 0.85,
    "lc_suppliers": 0.70,
    "lc_taxes": 0.82,
    "lc_financing": 0.75,
    "lc_ownership": 0.95,
    "lc_aggregate": 0.791,
    "data_source": "mixed"
  },
  
  "financing_details": {
    "financed_amount": 80.00,
    "apr": 5.5,
    "loan_term_months": 12,
    "monthly_payment": 6.82,
    "total_interest": 1.88,
    "local_interest_retained": 1.32
  },
  
  "ejv_v2_baseline": {
    "EJV": 67.2,
    "justice_score": 72.4,
    "dimensions": {
      "AES": 0.68,
      "ART": 0.74,
      "HWI": 0.71,
      ...
    }
  },
  
  "calculation_method": "decomposed_flows",
  "data_disclaimer": "Estimates based on public data and economic modeling",
  "formula": "ELVR = 100 × 0.791 = $79.10"
}
```

---

## Data Sources & Methodology

### Overview

EJV v4.1 combines **government data** (where available) with **economic modeling estimates** to decompose transaction flows into 5 components.

**Data Philosophy:**
- Use government data for wages, demographics, taxes
- Use industry research for supply chain patterns
- Use economic modeling for business-specific LC components
- Clearly label estimates vs. measured data

### Component-Specific Data Sources

#### 1. LC_wages (35% weight)

**Primary Data:**

**A. BLS OEWS (Occupation Employment and Wage Statistics)**
- **URL**: https://www.bls.gov/oes/
- **Version**: May 2024
- **Use**: Wage levels by occupation and location
- **Reliability**: ±5% accuracy

**B. Census LODES (Worker Flows)**
- **URL**: https://lehd.ces.census.gov/data/
- **Version**: 2021
- **Use**: Where workers live vs. work (commute patterns)
- **Coverage**: Block-level employment flows

**C. BLS LAUS (Unemployment)**
- **URL**: https://www.bls.gov/lau/
- **Update**: Monthly
- **Use**: Unemployment rate affects local hiring
- **Formula**: Higher unemployment → Higher local hire (+0-20% bonus)

**Business Type Defaults** (when specific data unavailable):
- Large corporation: 0.40 (40% workers local)
- National chain: 0.50
- Regional chain: 0.60
- Local small business: 0.80
- Worker cooperative: 0.95

**Source**: Industry employment patterns + regional labor market analysis

---

#### 2. LC_suppliers (25% weight)

**Data Sources (Industry Research):**

**A. BEA Regional Accounts**
- **URL**: https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas
- **Use**: Regional supply chain patterns
- **Measures**: Input-output tables, procurement patterns

**B. Economic Census**
- **URL**: https://www.census.gov/programs-surveys/economic-census.html
- **Frequency**: Every 5 years (2022 most recent)
- **Use**: Business-to-business transactions, supply chain concentration

**C. Industry Supply Chain Studies**
- **Sources**: Industry associations, academic research, CSR reports
- **Coverage**: Varies by industry (food retail better documented)

**Reliability**: ±20-30% (most estimated, limited transparency)

---

#### 3. LC_taxes (15% weight)

**Primary Data:**

**A. BEA Government Finances**
- **URL**: https://www.bea.gov/data/income-saving/state-and-local-government-finances
- **Use**: Tax revenue distribution (local/state/federal)

**B. Census Government Finances**
- **URL**: https://www.census.gov/programs-surveys/gov-finances.html
- **Use**: State and local tax revenues, property tax, sales tax rates

**C. State/Local Tax Codes**
- **Sources**: State revenue departments, municipal codes
- **Use**: Sales tax rates (state + local), property tax rates

**Typical breakdown**:
- Local + State taxes: 60-90% (usually 70-80%)
- Federal taxes: 10-40% (usually 20-30%)

**Reliability**: High (±5%), tax structures are public

---

#### 4. LC_financing (15% weight)

**Data Sources:**

**A. FDIC Bank Data**
- **URL**: https://www.fdic.gov/analysis/bank-find/
- **Use**: Bank locations and deposit sources
- **Coverage**: All FDIC-insured banks

**B. NCUA Credit Union Data**
- **URL**: https://www.ncua.gov/analysis/credit-union-corporate-call-report-data
- **Use**: Credit union locations and membership

**C. CDFI Fund**
- **URL**: https://www.cdfifund.gov/
- **Use**: Community Development Financial Institutions directory

**Lender Type Classification:**

| Lender Type | LC_financing | Reliability |
|-------------|--------------|-------------|
| CDFI | 0.90-0.95 | High |
| Credit Union | 0.80-0.90 | High |
| Community Bank | 0.70-0.80 | Medium |
| Regional Bank | 0.40-0.60 | Medium |
| National Bank | 0.20-0.30 | Medium |
| Private Equity | 0.05-0.15 | Low |

**Reliability**: Medium (±15%), based on lender type identification

---

#### 5. LC_ownership (10% weight)

**Data Sources:**

**A. Business Registration Records**
- **Sources**: State Secretaries of State
- **Use**: Legal ownership structure (corporation vs. LLC vs. cooperative)

**B. SEC EDGAR (Public Companies)**
- **URL**: https://www.sec.gov/edgar
- **Use**: Shareholder information for public companies

**C. Cooperative Registries**
- **Sources**: National Cooperative Business Association, state registries
- **Use**: Identify worker/consumer cooperatives

**D. B Corp Directory**
- **URL**: https://www.bcorporation.net/en-us/find-a-b-corp
- **Use**: B Corp certified businesses

**Ownership Type Classification:**

| Ownership Type | LC_ownership | Data Source |
|----------------|--------------|-------------|
| Worker Cooperative | 1.00 | Cooperative registries |
| Local Family Business | 0.85-0.95 | Business registration + local address |
| ESOP (Broad-based) | 0.75-0.85 | DOL ESOP database |
| Regional Corp | 0.25-0.40 | SEC filings + HQ location |
| National Corp | 0.10-0.20 | SEC filings, diffuse ownership |

**Reliability**: Medium (±20%), ownership structures complex

---

### Data Quality Summary

| Component | Primary Source | Reliability | Transparency |
|-----------|----------------|-------------|--------------|
| **LC_wages** | BLS OEWS + LODES | ±10% | High (government data) |
| **LC_suppliers** | Industry research + BEA | ±25% | Low (proprietary) |
| **LC_taxes** | BEA + tax codes | ±5% | High (public records) |
| **LC_financing** | FDIC + NCUA + lender type | ±15% | Medium (lender classification) |
| **LC_ownership** | Business registrations + SEC | ±20% | Medium (complex structures) |

### Default Business Type Values

Used when specific business data unavailable:

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

**Source**: Industry employment patterns, supply chain research, ownership structure analysis

### Data Limitations

**Important Disclaimers:**

1. **Estimates, Not Audited Flows**: v4.1 provides directional estimates based on public data and economic modeling, not audited financial flow tracking.

2. **Business Type Generalizations**: Default LC values are industry averages; actual businesses may vary significantly.

3. **Supply Chain Opacity**: LC_suppliers is least transparent—supply chains are often proprietary and complex.

4. **Time-Aware Approximation**: Financing calculations use standard amortization; actual terms may vary.

5. **Ownership Complexity**: Corporate structures can be multi-layered; LC_ownership estimates primary level only.

### Citation Format

**For Research/Academic Use:**
```
EJV v4.1 calculations use publicly available data from:

- Bureau of Labor Statistics (2024). Occupational Employment and Wage 
  Statistics (OEWS), May 2024. https://www.bls.gov/oes/

- U.S. Census Bureau (2021). LEHD Origin-Destination Employment Statistics 
  (LODES). https://lehd.ces.census.gov/data/

- Bureau of Economic Analysis (2024). Regional Economic Accounts. 
  https://www.bea.gov/data/gdp/gdp-county-metro-and-other-areas

- Federal Deposit Insurance Corporation. Bank Find Suite. 
  https://www.fdic.gov/analysis/bank-find/

All data accessed: January 2026
```

**For Tool Attribution:**
```
EJV v4.1 decomposes economic flows using:
- Government data (BLS, Census, BEA, FDIC/NCUA)
- Industry research (supply chain analysis)
- Economic modeling (business type defaults)

This is a directional estimate, not audited financial tracking.
```

---

## Workflow Usage

### LOCATOR Page:
1. **Default:** Show EJV v2 (government-only baseline)
2. **Optional Toggle:** "Show Advanced Impact (v4.1)"
   - Displays ELVR/EVL breakdown
   - Shows decomposed components
   - Includes financing analysis if available

### Never Show v4.2 in LOCATOR
- v4.2 (participation) belongs only in ENABLE workflow
- Keeps LOCATOR objective and data-driven

---

## Key Advantages of v4.1

### vs v2:
- **Dollar-based** instead of 0-100 score
- **Decomposed** into actionable components
- **Directional** retention vs leakage insight
- **Time-aware** for financed purchases

### vs Traditional Impact:
- **Transparent** calculation methodology
- **Government data** where possible
- **Comparable** across business types
- **Not proprietary** scoring

### Use Cases:
- Side-by-side business comparison
- Consumer optimization decisions
- Policy discussion framing
- Business improvement targeting

---

## Documentation

**Related Guides:**
- [EJV v2 Calculation Guide](EJV_V2_CALCULATION_GUIDE.md)
- [EJV v4.2 Calculation Guide](EJV_V4.2_CALCULATION_GUIDE.md)

**API Endpoints:**
- `/api/ejv-v2/<store_id>` - Baseline (9 dimensions)
- `/api/ejv-v4.1/<store_id>` - Decomposed flows (this guide)
- `/api/ejv-v4.2/<store_id>` - Participation amplification

**Live Application:**
https://fix-app-three.vercel.app

---

**Last Updated:** January 23, 2026
