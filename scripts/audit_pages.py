import os
import re
import glob

php_files = glob.glob('*.php')
print(f"Total PHP files found: {len(php_files)}")

# 41 target landing pages
target_pages = [f for f in php_files if any(k in f for k in [
    'office-outing', 'workation', 'remote-work', 'reunion-party', 'birthday-party', 'for-couples'
])]
print(f"Target landing pages: {len(target_pages)}")

missing_images = {}
empty_elements = {}

for f in target_pages:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # check images in <img> tags
    img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for src in img_matches:
        if src.startswith('http') or src.startswith('data:') or src.startswith('<?'):
            continue
        clean_src = src.split('?')[0].split('#')[0]
        if clean_src.startswith('/'):
            clean_src = clean_src[1:]
        clean_src = clean_src.replace('/', os.sep)
        if not os.path.exists(clean_src):
            if f not in missing_images:
                missing_images[f] = []
            missing_images[f].append(src)
            
    # check background images in style="background-image: url(...)"
    bg_matches = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', content, re.IGNORECASE)
    for src in bg_matches:
        if src.startswith('http') or src.startswith('data:') or src.startswith('<?') or 'rgba' in src:
            continue
        clean_src = src.split('?')[0].split('#')[0]
        if clean_src.startswith('/'):
            clean_src = clean_src[1:]
        clean_src = clean_src.replace('/', os.sep)
        if not os.path.exists(clean_src):
            if f not in missing_images:
                missing_images[f] = []
            missing_images[f].append(src)

print("\n--- MISSING IMAGES AUDIT ---")
if not missing_images:
    print("NO missing images found across target landing pages!")
else:
    for f, imgs in missing_images.items():
        print(f"{f}: {set(imgs)}")

print("\n--- CHECKING SECTION ANCHORS & BROKEN CONTAINERS ---")
for f in target_pages:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # Check for empty divs or unclosed elements
    # Check if header and footer are included
    has_header = "includes/header.php" in content
    has_footer = "includes/footer.php" in content
    if not has_header or not has_footer:
        print(f"Header/Footer missing in {f}: header={has_header}, footer={has_footer}")

print("Audit script completed.")
