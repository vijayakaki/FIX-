import requests
import random
import hashlib
from datetime import datetime
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import database
import os

app = Flask(__name__)
CORS(app)

# Initialize database
@app.before_request
def initialize_database():
    if not hasattr(app, 'db_initialized'):
        try:
            database.init_database()
            app.db_initialized = True
            print("✓ Database initialized")
        except Exception as e:
            print(f"Database error: {e}")

# ==========================================
# BLS OEWS Wage Data (May 2024)
# ==========================================
BLS_WAGE_DATA = {
    "41-2031": {"wage": 15.02, "title": "Retail Salespersons"},
    "53-7064": {"wage": 17.02, "title": "Packers and Packagers"},
    "53-6031": {"wage": 14.75, "title": "Service Attendants"},
    "29-2052": {"wage": 18.79, "title": "Pharmacy Technicians"},
    "35-3031": {"wage": 15.15, "title": "Waiters and Waitresses"},
    "35-3023": {"wage": 14.33, "title": "Fast Food Workers"},
}

INDUSTRY_CODES = {
    "supermarket": {"soc_code": "41-2031", "naics": "4451"},
    "grocery": {"soc_code": "41-2031", "naics": "4451"},
    "warehouse_club": {"soc_code": "53-7064", "naics": "45291"},
    "convenience": {"soc_code": "41-2031", "naics": "4471"},
    "fuel": {"soc_code": "53-6031", "naics": "4471"},
    "pharmacy": {"soc_code": "29-2052", "naics": "4461"},
    "restaurant": {"soc_code": "35-3031", "naics": "7225"},
    "fast_food": {"soc_code": "35-3023", "naics": "7225"},
}

WAGE_STANDARDS = {
    "supermarket": {"min": 13.5, "max": 18.0, "avg_employees": 48},
    "grocery": {"min": 13.0, "max": 17.5, "avg_employees": 35},
    "warehouse_club": {"min": 15.0, "max": 20.0, "avg_employees": 72},
    "convenience": {"min": 12.0, "max": 15.5, "avg_employees": 9},
    "pharmacy": {"min": 16.0, "max": 22.0, "avg_employees": 21},
    "restaurant": {"min": 13.0, "max": 18.0, "avg_employees": 17},
    "default": {"min": 13.0, "max": 17.0, "avg_employees": 25}
}

def generate_consistent_random(store_id, seed_suffix=""):
    """Generate consistent random value for store"""
    combined = f"{store_id}{seed_suffix}"
    hash_value = int(hashlib.md5(combined.encode()).hexdigest(), 16)
    return (hash_value % 10000) / 10000.0

def get_local_economic_data(zip_code):
    """Get economic data from Census API"""
    try:
        url = "https://api.census.gov/data/2022/acs/acs5/profile"
        params = {
            'get': 'NAME,DP03_0005PE,DP03_0062E',
            'for': f'zip code tabulation area:{zip_code.zfill(5)}'
        }
        response = requests.get(url, params=params, timeout=10)
        if response.ok:
            data = response.json()
            if len(data) > 1:
                unemployment = float(data[1][1]) if data[1][1] != 'null' else 5.0
                income = int(float(data[1][2])) if data[1][2] != 'null' else 50000
                return {'unemployment_rate': unemployment, 'median_income': income}
    except Exception as e:
        print(f"Census API error: {e}")
    return {'unemployment_rate': 5.0, 'median_income': 50000}

