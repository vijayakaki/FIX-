import sqlite3
import os
from datetime import datetime

DATABASE_PATH = 'fixapp_arcgis.db'

def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Stores table with geographic coordinates
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            address TEXT,
            city TEXT,
            state TEXT,
            zip_code TEXT,
            latitude REAL,
            longitude REAL,
            ejv_score REAL,
            ejv_v1_score REAL,
            last_calculated TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # EJV Calculations history
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ejv_calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            store_id TEXT NOT NULL,
            ejv_score REAL NOT NULL,
            wealth_retained REAL,
            local_hiring_score REAL,
            wage_equity_score REAL,
            unemployment_rate REAL,
            median_income INTEGER,
            avg_wage REAL,
            employee_count INTEGER,
            calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (store_id) REFERENCES stores (store_id)
        )
    ''')
    
    # Create indexes for performance
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_store_id ON stores(store_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_zip_code ON stores(zip_code)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_ejv_calc_store ON ejv_calculations(store_id)')
    
    conn.commit()
    conn.close()
    print("✓ Database initialized successfully")

def add_store(store_data):
    """Add a new store to the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO stores (store_id, name, type, address, city, state, zip_code, 
                          latitude, longitude, ejv_score, last_calculated)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        store_data.get('store_id'),
        store_data.get('name'),
        store_data.get('type'),
        store_data.get('address'),
        store_data.get('city'),
        store_data.get('state'),
        store_data.get('zip_code'),
        store_data.get('latitude'),
        store_data.get('longitude'),
        store_data.get('ejv_score'),
        datetime.now()
    ))
    
    conn.commit()
    conn.close()
    return cursor.lastrowid

def update_store_coordinates(store_id, latitude, longitude):
    """Update store geographic coordinates"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE stores 
        SET latitude = ?, longitude = ?
        WHERE store_id = ?
    ''', (latitude, longitude, store_id))
    
    conn.commit()
    conn.close()

def update_store_ejv(store_id, ejv_v2_score, ejv_v1_score=None):
    """Update store EJV scores"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if ejv_v1_score is not None:
        cursor.execute('''
            UPDATE stores 
            SET ejv_score = ?, ejv_v1_score = ?, last_calculated = ?
            WHERE store_id = ?
        ''', (ejv_v2_score, ejv_v1_score, datetime.now(), store_id))
    else:
        cursor.execute('''
            UPDATE stores 
            SET ejv_score = ?, last_calculated = ?
            WHERE store_id = ?
        ''', (ejv_v2_score, datetime.now(), store_id))
    
    conn.commit()
    conn.close()

def save_ejv_calculation(calc_data):
    """Save EJV calculation to history"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO ejv_calculations 
        (store_id, ejv_score, wealth_retained, local_hiring_score, wage_equity_score,
         unemployment_rate, median_income, avg_wage, employee_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        calc_data.get('store_id'),
        calc_data.get('ejv_score'),
        calc_data.get('wealth_retained'),
        calc_data.get('local_hiring_score'),
        calc_data.get('wage_equity_score'),
        calc_data.get('unemployment_rate'),
        calc_data.get('median_income'),
        calc_data.get('avg_wage'),
        calc_data.get('employee_count')
    ))
    
    conn.commit()
    conn.close()

def get_all_stores():
    """Get all stores from database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores ORDER BY ejv_score DESC')
    stores = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return stores

def get_store_by_id(store_id):
    """Get store by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores WHERE store_id = ?', (store_id,))
    store = cursor.fetchone()
    conn.close()
    return dict(store) if store else None

def delete_store(store_id):
    """Delete store and its calculations"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ejv_calculations WHERE store_id = ?', (store_id,))
    cursor.execute('DELETE FROM stores WHERE store_id = ?', (store_id,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_database()
