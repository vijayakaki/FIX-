# User Dashboard Implementation Plan

## Overview
Implementation of a personalized GeoEquity tracking dashboard that monitors user spending patterns and calculates a Whole-Person GeoEquity Score based on their shopping choices.

## Data Requirements

### User Profile Data (One-time setup)
- **Name**: User's full name
- **ZIP Code**: Home location for distance calculations
- **Monthly Spending Goal**: Optional target for tracking

### Transaction Data (Ongoing tracking)
- Purchase amount ($)
- Store name/location
- Purchase date
- Store EJV score (from calculations)
- Distance from home
- Local retention percentage

## Data Storage

**Current Implementation: Browser localStorage**
- All user data stored in browser localStorage
- JSON structure for easy manipulation
- No backend required for MVP
- Data persists across sessions

**Future Enhancement: Backend API**
- Can migrate to database later
- Enable multi-device sync
- Cloud backup capabilities

## Metrics & Calculations

### Whole-Person GeoEquity Score (0-100)
Weighted average of 4 core dimensions:

```
GeoEquity Score = 
  (LOCATOR * 0.20) + 
  (COMPARE * 0.30) + 
  (OPTIMIZE * 0.25) + 
  (ENGAGE * 0.25)
```

### Core Dimensions

#### 1. LOCATOR Awareness (0-100)
- **Tracks**: Number of store searches, stores discovered
- **Formula**: `(stores_discovered / 50) * 100`
- **Purpose**: Measures exploration of local options

#### 2. COMPARE Equity Alignment (0-100)
- **Tracks**: Average EJV of stores purchased from
- **Formula**: `Average of all purchased store EJV scores`
- **Purpose**: Measures alignment with high-impact stores

#### 3. OPTIMIZE (0-100)
- **Tracks**: Suggestions shown vs adopted
- **Formula**: `(suggestions_adopted / suggestions_shown) * 100`
- **Purpose**: Measures action on recommendations

#### 4. ENGAGE Collective Impact (0-100)
- **Tracks**: Civic participation activities
- **Formula**: `PAF (Participation Amplification Factor) * 100`
- **Purpose**: Measures community engagement

### Spending Flow Metrics

**Calculated from purchase history:**
- **Local Retained %**: Sum of (purchase_amount * store_retention_rate)
- **Regional Leak %**: Money going to regional suppliers
- **National Leak %**: Money going to national/corporate entities
- **Average Distance**: Mean distance of all purchases from home

### Progress Timeline
- Monthly GeoEquity scores stored for trend analysis
- Line chart visualization
- Month-over-month comparison

## User Interface Components

### 1. Top Score Card
```
┌─────────────────────────────────────┐
│ Whole-Person GeoEquity Score        │
│                                     │
│     78 / 100      ↑ +6 this month   │
│                                     │
│ "Your choices retained $412 more    │
│  locally this quarter."             │
│                                     │
│ [View Methodology] [Adjust Weights] │
└─────────────────────────────────────┘
```

### 2. Core Dimensions Grid (2x2)
```
┌─────────────────┬─────────────────┐
│ LOCATOR         │ COMPARE         │
│ Awareness       │ Equity Align    │
│ 65/100  ↑ +4    │ 81/100  ↑ +2    │
│ "5 range more"  │ "Your avg EJV   │
│                 │  is higher"     │
├─────────────────┼─────────────────┤
│ OPTIMIZE        │ ENGAGE          │
│                 │ Collective      │
│ 74/100  ↑ +8    │ 92/100  ↑ +10   │
│ "You adopted    │ "Your PAF       │
│  3 suggestions" │ influenced 4"   │
└─────────────────┴─────────────────┘
```

### 3. Spending Flow Visual
```
Where Your Money Goes
┌─────────────────────────────────────┐
│ Local Retained:  ██████████  68%    │
│ Regional Leak:   ███         22%    │
│ National Leak:   ██          10%    │
│                                     │
│ Avg Distance Traveled: 14.2 miles   │
└─────────────────────────────────────┘
```

### 4. Progress Timeline
```
Your Progress Over Time
┌─────────────────────────────────────┐
│ 100 │                         •─•   │
│  80 │             •──•    •          │
│  60 │       •──•                     │
│  40 │                                │
│  20 │                                │
│     └───────────────────────────────│
│      Jan Feb Mar Apr May Jun Jul Aug│
└─────────────────────────────────────┘
```

### 5. Purchase Logging
**Floating Action Button**: "Log Purchase" or "Add Transaction"
**Quick Add from Search**: Button in store results list

## User Flow

### Initial Setup (First Visit)
1. Welcome modal appears
2. User enters:
   - Name
   - Home ZIP code
   - Optional: Monthly spending goal
3. Data saved to localStorage
4. Dashboard displays with initial state

### Logging a Purchase
1. Click "Log Purchase" button
2. Modal/form appears:
   - Store name (dropdown of recently searched stores)
   - Purchase amount
   - Date (defaults to today)
   - Optional: Category
