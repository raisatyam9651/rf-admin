from PIL import Image
import os
import glob

heavy_files = [
    'images/v1769868140_B30_yc8rqu.webp',
    'images/v1769868140_C26_j6pstx.webp',
    'images/v1774807173_04_y636xz.webp',
    'images/v1769868155_M08_qewdva.webp',
    'images/v1769868144_M09_hilzeh.webp',
    'images/v1769868143_F18A_qmvadk.webp',
    'images/v1769868143_M01_jjmwdw.webp',
    'images/v1769868140_05_ivb2yz.webp',
    'images/v1769868141_E06_tevptf.webp',
    'images/v1769863040_05_sty1kz.webp',
    'images/v1769863054_12_myvknr.webp',
    'images/v1774810653_N35_h2djzp.webp',
    'images/v1769863054_03.1_c7vcel.webp',
    'images/v1769868141_I08_mjtxcg.webp',
    'images/v1769868142_H10_byp3oh.webp',
    'images/v1769868142_G31_mdlfjh.webp',
    'images/v1769868143_J24_wrncmb.webp',
    'images/v1769868144_M21_c2fjh0.webp',
    'images/v1769863051_07.1_u8yrn6.webp',
    'images/v1769863043_09_ufowaj.webp',
    'images/v1769863041_04_s8l8dy.webp',
    'images/v1770226534_N36_om6t9d.webp',
    'images/v1774807176_34_vpeqgv.webp'
]

total_old = 0
total_new = 0

for fp in heavy_files:
    if not os.path.exists(fp):
        continue
    old_size = os.path.getsize(fp) / 1024
    total_old += old_size
    im = Image.open(fp)
    w, h = im.size
    
    max_dim = max(w, h)
    if max_dim > 1920:
        ratio = 1920.0 / max_dim
        new_w = int(w * ratio)
        new_h = int(h * ratio)
        im = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Save optimized webp
    tmp_path = fp + ".tmp.webp"
    im.save(tmp_path, "WEBP", quality=82, method=6)
    new_size = os.path.getsize(tmp_path) / 1024
    
    if new_size < old_size:
        os.replace(tmp_path, fp)
        total_new += new_size
        print(f"Compressed {fp}: {old_size:.1f} KB -> {new_size:.1f} KB (-{((old_size-new_size)/old_size)*100:.1f}%)")
    else:
        os.remove(tmp_path)
        total_new += old_size
        print(f"Kept original {fp}: {old_size:.1f} KB")

print(f"\nTOTAL: {total_old:.1f} KB -> {total_new:.1f} KB (Saved {total_old - total_new:.1f} KB / {((total_old-total_new)/total_old)*100:.1f}%)")
