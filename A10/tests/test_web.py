import re
import pytest
import asyncio
from playwright.sync_api import Page, Playwright, sync_playwright, expect
from playwright.async_api import async_playwright


def test_ahoj(page: Page) -> None:
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("http://localhost:8000/")
    page.get_by_role("textbox", name="Enter SMILES String:").click()
    page.get_by_role("textbox", name="Enter SMILES String:").fill("O=C(O)CCC(=O)O")
    page.get_by_role("button", name="Search ChEMBL Database").click()

    # ---------------------
    # context.close()
    # browser.close()

BASE_URL = "http://localhost:8000"

def test_homepage_loads(page: Page):
    """Test that homepage loads successfully"""
    # Navigate to homepage
    page.goto(BASE_URL)
    # Check title
    expect(page).to_have_title(re.compile(r'.*ChEMBL SMILES Lookup.*'))
    # Check main heading exists
    heading = page.locator("h1")
    expect(heading).to_be_visible()
    expect(heading).to_contain_text("ChEMBL SMILES Lookup")

def test_search_form_exists(page: Page):
    """Test that search form elements exist"""
    page.goto(BASE_URL)
    # Check form exists 
    form = page.locator("#searchForm")
    expect(form).to_be_visible()
    # Check input field exists
    input_field = page.locator("#smiles")
    expect(input_field).to_be_visible()
    expect(input_field).to_be_editable()
    # Check if the button with specific text exists
    button = page.locator("button:has-text('Search ChEMBL Database')")
    expect(button).to_be_visible()
    expect(button).to_be_enabled()

@pytest.mark.asyncio
async def test_search_succinic_acid(page: Page):
    """Test searching for succinic acid"""
    # Navigate to homepage
    await page.goto(BASE_URL)
    # Fill in search form
    await page.fill("#smiles", "O=C(O)CCC(=O)O")
    # Click search button
    await page.locator("button:has-text('Search ChEMBL Database')").click()
    # Wait for results to appear
    # The loading indicator should appear first
    loading = page.locator("p:has-text('Loading...')")
    await expect(loading).to_be_visible()
    # Check result molecule name
    result_name = page.get_by_role("heading", name="SUCCINIC ACID")
    await expect(result_name).to_be_visible()
    # Check that molecule image loaded
    await expect(page.get_by_role("img", name="3D Molecule")).to_be_visible()

# def test_search_aspirin_by_name(page: Page):
#     """Test searching for aspirin by name"""
#     # Navigate to homepage
#     page.goto(BASE_URL)
#     # Fill in search form
#     page.fill("#smiles", "O=C(O)CCC(=O)O")
#     # Click search button
#     page.locator("button:has-text('Search ChEMBL Database')").click()
#     # Wait for results to appear
#     # The loading indicator should appear first
#     loading = page.locator("p:has-text('Loading...')")
#     expect(loading).to_be_visible()
#     # Check result molecule name
#     expect(page.get_by_role("heading", name="SUCCINIC ACID")).to_be_visible()
#     # Check that molecule image loaded
#     expect(page.get_by_role("img", name="3D Molecule")).to_be_visible()
#     # molecule_img = page.get_by_role("img")
#     # expect(molecule_img).to_be_visible()
#     # expect(molecule_img).to_have_attribute("src")

# with sync_playwright() as playwright:
    # test_ahoj(playwright)
    # test_homepage_loads(playwright)
