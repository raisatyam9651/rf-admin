import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_website_pages import build_native_page

# -------------------------------------------------------------
# CATEGORY 1: FAMILY HOMESTAYS (16 PAGES INCLUDING MUMBAI)
# -------------------------------------------------------------
family_locations = [
    ("mumbai", "Mumbai", "~85 km", "~90 mins", "via Expressway or Atal Setu", "images/v1773076226_27_ipqwdd.webp"),
    ("pune", "Pune", "~65 km", "~60 mins", "via Mumbai-Pune Expressway", "images/v1773076226_27_ipqwdd.webp"),
    ("navi-mumbai", "Navi Mumbai", "~70 km", "~60 mins", "via Kalamboli toll plaza", "images/v1773076226_27_ipqwdd.webp"),
    ("thane", "Thane", "~95 km", "~90 mins", "via Airoli - Shilphata bypass", "images/v1773076226_27_ipqwdd.webp"),
    ("panvel", "Panvel", "~55 km", "~50 mins", "direct Expressway access", "images/v1773076226_27_ipqwdd.webp"),
    ("kharghar", "Kharghar", "~65 km", "~55 mins", "via Sion-Panvel expressway", "images/v1773076226_27_ipqwdd.webp"),
    ("kalyan", "Kalyan", "~90 km", "~90 mins", "via Kalyan-Shil corridor", "images/v1773076226_27_ipqwdd.webp"),
    ("dombivli", "Dombivli", "~85 km", "~85 mins", "via Shilphata onto Expressway", "images/v1773076226_27_ipqwdd.webp"),
    ("airoli", "Airoli", "~85 km", "~75 mins", "via Thane-Belapur Expressway link", "images/v1773076226_27_ipqwdd.webp"),
    ("hinjewadi", "Hinjewadi", "~55 km", "~50 mins", "direct IT Park Expressway link", "images/v1773076226_27_ipqwdd.webp"),
    ("wakad", "Wakad", "~55 km", "~50 mins", "via Bhumkar Chowk to Expressway", "images/v1773076226_27_ipqwdd.webp"),
    ("baner", "Baner", "~60 km", "~55 mins", "smooth Expressway bypass run", "images/v1773076226_27_ipqwdd.webp"),
    ("kharadi", "Kharadi", "~80 km", "~80 mins", "via Pune Ring Road to Expressway", "images/v1773076226_27_ipqwdd.webp"),
    ("mumbai-airport", "Mumbai Airport", "~95 km", "~100 mins", "via Western Express Highway & Expressway", "images/v1773076226_27_ipqwdd.webp"),
    ("pune-airport", "Pune Airport", "~75 km", "~75 mins", "via Lohegaon ring corridor", "images/v1773076226_27_ipqwdd.webp"),
    ("navi-mumbai-airport", "Navi Mumbai Airport", "~60 km", "~55 mins", "via Panvel Expressway corridor", "images/v1773076226_27_ipqwdd.webp"),
]

