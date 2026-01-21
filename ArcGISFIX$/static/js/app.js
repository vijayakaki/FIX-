require([
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/GraphicsLayer",
    "esri/Graphic",
    "esri/geometry/Point",
    "esri/symbols/SimpleMarkerSymbol",
    "esri/widgets/Legend",
    "esri/widgets/BasemapToggle",
    "esri/widgets/Search",
    "esri/widgets/Locate",
    "esri/PopupTemplate"
], function(Map, MapView, GraphicsLayer, Graphic, Point, SimpleMarkerSymbol, Legend, BasemapToggle, Search, Locate, PopupTemplate) {

    // API Base URL
    const API_BASE = window.location.origin + '/api';

    // Create map
    const map = new Map({
        basemap: "streets-navigation-vector"
    });

    // Create graphics layer for stores
    const storesLayer = new GraphicsLayer({
        title: "FIX$ Stores"
    });
    map.add(storesLayer);

    // Create map view
    const view = new MapView({
        container: "viewDiv",
        map: map,
        center: [-98.5795, 39.8283], // Center of USA
        zoom: 4
    });

    // Add widgets
    const basemapToggle = new BasemapToggle({
        view: view,
        nextBasemap: "hybrid"
    });
    view.ui.add(basemapToggle, "bottom-right");

    const search = new Search({
        view: view
    });
    view.ui.add(search, "top-right");

    const locate = new Locate({
        view: view
    });
    view.ui.add(locate, "top-right");

    // Helper: Get marker color based on EJV score
    function getEJVColor(ejvScore) {
        if (ejvScore >= 90) return [46, 204, 113]; // Green
        if (ejvScore >= 80) return [52, 152, 219]; // Blue
        if (ejvScore >= 70) return [243, 156, 18]; // Orange
        return [231, 76, 60]; // Red
    }

    function getEJVCategory(ejvScore) {
        if (ejvScore >= 90) return 'Excellent';
        if (ejvScore >= 80) return 'Good';
        if (ejvScore >= 70) return 'Fair';
        return 'Poor';
    }

    // Add store to map
    function addStoreToMap(store) {
        if (!store.latitude || !store.longitude) return;

        const point = new Point({
            longitude: store.longitude,
            latitude: store.latitude
        });

        const color = getEJVColor(store.ejv_score || 0);
        const symbol = new SimpleMarkerSymbol({
            color: color,
            size: "16px",
            outline: {
                color: [255, 255, 255],
                width: 2
            }
        });

        // Create popup template
        const popupTemplate = new PopupTemplate({
            title: store.name,
            content: `
                <div class="popup-content">
                    <div class="ejv-scores-container">
                        <div class="ejv-score-box ejv-${getEJVCategory(store.ejv_score || 0).toLowerCase()}">
                            <div class="ejv-label">EJV V2</div>
                            <div class="ejv-value">${(store.ejv_score || 0).toFixed(1)}</div>
                        </div>
                        <div class="ejv-score-box ejv-${getEJVCategory(store.ejv_v1_score || 0).toLowerCase()}">
                            <div class="ejv-label">EJV V1</div>
                            <div class="ejv-value">${(store.ejv_v1_score || 0).toFixed(1)}</div>
                        </div>
                    </div>
                    <div class="popup-row">
                        <span class="popup-label">Store ID:</span>
                        <span class="popup-value">${store.store_id}</span>
                    </div>
                    <div class="popup-row">
                        <span class="popup-label">Type:</span>
                        <span class="popup-value">${store.type}</span>
                    </div>
                    <div class="popup-row">
                        <span class="popup-label">Location:</span>
                        <span class="popup-value">${store.city}, ${store.state}</span>
                    </div>
                    <div class="popup-row">
                        <span class="popup-label">ZIP Code:</span>
                        <span class="popup-value">${store.zip_code}</span>
                    </div>
                    <button onclick="recalculateStore('${store.store_id}')" class="btn btn-primary" style="width: 100%; margin-top: 10px;">
                        🔄 Recalculate EJV
                    </button>
                    <button onclick="deleteStore('${store.store_id}')" class="btn btn-secondary" style="width: 100%; margin-top: 5px; background: #e74c3c; color: white;">
                        🗑️ Delete Store
                    </button>
                </div>
            `
        });

        const graphic = new Graphic({
            geometry: point,
            symbol: symbol,
            attributes: store,
            popupTemplate: popupTemplate
        });

        storesLayer.add(graphic);
    }

    // Load all stores
    async function loadStores() {
        try {
            const response = await fetch(`${API_BASE}/stores`);
            const stores = await response.json();
            
            // Clear existing graphics
            storesLayer.removeAll();
            
            // Add each store to map
            stores.forEach(store => addStoreToMap(store));
            
            // Update statistics
            updateStatistics(stores);
            
            // Update stores list
            updateStoresList(stores);
            
            // Update geoequity impact
            updateGeoequityImpact(stores);
            
            // Zoom to stores if any exist
            if (stores.length > 0) {
                view.goTo(storesLayer.graphics, { duration: 1000 });
            }
            
            console.log(`Loaded ${stores.length} stores`);
        } catch (error) {
            console.error('Error loading stores:', error);
            alert('Failed to load stores. Make sure the server is running.');
        }
    }

    // Update statistics panel
    function updateStatistics(stores) {
        const totalStores = stores.length;
        const avgEJV_V2 = stores.reduce((sum, s) => sum + (s.ejv_score || 0), 0) / (totalStores || 1);
        const avgEJV_V1 = stores.reduce((sum, s) => sum + (s.ejv_v1_score || 0), 0) / (totalStores || 1);
        
        document.getElementById('totalStores').textContent = totalStores;
        document.getElementById('avgEJV_V2').textContent = avgEJV_V2.toFixed(1);
        document.getElementById('avgEJV_V1').textContent = avgEJV_V1.toFixed(1);
        document.getElementById('totalWealth').textContent = '$' + (totalStores * 5000).toLocaleString();
    }

    // Update stores list
    function updateStoresList(stores) {
        const storesList = document.getElementById('storesList');
        const storeCount = document.getElementById('storeCount');
        
        storeCount.textContent = stores.length;
        
        if (stores.length === 0) {
            storesList.innerHTML = '<p style=\"color: #999; text-align: center; padding: 20px;\">No stores added yet</p>';
            return;
        }
        
        // Sort by EJV V2 score descending
        const sortedStores = [...stores].sort((a, b) => (b.ejv_score || 0) - (a.ejv_score || 0));
        
        storesList.innerHTML = sortedStores.map(store => {
            const ejvColor = getEJVColor(store.ejv_score || 0);
            const colorHex = `rgb(${ejvColor[0]}, ${ejvColor[1]}, ${ejvColor[2]})`;
            
            return `
                <div class=\"store-list-item\" onclick=\"zoomToStore('${store.store_id}')\" style=\"
                    padding: 10px;
                    margin: 5px 0;
                    border-left: 4px solid ${colorHex};
                    background: #f8f9fa;
                    border-radius: 4px;
                    cursor: pointer;
                    transition: all 0.3s;
                \">
                    <div style=\"display: flex; justify-content: space-between; align-items: center;\">
                        <div style=\"flex: 1;\">
                            <strong style=\"font-size: 0.9rem;\">${store.name}</strong>
                            <br><small style=\"color: #666;\">${store.city}, ${store.state} ${store.zip_code}</small>
                        </div>
                        <div style=\"text-align: right;\">
                            <div style=\"font-size: 1.1rem; font-weight: bold; color: ${colorHex};\">${(store.ejv_score || 0).toFixed(1)}</div>
                            <small style=\"color: #999;\">EJV V2</small>
                        </div>
                    </div>
                </div>
            `;
        }).join('');
    }

    // Update geoequity impact analysis
    function updateGeoequityImpact(stores) {
        const geoequityContent = document.getElementById('geoequityContent');
        
        if (stores.length === 0) {
            geoequityContent.innerHTML = '<p style=\"color: #999; text-align: center; padding: 20px;\">Add stores to see impact analysis</p>';
            return;
        }
        
        // Group by ZIP code
        const zipGroups = {};
        stores.forEach(store => {
            const zip = store.zip_code || 'Unknown';
            if (!zipGroups[zip]) {
                zipGroups[zip] = [];
            }
            zipGroups[zip].push(store);
        });
        
        // Calculate impact by area
        let html = '';
        Object.keys(zipGroups).sort().forEach(zip => {
            const areaStores = zipGroups[zip];
            const avgEJV = areaStores.reduce((sum, s) => sum + (s.ejv_score || 0), 0) / areaStores.length;
            const totalWealth = areaStores.length * 5000; // Simplified calculation
            
            const impactColor = avgEJV >= 80 ? '#2ecc71' : avgEJV >= 70 ? '#f39c12' : '#e74c3c';
            const impactLevel = avgEJV >= 80 ? 'High' : avgEJV >= 70 ? 'Medium' : 'Low';
            
            html += `
                <div style="padding: 10px; margin: 5px 0; border-radius: 4px; background: #f8f9fa; border-left: 4px solid ${impactColor};">
                    <div style="display: flex; justify-content: space-between;">
                        <div>
                            <strong>ZIP ${zip}</strong>
                            <br><small style="color: #666;">${areaStores.length} store(s)</small>
                        </div>
                        <div style="text-align: right;">
                            <div style="font-weight: bold; color: ${impactColor};">${impactLevel}</div>
                            <small style="color: #999;">${avgEJV.toFixed(1)} avg</small>
                        </div>
                    </div>
                    <div style="margin-top: 5px; font-size: 0.85rem; color: #666;">
                        💰 $${totalWealth.toLocaleString()}/day wealth retained
                    </div>
                </div>
            `;
        });
        
        geoequityContent.innerHTML = html;
    }

    // Zoom to specific store
    window.zoomToStore = function(storeId) {
        const graphic = storesLayer.graphics.find(g => g.attributes.store_id === storeId);
        if (graphic) {
            view.goTo({
                target: graphic,
                zoom: 15
            }, {
                duration: 1000
            }).then(() => {
                view.popup.open({
                    features: [graphic],
                    location: graphic.geometry
                });
            });
        }
    };

    // Modal controls
    const modal = document.getElementById('searchStoresModal');
    const searchBtn = document.getElementById('searchStoresBtn');
    const closeBtn = document.getElementsByClassName('close')[0];
    const cancelBtn = document.getElementById('cancelSearchBtn');

    searchBtn.onclick = () => modal.style.display = 'block';
    closeBtn.onclick = () => modal.style.display = 'none';
    cancelBtn.onclick = () => modal.style.display = 'none';
    
    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };

    // Search stores form submission
    document.getElementById('searchStoresForm').onsubmit = async (e) => {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);
        
        const resultsDiv = document.getElementById('searchResults');
        const resultsList = document.getElementById('searchResultsList');
        const resultCount = document.getElementById('resultCount');
        
        resultsDiv.style.display = 'none';
        resultsList.innerHTML = '<p>🔍 Searching for stores...</p>';
        
        try {
            const response = await fetch(`${API_BASE}/search/stores`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (result.stores && result.stores.length > 0) {
                resultCount.textContent = result.count;
                resultsDiv.style.display = 'block';
                
                // Display search results
                resultsList.innerHTML = result.stores.map(store => `
                    <div class="search-result-item" style="padding: 10px; border: 1px solid #ddd; margin: 5px 0; border-radius: 4px; cursor: pointer;" 
                         onclick="addFoundStore('${JSON.stringify(store).replace(/'/g, "&apos;")}')">
                        <strong>${store.name}</strong> ${store.brand ? '(' + store.brand + ')' : ''}
                        <br><small>${store.address}, ${store.city || store.zip_code}</small>
                        <br><small style="color: #666;">Type: ${store.type}</small>
                        <button class="btn btn-primary" style="margin-top: 5px; font-size: 0.8rem;">Add to Map</button>
                    </div>
                `).join('');
                
            } else {
                resultsDiv.style.display = 'block';
                resultsList.innerHTML = '<p style="color: #e74c3c;">No stores found in this area. Try a different ZIP code or category.</p>';
            }
        } catch (error) {
            console.error('Error searching stores:', error);
            resultsDiv.style.display = 'block';
            resultsList.innerHTML = '<p style="color: #e74c3c;">Search failed. Please try again.</p>';
        }
    };

    // Add found store to map
    window.addFoundStore = async function(storeJson) {
        const store = JSON.parse(storeJson);
        
        try {
            const response = await fetch(`${API_BASE}/stores`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(store)
            });
            
            const result = await response.json();
            
            if (result.success) {
                alert(`Store added! EJV V2: ${result.ejv.ejv_score.toFixed(1)}`);
                loadStores();
            } else {
                alert('Failed to add store: ' + (result.error || 'Unknown error'));
            }
        } catch (error) {
            console.error('Error adding store:', error);
            alert('Failed to add store. Check console for details.');
        }
    };

    // Refresh button
    document.getElementById('refreshBtn').onclick = () => {
        loadStores();
    };

    // Apply filters
    document.getElementById('applyFilters').onclick = () => {
        const typeFilter = document.getElementById('typeFilter').value;
        const minEJV = parseFloat(document.getElementById('minEJV').value);
        
        storesLayer.graphics.forEach(graphic => {
            const store = graphic.attributes;
            let visible = true;
            
            if (typeFilter && store.type !== typeFilter) {
                visible = false;
            }
            
            if (minEJV && (store.ejv_score || 0) < minEJV) {
                visible = false;
            }
            
            graphic.visible = visible;
        });
    };

    // Global functions for popup buttons
    window.recalculateStore = async (storeId) => {
        try {
            const response = await fetch(`${API_BASE}/calculate/${storeId}`, {
                method: 'POST'
            });
            const result = await response.json();
            alert(`EJV Scores Recalculated:\nV2: ${result.ejv_v2.ejv_score.toFixed(1)}/100\nV1: ${result.ejv_v1.ejv_score.toFixed(1)}/100`);
            loadStores();
        } catch (error) {
            console.error('Error recalculating:', error);
            alert('Failed to recalculate EJV');
        }
    };

    window.deleteStore = async (storeId) => {
        if (!confirm('Are you sure you want to delete this store?')) return;
        
        try {
            await fetch(`${API_BASE}/stores/${storeId}`, {
                method: 'DELETE'
            });
            alert('Store deleted successfully');
            loadStores();
        } catch (error) {
            console.error('Error deleting:', error);
            alert('Failed to delete store');
        }
    };

    // Initial load
    view.when(() => {
        loadStores();
    });
});

