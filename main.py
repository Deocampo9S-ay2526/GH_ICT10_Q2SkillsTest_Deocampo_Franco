# Periodic Table Information Finder (non-metals)
from pyscript import display, document


nonmetal_list = {
    'H':  {'name': 'Hydrogen', 'number': 1, 'mass': 1.008},
    'HE': {'name': 'Helium', 'number': 2, 'mass': 4.0026},
    'C':  {'name': 'Carbon', 'number': 6, 'mass': 12.011},
    'N':  {'name': 'Nitrogen', 'number': 7, 'mass': 14.007},
    'O':  {'name': 'Oxygen', 'number': 8, 'mass': 15.999},
    'F':  {'name': 'Fluorine', 'number': 9, 'mass': 18.998},
    'NE': {'name': 'Neon', 'number': 10, 'mass': 20.180},
    'P':  {'name': 'Phosphorus', 'number': 15, 'mass': 30.974},
    'S':  {'name': 'Sulfur', 'number': 16, 'mass': 32.06},
    'CL': {'name': 'Chlorine', 'number': 17, 'mass': 35.45},
    'AR': {'name': 'Argon', 'number': 18, 'mass': 39.948},
    'SE': {'name': 'Selenium', 'number': 34, 'mass': 78.971},
    'BR': {'name': 'Bromine', 'number': 35, 'mass': 79.904},
    'KR': {'name': 'Krypton', 'number': 36, 'mass': 83.798},
    'I':  {'name': 'Iodine', 'number': 53, 'mass': 126.90},
    'XE': {'name': 'Xenon', 'number': 54, 'mass': 131.29},
    'RN': {'name': 'Radon', 'number': 86, 'mass': 222.02},
}


def nonmetal_elements(e):
    document.getElementById('input1').innerHTML = ""
    symbol = document.getElementById('input1').value.strip().upper()
    nonmetal_checked = symbol in nonmetal_list
    info = nonmetal_list.get(symbol, {'name': 'N/A', 'number': 'N/A', 'mass': 'N/A'})
    formatted_symbol = symbol.capitalize()
    found_element = (
        f"Symbol: {formatted_symbol}<br>"
        f"Element: {info['name']}<br>"
        f"Atomic Number: {info['number']}<br>"
        f"Atomic Mass: {info['mass']}"
    )
    
    notfound_element = f"The element symbol '{symbol}' is NOTTTTT on MY list...😬"
    response = (notfound_element, found_element)

    document.getElementById('output').innerHTML = response[nonmetal_checked]