# FIX$ ArcGIS Edition 🗺️
## Economic Equity Mapping with ArcGIS Integration

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![ArcGIS](https://img.shields.io/badge/ArcGIS-4.28-orange.svg)

Interactive geographic visualization of Economic Justice Value (EJV V2) calculations across store locations, powered by ArcGIS.

---

## 🌟 Features

### ArcGIS Integration
- **Interactive 3D Maps** - ArcGIS JavaScript API 4.28
- **Automatic Geocoding** - Convert addresses to coordinates
- **Spatial Analysis** - Buffer zones, clustering, spatial queries
- **Real-time Data** - BLS OEWS wages & Census economic indicators
- **Custom Popups** - Detailed store information with EJV metrics
- **Multiple Basemaps** - Streets, satellite, hybrid views

### EJV Calculations
- **Economic Justice Value V2** - Advanced equity scoring
- **Geographic Variations** - ZIP code-specific analysis
- **Real-Time Wages** - BLS May 2024 wage data
- **Census Integration** - Unemployment and income by area
- **Industry Standards** - Employee counts from research data

### Visualization
- **Color-Coded Markers** - EJV score ranges (Excellent/Good/Fair/Poor)
- **Heat Maps** - Economic impact visualization
- **Filters** - Store type, EJV score, location
- **Statistics Dashboard** - Network-wide metrics
- **Legend** - Clear score interpretation

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge)

### Installation

1. **Navigate to project directory:**
   ```powershell
   cd c:\FIX$APP\ArcGISFIX$
   ```

2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Initialize database:**
   ```powershell
   python database.py
   ```

4. **Run the application:**
   ```powershell
   python app.py
   ```

5. **Open in browser:**
   ```
   http://localhost:5000
   ```

---

## 📦 Technology Stack

### Backend
- **Flask 3.0** - Web framework
- **ArcGIS Python API 2.3** - Geocoding & spatial analysis
- **SQLite** - Database
- **Requests** - Census & BLS API integration

### Frontend
- **ArcGIS JavaScript API 4.28** - Interactive mapping
- **Vanilla JavaScript** - No framework dependencies
- **CSS3** - Modern responsive design

### APIs & Data Sources
- **Census Bureau ACS API** - Economic indicators
- **BLS OEWS** - May 2024 wage data
- **ArcGIS World Geocoding Service** - Address conversion
- **ArcGIS Basemaps** - Street, satellite, hybrid maps

---

## 📊 API Endpoints

### Stores
```http
GET  /api/stores              # Get all stores
POST /api/stores              # Add new store (auto-geocodes)
GET  /api/stores/:id          # Get specific store
DELETE /api/stores/:id        # Delete store
```

### Calculations
```http
POST /api/calculate/:id       # Calculate/recalculate EJV for store
```

### Geocoding
```http
POST /api/geocode             # Geocode an address
Body: {"address": "123 Main St, City, ST 12345"}
```

---

## 🗺️ How It Works

### 1. Add Store
- Enter store details (name, address, type)
- Backend geocodes address using ArcGIS
- Fetches Census data for ZIP code
- Calculates EJV score
- Adds marker to map

### 2. Geographic Analysis
- **Unemployment Rate** - From Census ACS API
- **Median Income** - Area-specific economic data
- **Living Wage** - Calculated per location
- **Wage Comparison** - BLS OEWS vs living wage

### 3. EJV Calculation
```
EJV Score = Local Hiring (40) + Wage Equity (40) + Economic Impact (20)
```

- **Local Hiring**: Based on unemployment rate (higher = more local hiring)
- **Wage Equity**: Ratio of actual wage to living wage
- **Economic Impact**: Daily wealth retained in community

### 4. Map Visualization
- **Green (90-100)**: Excellent equity
- **Blue (80-89)**: Good equity
- **Orange (70-79)**: Fair equity
- **Red (<70)**: Poor equity

---

## 🎯 Comparison: Original vs ArcGIS Edition

