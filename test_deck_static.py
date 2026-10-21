# -*- coding: utf-8 -*-
with open("Executive_D365_Copilot_Deck.html", "r", encoding="utf-8") as f:
    html = f.read()

for i in range(1, 11):
    tag = f'id="slide-{i}"'
    assert tag in html, f"Missing {tag}"
    print(f"Slide {i} present in HTML: True")

print("SUCCESS: All 10 slides are statically pre-rendered in HTML!")
