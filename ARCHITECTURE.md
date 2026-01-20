# FIX$ GeoEquity Impact Engine - Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[index.html<br/>Leaflet.js Map Interface]
        A1[User Interactions<br/>ZIP Search, Address, Polygon]
        A2[Store Markers<br/>Emoji Icons + Color Circles]
        A3[Grid Aggregation<br/>Area-level EJV Visualization]
        A4[Dashboard<br/>Real-time Metrics Display]
    end```mermaid
graph TB
    subgraph "Frontend Layer"
        A[index.html<br/>Leaflet.js Map Interface]
        A1[User Interactions<br/>ZIP Search, Address, Polygon]
        A2[Store Markers<br/>Emoji Icons + Color Circles]
        A3[Grid Aggregation<br/>Area-level EJV Visualization]
        A4[Dashboard<br/>Real-time Metrics Display]
    end

    subgraph "Backend API - Flask"
        B[app.py<br/>Python Flask Server]
        B1[/api/health]
        B2[/api/ejv/store_id]
        B3[/api/stores/demo]
        B4[/api/ejv/aggregate]
        B5[/ - Serves Frontend]
    end

    subgraph "External Data Sources"
        C1[BLS API<br/>Bureau of Labor Statistics<br/>Wage Data]
        C2[Census Bureau API<br/>Median Income<br/>Unemployment Rate]
        C3[Overpass API<br/>OpenStreetMap<br/>Store Locations]
    end

    subgraph "Core Calculation Engine"
        D[EJV Score Calculator]
        D1[Wage Score<br/>0-25 points]
        D2[Hiring Score<br/>0-25 points]
        D3[Community Score<br/>0-25 points]
        D4[Participation Score<br/>0-25 points]
        D5[Wealth Metrics<br/>Retained vs Leakage]
    end

    subgraph "Deployment & Hosting"
        E[Vercel<br/>Production Hosting]
        E1[fixapp-phi.vercel.app]
    end

    %% Frontend to Backend
    A --> A1 --> B
    A --> A2
    A --> A3
    A --> A4 --> B2

    %% Backend Routes
    B --> B1
    B --> B2
    B --> B3
    B --> B4
    B --> B5 --> A

    %% Backend to External APIs
    B2 --> C1
    B2 --> C2
    A1 --> C3

    %% Backend to Calculation Engine
    B2 --> D
    D --> D1
    D --> D2
    D --> D3
    D --> D4
    D --> D5

    %% Deployment
    B --> E
    A --> E
    E --> E1

    style A fill:#3498db,color:#fff
    style B fill:#e67e22,color:#fff
    style D fill:#27ae60,color:#fff
    style E fill:#9b59b6,color:#fff
    style C1 fill:#e74c3c,color:#fff
    style C2 fill:#e74c3c,color:#fff
    style C3 fill:#e74c3c,color:#fff
```

## System Components

### 1. Frontend (index.html)
**Technology:** HTML5, JavaScript, Leaflet.js 1.9.4

**Key Features:**
- 🗺️ **Interactive Map:** OpenStreetMap base layer with pan/zoom
- 🔍 **Search Methods:**
  - ZIP Code search with radius selection (1-10 miles)
  - Address geocoding search
  - Polygon drawing for custom areas
  - Demo data loader (NYC Times Square)
- 📊 **Visualizations:**
  - Emoji markers for each store type
  - Color-coded circles (200m radius) based on EJV score
  - Grid-based area aggregation (~500m cells)
  - Real-time dashboard with metrics
