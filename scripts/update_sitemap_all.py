import os

slugs = [
    "homestay-near-mumbai-for-family",
    "homestay-near-pune-for-family",
    "homestay-near-navi-mumbai-for-family",
    "homestay-near-thane-for-family",
    "homestay-near-panvel-for-family",
    "homestay-near-kharghar-for-family",
    "homestay-near-kalyan-for-family",
    "homestay-near-dombivli-for-family",
    "homestay-near-airoli-for-family",
    "homestay-near-hinjewadi-for-family",
    "homestay-near-wakad-for-family",
    "homestay-near-baner-for-family",
    "homestay-near-kharadi-for-family",
    "homestay-near-mumbai-airport-for-family",
    "homestay-near-pune-airport-for-family",
    "homestay-near-navi-mumbai-airport-for-family",
    "homestay-near-mumbai-for-team-outing",
    "homestay-near-pune-for-team-outing",
    "homestay-near-navi-mumbai-for-team-outing",
    "homestay-near-thane-for-team-outing",
    "homestay-near-panvel-for-team-outing",
    "homestay-near-kharghar-for-team-outing",
    "homestay-near-hinjewadi-for-team-outing",
    "homestay-near-kharadi-for-team-outing",
    "homestay-in-lonavala-with-wifi-for-workation",
    "homestay-near-mumbai-with-wifi-for-workation",
    "homestay-near-pune-with-wifi-for-workation",
    "4bhk-villa-near-mumbai-with-wifi-for-workation",
    "4bhk-villa-near-pune-with-wifi-for-workation",
    "private-pool-homestay-near-mumbai-with-wifi-for-workation",
    "private-pool-homestay-in-lonavala-for-reunion-party",
    "private-pool-homestay-near-mumbai-for-reunion-party",
    "private-pool-homestay-near-pune-for-reunion-party",
    "private-pool-4bhk-villa-near-mumbai-for-reunion-party",
    "private-pool-4bhk-villa-near-pune-for-reunion-party",
    "4bhk-villa-near-mumbai-for-corporate-party",
    "4bhk-villa-near-pune-for-corporate-party",
    "4bhk-villa-near-mumbai-for-office-outing",
    "4bhk-villa-near-pune-for-office-outing",
    "4bhk-villa-near-mumbai-for-team-outing",
    "4bhk-villa-near-pune-for-team-outing"
]

with open("sitemap.xml", "r", encoding="utf-8") as f:
    content = f.read()

added_count = 0
entries_to_add = []

for slug in slugs:
    url = f"https://retrofusion.in/{slug}"
    if url not in content:
        entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-11-12</lastmod>
  </url>"""
        entries_to_add.append(entry)
        added_count += 1

if entries_to_add:
    # insert before </urlset>
    pos = content.rfind("</urlset>")
    if pos != -1:
        new_content = content[:pos] + "\n".join(entries_to_add) + "\n" + content[pos:]
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Added {added_count} new URLs to sitemap.xml!")
    else:
        print("ERROR: </urlset> tag not found in sitemap.xml")
else:
    print("All URLs already exist in sitemap.xml!")