def calculate_ejv_v1(store_data, payroll_data, economic_data):
    """Calculate EJV V1 score - original algorithm"""
    
    unemployment_rate = economic_data.get('unemployment_rate', 5.0)
    median_income = economic_data.get('median_income', 50000)
    avg_wage = payroll_data.get('avg_wage', 15.0)
    employee_count = payroll_data.get('active_employees', 25)
    
    # Simple living wage (70% of median income hourly)
    living_wage = (median_income * 0.7) / 2080
    
    # V1 Components (simpler)
    # 1. Wage Score (50 points)
    wage_ratio = min(avg_wage / living_wage, 1.2)
    wage_score = (wage_ratio / 1.2) * 50
    
    # 2. Local Impact (50 points)
    local_factor = 0.75 + (unemployment_rate / 20.0)
    daily_wealth = avg_wage * 8 * employee_count * local_factor
    impact_score = min(daily_wealth / 250, 1.0) * 50
    
    ejv_v1 = wage_score + impact_score
    
    return {
        'ejv_score': round(ejv_v1, 2),
        'wage_score': round(wage_score, 2),
        'impact_score': round(impact_score, 2),
        'wealth_retained_daily': round(daily_wealth, 2),
        'living_wage': round(living_wage, 2)
    }

def calculate_ejv_v2(store_data, payroll_data, economic_data):
    """Calculate EJV V2 score with real-time data"""
    
    # Extract data
    unemployment_rate = economic_data.get('unemployment_rate', 5.0)
    median_income = economic_data.get('median_income', 50000)
    avg_wage = payroll_data.get('avg_wage', 15.0)
    employee_count = payroll_data.get('active_employees', 25)
    
    # Living wage calculation (simplified)
    living_wage = (median_income / 2080) * 1.2  # Annual to hourly + 20% buffer
    living_wage = max(15.0, min(living_wage, 25.0))
    
    # Component calculations
    # 1. Local Hiring Score (40 points)
    unemployment_factor = min(unemployment_rate / 10.0, 1.0)
    local_hiring = 0.85 + (unemployment_factor * 0.15)
    local_hiring_score = local_hiring * 40
    
    # 2. Wage Equity Score (40 points)
    wage_ratio = avg_wage / living_wage
    wage_ratio_clamped = max(0.889, min(wage_ratio, 0.925))
    wage_equity_score = (wage_ratio_clamped - 0.889) / (0.925 - 0.889) * 40
    
    # 3. Economic Impact (20 points)
    daily_payroll = avg_wage * 8 * employee_count
    wealth_retained = daily_payroll * local_hiring
    impact_score = min(wealth_retained / 300, 1.0) * 20
    
    # Total EJV Score
    ejv_score = local_hiring_score + wage_equity_score + impact_score
    
    return {
        'ejv_score': round(ejv_score, 2),
        'local_hiring_score': round(local_hiring_score, 2),
        'wage_equity_score': round(wage_equity_score, 2),
        'economic_impact_score': round(impact_score, 2),
        'wealth_retained_daily': round(wealth_retained, 2),
        'living_wage': round(living_wage, 2),
        'wage_ratio': round(wage_ratio, 4),
        'local_hiring_percent': round(local_hiring * 100, 1)
    }

# ==========================================
# Geocoding Functions (using ArcGIS REST API)
# ==========================================
def geocode_address(address):
    """Geocode address using ArcGIS World Geocoding Service"""
    try:
        # Use ArcGIS World Geocoding Service (free, no token required for basic use)
        url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates"
        params = {
            'singleLine': address,
            'f': 'json',
            'outFields': 'Match_addr',
            'maxLocations': 1
        }
        
        response = requests.get(url, params=params, timeout=10)
        if response.ok:
            data = response.json()
            if data.get('candidates') and len(data['candidates']) > 0:
                candidate = data['candidates'][0]
                location = candidate['location']
                return {
                    'latitude': location['y'],
                    'longitude': location['x'],
                    'formatted_address': candidate.get('address', address)
                }
    except Exception as e:
        print(f"Geocoding error: {e}")
    return None

# ==========================================
# API Routes
# ==========================================
@app.route('/')
def index():
    """Serve main map interface"""
    return render_template('index.html')

@app.route('/api/stores', methods=['GET'])
def get_stores():
    """Get all stores with coordinates"""
    stores = database.get_all_stores()
    return jsonify(stores)

