# EJV Architecture Revision Summary
## Aligning Implementation with EJV Discussion Document

**Date:** January 23, 2026  
**Source:** EJV discussion 01222026.docx

---

## Key Changes Made

### 1. **Removed EDL as a Dimension from v4.1**

**Previous (Incorrect):**
- v4.1 had 10 dimensions: 9 from v2 + EDL (Engage in Decision Loop)
- EDL was calculated from employee_voice, customer_engagement, community_input
- Treated participation as a structural dimension

**Current (Correct):**
- v4.1 focuses on **decomposed local capture flows**
- Participation belongs in v4.2 as PAF multiplier, not as a dimension
- EDL concept merged into v4.2's participation pathways

---

### 2. **Redesigned v4.1: Decomposed Local Capture**

**New Architecture:**
v4.1 now decomposes transactions into 5 components:

| Component | Weight | Description |
|-----------|--------|-------------|
| **LC_wages** | 35% | % wages to local workers |
| **LC_suppliers** | 25% | % from local suppliers |
| **LC_taxes** | 15% | % taxes paid locally |
| **LC_financing** | 15% | % financing costs local |
| **LC_ownership** | 10% | % local ownership |

**Key Outputs:**
- **ELVR** (Estimated Local Value Retained) = P × ΣLCᵢ
- **EVL** (Estimated Value Leakage) = P - ELVR
- Retention percentage and leakage percentage

**Time-Aware Financing:**
- Calculates interest over loan life
- Applies LC_financing to determine local interest retention

---

### 3. **Clarified Version Architecture**

```
EJV v2 (Baseline)
   ↓
   Government-only data
   9 dimensions
   0-100 score
   Used in: LOCATOR (default)

EJV v4.1 (Decomposed Flows)
   ↓
   Decomposed local capture
   5 components (wages, suppliers, taxes, financing, ownership)
   ELVR/EVL dollar values
   Used in: LOCATOR (optional advanced view)

EJV v4.2 (Participation Amplification)
   ↓
   PAF multiplier on v4.1's ELVR
   Verified participation actions
   ELVR × (1.0 to 1.25)
   Used in: ENABLE (only)
```

---

## Code Changes

### File: `api/index.py`

#### Removed:
- `EDL_DEFAULTS` dictionary
- `calculate_edl_score()` function
- 10-dimension justice score calculation

#### Added:
- `LOCAL_CAPTURE_DEFAULTS` dictionary (by business type)
- `calculate_local_capture_components()` function
- Decomposed flow calculation in `calculate_ejv_v41()`
- Financing-aware interest calculation
- ELVR and EVL calculation

#### Modified `calculate_ejv_v41()`:
**New Parameters:**
```python
def calculate_ejv_v41(
    store_id, 
    purchase_amount=100.0,
    business_type="unknown",
    local_hire_pct=None,
    supplier_local_pct=None,
    tax_local_pct=None,
    financing_local_pct=None,
    ownership_local_pct=None,
    apr=None,
    loan_term_months=None,
    down_payment=0.0
    ...
)
```

**New Return Structure:**
```python
{
    "elvr": 75.75,  # Estimated Local Value Retained
    "evl": 24.25,   # Estimated Value Leakage
    "retention_percentage": 75.8,
    "local_capture_components": {
        "lc_wages": 0.80,
        "lc_suppliers": 0.65,
        "lc_taxes": 0.80,
        "lc_financing": 0.70,
        "lc_ownership": 0.90,
        "lc_aggregate": 0.7575
    },
    "financing_details": { ... },
    "ejv_v2_baseline": { ... }
}
```

#### Modified v4.1 Endpoint (`/api/ejv-v4.1/<store_id>`):
- Accepts decomposed local capture parameters
- Accepts financing parameters (apr, loan_term_months, down_payment)
- Removed EDL decision_engagement parameters
- Returns ELVR/EVL instead of justice-weighted dollar impact

#### Modified v4.2 Endpoint (`/api/ejv-v4.2/<store_id>`):
- Now applies PAF to v4.1's ELVR (not community_ejv_v41)
- Returns `elvr_amplified` instead of `community_impact`
- Uses v4.1 decomposed flows as base
- Properly shows base_v41_metrics with new structure

---

## Documentation Changes

### 1. **Created: `EJV_V4.1_CALCULATION_GUIDE.md`**
New comprehensive guide covering:
- Five local capture components
- Aggregate LC calculation formula
- ELVR/EVL formulas
- Financing-aware calculation
- Business type comparisons
- API usage examples
- Workflow integration
- Terminology and disclaimers

### 2. **Updated: `EJV_V4.2_CALCULATION_GUIDE.md`**
Revisions:
- Changed from "Base EJV v4.1" to "Base ELVR v4.1"
- Updated architecture section to clarify v2 → v4.1 → v4.2 flow
- Changed formulas from `EJV v4.2 = Community EJV × PAF` to `ELVR v4.2 = ELVR v4.1 × PAF`
- Updated worked examples to use decomposed flows
- Added "Workflow & Version Usage" section
- Added API usage examples with new request/response structure
- Clarified: "Never show v4.2 in LOCATOR"

