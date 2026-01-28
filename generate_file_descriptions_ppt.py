"""
FIX$ Application - File Descriptions for PowerPoint Presentation
Generates concise 2-line descriptions for each file with key comparisons
"""

file_descriptions = {
    "CORE BACKEND FILES": [
        {
            "file": "app.py",
            "desc_line1": "Flask application server for local development with all API endpoints and calculation logic.",
            "desc_line2": "Runs on localhost:5000 when you execute 'python run.py' for testing on your computer."
        },
        {
            "file": "api/index.py",
            "desc_line1": "Production version of Flask app deployed on Vercel cloud platform as serverless function.",
            "desc_line2": "Same code as app.py but optimized for cloud deployment at https://fix-app-three.vercel.app"
        },
        {
            "file": "database.py",
            "desc_line1": "SQLite database manager handling user accounts, authentication, and session management.",
            "desc_line2": "Uses file-based storage locally (fixapp.db) and in-memory storage on Vercel for serverless compatibility."
        },
        {
            "file": "run.py",
            "desc_line1": "Development server launcher that initializes database and starts Flask app on localhost:5000.",
            "desc_line2": "Provides console messages with URLs, demo credentials, and enables debug mode for auto-reload."
        }
    ],
    
    "FRONTEND FILES": [
        {
            "file": "public/index.html",
            "desc_line1": "Main application interface with interactive map (Leaflet.js), store search, and EJV score visualization.",
            "desc_line2": "Communicates with backend APIs to display economic justice calculations and geographic analysis."
        },
        {
            "file": "public/login-simple.html",
            "desc_line1": "User authentication page with username/password input and session management.",
            "desc_line2": "Redirects to main app after successful login (demo: username=admin, password=fix123)."
        }
    ],
    
    "CONFIGURATION FILES": [
        {
            "file": "vercel.json",
            "desc_line1": "Deployment configuration for Vercel cloud platform specifying routes and build settings.",
            "desc_line2": "Routes API requests to index.py (Python serverless) and static files to public/ directory."
        },
        {
            "file": "requirements.txt",
            "desc_line1": "Python package dependencies list: Flask, Flask-CORS, requests, Werkzeug.",
            "desc_line2": "Install all dependencies with 'pip install -r requirements.txt' command."
        },
        {
            "file": ".gitignore",
            "desc_line1": "Specifies files/folders to exclude from Git version control (databases, cache, secrets).",
            "desc_line2": "Prevents sensitive data (.env files) and build artifacts (__pycache__) from being committed."
        },
        {
            "file": ".env.local",
            "desc_line1": "Local environment variables storing API keys, secrets, and configuration (not tracked in Git).",
            "desc_line2": "Keeps sensitive information secure and separate from source code."
        }
    ],
    
    "UTILITY SCRIPTS": [
        {
            "file": "START_SERVER.bat",
            "desc_line1": "Windows batch script that runs 'python run.py' to start the Flask development server.",
            "desc_line2": "Displays server status messages and waits for keypress on exit."
        }
    ],
    
    "DOCUMENTATION FILES": [
        {
            "file": "README.md",
            "desc_line1": "Project overview, installation instructions, and quick start guide.",
            "desc_line2": "First file users read to understand the application and get started."
        },
        {
            "file": "EJV_COMPLETE_CALCULATION_GUIDE.md",
            "desc_line1": "Comprehensive guide with all 6 EJV calculation versions, formulas, and worked examples (470+ lines).",
            "desc_line2": "Includes data sources (BLS, Census, BEA), API documentation, and academic citation formats."
        },
        {
            "file": "EJV_V2_CALCULATION_GUIDE.md",
            "desc_line1": "Detailed documentation for EJV v2: Justice-weighted dollar-based impact metric.",
            "desc_line2": "Explains 9-dimension equity assessment and ZIP code economic modifiers."
        },
        {
            "file": "EJV_V4.1_CALCULATION_GUIDE.md",
            "desc_line1": "Documentation for EJV v4.1: Decomposed local capture showing 5 economic flows.",
            "desc_line2": "Breaks down spending into wages, suppliers, taxes, financing, and ownership components."
        },
        {
            "file": "EJV_V4.2_CALCULATION_GUIDE.md",
            "desc_line1": "Documentation for EJV v4.2: Participation amplification based on civic engagement.",
            "desc_line2": "Explains PAF (1.0-1.25 range) calculation from mentoring, volunteering, and community activities."
        },
        {
            "file": "FILE_STRUCTURE_DOCUMENTATION.md",
            "desc_line1": "Complete guide explaining every file in the application with purpose and features.",
            "desc_line2": "Technical reference for developers understanding the codebase structure."
        },
        {
            "file": "LINKEDIN_POST.md",
            "desc_line1": "Social media content showcasing AI-powered development journey and applications built.",
            "desc_line2": "Highlights CMMC AI, Medical AI, Urban AI, and FIX$ apps with tech stack details."
        }
    ],
    
    "DATABASE FILES": [
        {
            "file": "fixapp.db",
            "desc_line1": "SQLite database file storing user accounts and sessions (local development only).",
            "desc_line2": "Auto-generated when running locally, excluded from Git, not used on Vercel (uses in-memory)."
        }
    ],
    
    "CACHE/GENERATED": [
        {
            "file": "__pycache__/",
            "desc_line1": "Python bytecode cache folder for faster loading of compiled .pyc files.",
            "desc_line2": "Auto-generated by Python, excluded from Git, safe to delete (regenerates automatically)."
        },
        {
            "file": ".vercel/",
            "desc_line1": "Vercel deployment cache and configuration folder created during 'vercel deploy' command.",
            "desc_line2": "Contains build artifacts and deployment metadata, excluded from Git version control."
        },
        {
            "file": ".git/",
            "desc_line1": "Git version control repository storing commit history, branches, and remote configuration.",
            "desc_line2": "Created by 'git init', manages all code changes and collaboration workflow."
        }
    ]
}

