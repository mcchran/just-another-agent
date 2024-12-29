# that is the list of all cations available in the ai agent
from typing import Dict, Text, Any, List, Union, Optional

def get_response_time(url: Text) -> float:
    """Returns the basic latency for a given URL."""
    
    # let's hard code that for quick demo
    if url == "https://www.google.com":
        return 0.5
    if url == "https://www.facebook.com":
        return 1.0
    return 2.0