for loc_key, loc_name, dist, time_str, route_info, hero_img in family_locations:
    slug = f"homestay-near-{loc_key}-for-family"
    title = f"Homestay Near {loc_name} for Family | Private Pool Villa Lonavala"
    description = f"Book the best homestay near {loc_name} for family vacations. Just {time_str} drive to Lonavala. 4BHK luxury private pool villa with senior-friendly rooms, kids lawn & fresh home food."
    keywords = f"homestay near {loc_name.lower()} for family, family homestay near {loc_name.lower()}, best homestay near {loc_name.lower()} for family, 4bhk homestay near {loc_name.lower()} for family, private pool villa for family {loc_name.lower()}"
    badge = f"Just {time_str} from {loc_name} • Multi-Generational Family Haven"
    h1_html = f"Homestay Near <span class='text-gold'>{loc_name}</span> for Family"
    lead_text = f"Escape city noise and treat your loved ones to an exclusive 4BHK private pool homestay in Lonavala, located just {time_str} from {loc_name}. Senior-friendly ground-floor suites, clean private pool with kids' splash zone, expansive lawns, and warm home-cooked meals by a personal chef."
    
    stat_boxes = [
        (f"From {loc_name}", dist, time_str + " drive", "text-gold"),
        ("Family Capacity", "12 – 20 Pax", "4 En-Suite Bedrooms", "text-gold"),
        ("Kid & Senior Friendly", "Safe & Secure", "Ground floor suites & lawn", "text-white"),
        ("Culinary Service", "Veg & Jain", "Fresh home-cooked meals", "text-white")
    ]
    editorial_h2 = f"The Ideal Family Sanctuary Near {loc_name} in Lonavala"
    editorial_paragraphs = [
        f"Planning a multi-generational family holiday from {loc_name} with grandparents, parents, teenagers, and energetic toddlers often creates dilemmas. Standard commercial hotels separate family members into disconnected rooms, force everyone to adhere to strict restaurant buffet timings, and lack the privacy needed for true relaxation.",
        f"At <strong>Retrofusion Luxury Homestays</strong> in Lonavala, just {dist} ({time_str}) from {loc_name}, your family enjoys a private 4BHK estate entirely to yourselves. With zero shared areas, grandparents can relax peacefully on the garden veranda, children can swim safely in the private pool, and everyone gathers in the double-height living room for memorable evenings.",
        f"Our dedicated on-site chefs prepare customized, wholesome home-style meals — including strict Pure Jain, Pure Vegetarian, and kid-friendly mild food — tailored to your family's exact taste and schedule."
    ]
    editorial_cards = [
        ("Senior & Child Friendly", "Step-free ground-floor master bedrooms, anti-skid bathroom surfaces, and shallow pool ledges offer complete peace of mind for all generations."),
        ("Home-Cooked Culinary Care", "Delicious multi-course meals prepared fresh using premium local ingredients. Custom breakfast, evening high tea, and live poolside BBQ on demand.")
    ]
    faqs = [
        (f"How far is the homestay from {loc_name} and what is the best route?", f"Our villas are in Lonavala, roughly {dist} ({time_str} drive) from {loc_name} {route_info}. Access is smooth and direct with no steep mountain driving."),
        ("Is the homestay suitable for elderly family members and toddlers?", "Yes! Our villas feature spacious ground-floor bedrooms with step-free entrances, attached bathrooms, anti-skid pool decks, and fenced gardens safe for young kids and seniors."),
        ("Can we get home-cooked pure veg or Jain meals for the family?", "Yes! Our in-house chefs specialize in pure vegetarian, Jain, and non-vegetarian home-style Maharashtrian, North Indian, and continental dishes prepared fresh with separate cookware."),
        ("How many family members can sleep comfortably in this 4BHK homestay?", "A 4BHK villa comfortably accommodates 12 to 20 family members with plush king beds, luxury extra rollaway mattresses, and spacious living spaces.")
    ]
    related_links = [
        ("/4bhk-villa-near-mumbai-for-family", "4BHK Villa Near Mumbai for Family"),
        ("/best-4bhk-homestay-in-lonavala-for-family", "Best 4BHK Homestay in Lonavala for Family"),
        ("/homestay-near-mumbai", "Homestay Near Mumbai"),
        ("/pet-friendly-homestay-near-mumbai", "Pet Friendly Homestay Near Mumbai")
    ]
    build_native_page(slug, title, description, keywords, badge, h1_html, lead_text, hero_img, stat_boxes, editorial_h2, editorial_paragraphs, editorial_cards, faqs, related_links)

print("Completed Category 1 (Family Homestays)!")

# -------------------------------------------------------------
# CATEGORY 2: TEAM OUTING HOMESTAYS (8 PAGES)
# -------------------------------------------------------------
team_locations = [
    ("mumbai", "Mumbai", "~85 km", "~90 mins", "via Expressway", "images/office_team_building_villa_mumbai.webp"),
    ("pune", "Pune", "~65 km", "~60 mins", "via Mumbai-Pune Expressway", "images/office_team_building_villa_mumbai.webp"),
    ("navi-mumbai", "Navi Mumbai", "~70 km", "~60 mins", "via Kalamboli toll plaza", "images/office_team_building_villa_mumbai.webp"),
    ("thane", "Thane", "~95 km", "~90 mins", "via Airoli - Shilphata bypass", "images/office_team_building_villa_mumbai.webp"),
    ("panvel", "Panvel", "~55 km", "~50 mins", "direct Expressway access", "images/office_team_building_villa_mumbai.webp"),
    ("kharghar", "Kharghar", "~65 km", "~55 mins", "via Sion-Panvel corridor", "images/office_team_building_villa_mumbai.webp"),
    ("hinjewadi", "Hinjewadi", "~55 km", "~50 mins", "direct IT Park bypass link", "images/office_team_building_villa_mumbai.webp"),
    ("kharadi", "Kharadi", "~80 km", "~80 mins", "via Pune Ring Road to Expressway", "images/office_team_building_villa_mumbai.webp"),
]

