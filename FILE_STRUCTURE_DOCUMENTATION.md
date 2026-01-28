# FIX$ Application - File Structure Documentation

Complete guide to every file in the FIX$ GeoEquity Impact Engine application.

---

## Core Application Files

### app.py
**Purpose**: Main Flask application server for local development
**Type**: Python Backend
**Key Features**:
- Contains all Flask route handlers and API endpoints
- Implements EJV calculation versions (v1, v2, v4.1, v4.2)
- Handles user authentication (login, logout, session management)
- Integrates with government data APIs (BLS, Census Bureau, BEA)
- Serves frontend HTML files
- Database initialization and connection management
- CORS configuration for frontend-backend communication
**Size**: Approximately 1750 lines
**Dependencies**: Flask, Flask-CORS, requests, Werkzeug
**Entry Point**: Can be run directly with `python app.py` or via run.py

### api/index.py
**Purpose**: Vercel serverless deployment version of the Flask application
**Type**: Python Backend
**Key Features**:
- Identical functionality to app.py but optimized for Vercel serverless environment
- All EJV calculation logic (v1, v2, v4.1, v4.2)
- API endpoints for economic justice calculations
- User authentication system
- Government data API integration
- Serverless-compatible database handling (in-memory for Vercel)
**Size**: Approximately 2166 lines
**Deployment**: Automatically deployed to Vercel at https://fix-app-three.vercel.app
**Note**: This is the production version used on Vercel

### database.py
**Purpose**: Database management and operations module
**Type**: Python Module
**Key Features**:
- SQLite database connection management
- User table creation and management
- Session table for authentication
- Dual-mode operation (file-based for local, in-memory for serverless)
- User CRUD operations (create, authenticate, update)
- Demo user initialization (username: admin, password: fix123)
- Automatic detection of serverless environment (Vercel/AWS Lambda)
**Size**: Approximately 181 lines
**Tables Created**:
  - users: Stores user accounts (username, email, password_hash, full_name)
  - sessions: Manages user login sessions (session_token, expires_at)

### run.py
**Purpose**: Development server launcher script
**Type**: Python Script
**Key Features**:
- Initializes database on startup
- Starts Flask development server on localhost:5000
- Enables debug mode for auto-reload on code changes
- Provides console output with access URLs and demo credentials
- Makes server accessible from network (host='0.0.0.0')
**Usage**: `python run.py`
**Console Output**: Shows server status, URLs, and demo credentials

---

## Frontend Files

### public/index.html
**Purpose**: Main application interface
**Type**: HTML/CSS/JavaScript Frontend
**Key Features**:
- Interactive map interface using Leaflet.js
- Store search and location functionality
- EJV score display and visualization
- Multi-version EJV support (v1, v2, v4.1, v4.2)
- Business type selection and filtering
- ZIP code-based economic analysis
- Color-coded score indicators (green/yellow/red)
- Real-time API communication with backend
- Responsive design for mobile and desktop
- User authentication UI
- Demo data loading functionality
**Technologies**: HTML5, CSS3, JavaScript (Vanilla), Leaflet.js for interactive maps
**API Endpoints Used**:
  - /api/ejv/v1/<store_id>
  - /api/ejv-v2/<store_id>
  - /api/ejv-v4.1/<store_id>
  - /api/ejv-v4.2/<store_id>
  - /api/user
  - /api/logout

### public/login-simple.html
**Purpose**: User authentication page
**Type**: HTML/CSS/JavaScript Frontend
**Key Features**:
- Clean, minimal login interface
- Username and password input fields
- Form validation
- Session token management
- Redirect to main app after successful login
- Error message display for failed authentication
- Demo credentials display for testing
**Demo Credentials**: username=admin, password=fix123
**Technologies**: HTML5, CSS3, JavaScript (Vanilla)
**API Endpoint Used**: /api/login

---

## Configuration Files

### vercel.json
**Purpose**: Vercel deployment configuration
**Type**: JSON Configuration
**Key Features**:
- Defines build configuration for Vercel platform
- Routes API requests to api/index.py (Python serverless function)
- Routes static files to public/ directory
- Maps root URL (/) to index.html
- Specifies Python runtime for backend
**Build Configuration**:
  - Backend: @vercel/python for api/index.py
  - Frontend: @vercel/static for public files
