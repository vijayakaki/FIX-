# FIX$ GeoEquity Impact Engine
## Geographic Area-Wise Economic Impact Analysis

---

## 🌍 Overview

FIX$ now provides **geographic area-wise analysis** showing how economic equity varies across different ZIP codes and cities using **real Census Bureau data**.

---

## 📍 Key Features

### 1. **Location-Specific EJV Calculation**
- Each store is analyzed with real economic data from its ZIP code
- Unemployment rates, median income, and cost of living vary by area
- Same business type shows different equity impacts in different locations

### 2. **Real Data Sources by Area**

| Data Point | Source | Frequency |
|------------|--------|-----------|
| **Unemployment Rate** | Census ACS API | Real-time |
| **Median Income** | Census ACS API | Real-time |
| **Wages** | BLS OEWS May 2024 | Annual |
| **Industry Employment** | BLS Research | Annual |

---

## 🎯 Example: Geographic Impact Comparison

### Same Supermarket in 5 Different Areas:

#### **Manhattan, NY (ZIP 10001)**
- Median Income: $106,509
- Unemployment: 3.1%
- EJV Score: **75.75/100**
- Wealth Retained: $5,652/day
- **Insight**: High income = high living wage threshold, harder to achieve equity

#### **South LA, CA (ZIP 90011)**  
- Median Income: $51,819
- Unemployment: 6.8%
- EJV Score: **78.41/100**
- Wealth Retained: $5,746/day
- **Insight**: Higher unemployment drives more local hiring

#### **Seattle, WA (ZIP 98101)**
- Median Income: $111,099  
- Unemployment: 2.3%
- EJV Score: **77.85/100**
- Wealth Retained: $6,137/day
- **Insight**: Tech hub with high wages but also high living costs

#### **Chicago, IL (ZIP 60614)**
- Median Income: $135,364
- Unemployment: 2.7%
- EJV Score: **78.64/100** ⭐ Highest
- Wealth Retained: $5,628/day

#### **Atlanta, GA (ZIP 30303)**
- Median Income: $50,000
- Unemployment: 3.5%
- EJV Score: **78.36/100**
- Wealth Retained: $6,254/day

---

## 💡 Key Geographic Insights

### **Why Wealthier Areas May Have LOWER EJV Scores:**

1. **Living Wage Gap**: High-income areas have higher living costs
   - Manhattan living wage: Higher threshold
   - Same $15/hr wage is less equitable in expensive areas

2. **Unemployment Impact**: Lower unemployment = less local hiring pressure
   - Areas with 6.8% unemployment → 86% local hiring
   - Areas with 2.3% unemployment → 95% local hiring (but less need)

3. **Equity vs. Absolute Wages**:
   - A $15/hr job in Manhattan ≠ equity
   - A $15/hr job in Atlanta = better equity
   - **Equity is CONTEXTUAL**

---

## 📊 How to Use Area-Wise Analysis

### **For City Planners:**
```
1. Identify neighborhoods with lowest EJV scores
2. Target economic development programs
3. Track wealth retention vs. leakage by ZIP code
4. Compare equity impact across districts
```

### **For Policymakers:**
```
1. Set minimum wages based on area-specific living costs
2. Design incentives for high-EJV businesses
3. Monitor economic inequality geographically
4. Track Community Benefit Agreements (CBAs)
```

### **For Community Organizations:**
```
1. Advocate for better local hiring in low-scoring areas
2. Show which businesses create local wealth
3. Map economic justice across neighborhoods
4. Support businesses with high local impact
```

---

## 🔌 API Endpoints

### **1. Area Comparison**
```
GET /api/area-comparison
```
Returns EJV analysis for supermarkets in 5 major US cities

**Response includes:**
- Individual area analysis
- Summary statistics
- Average EJV across areas
- Total wealth retained vs. leakage

### **2. Custom Location Query**
```
GET /api/ejv/<store_id>?zip=XXXXX&location=City%20Name
```
Calculate EJV for any store in any ZIP code

**Example:**
```
/api/ejv/supermarket_123?zip=90210&location=Beverly%20Hills
```

### **3. Demo Stores by Location**
```
GET /api/stores/demo
```
Returns 8 stores across 5 different cities with location-grouped data

---

## 📈 Sample Results

**Overall Statistics (5 Supermarkets):**
- Average EJV: **77.80/100**
- Total Wealth Retained: **$29,418/day**
- Total Wealth Leakage: **$2,653/day**
- Overall Retention Rate: **91.7%**

**Equity Gap:**
- Highest: Chicago, IL (78.64)
- Lowest: Manhattan, NY (75.75)
- **Gap: 2.9 points** shows geographic equity variance

---

## 🎓 For Your Presentation

### **Key Message:**
> "Economic equity isn't just about wages—it's about the **relationship** between wages, local living costs, and community participation. The same business can create very different equity outcomes in different neighborhoods."

### **Visual Talking Points:**
1. Show the 5-city comparison table
2. Highlight income disparities (Manhattan $106k vs. Atlanta $50k)
3. Explain why lower-income areas can have HIGHER equity scores
4. Demonstrate wealth retention differences
5. Show real Census data being pulled live

### **Call to Action:**
> "FIX$ helps policymakers identify WHERE economic intervention is needed and WHICH businesses are creating local wealth in each community."

---

## 🔍 Technical Implementation

**Data Flow:**
```
User Request → ZIP Code
    ↓
Census API → Real Demographics (Unemployment, Income)
    ↓
BLS OEWS → Real Wages by Occupation
    ↓
Calculate Living Wage (Income-Based)
    ↓
Adjust Local Hiring (Unemployment-Based)
    ↓
Compute EJV Score
    ↓
Return Location-Specific Results
```

**Benefits:**
- ✅ Real government data
- ✅ Location-aware calculations
- ✅ Transparent methodology
- ✅ Reproducible results
- ✅ API-accessible for integration

---

## 🌟 Impact Metrics Explained

### **Wealth Retention** = Money staying in community
- Local wages paid to residents
- Community spending/investment
- Higher = better local economic benefit

### **Wealth Leakage** = Money leaving community  
- Wages paid to non-local workers
- Lower = better wealth circulation

### **EJV Score Components by Area:**
1. **Wage Score** (25 pts): Wage vs. local living wage
2. **Hiring Score** (25 pts): Local hiring % (unemployment-adjusted)
3. **Community Score** (25 pts): Local reinvestment rate
4. **Participation Score** (25 pts): Employment access/intensity

---

## 🚀 Next Steps

**Enhance with:**
- County-level aggregation
- Time-series tracking (watch equity change over time)
- Neighborhood-level analysis (Census tracts)
- Comparison to local competitors
- Integration with GIS mapping tools

---

**FIX$ transforms geographic economic data into actionable equity intelligence.**
