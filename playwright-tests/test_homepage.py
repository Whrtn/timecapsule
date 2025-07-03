from playwright.sync_api import sync_playwright


def test_homepage_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/")
        assert "Time Capsule - Home" in page.title()
        browser.close()
