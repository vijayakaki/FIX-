# EJV v2 User Guide

## Accessing EJV v2

The FIX$ application now supports **two versions** of Economic Justice Value calculations:

### EJV v1 (Traditional)
- **Score Range**: 0-100
- **Display**: Composite score showing overall economic justice quality
- **Components**: Wage Score, Hiring Score, Community Score, Participation Score (each 0-25)
- **Use Case**: Quick comparison between stores

### EJV v2 (Justice-Weighted Local Impact)
- **Score Range**: Dollar amount ($)
- **Display**: Justice-weighted local impact per purchase
- **Components**: Purchase Amount × Local Capture × Justice Score
- **Use Case**: Understanding direct economic impact of spending

## How to Use

### Step 1: Select a Store
1. Open the FIX$ map at https://fixapp-phi.vercel.app
2. Use one of these methods to find stores:
   - **Demo Data**: Click "Load Demo Data" button
   - **Search by Address**: Enter an address and search radius
   - **Search by Category**: Select a business category (e.g., supermarket, restaurant)
   - **Draw Area**: Use polygon tool to select a custom area

### Step 2: View Store Details
When you click on a store marker, the dashboard will display:
- Store name
- EJV v1 score (0-100)
- Component scores with color coding:
  - 🟢 Green: High (80%+)
  - 🟡 Yellow: Medium (50-79%)
  - 🔴 Red: Low (<50%)
- Wealth retained and wealth leakage per day
- 9 Community Impact Dimensions

### Step 3: Toggle to EJV v2
1. With a store selected, click the **"Switch to EJV v2"** button
2. The display will switch to show:
   - **EJV v2 Score**: Dollar amount (e.g., $58.63)
   - **Purchase Amount**: Base transaction amount (default: $100)
   - **Local Capture**: Percentage of wages staying in community (e.g., 82%)
   - **Justice Score (ZIP)**: Quality score for the ZIP code (0-100)
   - **ZIP Need Modifiers**: Equity adjustments for 3 dimensions
     - AES (Access to Essential Services)
     - HWI (Health, Wellness & Inclusion)
     - ART (Access to Resources & Technology)
   - **Calculation Formula**: Shows the step-by-step calculation

### Step 4: Interpret the Results

#### EJV v2 Score Interpretation
```
EJV v2 = $58.63 per $100 spent
```

This means:
- For every **$100** you spend at this store
- **$58.63** creates justice-weighted local economic impact
- This accounts for:
  - How much money stays in the community (Local Capture)
  - The quality of equity dimensions in the area (Justice Score)
  - Local economic needs (ZIP Need Modifiers)

#### High EJV v2 Scores
- More money creates local impact
- Store pays fair wages
- Hires locally
- Reinvests in community
- Serves high-need areas

#### Low EJV v2 Scores
- Less money creates local impact
- Lower wage quality
- Less local hiring
- Less community reinvestment
- May be in lower-need areas (high income, low unemployment)

## Understanding ZIP Need Modifiers

**Range**: 0.80 - 1.10

### What They Mean
- **1.10**: Very high need (high unemployment, low income)
- **1.05**: High need
- **1.00**: Moderate need (baseline)
- **0.95**: Low need
- **0.90-0.80**: Very low need (low unemployment, high income)

### How They Work
ZIP Need Modifiers **amplify** the impact of positive economic actions in higher-need communities:

**Example 1: High-Need Area (ZIP 90011, South LA)**
```
Unemployment: 12%
Median Income: $32,000
NM_AES = 1.10 (high need)

Base Community Score: 0.50
Adjusted Score: 0.50 × 1.10 = 0.55 ✅ Amplified!
```

**Example 2: Low-Need Area (ZIP 10001, Manhattan)**
```
Unemployment: 3.1%
Median Income: $106,509
NM_AES = 0.925 (low need)

Base Community Score: 0.50
Adjusted Score: 0.50 × 0.925 = 0.46 ✓ Standard
```

This ensures that stores serving disadvantaged communities receive appropriate recognition for their economic justice contributions.

## Switching Between Versions

### Toggle Button
- **"Switch to EJV v2"**: Shows dollar-based justice-weighted impact
- **"Switch to EJV v1"**: Shows traditional 0-100 score

### When to Use Each Version

#### Use EJV v1 When:
- Comparing multiple stores quickly
- Need a simple quality score
- Looking for relative rankings
- Familiar with 0-100 scales

#### Use EJV v2 When:
- Want to understand direct economic impact
- Planning institutional purchasing decisions
- Need dollar-based metrics for reporting
- Analyzing equity-weighted outcomes
- Comparing impact across different purchase amounts

## Advanced Features

### Area Aggregation
- View multiple stores at once
- Switch between viewing modes:
  - **EJV Mode**: Color-coded by quality score
  - **Wealth Retained Mode**: Green gradient showing daily retained wealth
  - **Wealth Leakage Mode**: Red gradient showing daily lost wealth

### Heatmap View
- Visual representation of economic justice across neighborhoods
- Darker colors = higher impact

### Custom Purchase Amounts
To calculate EJV v2 for different purchase amounts:
1. Use API endpoint: `/api/ejv-v2/<store_id>?purchase=250`
2. Or modify the frontend code to allow custom input

## Example Use Cases

### Consumer Decision-Making
**Scenario**: Choosing between two grocery stores

**Store A (Local Chain)**
- EJV v1: 78.5
- EJV v2: $64.20 per $100
- Interpretation: Good overall quality, high local impact

**Store B (National Chain)**
- EJV v1: 45.2
- EJV v2: $28.40 per $100
- Interpretation: Lower quality, less local impact

**Decision**: Store A creates **2.3× more** justice-weighted local impact

### Institutional Procurement
**Scenario**: City government purchasing $1,000,000 in supplies

**Store A EJV v2**: $64.20 per $100
- Total Impact: ($1,000,000 / $100) × $64.20 = **$642,000** local impact

**Store B EJV v2**: $28.40 per $100
- Total Impact: ($1,000,000 / $100) × $28.40 = **$284,000** local impact

**Difference**: Choosing Store A creates **$358,000 more** local impact

### Community Analysis
**Scenario**: Assessing economic equity in a neighborhood

1. Load all stores in the area
2. View aggregate metrics
3. Compare EJV v2 across business types
4. Identify opportunities for improvement

## Troubleshooting

### "Please select a store first" Error
- Make sure to click on a store marker before toggling
- Load demo data if no stores are visible

### "Error loading EJV v2 data" Error
- Check internet connection
- Verify API is accessible
- Try refreshing the page

### Scores Seem Unusual
- EJV v2 scores are in **dollars**, not 0-100
- ZIP Need Modifiers can increase or decrease scores
- High-income areas may have lower need modifiers (0.80-0.95)
- High-unemployment areas may have higher need modifiers (1.05-1.10)

## Data Sources

All calculations use real-time data from:
- **Bureau of Labor Statistics (BLS)**: Wage data (May 2024)
- **U.S. Census Bureau**: Economic indicators (2022 ACS)
- **OpenStreetMap**: Business location data
- **Living Wage Calculator**: Cost of living adjustments

## Feedback and Support

For questions, issues, or suggestions:
- GitHub: [Your Repository]
- Email: [Your Contact]
- Documentation: [EJV_V2_DOCUMENTATION.md](./EJV_V2_DOCUMENTATION.md)

---

**Version**: 2.0  
**Last Updated**: January 2025  
**Live Application**: https://fixapp-phi.vercel.app