- 🎨 **Color Scheme:**
  - Red (#e74c3c): EJV 0-40
  - Orange (#ff6b35): EJV 40-55
  - Yellow (#f7b801): EJV 55-70
  - Cyan (#00d9ff): EJV 70-80
  - Light Green (#2ecc71): EJV 80-90
  - Dark Green (#27ae60): EJV 90-100

### 2. Backend API (app.py)
**Technology:** Python 3.14.2, Flask 3.0.0, Flask-CORS 4.0.0

**API Endpoints:**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serves index.html |
| `/api/health` | GET | Health check |
| `/api/ejv/<store_id>` | GET | Calculate EJV for single store |
| `/api/ejv/aggregate` | POST | Calculate aggregate EJV for multiple stores |
| `/api/stores/demo` | GET | Return 17 demo NYC stores |
| `/api/about/fix` | GET | About FIX$ methodology |

**Caching:**
- Wage data cached per industry code
- Employee count cached per store
- Prevents API rate limiting

### 3. External APIs

#### Bureau of Labor Statistics (BLS)
- **Endpoint:** `https://api.bls.gov/publicAPI/v2/timeseries/data/`
- **Purpose:** Real-time wage data by industry
- **Rate Limit:** Free tier, rate limited
- **Timeout:** 5 seconds

#### US Census Bureau
- **Endpoint:** `https://api.census.gov/data/`
- **Purpose:** Median income, unemployment rates
- **Data:** ACS (American Community Survey)
- **Timeout:** 5 seconds

#### Overpass API (OpenStreetMap)
- **Endpoint:** `https://overpass-api.de/api/interpreter`
- **Purpose:** Real-time store locations by type
- **Query:** Node/way search within radius
- **Timeout:** 20 seconds (frontend)

### 4. EJV Calculation Engine

**Formula:**
```
EJV = Wage Score + Hiring Score + Community Score + Participation Score
```

**Components:**

1. **Wage Score (0-25 points)**
   - Compares avg_wage to local living wage
   - `min(25, max(0, (avg_wage - living_wage) / living_wage * 50))`

2. **Hiring Score (0-25 points)**
   - Based on local hire percentage
   - `local_hire_pct * 25`

3. **Community Score (0-25 points)**
   - Community spending as % of payroll
   - `(community_spend / daily_payroll) * 100`

4. **Participation Score (0-25 points)**
   - Based on employee count (job creation)
   - `min(25, (active_employees / 100) * 25)`

**Wealth Metrics:**
```python
daily_payroll = active_employees × avg_wage × 8 hours
wealth_retained = daily_payroll × local_hire_pct + community_spend
wealth_leakage = daily_payroll × (1 - local_hire_pct)
```

### 5. Data Flow

```
User Action → Frontend Request → Backend Processing → External APIs → Calculation → Response → Visualization
```

**Example Flow (Store Hover):**
1. User hovers over CVS Pharmacy marker
2. Frontend sends: `GET /api/ejv/pharmacy_1004`
3. Backend generates store_id hash for consistency
4. Fetches BLS wage data (cached if available)
5. Fetches Census economic indicators
6. Calculates EJV components
7. Returns JSON: `{EJV: 65.91, wage_score: 25, ...}`
8. Frontend updates dashboard display
9. Frontend adds colored circle to map

### 6. Deployment Architecture

**Platform:** Vercel (Serverless)

**Configuration (vercel.json):**
```json
{
  "version": 2,
  "builds": [{"src": "app.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "app.py"}]
}
```

**Files:**
- `app.py` → Serverless function
- `index.html` → Static file served by app.py
- `requirements.txt` → Python dependencies
- `.vercelignore` → Excludes .venv, __pycache__

**Domain:** https://fixapp-phi.vercel.app

**Performance:**
- Cold start: ~1-3 seconds
- Warm requests: <100ms (API endpoints)
- Frontend: Cached by CDN

### 7. Color Aggregation Logic

**Individual Stores:**
- Each store gets a colored circle (200m radius)
- Color based on individual EJV score
- Overlapping circles create visual blending

**Grid Aggregation:**
- Map divided into 0.005° cells (~500m)
- For each cell:
  - Find all stores within bounds
  - Calculate average EJV
  - Color entire cell by average
- Provides true mathematical aggregation

### 8. Security & Performance

**CORS:** Enabled for cross-origin requests
**Timeouts:** All external APIs have timeouts (5-20s)
**Error Handling:** Graceful fallbacks for API failures
**Caching:** Reduces redundant API calls
**Rate Limiting:** Respects external API limits

## Tech Stack Summary

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, JavaScript, Leaflet.js |
| Backend | Python 3.14, Flask 3.0 |
| Hosting | Vercel (Serverless) |
| Maps | OpenStreetMap, Leaflet |
| Data | BLS API, Census API, Overpass API |
| Styling | Inline CSS, Custom markers |

## Key Design Decisions

1. **Client-Server Split:** Frontend handles mapping, backend handles calculations
2. **Real-time APIs:** Uses live government data instead of static datasets
3. **Consistent Randomization:** Hash-based RNG ensures same store_id always returns same EJV
4. **Dual Visualization:** Both individual circles and grid aggregation for clarity
5. **Progressive Enhancement:** Works without real-time APIs (fallback data)
6. **Serverless:** No infrastructure management, scales automatically

## Future Enhancements

- [ ] PWA (Progressive Web App) support
- [ ] Mobile-optimized interface
- [ ] User authentication for saved searches
- [ ] Historical EJV tracking
- [ ] Comparative analytics between areas
- [ ] Export to CSV/PDF reports
- [ ] Integration with Yelp/Google Places for business names


    subgraph "Backend API - Flask"
        B[app.py<br/>Python Flask Server]
        B1[/api/health]
        B2[/api/ejv/store_id]
        B3[/api/stores/demo]
        B4[/api/ejv/aggregate]
        B5[/ - Serves Frontend]
    end

    subgraph "External Data Sources"
        C1[BLS API<br/>Bureau of Labor Statistics<br/>Wage Data]
        C2[Census Bureau API<br/>Median Income<br/>Unemployment Rate]
        C3[Overpass API<br/>OpenStreetMap<br/>Store Locations]
    end

    subgraph "Core Calculation Engine"
        D[EJV Score Calculator]
        D1[Wage Score<br/>0-25 points]
        D2[Hiring Score<br/>0-25 points]
        D3[Community Score<br/>0-25 points]
        D4[Participation Score<br/>0-25 points]
        D5[Wealth Metrics<br/>Retained vs Leakage]
    end

    subgraph "Deployment & Hosting"
        E[Vercel<br/>Production Hosting]
        E1[fixapp-phi.vercel.app]
    end

    %% Frontend to Backend
    A --> A1 --> B
    A --> A2
    A --> A3
    A --> A4 --> B2

    %% Backend Routes
    B --> B1
    B --> B2
    B --> B3
    B --> B4
    B --> B5 --> A

    %% Backend to External APIs
    B2 --> C1
    B2 --> C2
    A1 --> C3

    %% Backend to Calculation Engine
    B2 --> D
    D --> D1
    D --> D2
    D --> D3
    D --> D4
    D --> D5

    %% Deployment
    B --> E
    A --> E
    E --> E1

    style A fill:#3498db,color:#fff
    style B fill:#e67e22,color:#fff
    style D fill:#27ae60,color:#fff
    style E fill:#9b59b6,color:#fff
    style C1 fill:#e74c3c,color:#fff
    style C2 fill:#e74c3c,color:#fff
    style C3 fill:#e74c3c,color:#fff
```

## System Components

### 1. Frontend (index.html)
**Technology:** HTML5, JavaScript, Leaflet.js 1.9.4

**Key Features:**
- 🗺️ **Interactive Map:** OpenStreetMap base layer with pan/zoom
- 🔍 **Search Methods:**
  - ZIP Code search with radius selection (1-10 miles)
  - Address geocoding search
  - Polygon drawing for custom areas
  - Demo data loader (NYC Times Square)
- 📊 **Visualizations:**
  - Emoji markers for each store type
  - Color-coded circles (200m radius) based on EJV score
  - Grid-based area aggregation (~500m cells)
  - Real-time dashboard with metrics
- 🎨 **Color Scheme:**
  - Red (#e74c3c): EJV 0-40
  - Orange (#ff6b35): EJV 40-55
  - Yellow (#f7b801): EJV 55-70
  - Cyan (#00d9ff): EJV 70-80
  - Light Green (#2ecc71): EJV 80-90
  - Dark Green (#27ae60): EJV 90-100

### 2. Backend API (app.py)
**Technology:** Python 3.14.2, Flask 3.0.0, Flask-CORS 4.0.0

**API Endpoints:**
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serves index.html |
| `/api/health` | GET | Health check |
| `/api/ejv/<store_id>` | GET | Calculate EJV for single store |
| `/api/ejv/aggregate` | POST | Calculate aggregate EJV for multiple stores |
| `/api/stores/demo` | GET | Return 17 demo NYC stores |
| `/api/about/fix` | GET | About FIX$ methodology |

**Caching:**
- Wage data cached per industry code
- Employee count cached per store
- Prevents API rate limiting

### 3. External APIs

#### Bureau of Labor Statistics (BLS)
- **Endpoint:** `https://api.bls.gov/publicAPI/v2/timeseries/data/`
- **Purpose:** Real-time wage data by industry
- **Rate Limit:** Free tier, rate limited
- **Timeout:** 5 seconds

#### US Census Bureau
- **Endpoint:** `https://api.census.gov/data/`
- **Purpose:** Median income, unemployment rates
- **Data:** ACS (American Community Survey)
- **Timeout:** 5 seconds

#### Overpass API (OpenStreetMap)
- **Endpoint:** `https://overpass-api.de/api/interpreter`
- **Purpose:** Real-time store locations by type
- **Query:** Node/way search within radius
- **Timeout:** 20 seconds (frontend)

### 4. EJV Calculation Engine

**Formula:**
```
EJV = Wage Score + Hiring Score + Community Score + Participation Score
```

**Components:**

1. **Wage Score (0-25 points)**
   - Compares avg_wage to local living wage
   - `min(25, max(0, (avg_wage - living_wage) / living_wage * 50))`

2. **Hiring Score (0-25 points)**
   - Based on local hire percentage
   - `local_hire_pct * 25`

3. **Community Score (0-25 points)**
   - Community spending as % of payroll
   - `(community_spend / daily_payroll) * 100`

4. **Participation Score (0-25 points)**
   - Based on employee count (job creation)
   - `min(25, (active_employees / 100) * 25)`

**Wealth Metrics:**
```python
daily_payroll = active_employees × avg_wage × 8 hours
wealth_retained = daily_payroll × local_hire_pct + community_spend
wealth_leakage = daily_payroll × (1 - local_hire_pct)
```

### 5. Data Flow

```
User Action → Frontend Request → Backend Processing → External APIs → Calculation → Response → Visualization
```

**Example Flow (Store Hover):**
1. User hovers over CVS Pharmacy marker
2. Frontend sends: `GET /api/ejv/pharmacy_1004`
3. Backend generates store_id hash for consistency
4. Fetches BLS wage data (cached if available)
5. Fetches Census economic indicators
6. Calculates EJV components
7. Returns JSON: `{EJV: 65.91, wage_score: 25, ...}`
8. Frontend updates dashboard display
9. Frontend adds colored circle to map

### 6. Deployment Architecture

**Platform:** Vercel (Serverless)

**Configuration (vercel.json):**
```json
{
  "version": 2,
  "builds": [{"src": "app.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "app.py"}]
}
```

**Files:**
- `app.py` → Serverless function
- `index.html` → Static file served by app.py
- `requirements.txt` → Python dependencies
- `.vercelignore` → Excludes .venv, __pycache__

**Domain:** https://fixapp-phi.vercel.app

**Performance:**
- Cold start: ~1-3 seconds
- Warm requests: <100ms (API endpoints)
- Frontend: Cached by CDN

### 7. Color Aggregation Logic

**Individual Stores:**
- Each store gets a colored circle (200m radius)
- Color based on individual EJV score
- Overlapping circles create visual blending

**Grid Aggregation:**
- Map divided into 0.005° cells (~500m)
- For each cell:
  - Find all stores within bounds
  - Calculate average EJV
  - Color entire cell by average
- Provides true mathematical aggregation

### 8. Security & Performance

**CORS:** Enabled for cross-origin requests
**Timeouts:** All external APIs have timeouts (5-20s)
**Error Handling:** Graceful fallbacks for API failures
**Caching:** Reduces redundant API calls
**Rate Limiting:** Respects external API limits

## Tech Stack Summary

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, JavaScript, Leaflet.js |
| Backend | Python 3.14, Flask 3.0 |
| Hosting | Vercel (Serverless) |
| Maps | OpenStreetMap, Leaflet |
| Data | BLS API, Census API, Overpass API |
| Styling | Inline CSS, Custom markers |

## Key Design Decisions

1. **Client-Server Split:** Frontend handles mapping, backend handles calculations
2. **Real-time APIs:** Uses live government data instead of static datasets
3. **Consistent Randomization:** Hash-based RNG ensures same store_id always returns same EJV
4. **Dual Visualization:** Both individual circles and grid aggregation for clarity
5. **Progressive Enhancement:** Works without real-time APIs (fallback data)
6. **Serverless:** No infrastructure management, scales automatically

## Future Enhancements

- [ ] PWA (Progressive Web App) support
- [ ] Mobile-optimized interface
- [ ] User authentication for saved searches
- [ ] Historical EJV tracking
- [ ] Comparative analytics between areas
- [ ] Export to CSV/PDF reports
- [ ] Integration with Yelp/Google Places for business names
