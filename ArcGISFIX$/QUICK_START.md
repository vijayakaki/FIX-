# Quick Start Guide - FIX$ ArcGIS Edition

## 🚀 Get Started in 3 Minutes

### Step 1: Start the Server (Already Running!)
Your server is running at: **http://127.0.0.1:5000**

### Step 2: Add Your First Store

1. Click the **"+ Add Store"** button (top right)
2. Fill in the form:

```
Store ID: STORE001
Store Name: Downtown Supermarket
Type: Supermarket
Address: 1234 Market St
City: Los Angeles
State: CA
ZIP Code: 90012
```

3. Click **"Add Store"**
4. Watch as the store marker appears on the map!

### Step 3: Explore the Map

- **Click any marker** to see detailed EJV information
- **Zoom** with mouse wheel or +/- buttons
- **Pan** by clicking and dragging
- **Search** for addresses using the search box (top right)
- **Change basemap** using toggle button (bottom right)

### Step 4: Try More Stores

Add stores in different areas to compare:

**High Income Area (Manhattan, NY):**
```
Store ID: STORE002
Name: Manhattan Market
Type: Supermarket
Address: 123 5th Avenue
City: New York
State: NY
ZIP: 10001
```

**Lower Income Area (South LA):**
```
Store ID: STORE003
Name: South LA Grocery
Type: Grocery
Address: 4567 Central Ave
City: Los Angeles
State: CA
ZIP: 90011
```

**Watch how EJV scores vary by location!**

---

## 🎨 Understanding the Map

### Marker Colors
- 🟢 **Green (90-100)**: Excellent equity
- 🔵 **Blue (80-89)**: Good equity
- 🟠 **Orange (70-79)**: Fair equity
- 🔴 **Red (<70)**: Poor equity

### Popup Information
Click any marker to see:
- EJV Score (large, color-coded)
- Store details
- Location info
- Action buttons (Recalculate, Delete)

---

## 🔍 Using Filters

1. **Store Type Filter**
   - Select specific type (supermarket, grocery, etc.)
   - Click "Apply"

2. **EJV Score Filter**
   - Set minimum score (e.g., 75)
   - Only high-performing stores show

3. **Clear Filters**
   - Set back to "All Types" and 0
   - Click "Apply"

---

## 📊 Statistics Panel

The right panel shows:
- **Total Stores**: Count of all stores
- **Avg EJV Score**: Network average
- **Daily Wealth**: Estimated retained wealth

Updates automatically when stores are added/removed.

---

## ⚡ Quick Actions

### Add Multiple Stores Quickly
Use this template format:

| ID | Name | Type | Address | City | State | ZIP |
|----|------|------|---------|------|-------|-----|
| S001 | Store A | supermarket | 123 Main | LA | CA | 90001 |
| S002 | Store B | grocery | 456 Oak | NYC | NY | 10001 |

### Recalculate All Stores
1. Click each marker
2. Click "🔄 Recalculate EJV"
3. Updated scores reflect latest data

### Export Map View
- Take screenshot (Windows: Win+Shift+S)
- Or use browser print function

---

## 🌍 Sample Store Data

Copy/paste these for quick testing:

### West Coast
```
ID: WC001 | Name: Seattle Fresh | Type: supermarket
Address: 789 Pike St | City: Seattle | State: WA | ZIP: 98101

ID: WC002 | Name: Portland Market | Type: grocery
Address: 321 Broadway | City: Portland | State: OR | ZIP: 97201

ID: WC003 | Name: San Diego Foods | Type: warehouse_club
Address: 555 Harbor Dr | City: San Diego | State: CA | ZIP: 92101
```

### East Coast
```
ID: EC001 | Name: Boston Market | Type: supermarket
Address: 777 Boylston St | City: Boston | State: MA | ZIP: 02199

ID: EC002 | Name: Miami Fresh | Type: grocery
Address: 888 Ocean Dr | City: Miami | State: FL | ZIP: 33139

ID: EC003 | Name: DC Warehouse | Type: warehouse_club
Address: 999 Constitution | City: Washington | State: DC | ZIP: 20001
```

---

## 🎯 Common Tasks

### Compare Two Regions
1. Add stores in both areas
2. Look at marker colors
3. Click each to see exact scores
4. Notice how economic factors differ

### Find Best Performing Stores
1. Set "Min EJV Score" to 85
2. Click "Apply"
3. Only excellent stores show

### Identify Problem Areas
1. Look for red markers
2. Click to see why score is low
3. Check wage equity and local hiring components

---

## 🆘 Troubleshooting

### Marker Not Appearing
- Check if geocoding succeeded
- Try more specific address
- Add full street address

### Map Not Loading
- Check internet connection
- Refresh page (F5)
- Clear browser cache

### Slow Performance
- Close other browser tabs
- Limit to <100 stores visible
- Use filters to reduce markers

---

## 📱 Mobile Access

Access from phone/tablet:
```
http://192.168.1.247:5000
(Use IP from terminal output)
```

Works great on mobile with touch gestures!

---

## 🎬 Ready for Demo Video?

Record these steps:
1. **Intro** (10s): Show map overview
2. **Add Store** (30s): Fill form, watch marker appear
3. **Explore** (20s): Click marker, show details
4. **Compare** (30s): Add second store, compare scores
5. **Features** (30s): Basemap toggle, search, filters
6. **Conclusion** (10s): Recap benefits

Total: ~2.5 minutes

---

## 🚀 Advanced Features

### Custom Basemaps
Edit `static/js/app.js` line 15:
```javascript
basemap: "streets-navigation-vector"
// Options: "satellite", "hybrid", "dark-gray", "oceans"
```

### Clustering (for many stores)
Coming soon in next update!

---

## 📞 Need Help?

- Check [README.md](README.md) for full documentation
- Check [COMPARISON.md](COMPARISON.md) for vs original
- View terminal for error messages
- Check browser console (F12)

---

**You're all set! Enjoy exploring geographic equity patterns with FIX$ ArcGIS Edition! 🗺️**
