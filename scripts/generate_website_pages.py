import os
import sys

# Define template generator matching the exact website structure of 4bhk-villa-near-mumbai-for-family.php

def build_native_page(
    slug,
    title,
    description,
    keywords,
    badge,
    h1_html,
    lead_text,
    hero_img,
    stat_boxes, # list of 4 (label, value, subtext)
    editorial_h2,
    editorial_paragraphs, # list of strings
    editorial_cards, # list of 2 (title, desc)
    faqs, # list of (q, a)
    related_links # list of (url, label)
):
    canonical_url = f"https://retrofusion.in/{slug}"
    
    # FAQ Schema
    faq_schema_items = ",\n".join([
        f"""        {{
          "@type": "Question",
          "name": "{q}",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "{a}"
          }}
        }}""" for q, a in faqs
    ])

    # Stat boxes
    stat_boxes_html = "\n".join([
        f"""            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">{lbl}</p>
                <p class="text-xl sm:text-2xl font-bold {col}">{val}</p>
                <p class="text-gray-400 text-xs mt-1">{sub}</p>
            </div>""" for lbl, val, sub, col in stat_boxes
    ])

    # Editorial paragraphs
    editorial_p_html = "\n".join([f"            <p>{p}</p>" for p in editorial_paragraphs])

    # Editorial cards
    editorial_cards_html = "\n".join([
        f"""                <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-gold font-serif text-lg font-semibold mb-2">{c_title}</h3>
                    <p class="text-sm text-gray-400">{c_desc}</p>
                </div>""" for c_title, c_desc in editorial_cards
    ])

    # FAQ accordion
    faq_accordion_html = "\n".join([
        f"""            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>{q}</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    {a}
                </p>
            </details>""" for q, a in faqs
    ])

    # Related links
    related_links_html = "\n".join([
        f"""      <a href="{url}" class="px-5 py-2.5 rounded-full bg-white/10 hover:bg-gold hover:text-black transition text-sm font-medium">{lbl}</a>"""
        for url, lbl in related_links
    ])

    content = f"""<?php
$pageTitle = "{title}";
$pageDescription = "{description}";
$pageKeywords = "{keywords}";
$pageRobots = "index, follow";
$canonicalUrl = "{canonical_url}";
$ogTitle = "{title}";
$ogDescription = "{description}";
$ogImage = "https://retrofusion.in/{hero_img}";

include 'includes/header.php';

$num1 = rand(1, 9);
$num2 = rand(1, 9);
$_SESSION['captcha_answer'] = $num1 + $num2;
?>

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "LodgingBusiness",
      "@id": "{canonical_url}#lodging",
      "name": "Retrofusion Luxury Homestays & Private Villas",
      "url": "{canonical_url}",
      "telephone": "+91 8999036644",
      "priceRange": "₹₹₹",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Old Mumbai Pune Highway, Near Karla Caves & Wax Museum",
        "addressLocality": "Lonavala",
        "addressRegion": "Maharashtra",
        "postalCode": "410401",
        "addressCountry": "IN"
      }},
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 18.7557,
        "longitude": 73.4091
      }},
      "description": "{description}"
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://retrofusion.in/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "{title.split('|')[0].strip()}",
          "item": "{canonical_url}"
        }}
      ]
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
{faq_schema_items}
      ]
    }}
  ]
}}
</script>

<!-- Hero Section -->
<section class="relative pt-32 pb-20 md:pt-40 md:pb-28 bg-luxury-black text-white overflow-hidden">
    <div class="absolute inset-0 z-0">
        <img src="{hero_img}" alt="{title.split('|')[0].strip()}" class="w-full h-full object-cover opacity-35 filter brightness-75 scale-105 transition-transform duration-1000">
        <div class="absolute inset-0 bg-gradient-to-t from-luxury-black via-luxury-black/70 to-transparent"></div>
    </div>
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 max-w-5xl text-center">
        <span class="inline-block px-4 py-1.5 rounded-full bg-gold/20 border border-gold/40 text-gold text-xs uppercase tracking-widest font-medium mb-4">
            {badge}
        </span>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-serif font-bold text-white mb-6 leading-tight">
            {h1_html}
        </h1>
        <p class="text-base sm:text-lg text-gray-300 max-w-3xl mx-auto mb-8 font-light leading-relaxed">
            {lead_text}
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="#inquiry-form" class="w-full sm:w-auto px-8 py-3.5 rounded-full bg-gold text-luxury-black font-semibold text-sm hover:bg-gold-light transition duration-300 shadow-lg shadow-gold/20">
                Check Availability & Rates
            </a>
            <a href="https://wa.me/918999036644?text=Hi%2C%20I%20am%20inquiring%20about%20villa%20availability%20for%20{slug}." target="_blank" class="w-full sm:w-auto px-8 py-3.5 rounded-full border border-white/30 text-white font-medium text-sm hover:bg-white/10 transition duration-300 flex items-center justify-center gap-2">
                <span>WhatsApp Concierge</span>
            </a>
        </div>
    </div>
</section>

<!-- Quick Facts / Stats Grid -->
<section class="py-12 bg-luxury-charcoal/40 border-y border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-5xl">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
{stat_boxes_html}
        </div>
    </div>
</section>

<!-- Editorial Section -->
<section class="py-20 bg-luxury-black text-gray-300">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl leading-relaxed">
        <div class="space-y-6">
            <h2 class="text-2xl sm:text-4xl font-serif font-bold text-white tracking-wide">
                {editorial_h2}
            </h2>
{editorial_p_html}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
{editorial_cards_html}
            </div>
        </div>
    </div>
</section>

<!-- Villa Showcase -->
<section class="py-20 bg-luxury-charcoal/20 border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-6xl">
        <div class="text-center mb-16">
            <span class="text-gold text-xs uppercase tracking-widest font-semibold">Handpicked Private Estates</span>
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Our Signature 4BHK Luxury Villas</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1773076226_27_ipqwdd.webp" alt="Retro Visawa Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Retro Visawa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Mountain-view infinity pool, indoor pool table, open garden, and spacious living areas.</p>
                    <a href="/retro-viswa-lonavala" class="text-gold text-sm font-semibold hover:underline">Explore Retro Visawa &rarr;</a>
                </div>
            </div>
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1774810269_12_lo4gpx.webp" alt="Neo Retro Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Neo Retro Villa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Modern contemporary architecture, private pool, lavish dining room, and luxury suites.</p>
                    <a href="/neo-retro" class="text-gold text-sm font-semibold hover:underline">Explore Neo Retro &rarr;</a>
                </div>
            </div>
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1769868155_M08_qewdva.webp" alt="Retro Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Retro Villa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Vintage warmth, sheltered garden, private pool, and traditional home-cooked cuisine.</p>
                    <a href="/retro-villas" class="text-gold text-sm font-semibold hover:underline">Explore Retro Villa &rarr;</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Accordion -->
<section class="py-20 bg-luxury-black border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl">
        <div class="text-center mb-12">
            <span class="text-gold text-xs uppercase tracking-widest font-semibold">Got Questions?</span>
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Frequently Asked Questions</h2>
        </div>
        <div class="space-y-4">
{faq_accordion_html}
        </div>
    </div>
</section>

<!-- Inquiry Form -->
<section id="inquiry-form" class="py-20 bg-luxury-charcoal/30 border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-3xl">
        <div class="bg-luxury-black p-8 sm:p-12 rounded-3xl border border-white/10 shadow-2xl">
            <div class="text-center mb-8">
                <span class="text-gold text-xs uppercase tracking-widest font-semibold">Reserve Your Private Stay</span>
                <h2 class="text-2xl sm:text-3xl font-serif font-bold text-white mt-2">Check Villa Availability</h2>
                <p class="text-gray-400 text-sm mt-2">Get direct villa rates, seasonal offers, and instant date confirmation.</p>
            </div>
            <form action="mail1.php" method="POST" class="space-y-5">
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Your Name *</label>
                        <input type="text" name="name" required class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                    </div>
                    <div>
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Phone Number *</label>
                        <input type="tel" name="phone" required class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Email Address *</label>
                        <input type="email" name="email" required class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                    </div>
                    <div>
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Number of Guests</label>
                        <input type="number" name="guests" min="1" placeholder="e.g. 15 Guests" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Check-In Date *</label>
                        <input type="date" name="checkIn" required class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                    </div>
                    <div>
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Check-Out Date *</label>
                        <input type="date" name="checkOut" required class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                    </div>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Select Preferred Villa</label>
                    <select name="villa" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                        <option value="Any Villa" class="bg-luxury-black">Any Available 4BHK Villa</option>
                        <option value="Retro Visawa" class="bg-luxury-black">Retro Visawa (Infinity Pool & Snooker)</option>
                        <option value="Neo Retro Villa" class="bg-luxury-black">Neo Retro Villa (Ultra Luxury)</option>
                        <option value="Retro Villa" class="bg-luxury-black">Retro Villa (Vintage Garden Retreat)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Special Requests / Notes</label>
                    <textarea name="message" rows="3" placeholder="Dietary preferences (Veg/Jain/Non-veg), event plans, or specific requirements..." class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition"></textarea>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Security Verification: <?php echo "$num1 + $num2 = ?"; ?> *</label>
                    <input type="number" name="captcha" required placeholder="Enter total" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                </div>
                <button type="submit" class="w-full py-4 rounded-xl bg-gold text-luxury-black font-bold uppercase tracking-wider text-sm hover:bg-gold-light transition duration-300 shadow-lg shadow-gold/20">
                    Send Booking Inquiry
                </button>
            </form>
        </div>
    </div>
</section>

<!-- ===== EXPLORE RELATED GETAWAYS ===== -->
<section class="py-12 bg-stone-900 border-t border-white/10 text-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <h3 class="text-xl font-bold font-display text-white mb-6">Explore More Curated Getaways</h3>
    <div class="flex flex-wrap justify-center gap-3">
{related_links_html}
    </div>
  </div>
</section>

<?php include 'includes/footer.php'; ?>
"""
    filename = f"{slug}.php"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filename}")

