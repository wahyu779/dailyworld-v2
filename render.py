#!/usr/bin/env python3
"""Render page.html to entry.png (1024x1024) with headless Chromium via Playwright.

Deterministic: fixed viewport, no network, local assets only.
Usage: python3 render.py  (writes entry.png next to this file)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(HERE, "page.html")
OUT = os.path.join(HERE, "entry.png")

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-gpu"])
    page = browser.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
    page.goto("file://" + PAGE)
    page.wait_for_timeout(400)
    page.screenshot(path=OUT)
    browser.close()

print("wrote " + OUT + " (" + str(os.path.getsize(OUT)) + " bytes)")
