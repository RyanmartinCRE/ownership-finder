# 🛠  stub: replace selectors later
import asyncio, json, playwright.async_api as pw

async def run(address: str) -> dict:
    async with pw.async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.asr.pima.gov/parcel-search")
        await page.fill("#address", address)
        await page.click("#search-btn")
        await page.wait_for_selector(".owner-name")
        entity = await page.inner_text(".owner-name")
        await browser.close()
    return {"entity_name": entity.strip()}
