# Overpass API Troubleshooting Guide

## What is Overpass API?

Overpass API is a read-only API that serves OpenStreetMap (OSM) data. It allows you to query for specific map features like stores, restaurants, pharmacies, etc.

## Common Failure Reasons

### 1. **Rate Limiting**
- **Problem**: Too many requests in short time
- **Symptoms**: 429 error or "Too Many Requests"
- **Solution**: Wait 1-2 minutes between large queries, or use multiple servers

### 2. **Server Overload**
- **Problem**: Public server is busy handling many requests
- **Symptoms**: Timeouts, 504 Gateway Timeout errors
- **Solution**: Use multiple fallback servers (already implemented)

### 3. **Query Timeout**
- **Problem**: Query is too complex or area is too large
- **Symptoms**: "Query timeout" error after 25 seconds
- **Solution**: 
  - Reduce search radius (use 1-2 miles instead of 10)
  - Search for specific categories instead of "all"
  - Increase timeout in query: `[timeout:60]` instead of `[timeout:25]`

### 4. **Network Issues**
- **Problem**: Internet connection problems or DNS issues
- **Symptoms**: "Failed to fetch" or network errors
- **Solution**: Check internet connection, try different network

### 5. **Query Syntax Errors**
- **Problem**: Malformed Overpass QL query
- **Symptoms**: Error messages about syntax
- **Solution**: Check query format, test in https://overpass-turbo.eu/

## Our Implementation (Fixed Version)

We now use **3 backup servers** with automatic failover:

```javascript
const overpassServers = [
    'https://overpass-api.de/api/interpreter',        // Main (Germany)
    'https://overpass.kumi.systems/api/interpreter',  // Backup 1 (Germany)
    'https://overpass.openstreetmap.ru/api/interpreter' // Backup 2 (Russia)
];
```

### How It Works:
1. Try server 1 (overpass-api.de)
2. If it fails, wait 1 second
3. Try server 2 (overpass.kumi.systems)
4. If it fails, wait 1 second
5. Try server 3 (overpass.openstreetmap.ru)
6. If all fail, show error message

## How to Fix Common Issues Yourself

### Issue: "Query timeout exceeded"

**Current Query:**
```javascript
[out:json][timeout:25];
```

**Fix: Increase timeout**
```javascript
[out:json][timeout:60];  // Increase from 25 to 60 seconds
```

**Location in code:** Line ~1444 in index.html

---

### Issue: "Too many requests"

**Fix 1: Add delay between searches**
```javascript
async function searchStores(lat, lon, radiusMeters, category) {
    // Add minimum delay between searches
    const lastSearchTime = window.lastOverpassSearch || 0;
    const timeSinceLastSearch = Date.now() - lastSearchTime;
    
    if (timeSinceLastSearch < 2000) { // Wait at least 2 seconds
        await new Promise(resolve => setTimeout(resolve, 2000 - timeSinceLastSearch));
    }
    
    window.lastOverpassSearch = Date.now();
    
    // ... rest of function
}
```

**Fix 2: Cache results**
Already implemented with `ejvCache` - we cache EJV calculations to avoid re-fetching

---

### Issue: "No stores found" but you know they exist

**Possible causes:**
1. **Wrong OSM tag** - Try different tags:
   ```javascript
   // Instead of just "shop=cafe"
   node["amenity"="cafe"]  // Many cafes use amenity instead
   node["cuisine"="coffee_shop"]  // Some use cuisine tag
   ```

2. **Radius too small** - Increase from 1 mile to 3-5 miles

3. **Area has poor OSM data** - Some areas have incomplete OpenStreetMap data

**Fix: Broaden search**
```javascript
// Search both shop AND amenity tags
(
    node["shop"="${category}"](around:${radiusMeters},${lat},${lon});
    way["shop"="${category}"](around:${radiusMeters},${lat},${lon});
    node["amenity"="${category}"](around:${radiusMeters},${lat},${lon});
    way["amenity"="${category}"](around:${radiusMeters},${lat},${lon});
);
```

---

### Issue: Server responds but returns error

**Check response structure:**
```javascript
const response = await fetch(overpassUrl, {
    method: 'POST',
    body: query
});

if (!response.ok) {
    console.error('HTTP Error:', response.status, response.statusText);
    throw new Error(`Server returned ${response.status}`);
}

const data = await response.json();

// Check for Overpass API error messages
if (data.remark) {
    console.error('Overpass error:', data.remark);
}
```

---

## Testing Your Query

### Use Overpass Turbo (Web Tool)

