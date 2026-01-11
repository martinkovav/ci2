import re
from playwright.async_api import async_playwright, expect

BASE_URL = "http://localhost:8000"

async def test_homepage_loads():
    """Test that homepage loads successfully"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Navigate to homepage
        await page.goto(BASE_URL)
        # Check title
        await expect(page).to_have_title(re.compile(r'.*ChEMBL SMILES Lookup.*'))
        # Check main heading exists
        heading = page.locator("h1")
        await expect(heading).to_be_visible()
        await expect(heading).to_contain_text("ChEMBL SMILES Lookup")

async def test_search_form_exists():
    """Test that search form elements exist"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(BASE_URL)
        # Check form exists
        form = page.locator("#searchForm")
        await expect(form).to_be_visible()
        # Check input field exists
        input_field = page.locator("#smiles")
        await expect(input_field).to_be_visible()
        await expect(input_field).to_be_editable()
        # Check if the button with specific text exists
        button = page.locator("button:has-text('Search ChEMBL Database')")
        await expect(button).to_be_visible()
        await expect(button).to_be_enabled()

async def test_search_succinic_acid():
    """Test searching for succinic acid"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Navigate to homepage
        await page.goto(BASE_URL)
        # Fill in search form
        await page.fill("#smiles", "O=C(O)CCC(=O)O")
        # Click search button
        await page.locator("button:has-text('Search ChEMBL Database')").click()
        # Wait for results to appear
        # The loading indicator should appear first
        loading = page.get_by_text("Loading...")
        await expect(loading).to_be_visible()
        # Check result molecule name
        result_name = page.get_by_role("heading", name="SUCCINIC ACID")
        await expect(result_name).to_be_visible()
        #Check molecular formula
        molecular_formula = page.get_by_text("C4H6O4")
        await expect(molecular_formula).to_be_visible()
        # Check that molecule image loaded
        await expect(page.get_by_role("img", name="3D Molecule")).to_have_attribute("src", re.compile(".+"))

async def test_invalid_molecule_shows_error():
    """Test that invalid molecule name shows error"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        await page.goto(BASE_URL)
        # Search for nonexistent molecule
        await page.fill("#smiles", "ahoj")
        # Click search button
        await page.locator("button:has-text('Search ChEMBL Database')").click()
        # Browser will prevent form submission
        # Check that results don't appear
        error = page.get_by_text("No results found for the given SMILES.")
        await expect(error).to_be_visible()