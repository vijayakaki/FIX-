# FIX$ ArcGIS - Store Search Guide
## Search Real Stores and Compare EJV V1 vs V2

---

## 🔍 How to Use Store Search

### Step 1: Click "🔍 Search Stores" Button
Located in the top right of the header

### Step 2: Enter Search Criteria

**Required:**
- **ZIP Code**: 5-digit ZIP code (e.g., 90001, 10001)

**Optional:**
- **Address**: Street name or landmark for more specific results
- **Category**: Filter by store type

**Available Categories:**
- **All Categories** - Search all store types
- **Supermarkets** - Large grocery stores
- **Grocery Stores** - Smaller markets, convenience stores
- **Pharmacies** - Drug stores, medical supplies
- **Restaurants** - Full-service dining
- **Fast Food** - Quick service restaurants
- **Cafes** - Coffee shops, bakeries

### Step 3: Review Search Results
- Results show **real stores** from OpenStreetMap
- Up to 50 stores within 5km radius
- Each result shows:
  - Store name and brand
  - Address and location
  - Store type/category

### Step 4: Add Store to Map
- Click "Add to Map" button on any result
- App automatically:
  - Geocodes the location
  - Fetches Census economic data
  - Calculates **both EJV V1 and V2 scores**
  - Adds marker to map

### Step 5: View EJV Scores
Click any marker on the map to see:
- **EJV V2 Score** (left box) - Advanced algorithm
- **EJV V1 Score** (right box) - Original algorithm
- Color-coded by performance
- Detailed store information

---

## 📊 Understanding EJV Scores

### EJV V2 (Advanced Algorithm)
**100 Points Total:**
- **40 pts**: Local Hiring Score
  - Based on unemployment rate
  - Higher unemployment = more local hiring
- **40 pts**: Wage Equity Score
  - Compares actual wage to living wage
  - Clamped ratio: 0.889 to 0.925
- **20 pts**: Economic Impact
  - Daily wealth retained in community
  - Scaled by payroll and local hiring

### EJV V1 (Original Algorithm)
**100 Points Total:**
- **50 pts**: Wage Score
  - Simple wage-to-living-wage ratio
  - Capped at 120% of living wage
- **50 pts**: Local Impact
  - Daily wealth calculation
  - Unemployment factor included

### Key Differences
| Aspect | V1 | V2 |
|--------|----|----|
| **Complexity** | Simpler | More sophisticated |
| **Components** | 2 (50/50) | 3 (40/40/20) |
| **Living Wage** | 70% of median | Median + 20% buffer |
| **Wage Clamping** | None | 0.889-0.925 range |
| **Sensitivity** | Lower | Higher |

---

## 🎯 Example Searches

### High Income Area (Manhattan, NY)
```
ZIP Code: 10001
Category: Supermarkets
Expected: Higher living wage = lower EJV scores
```

### Lower Income Area (South LA)
```
ZIP Code: 90011
Category: Grocery Stores
Expected: Lower living wage = higher EJV scores
```

### Suburban Area (Seattle)
```
ZIP Code: 98101
Category: All Categories
Expected: Mixed results based on store type
```

### Rural Area
```
ZIP Code: 64701 (Harrisonville, MO)
Category: All Categories
Expected: Fewer stores, but good EJV scores
```

---

## 📈 Dashboard Statistics

The side panel now shows:
- **Total Stores**: Count of analyzed stores
- **Avg EJV V1**: Average score using V1 algorithm
- **Avg EJV V2**: Average score using V2 algorithm
- **Daily Wealth**: Total estimated community retention

Compare V1 vs V2 averages to see how algorithms differ!

---

## 🎨 Color Coding

Both V1 and V2 scores use the same color scheme:

- 🟢 **Green (90-100)**: Excellent equity
  - High wages, strong local impact
  - Gold standard performance

- 🔵 **Blue (80-89)**: Good equity
  - Above-average performance
  - Strong community benefit

- 🟠 **Orange (70-79)**: Fair equity
  - Room for improvement
  - Meets basic standards

- 🔴 **Red (<70)**: Poor equity
  - Below standards
  - Needs significant improvement

---

## 🔄 Recalculating Scores