| Feature | Original FIX$ | ArcGIS Edition |
|---------|--------------|----------------|
| **Mapping** | Basic static maps | Interactive 3D ArcGIS maps |
| **Geocoding** | Manual coordinates | Automatic ArcGIS geocoding |
| **Visualization** | Tables/lists | Color-coded markers, popups |
| **Basemaps** | Single map | Multiple (street, satellite, hybrid) |
| **Spatial Analysis** | None | Buffer zones, clustering |
| **User Experience** | Text-based | Interactive visual exploration |
| **Mobile Support** | Limited | Responsive ArcGIS widgets |
| **Data Layers** | Basic | Can add demographic overlays |

---

## 🔧 Configuration

### Optional: ArcGIS API Key
For premium features, add your ArcGIS API key:

1. Copy `.env.example` to `.env`
2. Get API key from: https://developers.arcgis.com/
3. Add to `.env`:
   ```
   ARCGIS_API_KEY=your_key_here
   ```

**Note**: Basic geocoding and mapping work without an API key using ArcGIS anonymous access.

---

## 📱 Usage Examples

### Adding a Store
1. Click **"+ Add Store"** button
2. Fill in form:
   - Store ID: `STORE001`
   - Name: `Green Valley Market`
   - Type: `Supermarket`
   - Address: `123 Main St`
   - City: `Los Angeles`
   - State: `CA`
   - ZIP: `90001`
3. Click **"Add Store"**
4. Watch as marker appears on map with EJV score

### Viewing Store Details
1. Click any marker on map
2. Popup shows:
   - EJV score with color coding
   - Store information
   - Location details
   - Action buttons (recalculate, delete)

### Filtering Stores
1. Use side panel filters:
   - Select store type
   - Set minimum EJV score
2. Click **"Apply"**
3. Map updates to show filtered results

---

## 🎨 Customization

### Change Map Style
Edit `static/js/app.js`:
```javascript
const map = new Map({
    basemap: "streets-navigation-vector" // or "satellite", "hybrid", "dark-gray"
});
```

### Adjust Marker Colors
Edit `getEJVColor()` function in `app.js`:
```javascript
function getEJVColor(ejvScore) {
    if (ejvScore >= 90) return [46, 204, 113]; // [R, G, B]
    // ...
}
```

### Modify Popup Content
Edit popup template in `addStoreToMap()` function.

---

## 🐛 Troubleshooting

### Map not loading
- Check internet connection (ArcGIS API loads from CDN)
- Open browser console for errors (F12)
- Verify Flask server is running

### Geocoding fails
- Verify address format is correct
- Check Census API is accessible
- Try with different address

### No stores appear
- Check database was initialized: `python database.py`
- Verify API endpoints return data: `http://localhost:5000/api/stores`
- Check browser console for errors

---

## 📚 Resources

- [ArcGIS JavaScript API](https://developers.arcgis.com/javascript/)
- [ArcGIS Python API](https://developers.arcgis.com/python/)
- [Census Bureau ACS API](https://www.census.gov/data/developers/data-sets/acs-5year.html)
- [BLS OEWS Data](https://www.bls.gov/oes/)

---

## 🤝 Contributing

To extend the application:
1. Add new store types in `INDUSTRY_CODES`
2. Create custom spatial analysis functions
3. Add demographic data layers
4. Implement route optimization
5. Add export features (GeoJSON, KML)

---

## 📄 License

MIT License - Free to use and modify

---

## 🎓 Next Steps

### Suggested Enhancements
1. **Cluster Analysis** - Group nearby stores automatically
2. **Drive-Time Analysis** - Show service areas
3. **Demographic Overlays** - Add Census data layers
4. **Heat Maps** - Visualize EJV density
5. **Export Reports** - PDF/Excel with maps
6. **Mobile App** - React Native with ArcGIS Runtime

---

## 📞 Support

For issues or questions:
- Check troubleshooting section
- Review ArcGIS API documentation
- Inspect browser console (F12)
- Check Flask server logs

---

**Built with ❤️ using Flask, ArcGIS, and real economic data**
