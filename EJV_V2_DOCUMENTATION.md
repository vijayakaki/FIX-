# EJV v2: Justice-Weighted Local Impact Calculation

## Overview

EJV v2 transforms the traditional 0-100 Economic Justice Value score into a **dollar-based metric** that quantifies the **Justice-Weighted Local Impact** of each purchase. This provides a more intuitive understanding of how consumer spending creates equitable economic outcomes in local communities.

## Formula

```
EJV v2 = (P × LC) × (JS_ZIP / 100)
```

Where:
- **P** = Purchase Amount ($)
- **LC** = Local Capture [0-1] (percentage of wages that stay in the community)
- **JS_ZIP** = Justice Score for ZIP code [0-100]

## Key Components

### 1. Transaction Parameters

- **Purchase Amount (P)**: The dollar amount of the transaction (default: $100)
- **Local Capture (LC)**: The percentage of economic value that remains in the local community through local hiring and wages

### 2. ZIP Need Modifiers (NM)

Need Modifiers adjust dimension scores based on local economic conditions to provide equity-weighted outcomes:

```python
# Calculation based on unemployment and median income
unemployment_rate = get_unemployment_rate(zip_code)
median_income = get_median_income(zip_code)

# Base modifier from unemployment (higher unemployment = higher need)
if unemployment_rate >= 10.0:
    nm_unemployment = 1.10  # Very high need
elif unemployment_rate >= 7.0:
    nm_unemployment = 1.05  # High need
elif unemployment_rate >= 5.0:
    nm_unemployment = 1.00  # Moderate need
elif unemployment_rate >= 3.0:
    nm_unemployment = 0.95  # Low need
else:
    nm_unemployment = 0.90  # Very low need

# Adjust based on income (lower income = higher need)
if median_income < 40000:
    nm_income = 1.10  # Very low income
elif median_income < 60000:
    nm_income = 1.05  # Low income
elif median_income < 80000:
    nm_income = 1.00  # Moderate income
else:
    nm_income = 0.95  # High income

# Final modifier: average of unemployment and income factors
nm = (nm_unemployment + nm_income) / 2  # Range: 0.80 - 1.10
```

**Applied Dimensions:**
- **AES** (Access to Essential Services) - Community Score × NM
- **HWI** (Health, Wellness & Inclusion) - Hiring Score × NM
- **ART** (Access to Resources & Technology) - Wage Score × NM

### 3. Dimension Scores (9 Dimensions)

Each dimension is normalized to [0-1] scale:

1. **AES** - Access to Essential Services (Community Score)
2. **ART** - Access to Resources & Technology (Wage Score)
3. **HWI** - Health, Wellness & Inclusion (Hiring Score)
4. **PSR** - Public Service Representation (Community Score)
5. **CAI** - Cultural Awareness & Inclusivity (Participation Score)
6. **JCE** - Job Creation/Economic Empowerment (Hiring Score)
7. **FSI** - Financial Support & Investment (Wage Score)
8. **CED** - Community Engagement & Development (Avg of Community & Participation)
9. **ESD** - Education & Skill Development (Hiring Score)

## Calculation Steps

### Step 1: Adjust Dimension Scores

```python
adjusted_dimensions = {}
for dimension, score in dimensions.items():
    if dimension == "AES":
        adjusted_dimensions[dimension] = min(1.0, max(0.0, score * nm_aes))
    elif dimension == "ART":
        adjusted_dimensions[dimension] = min(1.0, max(0.0, score * nm_art))
    elif dimension == "HWI":
        adjusted_dimensions[dimension] = min(1.0, max(0.0, score * nm_hwi))
    else:
        adjusted_dimensions[dimension] = score
```

### Step 2: Calculate Justice Score (JS_ZIP)

```python
# Average of all adjusted dimensions, scaled to 0-100
js_zip = sum(adjusted_dimensions.values()) / len(adjusted_dimensions) * 100
```

### Step 3: Compute EJV v2

```python
# Justice-Weighted Local Impact ($)
ejv_v2 = (purchase_amount * local_capture) * (js_zip / 100)
```

## Example Calculation

### Scenario: $100 purchase at a supermarket in ZIP 10001

**Input Data:**
- Purchase Amount: $100
- Local Capture: 0.82 (82% local hiring)
- ZIP 10001 Conditions:
  - Unemployment: 3.1%
  - Median Income: $106,509

**Step 1: Base Dimension Scores**
```
AES (Community): 0.036 (0-1 scale)
ART (Wage): 1.000 (0-1 scale)
HWI (Hiring): 1.000 (0-1 scale)
PSR: 0.036
CAI: 1.000
JCE: 1.000
FSI: 1.000
CED: 0.518
ESD: 1.000
```

**Step 2: Apply ZIP Need Modifiers**
```
NM_AES = 0.925 (low unemployment, high income = low need)
NM_ART = 0.925
NM_HWI = 0.925

Adjusted AES: 0.036 × 0.925 = 0.033
Adjusted ART: 1.000 × 0.925 = 0.925
Adjusted HWI: 1.000 × 0.925 = 0.925
```

