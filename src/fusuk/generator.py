# src/fusuk/generator.py
import random
import json
import pkgutil
from typing import Literal, Optional

# Load data ONCE at module import
def _load_local_data():
    """Load data from bundled package files."""
    
    # Load first names from JSON
    us_first_data = json.loads(pkgutil.get_data(__name__, "data/us_first_names.json"))
    uk_first_data = json.loads(pkgutil.get_data(__name__, "data/uk_first_names.json"))
    
    # Load last names from text files
    us_last_text = pkgutil.get_data(__name__, "data/us_last_names.txt").decode()
    uk_last_text = pkgutil.get_data(__name__, "data/uk_last_names.txt").decode()
    
    return {
        "us_first": us_first_data,
        "uk_first": uk_first_data,
        "us_last": [n.strip() for n in us_last_text.splitlines() if n.strip()],
        "uk_last": [n.strip() for n in uk_last_text.splitlines() if n.strip()],
    }

# Load data when module imports
_DATA = _load_local_data()

def getname(country="us", gender=None):
    """Fast version using local data."""
    # Use pre-loaded _DATA dictionary
    if country == "us":
        first_names = _DATA["us_first"]
        last_names = _DATA["us_last"]
    else:
        first_names = _DATA["uk_first"]
        last_names = _DATA["uk_last"]
    
    # Filter by gender
    if gender:
        first_names = [n for n in first_names if n.get("gender") == gender]
    
    if not first_names:
        gender = gender or "male"  # fallback
        return f"John {'Smith' if country == 'us' else 'Jones'}"
    
    # Pick random
    first = random.choice(first_names)["name"].title()
    last = random.choice(last_names).title()
    
    return f"{first} {last}"