# GeoEquity Impact Features Guide
## Radius Search, Store List & Geographic Analysis

---

## 🎯 New Features Added

### 1. **Custom Radius Search**
- Set search radius from **1 to 50 km**
- Default: 5 km
- Adjustable for urban (small) or rural (large) areas
- More radius = more stores found

### 2. **Stores List Panel**
- Shows all stores on map in a sortable list
- Sorted by EJV V2 score (highest first)
- Click any store to zoom to it on map
- Color-coded by performance
- Live count of total stores

### 3. **GeoEquity Impact Analysis**
- Grouped by ZIP code
- Shows equity impact by area
- Impact levels: High/Medium/Low
- Daily wealth retained per area
- Visual color indicators

---

## 🔍 How to Use

### Search with Custom Radius

**Example 1: Dense Urban Area**
```
ZIP Code: 10001 (Manhattan)
Radius: 2 km (small area, many stores)
Category: Supermarkets
```

**Example 2: Suburban Area**
```
ZIP Code: 90210 (Beverly Hills)
Radius: 10 km (medium area)
Category: All Categories
```

**Example 3: Rural Area**
```
ZIP Code: 64701 (Harrisonville, MO)
Radius: 25 km (large area, fewer stores)
Category: Grocery Stores
```

### Viewing Results

**On the Map:**
- Color-coded markers
- Click for detailed EJV scores
- Pan and zoom to explore

**In the Stores List:**
- Sorted by performance
- Quick overview of all stores
- Click to zoom to store on map
- See EJV V2 at a glance

**GeoEquity Impact:**
- See which ZIP codes perform best
- Compare areas side-by-side
- Understand regional patterns

---

## 📊 GeoEquity Impact Indicators

### **High Impact (Green)**
- EJV Score: 80+
- Strong local hiring
- Good wage equity
- Positive community benefit

### **Medium Impact (Orange)**
- EJV Score: 70-79
- Moderate performance
- Room for improvement
- Acceptable standards

### **Low Impact (Red)**
- EJV Score: <70
- Below standards
- Needs attention
- Limited community benefit

---

## 🌍 Real-World Examples

### Example 1: Manhattan Financial District
```
Search:
- ZIP: 10005
- Radius: 3 km
- Category: All

Expected Impact:
- High cost of living
- High wages needed
- Lower EJV scores (70-75)
- But high absolute wealth retention
```

### Example 2: South LA Community
```
Search:
- ZIP: 90011
- Radius: 5 km
- Category: Supermarkets

Expected Impact:
- Lower cost of living
- More achievable wages
- Higher EJV scores (75-85)
- Strong local impact
```

### Example 3: Multi-Area Comparison
```
1. Search NYC (10001, 5km)
2. Add 5 stores
3. Search LA (90001, 5km)
4. Add 5 stores
5. View GeoEquity Impact panel
6. Compare ZIP groups!
```

**You'll see:**
- Different scores by region
- Wealth retention varies
- Geographic equity patterns

---

## 📱 Interface Overview

### **Left Side: Interactive Map**
- ArcGIS 3D map
- Color-coded markers
- Click for details
- Zoom, pan, explore

### **Right Side: Analysis Panels**

**1. Network Statistics**
- Total stores count
- Avg EJV V1 score
- Avg EJV V2 score
- Total daily wealth

**2. Score Legend**
- Green: 90-100 (Excellent)
- Blue: 80-89 (Good)
- Orange: 70-79 (Fair)
- Red: <70 (Poor)

**3. Filters**
- Store type filter
- Min EJV score filter
- Apply to map/list

**4. GeoEquity Impact** ⭐ NEW
- Grouped by ZIP
- Impact level indicators
- Wealth retention by area
- Quick comparison

**5. Stores List** ⭐ NEW
- All stores sorted
- Click to zoom
- Quick overview
- Color indicators

---

## 💡 Pro Tips

### For Better Searches
1. **Start Small**: Try 5 km first
2. **Expand if Needed**: Increase to 10-15 km for rural
3. **Category Filter**: Narrow results by type
4. **Multiple Searches**: Compare different areas