**Routes**:
  - /api/* → api/index.py (backend API)
  - / and /index.html → public/index.html (frontend)

### requirements.txt
**Purpose**: Python package dependencies
**Type**: Pip Requirements File
**Dependencies**:
  - Flask==3.0.0 (Web framework)
  - Flask-CORS==4.0.0 (Cross-Origin Resource Sharing)
  - requests==2.31.0 (HTTP library for API calls)
  - Werkzeug==3.0.1 (WSGI utilities, password hashing)
**Installation**: `pip install -r requirements.txt`

### .gitignore
**Purpose**: Git version control exclusion rules
**Type**: Git Configuration
**Excluded Files/Folders**:
  - .vercel/ (Vercel deployment cache)
  - .venv/ (Python virtual environment)
  - __pycache__/ (Python bytecode cache)
  - *.pyc (Compiled Python files)
  - .env (Environment variables)
  - fixapp.db (SQLite database file)
  - *.db (All database files)
  - Test files (test_auth.py, minimal_test.py, etc.)
  - Local environment files (.env*.local)
**Purpose**: Prevents sensitive data and build artifacts from being committed to Git

### .env.local
**Purpose**: Local environment variables (not tracked in Git)
**Type**: Environment Configuration
**Contains**: API keys, secrets, and local configuration
**Security**: Never committed to version control
**Usage**: Stores sensitive information like database credentials, API keys, etc.

---

## Utility Scripts

### START_SERVER.bat
**Purpose**: Windows batch script to start the development server
**Type**: Windows Batch File
**Key Features**:
- Changes to application directory
- Executes run.py to start Flask server
- Displays title "FIX$ Authentication Server"
- Shows server status messages
- Waits for user keypress on exit
**Usage**: Double-click to run on Windows, or execute from command line
**Platform**: Windows only

---

## Documentation Files

### README.md
**Purpose**: Project overview and quick start guide
**Type**: Markdown Documentation
**Expected Contents**:
  - Application description
  - Installation instructions
  - Setup guide
  - Usage examples
  - API documentation links
**Status**: Currently minimal (only contains update timestamp)

### EJV_COMPLETE_CALCULATION_GUIDE.md
**Purpose**: Comprehensive guide to all EJV calculation methodologies
**Type**: Markdown Documentation
**Key Features**:
- All 6 EJV versions documented (v1, v2, v3, v4, v4.1, v4.2)
- Mathematical formulas for each version
- Component breakdowns with scoring ranges
- Worked calculation examples
- Version comparison matrix
- Consolidated data sources section
- Government data source details (BLS, Census, BEA, FDIC)
- API access information and rate limits
- Data reliability metrics and update frequencies
- Citation formats for academic use
**Size**: 470+ lines
**Target Audience**: Researchers, policymakers, developers, and users

### EJV_V2_CALCULATION_GUIDE.md
**Purpose**: Detailed documentation for EJV v2 (Justice-Weighted Local Impact)
**Type**: Markdown Documentation
**Key Features**:
- Justice-weighted dollar-based metric calculation
- 9 dimension equity assessment
- ZIP code-level economic modifiers
- Formula: EJV v2 = (P × LC) × (JS_ZIP / 100)
- Data sources section (BLS OEWS, Census ACS, LAUS, QCEW)
- ZIP Need Modifier calculation methodology
- Example calculations with real data
- Data quality metrics and reliability percentages
**Focus**: Converts traditional scoring to dollar-based impact measurement

### EJV_V4.1_CALCULATION_GUIDE.md
**Purpose**: Documentation for EJV v4.1 (Decomposed Local Capture)
**Type**: Markdown Documentation
**Key Features**:
- Economic flow decomposition (5 components)
- ELVR (Economic Local Value Retained) calculation
- EVL (Economic Value Leakage) calculation
- Component-specific data sources:
  - LC_wages (35%): BLS OEWS + Census LODES
  - LC_suppliers (25%): BEA Regional Accounts
  - LC_taxes (15%): BEA Government Finances
  - LC_financing (15%): FDIC + NCUA data
  - LC_ownership (10%): Business registrations
- Business type defaults with reliability estimates
- Time-aware financing calculations
**Focus**: Shows where money flows (wages, suppliers, taxes, financing, ownership)

### EJV_V4.2_CALCULATION_GUIDE.md
**Purpose**: Documentation for EJV v4.2 (Participation Amplification)
**Type**: Markdown Documentation
**Key Features**:
- Participation Amplification Factor (PAF) methodology
- 5 participation pathways (mentoring, volunteering, sponsorship, apprenticeships, facilities)
- Verification process (Gold/Silver/Bronze standards)
- PAF calculation formula and examples
- Data sources for participation verification
- Integration with ENABLE workflow
- Human-in-the-loop verification protocols
- Privacy and data protection guidelines
**Focus**: Amplifies economic impact based on civic engagement (PAF range 1.0 - 1.25)

### EJV_ARCHITECTURE_REVISION.md
**Purpose**: Technical architecture and system design documentation
**Type**: Markdown Documentation
**Expected Contents**:
  - System architecture diagrams
  - Component relationships
  - Data flow documentation
  - Technical decisions and rationale
  - Version evolution and design changes

### LINKEDIN_POST.md
**Purpose**: Social media content for LinkedIn
**Type**: Markdown Content
**Contents**:
- Personal developer journey narrative
- Description of 4 AI-powered applications built:
  - CMMC AI Assistant (cybersecurity compliance)
  - Medical AI Assistant (healthcare diagnostics)
  - Urban AI Assistant (city planning)
  - FIX$ GeoEquity Impact Engine (economic justice)
- Lessons learned from AI-assisted development
- Tech stack description
- Professional networking content
**Target**: LinkedIn professional network

---

## Database Files

### fixapp.db
**Purpose**: SQLite database file (local development only)
**Type**: SQLite Database
**Location**: Root directory (auto-generated)
**Tables**:
  - users: User accounts and credentials
  - sessions: Active user sessions
**Size**: Variable (grows with usage)
**Backup**: Not tracked in Git (in .gitignore)
**Serverless Mode**: Not used on Vercel (uses in-memory database instead)

---

## Generated/Cache Directories

### __pycache__/
**Purpose**: Python bytecode cache directory
**Type**: Auto-generated folder
**Contents**: Compiled Python files (.pyc) for faster loading
**Location**: Multiple locations (root, api/, etc.)
**Management**: Auto-created by Python, excluded from Git

### .vercel/
**Purpose**: Vercel deployment cache and configuration
**Type**: Auto-generated folder
**Contents**: Deployment metadata, build cache, project configuration
**Management**: Created during `vercel deploy`, excluded from Git

### .git/
**Purpose**: Git version control repository data
**Type**: Git folder
**Contents**: Commit history, branches, remote configuration, staging area
**Management**: Created by `git init`, contains entire project history

---

## File Organization Summary

```
FIX$APP/
├── Core Backend
│   ├── app.py                              (Local development server)
│   ├── api/index.py                        (Production serverless backend)
│   └── database.py                         (Database operations)
│
├── Frontend
│   └── public/
│       ├── index.html                      (Main application UI)
│       └── login-simple.html               (Login page)
│
├── Configuration
│   ├── vercel.json                         (Vercel deployment config)
│   ├── requirements.txt                    (Python dependencies)
│   ├── .gitignore                          (Git exclusions)
│   └── .env.local                          (Local environment variables)
│
├── Scripts
│   ├── run.py                              (Development server launcher)
│   └── START_SERVER.bat                    (Windows batch launcher)
│
├── Documentation
│   ├── README.md                           (Project overview)
│   ├── EJV_COMPLETE_CALCULATION_GUIDE.md   (All EJV versions)
│   ├── EJV_V2_CALCULATION_GUIDE.md         (EJV v2 details)
│   ├── EJV_V4.1_CALCULATION_GUIDE.md       (EJV v4.1 details)
│   ├── EJV_V4.2_CALCULATION_GUIDE.md       (EJV v4.2 details)
│   ├── EJV_ARCHITECTURE_REVISION.md        (System architecture)
│   ├── LINKEDIN_POST.md                    (Social media content)
│   └── FILE_STRUCTURE_DOCUMENTATION.md     (This file)
│
├── Database
│   └── fixapp.db                           (SQLite database - local only)
│
└── Generated/Cache
    ├── __pycache__/                        (Python bytecode cache)
    ├── .vercel/                            (Vercel deployment cache)
    └── .git/                               (Git version control)
```

---

## Development Workflow

### Local Development
1. Install dependencies: `pip install -r requirements.txt`
2. Initialize database: Automatic via run.py
3. Start server: `python run.py` or double-click `START_SERVER.bat`
4. Access application: http://localhost:5000/login-simple.html
5. Demo login: username=admin, password=fix123

### Production Deployment (Vercel)
1. Push code to Git repository
2. Vercel automatically deploys api/index.py as serverless function
3. Static files from public/ served via Vercel CDN
4. In-memory database used (ephemeral)
5. Access at: https://fix-app-three.vercel.app

---

## Key Technologies Used

**Backend**:
- Python 3.x
- Flask 3.0.0 (Web framework)
- SQLite (Database)
- Werkzeug (Password hashing)
- Requests (HTTP client for government APIs)

**Frontend**:
- HTML5 / CSS3
- JavaScript (Vanilla - no frameworks)
- Leaflet.js (Open-source interactive mapping library)
- Fetch API (Backend communication)

**Deployment**:
- Vercel (Serverless hosting)
- GitHub (Version control)

**External APIs**:
- BLS OEWS (Bureau of Labor Statistics - Occupational Employment and Wage Statistics)
- Census ACS (American Community Survey)
- Census LODES (Longitudinal Employer-Household Dynamics)
- BEA (Bureau of Economic Analysis)
- FDIC/NCUA (Banking data)

---

## Security Considerations

**Password Storage**: 
- Werkzeug password hashing (PBKDF2 with SHA-256)
- Never stores plaintext passwords

**Session Management**:
- Secure session tokens generated with secrets module
- Session expiration tracking
- Token validation on each request

**Database Security**:
- SQLite with parameterized queries (prevents SQL injection)
- File-based for local (persistent)
- In-memory for serverless (ephemeral, more secure)

**CORS Configuration**:
- Flask-CORS enables cross-origin requests
- Necessary for frontend-backend communication

**Sensitive Data**:
- .env.local not tracked in Git
- API keys and secrets stored as environment variables
- .gitignore prevents accidental exposure

---

## Maintenance Notes

**Adding New EJV Versions**:
1. Add calculation function in app.py and api/index.py
2. Create new API endpoint route
3. Add frontend UI in index.html
4. Document methodology in new markdown file

**Updating Dependencies**:
1. Modify requirements.txt
2. Test locally: `pip install -r requirements.txt`
3. Deploy to Vercel (automatic dependency installation)

**Database Schema Changes**:
1. Modify database.py init_database_tables()
2. For local: Delete fixapp.db and restart (recreates)
3. For Vercel: Automatic (in-memory database)

**Frontend Changes**:
1. Edit public/index.html or login-simple.html
2. Test locally at localhost:5000
3. Push to Git for Vercel deployment

---

## File Size Summary

| File | Approximate Lines | Purpose |
|------|------------------|---------|
| app.py | 1,751 | Local backend server |
| api/index.py | 2,166 | Production serverless backend |
| database.py | 181 | Database operations |
| public/index.html | ~3,000+ | Main UI (large due to inline CSS/JS) |
| public/login-simple.html | ~200 | Login interface |
| EJV_COMPLETE_CALCULATION_GUIDE.md | 470+ | Comprehensive EJV documentation |
| EJV_V2_CALCULATION_GUIDE.md | ~500 | EJV v2 details |
| EJV_V4.1_CALCULATION_GUIDE.md | ~400 | EJV v4.1 details |
| EJV_V4.2_CALCULATION_GUIDE.md | ~600 | EJV v4.2 details |

**Total Application Size**: ~10,000+ lines of code and documentation

---

## Contact and Support

For questions about specific files or components, refer to:
- Calculation methodology: EJV_COMPLETE_CALCULATION_GUIDE.md
- API endpoints: app.py or api/index.py (route handlers)
- Frontend functionality: public/index.html
- Database operations: database.py

---

**Last Updated**: January 26, 2026
**Application Version**: FIX$ GeoEquity Impact Engine v4.2
**Documentation Version**: 1.0