for loc_key, loc_name, dist, time_str, route_info, hero_img in team_locations:
    slug = f"homestay-near-{loc_key}-for-team-outing"
    title = f"Best Homestay Near {loc_name} for Team Outing | Corporate Retreat Villas"
    description = f"Host an unforgettable team outing near {loc_name} at Retrofusion Lonavala. 4BHK private pool estate, lawn team building, poolside BBQ, 300 Mbps Wi-Fi & GST invoice billing."
    keywords = f"homestay near {loc_name.lower()} for team outing, team outing places near {loc_name.lower()}, corporate offsite villa {loc_name.lower()}, team building homestay lonavala, private pool villa for team outing {loc_name.lower()}"
    badge = f"Just {time_str} from {loc_name} • Executive Team Outing & Offsite"
    h1_html = f"Homestay Near <span class='text-gold'>{loc_name}</span> for Team Outing"
    lead_text = f"Energize your team away from office cubicles and boring hotel conference halls. Book an exclusive 4BHK private pool homestay in Lonavala just {time_str} from {loc_name}. Complete privacy, lawn games, high-speed Wi-Fi, poolside live BBQ, and GST corporate billing."
    
    stat_boxes = [
        (f"From {loc_name}", dist, time_str + " drive", "text-gold"),
        ("Team Capacity", "15 – 25 Pax", "Full Estate Exclusivity", "text-gold"),
        ("Work & Brainstorm", "300 Mbps Wi-Fi", "Smart TV & Lounges", "text-white"),
        ("Corporate Billing", "GST Compliant", "Official Invoicing", "text-white")
    ]
    editorial_h2 = f"Why Companies Choose Retrofusion for Team Outings Near {loc_name}"
    editorial_paragraphs = [
        f"Whether celebrating quarterly milestones, welcoming new team members, or conducting leadership strategy offsites, teams from {loc_name} need an inspiring space where work and recreation blend effortlessly.",
        f"At <strong>Retrofusion Luxury Homestays</strong>, your team gets 100% exclusive access to a 4BHK estate with a private swimming pool, snooker table, manicured lawn for team building games, and spacious air-conditioned lounges for presentations.",
        f"Our in-house chef prepares freshly cooked corporate buffets, high tea, and evening live poolside BBQs, ensuring your colleagues stay refreshed and engaged throughout the retreat."
    ]
    editorial_cards = [
        ("Team Building & Recreation", "Expansive private lawn for outdoor team activities, pool volleyball, tournament carrom, and snooker table for evening relaxation."),
        ("Corporate Catering & Invoicing", "Tailored breakfast, lunch, and dinner buffets. Full GST invoice provided for hassle-free corporate tax claims and company expense reimbursements.")
    ]
    faqs = [
        (f"How long does it take to travel from {loc_name} to the homestay?", f"The travel time is approximately {time_str} ({dist}) {route_info} directly to our gates in Lonavala."),
        ("Can we get official GST invoices for company expense reimbursement?", "Yes, we provide official GST tax invoices for company bookings, corporate retreats, and offsites."),
        ("What team building activities can be conducted at the villa?", "Our large private lawns are perfect for outdoor games like cricket, badminton, and tug-of-war. Indoors, teams enjoy snooker, carrom, and board games."),
        ("Is there high-speed internet for presentations or remote work?", "Yes, all villas have blazing-fast 300 Mbps fiber internet with seamless coverage across rooms, living lounges, and garden sit-outs.")
    ]
    related_links = [
        (f"/4bhk-villa-near-{loc_key}-for-team-outing" if loc_key in ['mumbai', 'pune'] else "/homestay-near-mumbai-for-team-outing", f"4BHK Villa for Team Outing"),
        ("/homestay-near-mumbai-for-office-outing", "Homestay Near Mumbai for Office Outing"),
        ("/4bhk-villa-near-mumbai-for-corporate-party", "4BHK Villa for Corporate Party"),
        ("/homestay-near-mumbai", "Homestay Near Mumbai")
    ]
    build_native_page(slug, title, description, keywords, badge, h1_html, lead_text, hero_img, stat_boxes, editorial_h2, editorial_paragraphs, editorial_cards, faqs, related_links)