1. Go to https://overpass-turbo.eu/
2. Paste your query:
   ```
   [out:json][timeout:25];
   (
       node["shop"="supermarket"](around:3218.69,40.7128,-74.0060);
       way["shop"="supermarket"](around:3218.69,40.7128,-74.0060);
   );
   out center;
   ```
3. Click "Run" to test
4. If it works there, it should work in your app

### Debug in Browser Console

```javascript
// Test query directly in browser
const query = `
    [out:json][timeout:25];
    (
        node["shop"="supermarket"](around:5000,40.7128,-74.0060);
    );
    out center;
`;

fetch('https://overpass-api.de/api/interpreter', {
    method: 'POST',
    body: query
})
.then(r => r.json())
.then(data => console.log('Results:', data))
.catch(err => console.error('Error:', err));
```

---

## Alternative APIs (If Overpass Keeps Failing)

### Option 1: Local Overpass Server
- Download and run your own Overpass API server
- No rate limits, full control
- Requires: Docker or Linux server
- Setup: https://github.com/drolbr/Overpass-API

### Option 2: Nominatim Search
- Use Nominatim with category search
- Less detailed but more reliable
```javascript
const url = `https://nominatim.openstreetmap.org/search?format=json&q=supermarket&bounded=1&viewbox=${west},${south},${east},${north}`;
```

### Option 3: Google Places API
- Paid service, very reliable
- $17 per 1000 requests
- Requires API key
```javascript
const url = `https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${lon}&radius=${radius}&type=supermarket&key=YOUR_API_KEY`;
```

### Option 4: Mapbox Places API
- Paid service, good reliability
- $0.50 per 1000 requests
```javascript
const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/supermarket.json?proximity=${lon},${lat}&access_token=YOUR_TOKEN`;
```

---

## Monitoring & Prevention

### Add Request Counter
```javascript
let overpassRequestCount = 0;
let overpassRequestReset = Date.now();

function checkRateLimit() {
    const now = Date.now();
    
    // Reset counter every minute
    if (now - overpassRequestReset > 60000) {
        overpassRequestCount = 0;
        overpassRequestReset = now;
    }
    
    // Limit to 10 requests per minute
    if (overpassRequestCount >= 10) {
        throw new Error('Rate limit: Please wait a minute before searching again');
    }
    
    overpassRequestCount++;
}
```

### Log Server Health
```javascript
const serverHealth = {
    'overpass-api.de': { failures: 0, lastSuccess: Date.now() },
    'overpass.kumi.systems': { failures: 0, lastSuccess: Date.now() },
    'overpass.openstreetmap.ru': { failures: 0, lastSuccess: Date.now() }
};

// Track which servers are working best
function recordServerResult(server, success) {
    if (success) {
        serverHealth[server].lastSuccess = Date.now();
        serverHealth[server].failures = 0;
    } else {
        serverHealth[server].failures++;
    }
    
    // Start with best server next time
    console.log('Server health:', serverHealth);
}
```

---

## Quick Fixes Summary

| Problem | Quick Fix |
|---------|-----------|
| Timeout | Increase `[timeout:60]` or reduce radius |
| Rate limit | Wait 1-2 minutes, use caching |
| Server down | Automatic failover to backup servers (already implemented) |
| No results | Try broader search, check OSM tags |
| Network error | Check internet, try different network |
| Wrong data | Verify query at overpass-turbo.eu |

---

## Current Implementation Status

✅ **Already Fixed:**
- Multiple backup servers with automatic failover
- Proper error handling and messages
- Response validation
- User-friendly error messages

✅ **Already Implemented:**
- EJV result caching
- Debounced hover events (50ms)
- Query timeout set to 25 seconds

⚠️ **Could Add:**
- Request rate limiting (10/minute)
- Server health monitoring
- Automatic query simplification on timeout
- Local result caching with localStorage

---

## Support Resources

- **Overpass API Docs**: https://wiki.openstreetmap.org/wiki/Overpass_API
- **Overpass Turbo**: https://overpass-turbo.eu/ (query tester)
- **OSM Tag Info**: https://taginfo.openstreetmap.org/ (find correct tags)
- **Overpass API Status**: https://status.openstreetmap.org/

## Test URLs

Test if servers are working:
```bash
# Test server 1
curl -X POST https://overpass-api.de/api/interpreter -d "[out:json];node(1);out;"

# Test server 2  
curl -X POST https://overpass.kumi.systems/api/interpreter -d "[out:json];node(1);out;"

# Test server 3
curl -X POST https://overpass.openstreetmap.ru/api/interpreter -d "[out:json];node(1);out;"
```

All should return JSON with a single node element.
