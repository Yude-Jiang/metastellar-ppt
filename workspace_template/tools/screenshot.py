"""Capture a full-viewport screenshot of a URL with Playwright/Chromium.

Usage: python tools/screenshot.py <url> <out.png> [width] [height] [wait_ms]
Use only ST-owned / public pages. Never use AI-generated images in ST decks.
"""
import sys
from playwright.sync_api import sync_playwright


def main():
    url = sys.argv[1]
    out = sys.argv[2]
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
    height = int(sys.argv[4]) if len(sys.argv) > 4 else 1000
    wait_ms = int(sys.argv[5]) if len(sys.argv) > 5 else 4000

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": width, "height": height},
                                device_scale_factor=2)
        page.goto(url, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(wait_ms)
        page.screenshot(path=out, full_page=False)
        browser.close()
    print("saved", out)


if __name__ == "__main__":
    main()