### For Analysis
1. **Add Diverse Stores**: Different types show patterns
2. **Compare Regions**: Urban vs suburban vs rural
3. **Watch ZIP Groups**: Same area stores cluster
4. **Click List Items**: Quick way to explore

### For Presentations
1. **Load Multiple Areas**: Show geographic variation
2. **Use GeoEquity Panel**: Highlight regional differences
3. **Filter High Performers**: Show success stories
4. **Zoom to Specific Stores**: Deep dive on examples

---

## 🎬 Demo Video Script (Updated)

**Scene 1: Search with Radius** (30s)
- Click Search Stores
- Enter ZIP: 10001
- Set Radius: 3 km
- Select Supermarkets
- Show results

**Scene 2: Add to Map** (20s)
- Add 3-4 stores
- Watch markers appear
- Show color coding

**Scene 3: Stores List** (20s) ⭐ NEW
- Scroll through list
- Click a store
- Watch zoom to location
- Show popup

**Scene 4: GeoEquity Impact** (30s) ⭐ NEW
- Point to impact panel
- Explain ZIP grouping
- Show impact levels
- Highlight wealth retention

**Scene 5: Compare Regions** (30s)
- Search different ZIP
- Add more stores
- Show both ZIP groups
- Compare impact levels

**Scene 6: Filters** (15s)
- Apply EJV filter
- Show map/list update
- Reset to all

**Total: ~2.5 minutes**

---

## 🔮 Understanding the Data

### Stores List Sorting
- **Highest EJV first**: Best performers on top
- **Color-coded border**: Quick visual reference
- **Click to zoom**: Instant map navigation
- **Live updates**: Changes with filters

### GeoEquity Impact Calculation
```
For each ZIP code:
1. Group all stores in that ZIP
2. Calculate average EJV score
3. Estimate daily wealth retention
4. Determine impact level:
   - High: >= 80 EJV
   - Medium: 70-79 EJV
   - Low: < 70 EJV
5. Display with color indicator
```

### Why This Matters
- **Policy makers**: See which areas need support
- **Investors**: Find high-impact opportunities
- **Chains**: Compare location performance
- **Communities**: Understand local equity

---

## 🚀 Advanced Usage

### Multi-Region Analysis
1. Search Manhattan (10001, 3km) → Add 5 stores
2. Search Brooklyn (11201, 5km) → Add 5 stores
3. Search Queens (11101, 5km) → Add 5 stores
4. View GeoEquity Impact → See 3 ZIP groups
5. Compare scores and impact

### Category Comparison
1. Search same ZIP (90001)
2. First: Supermarkets → Add 3 stores
3. Second: Fast Food → Add 3 stores
4. Second: Pharmacies → Add 3 stores
5. See how categories differ in same area

### Radius Optimization
```
Urban (NYC, SF, LA):
- Start: 2-3 km
- Expand: 5 km if needed

Suburban:
- Start: 5-7 km
- Expand: 10-15 km

Rural:
- Start: 10-15 km
- Expand: 25-50 km
```

---

## ❓ FAQ

**Q: Why group by ZIP in GeoEquity Impact?**
A: ZIP codes represent economic areas with similar demographics, making them ideal for comparing equity patterns.

**Q: Can I see stores from multiple ZIP codes?**
A: Yes! Search multiple times and they'll all appear. The GeoEquity panel will show all ZIP groups.

**Q: What if stores have the same ZIP?**
A: They'll be grouped together in the GeoEquity Impact panel, showing aggregate performance.

**Q: How is "wealth retained" calculated?**
A: Simplified: Number of stores × $5,000/day average. Real calculation uses actual payroll data.

**Q: Why is stores list sorted by V2?**
A: V2 is the advanced algorithm and primary score. V1 is shown for comparison.

---

## 📞 Next Steps

1. **Try Different Radii** - See how it affects results
2. **Compare ZIP Codes** - Add stores from multiple areas
3. **Use Stores List** - Quick navigation and overview
4. **Analyze GeoEquity** - Understand regional patterns
5. **Create Comparisons** - Different categories, same area

---

**Now you can see economic equity patterns across entire regions! 🌍📊**
