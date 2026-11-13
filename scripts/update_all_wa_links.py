import glob
import re
import urllib.parse

target_text = "Hi, I'm interested in your services. Please share images"
encoded_text = urllib.parse.quote(target_text)

php_files = glob.glob('*.php') + glob.glob('includes/*.php')
updated_files = []

for p in php_files:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Pattern for wa.me links
    def repl(m):
        full = m.group(0)
        url = m.group(1)
        # Parse URL
        if 'wa.me' in url or 'api.whatsapp.com' in url:
            # If it's wa.me/918999036644 or wa.me/919011016791 without text or with other text
            base = url.split('?')[0]
            new_url = f"{base}?text={encoded_text}"
            return f'href="{new_url}"'
        return full

    new_content = re.sub(r'href=["\'](https?://(?:wa\.me|api\.whatsapp\.com)[^"\']*)["\']', repl, content)
    if new_content != content:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_files.append(p)

print(f"Updated WhatsApp links in {len(updated_files)} files.")

