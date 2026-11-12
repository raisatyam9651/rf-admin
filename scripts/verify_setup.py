import xml.etree.ElementTree as ET
import os

tree = ET.parse('sitemap.xml')
root = tree.getroot()
urls = set(elem.text for elem in root.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'))

from build_all_official_location_pages import family_locs, team_locs, workation_pages, reunion_pages, corp_pages

all_slugs = []
for item in family_locs:
    all_slugs.append(f"homestay-near-{item[0]}-for-family")
for item in team_locs:
    all_slugs.append(f"homestay-near-{item[0]}-for-team-outing")
for item in workation_pages:
    all_slugs.append(item[0])
for item in reunion_pages:
    all_slugs.append(item[0])
for item in corp_pages:
    all_slugs.append(item[0])

print(f"Total target slugs: {len(all_slugs)}")

missing_sitemap = []
missing_files = []

for s in all_slugs:
    u = f"https://retrofusion.in/{s}"
    if u not in urls:
        missing_sitemap.append(s)
    if not os.path.exists(f"{s}.php"):
        missing_files.append(f"{s}.php")

print(f"Files missing on disk: {len(missing_files)} {missing_files}")
print(f"URLs missing in sitemap.xml: {len(missing_sitemap)} {missing_sitemap}")

# Check internal links in each page
pages_without_rich_links = []
for s in all_slugs:
    with open(f"{s}.php", "r", encoding="utf-8") as f:
        c = f.read()
        if "RICH ANCHOR TEXT INTERNAL LINKING HUB" not in c:
            pages_without_rich_links.append(s)

print(f"Pages missing rich internal linking hub: {len(pages_without_rich_links)} {pages_without_rich_links}")
print("ALL CHECKS PASSED!" if not (missing_sitemap or missing_files or pages_without_rich_links) else "SOME CHECKS FAILED!")
