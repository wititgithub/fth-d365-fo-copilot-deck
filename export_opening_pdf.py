import asyncio
import os
from playwright.async_api import async_playwright
from PIL import Image

HTML_PATH = r"c:\FTH\FTH-D365_FO\FTH_D365_Executive_Opening_Deck.html"
OUT_PDFS = [
    r"c:\FTH\FTH-D365_FO\FTH_D365_Executive_Opening_Deck.pdf",
    r"c:\FTH\FTH-D365_FO\assets\FTH_D365_Executive_Opening_Deck.pdf",
    r"C:\Users\witit\.gemini\antigravity\brain\7bc4ceac-b79a-4881-9938-a5db0d7782a2\FTH_D365_Executive_Opening_Deck.pdf",
]
SCRATCH_DIR = r"C:\Users\witit\.gemini\antigravity\brain\7bc4ceac-b79a-4881-9938-a5db0d7782a2\scratch\opening_pdf_pages"
os.makedirs(SCRATCH_DIR, exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1.5)
        file_url = "file:///" + HTML_PATH.replace("\\", "/")
        await page.goto(file_url, wait_until="networkidle")
        await page.wait_for_timeout(500)

        # Hide the script drawer during PDF screenshot capture so the slide content is fully visible
        await page.add_style_tag(content="#scriptDrawer { display: none !important; } .slide-enter { animation: none !important; }")

        page_images = []
        for idx in range(4):
            await page.evaluate(f"currentSlide = {idx}; renderSlide();")
            await page.wait_for_timeout(250)
            img_path = os.path.join(SCRATCH_DIR, f"opening_page_{idx+1:02d}.png")
            await page.screenshot(path=img_path, full_page=False)
            page_images.append(img_path)
            print(f"Captured Opening Slide {idx+1}/4 -> {img_path}")

        await browser.close()

    pil_imgs = [Image.open(p).convert("RGB") for p in page_images]
    for out_pdf in OUT_PDFS:
        os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
        pil_imgs[0].save(out_pdf, save_all=True, append_images=pil_imgs[1:], resolution=150.0, quality=92)
        print(f"Saved 4-page Opening PDF -> {out_pdf} ({os.path.getsize(out_pdf)//1024} KB)")

if __name__ == "__main__":
    asyncio.run(main())
