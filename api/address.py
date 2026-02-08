"""
API endpoint to bridge frontend to MCP server for address geocoding
"""

from flask import Blueprint, jsonify, request
import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os

address_bp = Blueprint('address', __name__)

# Path to MCP server
MCP_SERVER_PATH = os.path.join(os.path.dirname(__file__), '..', 'mcp-server-address', 'server.py')


async def call_mcp_tool(tool_name: str, arguments: dict):
    """Call an MCP tool and return the result"""
    server_params = StdioServerParameters(
        command="python",
        args=[MCP_SERVER_PATH]
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                result = await session.call_tool(tool_name, arguments=arguments)
                
                # Parse the result
                if result and len(result) > 0:
                    content = result[0]
                    if hasattr(content, 'text'):
                        return json.loads(content.text)
                
                return {"success": False, "error": "No result from MCP server"}
    
    except Exception as e:
        return {"success": False, "error": str(e)}


@address_bp.route('/geocode', methods=['POST'])
def geocode_address():
    """
    Geocode an address using MCP server
    
    POST /api/address/geocode
    Body: {"address": "123 Main St, Boston, MA"}
    """
    try:
        data = request.get_json()
        address = data.get('address')
        
        if not address:
            return jsonify({"success": False, "error": "address is required"}), 400
        
        # Call MCP server
        result = asyncio.run(call_mcp_tool('geocode_address', {'address': address}))
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@address_bp.route('/stores', methods=['POST'])
def find_stores():
    """
    Find stores near coordinates
    
    POST /api/address/stores
    Body: {"lat": 42.36, "lon": -71.05, "radius": 500}
    """
    try:
        data = request.get_json()
        lat = data.get('lat')
        lon = data.get('lon')
        radius = data.get('radius', 500)
        
        if lat is None or lon is None:
            return jsonify({"success": False, "error": "lat and lon are required"}), 400
        
        # Call MCP server
        result = asyncio.run(call_mcp_tool('find_stores', {
            'lat': lat,
            'lon': lon,
            'radius': radius
        }))
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@address_bp.route('/search', methods=['POST'])
def search_address_with_stores():
    """
    Complete search: geocode address and find stores
    
    POST /api/address/search
    Body: {"address": "Boston, MA", "radius": 500}
    """
    try:
        data = request.get_json()
        address = data.get('address')
        radius = data.get('radius', 500)
        
        if not address:
            return jsonify({"success": False, "error": "address is required"}), 400
        
        # Call MCP server
        result = asyncio.run(call_mcp_tool('search_address_with_stores', {
            'address': address,
            'radius': radius
        }))
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@address_bp.route('/clear-cache', methods=['POST'])
def clear_cache():
    """
    Clear the MCP server cache
    
    POST /api/address/clear-cache
    """
    try:
        result = asyncio.run(call_mcp_tool('clear_cache', {}))
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