# Key comparisons for better understanding
comparisons = {
    "app.py vs api/index.py": {
        "app.py": "Local development - test on your computer (localhost:5000)",
        "api/index.py": "Production deployment - live on internet via Vercel cloud"
    },
    
    "Flask vs Vercel": {
        "Flask": "Python library that handles requests at API endpoints, runs functions, returns JSON",
        "Vercel": "Cloud hosting platform that deploys your code to internet as serverless application"
    },
    
    "Vercel vs Bluehost": {
        "Vercel": "Serverless (pay-per-use, auto-scaling, GitHub integration, modern apps)",
        "Bluehost": "Traditional hosting (always-on server, fixed resources, manual FTP upload, WordPress sites)"
    },
    
    "Local vs Serverless Database": {
        "Local (fixapp.db)": "File-based SQLite database stored on disk, persistent data",
        "Serverless (in-memory)": "Temporary database in RAM, resets on each deployment, ephemeral"
    },
    
    "Frontend vs Backend": {
        "Frontend (HTML/JS)": "What users see - interactive map, forms, buttons, visualization",
        "Backend (Python/Flask)": "What users don't see - calculations, database, API logic, data processing"
    },
    
    "Flask-CORS vs vercel.json": {
        "Flask-CORS": "Enables communication between frontend and backend (used everywhere)",
        "vercel.json": "Tells Vercel how to deploy and route your application (only for Vercel)"
    }
}