### 3. **Previous Documents (Now Obsolete/Needs Update):**
- `EJV_VERSIONS_KEPT_SEPARATE.md` - References old EDL implementation
- `IMPLEMENTATION_SUMMARY.md` - References old EDL implementation
- `test_edl.py` - Tests old EDL functionality

---

## Terminology Changes

### Old Terms (v4.1 with EDL):
- "Justice-Weighted Local Impact with EDL"
- "10 dimensions including EDL"
- "EDL (Engage in Decision Loop) dimension"
- "Community EJV v4.1"
- "Justice Score v4.1"

### New Terms (v4.1 Decomposed):
- "Decomposed Local Capture + Financing-Aware"
- "5 local capture components"
- "Estimated Local Value Retained (ELVR)"
- "Estimated Value Leakage (EVL)"
- "Retention percentage"
- "Directional estimates"

---

## Workflow Clarification

### LOCATOR Page:
**Always Show:**
- EJV v2 (government-only baseline)

**Optional Toggle ("Show Advanced Impact"):**
- EJV v4.1 (decomposed flows, ELVR/EVL)

**Never Show:**
- EJV v4.2 (participation belongs in ENABLE only)

### ENABLE Page:
**Only Show:**
- EJV v4.2 (participation amplification)
- Takes v4.1 as base, applies PAF

**Requires:**
- Verified participation evidence
- Human-in-the-loop checks
- Time-bound tracking

---

## Default Local Capture Values

Business types with default LC components:

| Business Type | Wages | Suppliers | Taxes | Financing | Ownership |
|---------------|-------|-----------|-------|-----------|-----------|
| worker_cooperative | 95% | 80% | 90% | 95% | 100% |
| b_corp | 85% | 70% | 85% | 80% | 80% |
| local_small_business | 80% | 65% | 80% | 70% | 90% |
| regional_chain | 60% | 40% | 70% | 50% | 30% |
| national_chain | 50% | 25% | 65% | 30% | 10% |
| large_corporation | 40% | 15% | 60% | 20% | 5% |
| unknown | 60% | 45% | 70% | 50% | 40% |

---

## API Request Changes

### v4.1 Request (Old):
```json
{
  "purchase": 100,
  "decision_engagement": {
    "employee_voice": 0.8,
    "customer_engagement": 0.7,
    "community_input": 0.6
  },
  "business_type": "local_small_business"
}
```

### v4.1 Request (New):
```json
{
  "purchase": 100,
  "business_type": "local_small_business",
  "local_hire_pct": 0.85,
  "supplier_local_pct": 0.70,
  "tax_local_pct": 0.82,
  "financing_local_pct": 0.75,
  "ownership_local_pct": 0.95,
  "apr": 5.5,
  "loan_term_months": 12,
  "down_payment": 20
}
```

---

## What Remains Unchanged

### EJV v2:
- Still has 9 dimensions
- Still uses ZIP need modifiers
- Still provides 0-100 justice score
- Still used as baseline in LOCATOR

### PAF Calculation (v4.2):
- Still has 5 participation types
- Still ranges from 1.0 to 1.25
- Still uses intensity × verification × duration
- Still amplifies base impact

### Data Sources:
- BLS OEWS wage data
- Census ACS demographics
- TIGER/Line geography
- FDIC/NCUA financing data (new)

---

## Testing Recommendations

### Unit Tests Needed:
1. `calculate_local_capture_components()` with various business types
2. `calculate_ejv_v41()` with defaults
3. `calculate_ejv_v41()` with overrides
4. `calculate_ejv_v41()` with financing parameters
5. v4.2 endpoint applying PAF to ELVR correctly

### Integration Tests Needed:
1. v4.1 endpoint with default LC values
2. v4.1 endpoint with custom LC values
3. v4.1 endpoint with financing
4. v4.2 endpoint building on v4.1
5. v2 baseline included in v4.1 response

### Example Test:
```python
# Test: Local small business, $100 purchase, default LC
result = calculate_ejv_v41(
    "test_store",
    purchase_amount=100,
    business_type="local_small_business"
)

assert result["elvr"] == 75.75  # Expected based on defaults
assert result["evl"] == 24.25
assert result["retention_percentage"] == 75.8
assert result["local_capture_components"]["lc_aggregate"] == 0.7575
```

---

## Summary

**What Changed:**
- v4.1 is now about **decomposed flows** (wages, suppliers, taxes, financing, ownership)
- EDL concept removed from v4.1
- Participation stays in v4.2 as PAF multiplier
- New terminology: ELVR, EVL, retention percentage
- Financing-aware calculation added
- Business type defaults for all 5 components

**Why Changed:**
- Aligns with EJV discussion document 01222026.docx
- Separates objective measurement (v2, v4.1) from participation (v4.2)
- Makes v4.1 suitable for LOCATOR (optional advanced view)
- Keeps v4.2 exclusive to ENABLE workflow
- Provides clearer, more defensible impact estimates

**Impact:**
- More transparent methodology
- Dollar-based retention vs leakage
- Government data where possible
- Suitable for reviewer scrutiny (NSF, cities)
- Clear separation of concerns across versions

---

**Next Steps:**
1. Update/remove obsolete documentation files
2. Create comprehensive test suite
3. Update frontend to use new API structure
4. Add database schema for storing LC components
5. Validate with sample businesses

---

**Document Version:** 1.0  
**Last Updated:** January 23, 2026