@app.route('/api/search/stores', methods=['POST'])
def search_stores():
    """Search for real stores by ZIP code and address using Overpass API"""
    data = request.json
    zip_code = data.get('zip_code', '')
    address = data.get('address', '')
    category = data.get('category', 'all')  # supermarket, grocery, etc.
    radius = int(data.get('radius', 5)) * 1000  # Convert km to meters
    
    # Geocode the search location first
    search_address = f"{address}, {zip_code}" if address else zip_code
    geo_result = geocode_address(search_address)
    
    if not geo_result:
        return jsonify({'error': 'Could not geocode location'}), 400
    
    lat = geo_result['latitude']
    lon = geo_result['longitude']
    
    # Map categories to Overpass tags
    category_mapping = {
        'supermarket': 'shop=supermarket',
        'grocery': 'shop=convenience|shop=greengrocer',
        'pharmacy': 'amenity=pharmacy',
        'restaurant': 'amenity=restaurant',
        'fast_food': 'amenity=fast_food',
        'cafe': 'amenity=cafe',
        'all': 'shop=supermarket|shop=convenience|amenity=pharmacy|amenity=restaurant'
    }
    
    query_tags = category_mapping.get(category, category_mapping['all'])
    
    # Search for stores using Overpass API (OpenStreetMap)
    try:
        # Overpass query for stores within custom radius
        overpass_url = "https://overpass-api.de/api/interpreter"
        overpass_query = f"""
        [out:json][timeout:25];
        (
          node[{query_tags}](around:{radius},{lat},{lon});
          way[{query_tags}](around:{radius},{lat},{lon});
        );
        out center 50;
        """
        
        response = requests.post(overpass_url, data={'data': overpass_query}, timeout=30)
        
        if response.ok:
            osm_data = response.json()
            stores = []
            
            for element in osm_data.get('elements', [])[:50]:  # Limit to 50 stores
                tags = element.get('tags', {})
                
                # Get coordinates
                if element['type'] == 'node':
                    store_lat = element['lat']
                    store_lon = element['lon']
                elif 'center' in element:
                    store_lat = element['center']['lat']
                    store_lon = element['center']['lon']
                else:
                    continue
                
                # Determine store type
                store_type = 'supermarket'
                if 'shop' in tags:
                    store_type = tags['shop']
                elif 'amenity' in tags:
                    store_type = tags['amenity']
                
                # Get ZIP from address if available
                store_zip = tags.get('addr:postcode', zip_code)
                
                # Create store entry
                store_id = f"OSM{element['id']}"
                store_name = tags.get('name', f"{store_type.title()} Store")
                
                stores.append({
                    'store_id': store_id,
                    'name': store_name,
                    'type': store_type,
                    'address': tags.get('addr:street', 'Unknown'),
                    'city': tags.get('addr:city', ''),
                    'state': tags.get('addr:state', ''),
                    'zip_code': store_zip,
                    'latitude': store_lat,
                    'longitude': store_lon,
                    'brand': tags.get('brand', '')
                })
            
            return jsonify({'stores': stores, 'count': len(stores)})
        else:
            return jsonify({'error': 'Failed to search stores'}), 500
            
    except Exception as e:
        print(f"Store search error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/stores', methods=['POST'])
def create_store():
    """Create new store with geocoding"""
    data = request.json
    
    # Build full address
    full_address = f"{data.get('address', '')}, {data.get('city', '')}, {data.get('state', '')} {data.get('zip_code', '')}"
    
    # Geocode address
    geo_result = geocode_address(full_address)
    if geo_result:
        data['latitude'] = geo_result['latitude']
        data['longitude'] = geo_result['longitude']
    
    # Get economic data
    economic_data = get_local_economic_data(data.get('zip_code', '10001'))
    
    # Generate payroll data
    industry_info = INDUSTRY_CODES.get(data.get('type', 'supermarket'), INDUSTRY_CODES['supermarket'])
    wage_info = BLS_WAGE_DATA.get(industry_info['soc_code'])
    avg_wage = wage_info['wage'] if wage_info else 15.0
    
    standards = WAGE_STANDARDS.get(data.get('type', 'supermarket'), WAGE_STANDARDS['default'])
    employee_count = standards['avg_employees']
    
    payroll_data = {
        'avg_wage': avg_wage,
        'active_employees': employee_count
    }
    
    # Calculate EJV
    ejv_v2_result = calculate_ejv_v2(data, payroll_data, economic_data)
    ejv_v1_result = calculate_ejv_v1(data, payroll_data, economic_data)
    data['ejv_score'] = ejv_v2_result['ejv_score']
    data['ejv_v1_score'] = ejv_v1_result['ejv_score']
    
    # Save to database
    store_id = database.add_store(data)
    
    # Save calculation
    calc_data = {
        'store_id': data['store_id'],
        'ejv_score': ejv_v2_result['ejv_score'],
        'wealth_retained': ejv_v2_result['wealth_retained_daily'],
        'local_hiring_score': ejv_v2_result['local_hiring_score'],
        'wage_equity_score': ejv_v2_result['wage_equity_score'],
        'unemployment_rate': economic_data['unemployment_rate'],
        'median_income': economic_data['median_income'],
        'avg_wage': avg_wage,
        'employee_count': employee_count
    }
    database.save_ejv_calculation(calc_data)
    
    return jsonify({
        'success': True, 
        'store_id': store_id, 
        'ejv_v1': ejv_v1_result,
        'ejv_v2': ejv_v2_result
    })

@app.route('/api/stores/<store_id>', methods=['GET'])
def get_store(store_id):
    """Get specific store details"""
    store = database.get_store_by_id(store_id)
    if store:
        return jsonify(store)
    return jsonify({'error': 'Store not found'}), 404

@app.route('/api/stores/<store_id>', methods=['DELETE'])
def delete_store(store_id):
    """Delete a store"""
    database.delete_store(store_id)
    return jsonify({'success': True})

@app.route('/api/calculate/<store_id>', methods=['POST'])
def calculate_store_ejv(store_id):
    """Calculate EJV for existing store"""
    store = database.get_store_by_id(store_id)
    if not store:
        return jsonify({'error': 'Store not found'}), 404
    
    # Get economic data
    economic_data = get_local_economic_data(store['zip_code'])
    
    # Generate payroll
    industry_info = INDUSTRY_CODES.get(store['type'], INDUSTRY_CODES['supermarket'])
    wage_info = BLS_WAGE_DATA.get(industry_info['soc_code'])
    avg_wage = wage_info['wage'] if wage_info else 15.0
    
    standards = WAGE_STANDARDS.get(store['type'], WAGE_STANDARDS['default'])
    employee_count = standards['avg_employees']
    
    payroll_data = {'avg_wage': avg_wage, 'active_employees': employee_count}
    
    # Calculate both V1 and V2
    ejv_v1_result = calculate_ejv_v1(store, payroll_data, economic_data)
    ejv_v2_result = calculate_ejv_v2(store, payroll_data, economic_data)
    
    # Update database with both scores
    database.update_store_ejv(store_id, ejv_v2_result['ejv_score'], ejv_v1_result['ejv_score'])
    
    calc_data = {
        'store_id': store_id,
        'ejv_score': ejv_result['ejv_score'],
        'wealth_retained': ejv_result['wealth_retained_daily'],
        'local_hiring_score': ejv_result['local_hiring_score'],
        'wage_equity_score': ejv_result['wage_equity_score'],
        'unemployment_rate': economic_data['unemployment_rate'],
        'median_income': economic_data['median_income'],
        'avg_wage': avg_wage,
        'employee_count': employee_count
    }
    database.save_ejv_calculation(calc_data)
    
    return jsonify({
        'ejv_v1': ejv_v1_result,
        'ejv_v2': ejv_v2_result,
        'economic_data': economic_data,
        'payroll_data': payroll_data
    })

@app.route('/api/geocode', methods=['POST'])
def geocode_endpoint():
    """Geocode an address"""
    data = request.json
    address = data.get('address', '')
    result = geocode_address(address)
    if result:
        return jsonify(result)
    return jsonify({'error': 'Geocoding failed'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Vercel serverless function export
app = app
