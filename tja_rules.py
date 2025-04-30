from typing import List, Optional

# Core mappings
LETTER_FUNCTIONS = {
    'A': 'Activate',
    'B': 'Balance',
    'C': 'Contain',
    'D': 'Direct',
    'E': 'Expand',
    'F': 'Focus',
    'G': 'Generate',
    'H': 'Harmonize',
    'I': 'Integrate',
    'J': 'Juxtapose',
    'K': 'Key',
    'L': 'Link',
    'M': 'Magnify',
    'N': 'Navigate',
    'O': 'Open',
    'P': 'Project',
    'Q': 'Query',
    'R': 'Relate',
    'S': 'Synthesize',
    'T': 'Transmit',
    'U': 'Unify',
    'V': 'Verify',
    'W': 'Weave',
    'X': 'Execute',
    'Y': 'Yield',
    'Z': 'Zero-in',
}

# Predefined symbolic opposites
PREDEFINED_OPPOSITES = {
    "AIT": "XYZ",
    "TJA": "ABC",
}

def get_letter_function(letter: str) -> Optional[str]:
    """Safely retrieves the function for a given letter."""
    return LETTER_FUNCTIONS.get(letter.upper())

def functional_scan(acronym: str) -> List[str]:
    """Returns a list of symbolic functions for each letter in the acronym."""
    return [get_letter_function(letter) for letter in acronym.upper() if get_letter_function(letter)]

def get_opposite(acronym: str) -> Optional[str]:
    """Retrieves the symbolic opposite of an acronym if predefined."""
    return PREDEFINED_OPPOSITES.get(acronym.upper())


if __name__ == "__main__":
    print(functional_scan("AIT"))    # ['Activate', 'Integrate', 'Transmit']
    print(get_opposite("ait"))      # XYZ
    print(get_opposite("TJA"))      # ABC