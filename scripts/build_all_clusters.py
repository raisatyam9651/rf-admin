import os
import sys
import subprocess

from page_components import (
    get_villa_section_html,
    get_estate_gallery_html,
    get_form_html,
    get_footer_scripts_and_modal
)

def create_page(
    filename,
    title,
    description,
    keywords,
    canonical_url,
    theme_bg,
    theme_accent,
    badge_text,
    h1_text,
    lead_text,
    hero_img,
    transit_title,
    transit_items,
    exp_heading,
    exp_sub,
    exp_items,
    pkg_heading,
    pkg_sub,
    pkg_items,
    seo_heading,
    seo_paragraphs,
    faqs,
    source_slug,
    is_corporate=True,
    villa_cluster_title="Our Featured Boutique Estates",
    villa_subtitle="Three homes. Three distinct moods. One unforgettable stay",
    trust_indicators=None
):
    if trust_indicators is None:
        trust_indicators = [
            ("100% Private", "Exclusive Pool & Entire Villa to Your Squad"),
            ("Gourmet Chef", "Custom Buffets, Snacks & Poolside Live BBQ"),
            ("Fast Highway", "Expressway Access into Lonavala Hills"),
            ("GST Invoicing", "Official Billing for Easy Reimbursements")
        ]
    # JSON-LD Schema
    faq_schema = ",\n".join([
        f"""        {{
          "@type": "Question",
          "name": "{q}",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "{a}"

          }}
        }}""" for q, a in faqs
    ])

    schema_markup = f"""<!-- JSON-LD Schema Markup -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "LodgingBusiness",
      "@id": "{canonical_url}#lodging",
      "name": "{title}",
      "description": "{description}",
      "url": "{canonical_url}",
      "image": [
        "https://retrofusion.in/{hero_img}",
        "https://retrofusion.in/images/v1770226533_N34_stewru.webp",
        "https://retrofusion.in/images/v1773076226_27_ipqwdd.webp"
      ],
      "telephone": "+91 8999036644",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Lonavala",
        "addressRegion": "Maharashtra",
        "postalCode": "410401",
        "addressCountry": "IN"
      }},
      "priceRange": "₹₹₹",
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": "18.7544",
        "longitude": "73.4062"
      }}
    }},
    {{
      "@type": "BreadcrumbList",
      "@id": "{canonical_url}#breadcrumb",
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
          "name": "{title}",
          "item": "{canonical_url}"
        }}
      ]
    }},
    {{
      "@type": "FAQPage",
      "@id": "{canonical_url}#faq",
      "mainEntity": [
{faq_schema}
      ]
    }}
  ]
}}
</script>"""

    # Transit boxes
    transit_boxes_html = "\n".join([
        f"""      <div class="p-5 rounded-2xl bg-white border border-stone-200 shadow-sm text-center">
        <h4 class="font-bold text-[#0F2A24] text-sm">{node}</h4>
        <div class="text-xl font-extrabold text-amber-600 my-1">{time_str}</div>
        <p class="text-xs text-stone-400">{desc}</p>
      </div>""" for node, time_str, desc in transit_items
    ])

    # Experiences
    exp_cards_html = ""
    for i, (tag, card_title, card_desc, bullets, img_src) in enumerate(exp_items):
        reverse = ' lg:order-2' if i % 2 == 1 else ''
        img_order = ' lg:order-1' if i % 2 == 1 else ''
        bullet_list = "\n".join([
            f"""          <li class="flex items-center text-stone-700 text-sm font-medium">
            <svg class="w-5 h-5 text-amber-500 mr-3 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
            {b}
          </li>""" for b in bullets
        ])
        exp_cards_html += f"""
    <!-- Experience {i+1} -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-center mb-20">
      <div{reverse}>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-100 text-amber-800 text-xs font-bold uppercase tracking-wider mb-4">
          {tag}
        </div>
        <h3 class="text-2xl sm:text-3xl font-bold text-[#0F2A24] font-display mb-4">
          {card_title}
        </h3>
        <p class="text-stone-600 text-base leading-relaxed mb-6">
          {card_desc}
        </p>
        <ul class="space-y-3">
{bullet_list}
        </ul>
      </div>
      <div{img_order}>
        <img loading="lazy" src="{img_src}" alt="{card_title}" class="w-full h-80 sm:h-96 object-cover rounded-3xl shadow-2xl border border-stone-200" />
      </div>
    </div>"""

    # Packages
    pkg_cards_html = ""
    for i, (opt, pkg_name, pkg_desc, features, is_featured) in enumerate(pkg_items):
        if is_featured:
            pkg_cards_html += f"""
      <!-- Package {i+1}: Featured -->
      <div class="bg-gradient-to-b from-[#0F2A24] to-stone-800 rounded-3xl p-8 border-2 border-amber-500 relative flex flex-col justify-between shadow-2xl">
        <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-amber-500 text-stone-950 font-extrabold text-xs uppercase tracking-widest px-4 py-1 rounded-full shadow">
          Most Popular
        </div>
        <div>
          <div class="text-xs uppercase tracking-widest text-amber-400 font-bold mb-2 mt-2">{opt}</div>
          <h3 class="text-2xl font-bold text-white font-display mb-3">{pkg_name}</h3>
          <p class="text-stone-300 text-sm mb-6">{pkg_desc}</p>
          <ul class="space-y-3 text-sm text-stone-200 mb-8">
""" + "\n".join([f'            <li class="flex items-center gap-2">✓ {f}</li>' for f in features]) + f"""
          </ul>
        </div>
        <a href="#corporate-quote" class="w-full py-3.5 bg-amber-500 hover:bg-amber-600 text-stone-950 font-bold rounded-xl text-center text-xs uppercase tracking-wider transition shadow-lg shadow-amber-500/20">
          Inquire This Package
        </a>
      </div>"""
        else:
            pkg_cards_html += f"""
      <!-- Package {i+1} -->
      <div class="bg-stone-800/80 rounded-3xl p-8 border border-white/10 hover:border-amber-500/50 transition-all flex flex-col justify-between">
        <div>
          <div class="text-xs uppercase tracking-widest text-stone-400 font-bold mb-2">{opt}</div>
          <h3 class="text-2xl font-bold text-white font-display mb-3">{pkg_name}</h3>
          <p class="text-stone-400 text-sm mb-6">{pkg_desc}</p>
          <ul class="space-y-3 text-sm text-stone-300 mb-8">
""" + "\n".join([f'            <li class="flex items-center gap-2">✓ {f}</li>' for f in features]) + f"""
          </ul>
        </div>
        <a href="#corporate-quote" class="w-full py-3.5 bg-white/10 hover:bg-amber-500 hover:text-stone-950 text-white font-bold rounded-xl text-center text-xs uppercase tracking-wider transition">
          Inquire This Option
        </a>
      </div>"""

    # SEO Paragraphs
    seo_content_html = "\n".join([f"    <p>{p}</p>" if not p.startswith("<h3>") else f"    {p}" for p in seo_paragraphs])

    # FAQs
    faq_items_html = ""
    for idx, (q, a) in enumerate(faqs):
        faq_items_html += f"""
      <!-- FAQ {idx+1} -->
      <div class="bg-white rounded-2xl border border-stone-200 overflow-hidden shadow-sm">
        <button class="w-full px-6 py-5 text-left flex justify-between items-center group" onclick="toggleFaq({idx})">
          <span class="font-bold text-[#0F2A24] text-base sm:text-lg font-display group-hover:text-amber-600 transition-colors">
            {q}
          </span>
          <svg id="faq-icon-{idx}" class="w-5 h-5 text-stone-400 transition-transform duration-300 shrink-0 ml-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
        </button>
        <div id="faq-ans-{idx}" class="hidden px-6 pb-6 text-stone-600 text-sm leading-relaxed">
          {a}
        </div>
      </div>"""

    villa_section = get_villa_section_html(villa_cluster_title, villa_subtitle)
    estate_gallery = get_estate_gallery_html(theme_bg)
    form_section = get_form_html(source_slug, title, is_corporate=is_corporate, theme_bg=theme_bg)
    footer_scripts = get_footer_scripts_and_modal()

    trust_boxes_html = "\n".join([
        f"""        <div class="bg-white/5 backdrop-blur-sm p-4 rounded-2xl border border-white/10">
          <div class="text-amber-400 font-bold text-xl md:text-2xl font-display">{t_title}</div>
          <div class="text-xs text-stone-300 font-medium">{t_sub}</div>
        </div>""" for t_title, t_sub in trust_indicators
    ])

    content = f"""<?php
$pageTitle = "{title}";
$pageDescription = "{description}";
$pageKeywords = "{keywords}";
$pageRobots = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1";
$pageAuthor = "Retrofusion Boutique Homestays";
$pagePublisher = "Retrofusion Boutique Homestays";
$canonicalUrl = "{canonical_url}";
$ogTitle = "{title}";
$ogImage = "https://retrofusion.in/{hero_img}";
include 'includes/header.php';
?>

{schema_markup}

<style>
  .glass-card {{
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.15);
  }}
  .highlight-gradient {{
    background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .corporate-pattern {{
    background-image: radial-gradient(rgba(245, 158, 11, 0.15) 1px, transparent 1px);
    background-size: 24px 24px;
  }}
  .btn-gold {{
    background: #f59e0b !important;
    color: #1c1917 !important;
    font-weight: 700 !important;
    box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.4) !important;
  }}
  .btn-gold:hover {{
    background: #d97706 !important;
  }}
  .badge-gold {{
    background: rgba(245, 158, 11, 0.15) !important;
    border: 1px solid rgba(245, 158, 11, 0.4) !important;
    color: #fbbf24 !important;
  }}
  .mobile-hero-padding {{
    padding-top: 170px !important;
  }}
  @media (min-width: 1024px) {{
    .desktop-hero-padding {{
      padding-top: 140px !important;
    }}
  }}
  .seo-article h2 {{ font-family: var(--font-display, serif); color: #0F2A24; font-size: 1.85rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.75rem; }}
  .seo-article h3 {{ font-family: var(--font-display, serif); color: #0F2A24; font-size: 1.35rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.5rem; }}
  .seo-article p {{ color: #44403c; line-height: 1.8; margin-bottom: 1rem; font-size: 1rem; }}
  .seo-article ul {{ list-style: disc; padding-left: 1.5rem; margin-bottom: 1.25rem; color: #44403c; }}
  .seo-article li {{ margin-bottom: 0.5rem; line-height: 1.6; }}
</style>

<!-- ===== HERO SECTION ===== -->
<section class="relative min-h-[90vh] flex items-center justify-center bg-[{theme_bg}] overflow-hidden mobile-hero-padding desktop-hero-padding pb-16 px-4 sm:px-6 lg:px-8">
  <div class="absolute inset-0 z-0">
    <img src="{hero_img}" alt="{title}" class="w-full h-full object-cover opacity-35 scale-105 transform transition duration-1000 ease-out" />
    <div class="absolute inset-0 bg-gradient-to-t from-[{theme_bg}] via-[{theme_bg}]/75 to-transparent"></div>
    <div class="absolute inset-0 bg-gradient-to-r from-[{theme_bg}]/90 via-transparent to-[{theme_bg}]/90"></div>
  </div>

  <div class="max-w-7xl mx-auto relative z-10 w-full">
    <div class="text-center max-w-4xl mx-auto">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full badge-gold text-xs sm:text-sm font-semibold uppercase tracking-widest mb-6">
        <span class="w-2.5 h-2.5 rounded-full bg-amber-400 animate-pulse"></span>
        {badge_text}
      </div>

      <h1 class="text-3xl sm:text-5xl md:text-6xl lg:text-7xl font-bold text-white mb-6 font-display leading-[1.12]">
        {h1_text}
      </h1>

      <p class="text-base sm:text-lg md:text-xl text-stone-200 font-light max-w-3xl mx-auto mb-10 leading-relaxed">
        {lead_text}
      </p>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 sm:gap-5 mb-14">
        <a href="#corporate-quote" class="w-full sm:w-auto px-8 py-4 btn-gold rounded-xl transition-all uppercase tracking-wider text-sm flex items-center justify-center gap-2 group">
          <span>Request Pricing & Availability</span>
          <svg class="w-4 h-4 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>

        <a href="https://wa.me/918999036644?text=Hi%20Retrofusion,%20I%20am%20inquiring%20about%20villa%20availability%20in%20Lonavala." target="_blank" class="w-full sm:w-auto px-8 py-4 glass-card hover:bg-white/15 text-white font-bold rounded-xl transition-all uppercase tracking-wider text-sm flex items-center justify-center gap-2 border border-white/20">
          <svg class="w-5 h-5 text-emerald-400" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.27 9.27 0 01-4.737-1.283l-.34-.202-3.523.923.94-3.435-.222-.353a9.268 9.268 0 01-1.423-4.87c0-5.118 4.162-9.28 9.282-9.28 2.481 0 4.814.966 6.566 2.719a9.23 9.23 0 012.714 6.56c0 5.118-4.163 9.28-9.283 9.28m8.209-17.487A10.74 10.74 0 0012.048 1.5c-5.94 0-10.775 4.835-10.778 10.776 0 1.9.488 3.754 1.414 5.418L1.133 22.4l4.825-1.265a10.73 10.73 0 005.087 1.298h.005c5.941 0 10.777-4.835 10.781-10.776a10.71 10.71 0 00-3.155-7.618z"/></svg>
          <span>Chat on WhatsApp</span>
        </a>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 pt-8 border-t border-white/10 text-left">
{trust_boxes_html}
      </div>
    </div>
  </div>
</section>

<!-- ===== LOCAL TRANSIT TIME GUIDE ===== -->
<section class="py-16 bg-stone-50 border-b border-stone-200">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-10">
      <span class="text-amber-600 font-bold uppercase tracking-widest text-xs">Seamless Highway Route</span>
      <h2 class="text-2xl sm:text-3xl font-bold text-[#0F2A24] font-display mt-2">
        {transit_title}
      </h2>
      <p class="text-stone-500 text-sm mt-2">Skip painful city gridlocks. Arrive effortlessly at our private gated estates.</p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
{transit_boxes_html}
    </div>
  </div>
</section>

<!-- ===== CURATED EXPERIENCES ===== -->
<section class="py-20 bg-white" id="experiences">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-16">
      <span class="text-amber-600 font-bold uppercase tracking-widest text-xs">Curated Highlights</span>
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold text-[#0F2A24] font-display mt-2 mb-4">
        {exp_heading}
      </h2>
      <p class="text-stone-600 text-base md:text-lg">
        {exp_sub}
      </p>
    </div>

{exp_cards_html}
  </div>
</section>

<!-- ===== PACKAGE OPTIONS ===== -->
<section class="py-20 bg-stone-900 text-white" id="packages">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-16">
      <span class="text-amber-400 font-bold uppercase tracking-widest text-xs">Tailored Itineraries</span>
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-bold font-display mt-2 mb-4">
        {pkg_heading}
      </h2>
      <p class="text-stone-400 text-base md:text-lg">
        {pkg_sub}
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
{pkg_cards_html}
    </div>
  </div>
</section>

{villa_section}

{estate_gallery}

{form_section}

<!-- ===== SEO CONTENT ARTICLE ===== -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 seo-article text-left">
    <h2>{seo_heading}</h2>
{seo_content_html}
  </div>
</section>

<!-- ===== FAQ SECTION ===== -->
<section class="py-16 bg-stone-50" id="faq">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-12">
      <span class="text-amber-600 font-bold uppercase tracking-widest text-xs">Common Questions</span>
      <h2 class="text-3xl sm:text-4xl font-bold text-[#0F2A24] font-display mt-2">
        Frequently Asked Questions
      </h2>
      <p class="text-stone-500 text-sm mt-2">Everything you need to know before locking in your stay.</p>
    </div>

    <div class="space-y-4">
{faq_items_html}
    </div>
  </div>
</section>

{footer_scripts}
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Generated: {filename}")