3. System auto-fetches:
   - Store EJV score (if available)
   - Local retention %
   - Distance from home
4. Purchase added to history
5. All metrics recalculated
6. Dashboard updates in real-time

### Automated Tracking
- **Searches**: Auto-increment LOCATOR score
- **Store Hovers**: Track which stores user explores
- **Compare Actions**: Track when user uses BENCHMARK
- **Suggestions**: Track when SURFACE OPPORTUNITIES used
- **Engagement**: Track PAF activities

## Data Structure (localStorage)

```javascript
// User Profile
{
  "userProfile": {
    "name": "John Doe",
    "zipCode": "10001",
    "monthlyGoal": 5000,
    "createdDate": "2026-01-15"
  },
  
  // Purchase History
  "purchases": [
    {
      "id": "uuid-1",
      "storeName": "Local Grocery Co",
      "storeId": "osm-12345",
      "amount": 156.50,
      "date": "2026-01-20",
      "ejvScore": 78.5,
      "localRetention": 0.68,
      "distance": 2.3,
      "category": "grocery"
    }
  ],
  
  // Activity Tracking
  "activity": {
    "storesDiscovered": 32,
    "searchesMade": 45,
    "suggestionsShown": 12,
    "suggestionsAdopted": 3,
    "lastUpdated": "2026-01-29"
  },
  
  // Monthly History
  "monthlyScores": [
    {
      "month": "2026-01",
      "geoEquityScore": 78,
      "locatorScore": 65,
      "compareScore": 81,
      "optimizeScore": 74,
      "engageScore": 92,
      "totalSpent": 1245.60,
      "localRetained": 846.20
    }
  ]
}
```

## Implementation Phases

### Phase 1: Basic Setup ✓
- [ ] User profile modal/form
- [ ] localStorage initialization
- [ ] Profile display in dashboard
- [ ] Purchase logging form
- [ ] Purchase history display

### Phase 2: Score Calculations ✓
- [ ] LOCATOR score calculation
- [ ] COMPARE score calculation
- [ ] OPTIMIZE score calculation
- [ ] ENGAGE score calculation
- [ ] Overall GeoEquity score
- [ ] Monthly score tracking

### Phase 3: Visualizations ✓
- [ ] Top score card with trend
- [ ] Core dimensions 2x2 grid
- [ ] Spending flow bar chart
- [ ] Progress timeline chart
- [ ] Purchase history table

### Phase 4: Integrations ✓
- [ ] Auto-track searches in Locator
- [ ] Quick add from search results
- [ ] Link to store EJV data
- [ ] Calculate distances from home
- [ ] Monthly summary generation

### Phase 5: Enhancements (Future)
- [ ] Export data to CSV
- [ ] Monthly email reports
- [ ] Spending insights/tips
- [ ] Comparison with community averages
- [ ] Achievement badges
- [ ] Social sharing features

## Integration Points

### Existing Functions to Hook Into
1. **searchByZip()** - Increment LOCATOR awareness
2. **calculateEJV()** - Get store scores for purchases
3. **Store hover events** - Track exploration
4. **setDecisionMode()** - Track BENCHMARK/OPTIMIZE usage
5. **Nominatim API** - Calculate distances from home

### New Functions to Create
1. **initUserDashboard()** - Initialize on first load
2. **saveUserProfile()** - Save profile to localStorage
3. **logPurchase()** - Add new purchase
4. **calculateGeoEquityScore()** - Compute overall score
5. **updateDashboardMetrics()** - Refresh all displays
6. **generateMonthlyReport()** - End-of-month summary

## Technical Considerations

### Performance
- localStorage read/write on updates only
- Calculations cached where possible
- Debounced auto-tracking events

### Data Privacy
- All data stored locally in browser
- No external data transmission
- User can clear data anytime

### Scalability
- Design data structure for easy migration to backend
- Keep API-ready JSON format
- Modular code for future enhancements

## Success Metrics

### User Engagement
- % of users who complete profile setup
- Average purchases logged per user
- Dashboard visit frequency

### Score Trends
- Average GeoEquity score increase over time
- % of users improving scores month-over-month
- Most improved dimension

### Feature Usage
- Most used tracking features
- Quick add vs manual logging ratio
- Export/report generation frequency

## Future Enhancements

### Backend Integration
- RESTful API endpoints
- User authentication
- Multi-device sync
- Cloud backup

### Advanced Features
- Bank account linking (Plaid API)
- Receipt scanning (OCR)
- Location-based purchase detection
- Automated store matching
- Community leaderboards
- Impact challenges/goals

### Analytics
- Aggregate anonymized data
- Community impact reports
- Geographic insights
- Trend analysis

---

## Implementation Timeline

**Week 1**: Phase 1 - Basic Setup
**Week 2**: Phase 2 - Calculations
**Week 3**: Phase 3 - Visualizations
**Week 4**: Phase 4 - Integrations
**Ongoing**: Phase 5 - Enhancements

---

*Last Updated: January 29, 2026*
