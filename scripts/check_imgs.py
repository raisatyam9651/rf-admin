import re, glob

villas = ['retro-viswa-lonavala.php', 'neo-retro.php', 'retro-villas.php', 'index.php']
for v in villas:
    print(f"***** {v} *****")
    with open(v, 'r', encoding='utf-8') as f:
        content = f.read()
    for tag in re.findall(r'<img[^>]+>', content):
        src_m = re.search(r'src="([^"]+)"', tag)
        alt_m = re.search(r'alt="([^"]+)"', tag)
        if src_m:
            src = src_m.group(1)
            alt = alt_m.group(1) if alt_m else "NO_ALT"
            if 'images/' in src:
                print(f"  {src} | {alt}")