print("Completed Category 2 (Team Outing Homestays)!")

# -------------------------------------------------------------
# CATEGORY 3: WORKATION WITH WIFI (6 PAGES)
# -------------------------------------------------------------
workation_pages = [
    ("homestay-in-lonavala-with-wifi-for-workation", "Homestay in Lonavala with WiFi for Workation", "Lonavala", "images/v1773566229_for_neo_and_viswa_laptop_s58iv5.webp", "~90 mins from Mumbai & 60 mins from Pune"),
    ("homestay-near-mumbai-with-wifi-for-workation", "Homestay Near Mumbai with WiFi for Workation", "Mumbai", "images/v1773566229_for_neo_and_viswa_laptop_s58iv5.webp", "~85 km (approx. 90 mins via Expressway)"),
    ("homestay-near-pune-with-wifi-for-workation", "Homestay Near Pune with WiFi for Workation", "Pune", "images/v1773566229_for_neo_and_viswa_laptop_s58iv5.webp", "~65 km (approx. 60 mins via Expressway)"),
    ("4bhk-villa-near-mumbai-with-wifi-for-workation", "4BHK Villa Near Mumbai with WiFi for Workation", "Mumbai", "images/v1773566229_for_neo_and_viswa_laptop_s58iv5.webp", "~85 km (approx. 90 mins via Expressway)"),
    ("4bhk-villa-near-pune-with-wifi-for-workation", "4BHK Villa Near Pune with WiFi for Workation", "Pune", "images/v1773566229_for_neo_and_viswa_laptop_s58iv5.webp", "~65 km (approx. 60 mins via Expressway)"),
    ("private-pool-homestay-near-mumbai-with-wifi-for-workation", "Private Pool Homestay Near Mumbai with WiFi for Workation", "Mumbai", "images/v1773566229_for_neo_and_viswa_laptop_s58iv5.webp", "~85 km (approx. 90 mins via Expressway)"),
]

for slug, page_title, ref_city, hero_img, dist_text in workation_pages:
    title = f"{page_title} | 300 Mbps Fiber Internet & Private Pool"
    description = f"Work remotely surrounded by Lonavala hill views. 300 Mbps dual-band fiber WiFi, power backup, private pool, comfortable work desks & hot meals on demand."
    keywords = f"{slug.replace('-', ' ')}, workation villa lonavala, work from home villa near mumbai, homestay with wifi lonavala, remote work homestay near pune"
    badge = f"300 Mbps Fiber Wi-Fi • Scenic Hillside Workation in Lonavala"
    h1_html = f"{page_title.replace('with WiFi', 'with <span class=\"text-gold\">WiFi</span>')}"
    lead_text = f"Swap cramped home offices for breathtaking Western Ghats views. Enjoy seamless Zoom calls with 300 Mbps high-speed fiber internet, 100% power backup, quiet ergonomic workspaces, private swimming pool, and freshly prepared hot meals."
    
    stat_boxes = [
        ("Internet Speed", "300 Mbps", "Dual-Band Fiber Wi-Fi", "text-gold"),
        ("Power Security", "100% Backup", "Inverter & Generator", "text-gold"),
        ("Travel Time", dist_text.split('(')[-1].replace(')', '') if '(' in dist_text else dist_text, "Direct Expressway", "text-white"),
        ("Chef & Meals", "Fresh & Hot", "Tea/Coffee & Home Food", "text-white")
    ]
    editorial_h2 = f"The Ultimate Productive & Relaxing Workation Retreat in Lonavala"
    editorial_paragraphs = [
        f"Remote work doesn't mean staying trapped inside four walls in {ref_city}. At Retrofusion, we've designed our private pool villas for remote workers, startup founders, freelancers, and distributed tech teams who demand enterprise-grade connectivity alongside resort luxury.",
        "Take uninterrupted video conferences on high-speed 300 Mbps dual-band fiber internet backed by inverter and generator systems. Set up your laptop on scenic balconies, garden patios, or spacious air-conditioned work desks.",
        "When the workday ends, close your laptop and dive into your private swimming pool, relax with evening tea and pakodas on the lawn, or challenge colleagues to snooker and carrom."
    ]
    editorial_cards = [
        ("Zero Downtime Connectivity", "300 Mbps dual-band fiber network with extensive mesh coverage reaching garden verandas and poolside cabanas, plus full generator backup."),
        ("Work-Life Balance Perks", "Private swimming pool, snooker table, evening bonfire, and custom home-cooked breakfast, lunch, and dinner prepared fresh on your schedule.")
    ]
    faqs = [
        ("How fast and reliable is the internet at the villa?", "We provide high-speed 300 Mbps fiber Wi-Fi with dual-band routers providing full coverage across all bedrooms, living rooms, and garden terraces. Complete power backup ensures zero connection drops."),
        ("Is the environment quiet enough for professional video conference calls?", "Yes! Our estates are located in tranquil residential and nature-surrounded pockets of Lonavala, far from highway honking, making them ideal for high-stakes video meetings."),
        ("Can we book long-term or weekly workations with discounted rates?", "Yes, we offer attractive weekly and monthly workation tariffs with inclusive housekeeping, high-speed Wi-Fi, and custom meal subscriptions."),
        ("What are the dining options during work hours?", "Our resident caretaker and chef serve piping hot tea, coffee, breakfast, and wholesome home-cooked meals right on your schedule so you never have to worry about cooking.")
    ]
    related_links = [
        ("/homestay-in-lonavala-for-long-stay-workation", "Homestay in Lonavala for Long Stay Workation"),
        ("/villa-in-lonavala-for-remote-work", "Villa in Lonavala for Remote Work"),
        ("/work-from-villa-in-lonavala", "Work From Villa in Lonavala"),
        ("/homestay-near-mumbai", "Homestay Near Mumbai")
    ]
    build_native_page(slug, title, description, keywords, badge, h1_html, lead_text, hero_img, stat_boxes, editorial_h2, editorial_paragraphs, editorial_cards, faqs, related_links)