**Step 3: Calculate Justice Score**
```
JS_ZIP = Average(0.033, 0.925, 0.925, 0.036, 1.000, 1.000, 1.000, 0.518, 1.000) × 100
JS_ZIP = 0.715 × 100 = 71.5
```

**Step 4: Calculate EJV v2**
```
EJV v2 = ($100 × 0.82) × (71.5 / 100)
EJV v2 = $82.00 × 0.715
EJV v2 = $58.63
```

**Interpretation:**
For every $100 spent at this store, **$58.63** creates justice-weighted local economic impact, considering both the local capture rate and the quality of equity dimensions in the ZIP code.

## Comparison with EJV v1

| Metric | EJV v1 | EJV v2 |
|--------|--------|--------|
| **Scale** | 0-100 score | Dollar amount ($) |
| **Interpretation** | Composite quality score | Justice-weighted local impact per purchase |
| **Use Case** | Relative comparison between stores | Direct economic impact measurement |
| **Equity Adjustment** | None | ZIP-based need modifiers |
| **Example** | EJV = 75.91 | EJV v2 = $58.63 per $100 spent |

## API Endpoints

### Get EJV v2 for a Store
```http
GET /api/ejv-v2/<store_id>?zip=10001&purchase=100
```

**Response:**
```json
{
  "store_id": "supermarket_101",
  "location": "Manhattan",
  "zip_code": "10001",
  "ejv_version": "2.0",
  "ejv_v2": 58.63,
  "purchase_amount": 100.0,
  "local_capture": 0.820,
  "justice_score_zip": 71.5,
  "zip_modifiers": {
    "AES": 0.925,
    "ART": 0.925,
    "HWI": 0.925
  },
  "dimensions": {...},
  "adjusted_dimensions": {...},
  "calculation_formula": "EJV v2 = (100 × 0.82) × (71.5/100) = $58.63"
}
```

### Compare EJV v1 and v2
```http
GET /api/ejv-comparison/<store_id>?zip=10001&purchase=100
```

**Response:**
```json
{
  "store_id": "supermarket_101",
  "comparison": {
    "v1": {
      "name": "Traditional EJV (0-100 score)",
      "value": 75.91,
      "description": "Composite score of wage, hiring, community, and participation"
    },
    "v2": {
      "name": "Justice-Weighted Local Impact ($)",
      "value": 58.63,
      "description": "For every $100 spent, $58.63 creates justice-weighted local impact"
    }
  },
  "zip_analysis": {
    "need_modifiers": {...},
    "dimensions": {...},
    "adjusted_dimensions": {...}
  }
}
```

## Frontend Toggle Implementation

The user interface includes a toggle button to switch between EJV v1 and v2 displays:

```javascript
// Toggle between versions
async function toggleEJVVersion() {
  if (currentEJVVersion === 'v2') {
    // Fetch and display v2 data
    const v2Data = await fetch(`/api/ejv-v2/${storeId}`).then(r => r.json());
    document.getElementById('ejvV2Score').innerText = '$' + v2Data.ejv_v2.toFixed(2);
    document.getElementById('justiceScoreZip').innerText = v2Data.justice_score_zip.toFixed(1);
    // Display ZIP modifiers
    document.getElementById('nmAES').innerText = v2Data.zip_modifiers.AES.toFixed(2);
    document.getElementById('nmHWI').innerText = v2Data.zip_modifiers.HWI.toFixed(2);
    document.getElementById('nmART').innerText = v2Data.zip_modifiers.ART.toFixed(2);
  } else {
    // Display v1 data (traditional 0-100 score)
  }
}
```

## Benefits of EJV v2

1. **Intuitive Dollar-Based Metric**: Users can understand the direct economic impact of their spending
2. **Equity-Weighted**: ZIP-based need modifiers ensure that stores serving higher-need communities receive appropriate recognition
3. **Scalable**: Works for any purchase amount, making it useful for individual consumers and institutional buyers
4. **Transparent**: Clear formula shows how local capture, justice quality, and purchase amount combine
5. **Actionable**: Provides concrete dollar amounts that can guide purchasing decisions

## Implementation Status

✅ **Backend**: Fully implemented in `app.py`
- `get_zip_need_modifier()` function
- `calculate_ejv_v2()` function
- API endpoints: `/api/ejv-v2/<store_id>`, `/api/ejv-comparison/<store_id>`

✅ **Frontend**: Fully implemented in `index.html`
- Dual display system (v1 and v2)
- Toggle button for switching between versions
- ZIP Need Modifier display
- Justice Score display
- Formula visualization

✅ **Deployment**: Live at https://fixapp-phi.vercel.app

## Future Enhancements

- [ ] Historical tracking of EJV v2 over time
- [ ] Bulk purchasing impact calculator
- [ ] Community-level aggregation of EJV v2 impacts
- [ ] Comparative analysis across neighborhoods
- [ ] Integration with consumer receipt data

---

**Last Updated**: January 2025
**Version**: 2.0
**Author**: FIX$ GeoEquity Impact Engine