After adding stores, you can recalculate:
1. Click any marker on map
2. Click "🔄 Recalculate EJV"
3. Gets latest Census data
4. Updates both V1 and V2 scores
5. Alert shows both scores

---

## 💡 Tips for Best Results

### Search Tips
1. **Start broad**: Use "All Categories" first
2. **Refine**: Then filter by specific category
3. **Try nearby**: If no results, try adjacent ZIP
4. **Use landmarks**: Add street name for precision

### Analysis Tips
1. **Compare regions**: Search multiple ZIP codes
2. **Same chain, different areas**: See how location affects scores
3. **Urban vs rural**: Notice score variations
4. **High vs low income**: Living wage impact

### Data Quality
- **OpenStreetMap**: Community-maintained, may vary
- **Some stores may lack full details**: Normal for OSM
- **Brand data**: When available, shown in results
- **Coordinates**: Automatically geocoded

---

## 🌍 Real Data Sources

### Store Data
- **OpenStreetMap (OSM)** via Overpass API
- Community-contributed
- Global coverage
- Updated regularly

### Economic Data
- **Census Bureau ACS API** (2022)
  - Unemployment rates by ZIP
  - Median household income
- **BLS OEWS** (May 2024)
  - Industry wage data
  - Employee counts

### Geocoding
- **ArcGIS World Geocoding Service**
- Converts addresses to coordinates
- Free tier (no API key needed)

---

## 🚀 Quick Start Examples

### Example 1: Manhattan Supermarkets
```
1. Click "Search Stores"
2. ZIP: 10001
3. Category: Supermarkets
4. Click "Search"
5. Add 3-4 stores to map
6. Compare EJV scores
```

**Expected Results:**
- V2 scores: 70-80 (wage equity challenging)
- V1 scores: 75-85 (simpler calculation)
- High living wage threshold

### Example 2: Los Angeles Mix
```
1. ZIP: 90001
2. Category: All Categories
3. Add diverse store types
4. Notice type variations
```

**Expected Results:**
- Pharmacies: Higher scores
- Fast food: Lower scores
- Supermarkets: Mid-range

### Example 3: Regional Comparison
```
1. Search NYC (10001)
2. Add 2-3 stores
3. Search LA (90001)
4. Add 2-3 stores
5. Compare on map
```

**Visual Insight:**
- See geographic equity patterns
- Color differences by region
- Economic impact varies

---

## ❓ Troubleshooting

### No Stores Found
- **Try adjacent ZIP codes**
- **Select "All Categories"**
- **Urban areas have more data**
- **Rural areas may have fewer stores**

### Geocoding Fails
- **Check ZIP code is valid**
- **Try without address first**
- **Some international ZIPs unsupported**

### Slow Search
- **Overpass API can be slow**
- **Wait 30 seconds for timeout**
- **Try again if fails**

### Missing Data
- **OSM data quality varies**
- **Some stores lack details**
- **Still usable for EJV calc**

---

## 📱 Mobile Usage

Works great on phones!
- Search interface is responsive
- Touch-friendly buttons
- Zoom with pinch gesture
- Tap markers for details

Access via:
```
http://192.168.1.247:5000
```
(Use IP from terminal)

---

## 🎬 Demo Video Script

**Scene 1: Search** (30s)
- Click Search button
- Enter ZIP: 10001
- Select Supermarkets
- Show results list

**Scene 2: Add to Map** (20s)
- Click "Add to Map"
- Watch marker appear
- Show both EJV scores

**Scene 3: Compare** (30s)
- Search different ZIP
- Add more stores
- Pan map to compare
- Click markers to see scores

**Scene 4: Dashboard** (15s)
- Show statistics
- Point out V1 vs V2 averages
- Filter demonstration

**Total: ~1.5 minutes**

---

## 🔮 Next Steps

Now that you can search real stores:
1. **Build regional database** - Search multiple ZIPs
2. **Analyze patterns** - Urban vs suburban vs rural
3. **Compare chains** - Same brand, different locations
4. **Track changes** - Recalculate over time
5. **Export data** - For reporting and analysis

---

**Ready to explore economic equity in real stores across America! 🗺️📊**