print("Completed Category 3 (Workation with Wifi)!")

# -------------------------------------------------------------
# CATEGORY 4: REUNION PARTY WITH PRIVATE POOL (5 PAGES)
# -------------------------------------------------------------
reunion_pages = [
    ("private-pool-homestay-in-lonavala-for-reunion-party", "Private Pool Homestay in Lonavala for Reunion Party", "Lonavala", "images/v1769862646_pool_ckwldd.webp", "Central hill location in Lonavala"),
    ("private-pool-homestay-near-mumbai-for-reunion-party", "Private Pool Homestay Near Mumbai for Reunion Party", "Mumbai", "images/v1769862646_pool_ckwldd.webp", "~85 km (approx. 90 mins via Expressway)"),
    ("private-pool-homestay-near-pune-for-reunion-party", "Private Pool Homestay Near Pune for Reunion Party", "Pune", "images/v1769862646_pool_ckwldd.webp", "~65 km (approx. 60 mins via Expressway)"),
    ("private-pool-4bhk-villa-near-mumbai-for-reunion-party", "Private Pool 4BHK Villa Near Mumbai for Reunion Party", "Mumbai", "images/v1769862646_pool_ckwldd.webp", "~85 km (approx. 90 mins via Expressway)"),
    ("private-pool-4bhk-villa-near-pune-for-reunion-party", "Private Pool 4BHK Villa Near Pune for Reunion Party", "Pune", "images/v1769862646_pool_ckwldd.webp", "~65 km (approx. 60 mins via Expressway)"),
]