def print_for_powerpoint():
    """Print formatted output suitable for PowerPoint slides"""
    
    print("="*80)
    print("FIX$ APPLICATION FILE DESCRIPTIONS - POWERPOINT FORMAT")
    print("="*80)
    print()
    
    # Print file descriptions by category
    slide_number = 1
    for category, files in file_descriptions.items():
        print(f"\n{'='*80}")
        print(f"SLIDE {slide_number}: {category}")
        print(f"{'='*80}\n")
        
        for file_info in files:
            print(f"📄 {file_info['file']}")
            print(f"   • {file_info['desc_line1']}")
            print(f"   • {file_info['desc_line2']}")
            print()
        
        slide_number += 1
    
    # Print comparisons
    print(f"\n{'='*80}")
    print(f"SLIDE {slide_number}: KEY COMPARISONS FOR UNDERSTANDING")
    print(f"{'='*80}\n")
    
    for comparison_title, comparison_items in comparisons.items():
        print(f"🔄 {comparison_title}")
        for key, value in comparison_items.items():
            print(f"   {key}: {value}")
        print()

def generate_markdown_slides():
    """Generate markdown format for easy copy-paste"""
    
    output = []
    output.append("# FIX$ Application - File Descriptions\n")
    output.append("*PowerPoint Presentation Format*\n")
    output.append("---\n\n")
    
    slide_number = 1
    for category, files in file_descriptions.items():
        output.append(f"## Slide {slide_number}: {category}\n\n")
        
        for file_info in files:
            output.append(f"**{file_info['file']}**\n")
            output.append(f"- {file_info['desc_line1']}\n")
            output.append(f"- {file_info['desc_line2']}\n\n")
        
        output.append("---\n\n")
        slide_number += 1
    
    # Add comparisons slide
    output.append(f"## Slide {slide_number}: Key Comparisons\n\n")
    
    for comparison_title, comparison_items in comparisons.items():
        output.append(f"### {comparison_title}\n\n")
        output.append("| Aspect | Description |\n")
        output.append("|--------|-------------|\n")
        for key, value in comparison_items.items():
            output.append(f"| {key} | {value} |\n")
        output.append("\n")
    
    output.append("---\n\n")
    
    return ''.join(output)

def save_to_file():
    """Save descriptions to a text file"""
    
    with open('FILE_DESCRIPTIONS_FOR_PPT.txt', 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("FIX$ APPLICATION FILE DESCRIPTIONS - POWERPOINT FORMAT\n")
        f.write("="*80 + "\n\n")
        
        slide_number = 1
        for category, files in file_descriptions.items():
            f.write(f"\n{'='*80}\n")
            f.write(f"SLIDE {slide_number}: {category}\n")
            f.write(f"{'='*80}\n\n")
            
            for file_info in files:
                f.write(f"📄 {file_info['file']}\n")
                f.write(f"   • {file_info['desc_line1']}\n")
                f.write(f"   • {file_info['desc_line2']}\n\n")
            
            slide_number += 1
        
        # Add comparisons
        f.write(f"\n{'='*80}\n")
        f.write(f"SLIDE {slide_number}: KEY COMPARISONS FOR UNDERSTANDING\n")
        f.write(f"{'='*80}\n\n")
        
        for comparison_title, comparison_items in comparisons.items():
            f.write(f"🔄 {comparison_title}\n")
            for key, value in comparison_items.items():
                f.write(f"   {key}: {value}\n")
            f.write("\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write("END OF FILE DESCRIPTIONS\n")
        f.write("="*80 + "\n")
    
    print(f"✅ Saved to FILE_DESCRIPTIONS_FOR_PPT.txt")

    # Also save markdown version
    with open('FILE_DESCRIPTIONS_FOR_PPT.md', 'w', encoding='utf-8') as f:
        f.write(generate_markdown_slides())
    
    print(f"✅ Saved markdown version to FILE_DESCRIPTIONS_FOR_PPT.md")

if __name__ == "__main__":
    print("\n🎯 Generating file descriptions for PowerPoint presentation...\n")
    
    # Print to console
    print_for_powerpoint()
    
    # Save to files
    save_to_file()
    
    print("\n✅ Complete! Use the generated files for your presentation.")
    print("\n📌 Files created:")
    print("   • FILE_DESCRIPTIONS_FOR_PPT.txt (plain text)")
    print("   • FILE_DESCRIPTIONS_FOR_PPT.md (markdown format)")
    print("\n💡 Copy-paste into PowerPoint slides\n")
