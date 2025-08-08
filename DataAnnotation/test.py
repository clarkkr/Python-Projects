import requests
import pandas as pd
from bs4 import BeautifulSoup

def print_unicode_grid(url):
    # Step 1: Fetch HTML
    response = requests.get(url)
    # Check for client / not found errors
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step 2: Find the table and extract data
    table = soup.find("table")
    rows = []
    for tr in table.find_all("tr"):
        cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
        rows.append(cells)

    # Step 3: Load into DataFrame
    df = pd.DataFrame(rows[1:], columns=rows[0])  # skip header row
    df["x-coordinate"] = df["x-coordinate"].astype(int)
    df["y-coordinate"] = df["y-coordinate"].astype(int)

    # Step 4: Determine grid size
    max_x = df["x-coordinate"].max()
    max_y = df["y-coordinate"].max()
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Step 5: Place characters, flipping y-axis
    for _, row in df.iterrows():
        x = row["x-coordinate"]
        y = max_y - row["y-coordinate"]  # Flip y so 0,0 is bottom-left
        char = row["Character"]
        grid[y][x] = char

    # Step 6: Print grid
    for row in grid:
        print("".join(row))

# Example usage:
print_unicode_grid("https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub")