for slug, page_title, ref_city, hero_img, dist_text in reunion_pages:
    title = f"{page_title} | 4BHK Luxury Pool Estate"
    description = f"Host an unforgettable reunion party at Retrofusion Lonavala. 100% private pool, spacious party lawn, live BBQ, bonfire, music sound system & luxury suites for 15-25 guests."
    keywords = f"{slug.replace('-', ' ')}, reunion party villa lonavala, private pool villa for reunion near mumbai, 4bhk party villa near pune, college reunion homestay lonavala"
    badge = f"100% Private Pool & Party Lawn • School, College & Family Reunions"
    h1_html = f"{page_title.replace('for Reunion Party', 'for <span class=\"text-gold\">Reunion Party</span>')}"
    lead_text = f"Reunite with old schoolmates, college buddies, or extended family in an exclusive 4BHK private estate in Lonavala. Complete privacy with a sparkling swimming pool, lawn for music and memories, live poolside BBQ, and four lavish en-suite master suites."
    
    stat_boxes = [
        ("Group Capacity", "15 – 25 Pax", "Spacious 4BHK Layout", "text-gold"),
        ("Private Pool", "100% Exclusive", "Crystal-Clear Water", "text-gold"),
        ("Reunion Features", "BBQ & Music", "Party Lawn & Bonfire", "text-white"),
        ("Accessibility", dist_text.split('(')[-1].replace(')', '') if '(' in dist_text else dist_text, "Smooth Highway Run", "text-white")
    ]
    editorial_h2 = "Celebrate Lifelong Friendships & Family Bonds in Complete Exclusivity"
    editorial_paragraphs = [
        "Reunion parties deserve a special venue where you can laugh loudly, reminisce over nostalgic stories, and celebrate late into the night without noise complaints from hotel receptionists or snooty neighbors.",
        "At Retrofusion's private pool estates in Lonavala, you get an entire 4-bedroom luxury villa reserved strictly for your group. Relax around the private pool with drinks, challenge friends to snooker and carrom tournaments, and gather around the evening lawn bonfire.",
        "Our in-house culinary crew prepares customized feast buffets — from sizzling live barbecue chicken and paneer tikkas to authentic biryanis and late-night snacks."
    ]
    editorial_cards = [
        ("All-Night Celebration Freedom", "No shared areas and complete gated estate privacy. Enjoy pool games, music, late-night chats, and nostalgic celebrations in total comfort."),
        ("Live Poolside BBQ & Bonfire", "Savor hot, smoky kebabs grilled fresh beside the illuminated swimming pool, followed by a cozy winter bonfire under the starlit Lonavala sky.")
    ]
    faqs = [
        ("Can we play music and celebrate beside the pool?", "Yes! We provide sound systems for your private gathering. You can celebrate and enjoy music within reasonable community guidelines."),
        ("How many guests can stay together for a reunion?", "Our 4BHK villas comfortably accommodate 15 to 25 guests with plush king beds, high-quality extra bedding, and 4 spacious bathrooms."),
        ("Can you arrange custom cakes, decorations, or live BBQ?", "Yes! Our team can arrange festive party decorations, balloon arches, custom reunion cakes, and live poolside barbecue setups on advance request."),
        ("What indoor entertainment is available if it rains?", "We offer an indoor snooker/pool table, full-size carrom, classic board games, and 4K Smart TVs with streaming subscriptions.")
    ]
    related_links = [
        ("/4bhk-villa-in-lonavala-for-reunion-party", "4BHK Villa in Lonavala for Reunion Party"),
        ("/4bhk-villa-near-mumbai-for-reunion-party", "4BHK Villa Near Mumbai for Reunion Party"),
        ("/4bhk-villa-near-pune-for-reunion-party", "4BHK Villa Near Pune for Reunion Party"),
        ("/homestay-near-mumbai", "Homestay Near Mumbai")
    ]
    build_native_page(slug, title, description, keywords, badge, h1_html, lead_text, hero_img, stat_boxes, editorial_h2, editorial_paragraphs, editorial_cards, faqs, related_links)

print("Completed Category 4 (Reunion Party with Private Pool)!")

# -------------------------------------------------------------
# CATEGORY 5: CORPORATE / OFFICE / TEAM OUTING 4BHK VILLAS (6 PAGES)
# -------------------------------------------------------------
corporate_pages = [
    ("4bhk-villa-near-mumbai-for-corporate-party", "4BHK Villa Near Mumbai for Corporate Party", "Mumbai", "images/v1774810269_12_lo4gpx.webp", "~85 km (approx. 90 mins via Expressway)"),
    ("4bhk-villa-near-pune-for-corporate-party", "4BHK Villa Near Pune for Corporate Party", "Pune", "images/v1774810269_12_lo4gpx.webp", "~65 km (approx. 60 mins via Expressway)"),
    ("4bhk-villa-near-mumbai-for-office-outing", "4BHK Villa Near Mumbai for Office Outing", "Mumbai", "images/v1774810269_12_lo4gpx.webp", "~85 km (approx. 90 mins via Expressway)"),
    ("4bhk-villa-near-pune-for-office-outing", "4BHK Villa Near Pune for Office Outing", "Pune", "images/v1774810269_12_lo4gpx.webp", "~65 km (approx. 60 mins via Expressway)"),
    ("4bhk-villa-near-mumbai-for-team-outing", "4BHK Villa Near Mumbai for Team Outing", "Mumbai", "images/v1774810269_12_lo4gpx.webp", "~85 km (approx. 90 mins via Expressway)"),
    ("4bhk-villa-near-pune-for-team-outing", "4BHK Villa Near Pune for Team Outing", "Pune", "images/v1774810269_12_lo4gpx.webp", "~65 km (approx. 60 mins via Expressway)"),
]

for slug, page_title, ref_city, hero_img, dist_text in corporate_pages:
    title = f"{page_title} | Private Pool & BBQ Estate"
    description = f"Book an executive {page_title} in Lonavala. 4BHK luxury private pool estate, spacious presentation lounge, 300 Mbps Wi-Fi, chef-cooked buffet & GST billing."
    keywords = f"{slug.replace('-', ' ')}, corporate villa lonavala, office outing villa near mumbai, executive retreat villa pune, private pool villa for company offsite"
    badge = f"Executive 4BHK Private Pool Villa • Lonavala Offsites"
    h1_html = f"{page_title.replace('for ', 'for <span class=\"text-gold\">').replace('Party', 'Party</span>').replace('Outing', 'Outing</span>')}"
    if '</span>' not in h1_html:
        h1_html += "</span>"
    lead_text = f"Elevate your corporate culture with a private 4BHK hill estate in Lonavala just 60-90 minutes from {ref_city}. Complete executive exclusivity, private pool, presentation-ready air-conditioned lounge, high-speed Wi-Fi, and GST invoice billing."
    
    stat_boxes = [
        (f"From {ref_city}", dist_text.split('(')[0].strip(), dist_text.split('(')[-1].replace(')', ''), "text-gold"),
        ("Corporate Capacity", "15 – 25 Pax", "4 Master Suites + Hall", "text-gold"),
        ("Meeting Setup", "300 Mbps Wi-Fi", "Large 4K Display Lounge", "text-white"),
        ("Corporate Invoicing", "GST Invoices", "Tax Compliant Billing", "text-white")
    ]
    editorial_h2 = f"The Premier 4BHK Estate for Corporate Events Near {ref_city}"
    editorial_paragraphs = [
        f"High-performing teams require more than generic conference rooms in crowded hotels. An offsite at Retrofusion in Lonavala provides the ideal environment for executive strategy alignment, team bonding, and celebratory corporate gatherings.",
        "Our luxury 4BHK estates offer spacious double-height living rooms with comfortable seating and high-speed fiber internet for presentations, coupled with sprawling outdoor lawns for team activities and a private swimming pool for decompression.",
        "We take care of all corporate logistics — from customized meal buffets and live barbecue grilling to seamless GST tax invoices for company accounting."
    ]
    editorial_cards = [
        ("Executive Comfort & Privacy", "Full estate exclusivity ensures confidentiality for strategic corporate discussions, leadership meetings, and executive reviews."),
        ("Corporate Buffets & GST Billing", "Gourmet multi-cuisine breakfast, lunch, and dinner buffets. Official GST invoicing provided for smooth corporate expense processing.")
    ]
    faqs = [
        ("Can we get official GST invoices for our corporate booking?", "Yes, we issue formal GST tax invoices with your company's legal name and GSTIN for all corporate offsite bookings."),
        ("Are there presentation and meeting facilities available?", "Yes, our air-conditioned living lounges feature large 4K Smart TVs with HDMI/screen-mirroring and 300 Mbps Wi-Fi for presentations."),
        ("How many team members can stay at a 4BHK villa?", "A 4BHK villa accommodates 15 to 25 members with king beds, premium extra rollaway mattresses, and spacious en-suite bathrooms."),
        ("What meal arrangements are available for office groups?", "Our in-house chef prepares customized corporate buffets including morning tea/coffee, hot breakfast, business lunch, high tea with snacks, and evening poolside barbecue.")
    ]
    related_links = [
        ("/homestay-near-mumbai-for-office-outing", "Homestay Near Mumbai for Office Outing"),
        ("/homestay-near-pune-for-office-outing", "Homestay Near Pune for Office Outing"),
        ("/4bhk-villa-in-lonavala", "4BHK Villa in Lonavala"),
        ("/homestay-near-mumbai", "Homestay Near Mumbai")
    ]
    build_native_page(slug, title, description, keywords, badge, h1_html, lead_text, hero_img, stat_boxes, editorial_h2, editorial_paragraphs, editorial_cards, faqs, related_links)

print("Completed Category 5 (Corporate 4BHK Villas)!")
print("ALL 41 PAGES SUCCESSFULLY CREATED WITH NATIVE DARK LUXURY WEBSITE DESIGN!")
