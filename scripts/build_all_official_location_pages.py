import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_official_location_page import create_official_location_page

# Icons
icon1 = '<svg class="w-10 h-10 text-amber-600 group-hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>'
icon2 = '<svg class="w-10 h-10 text-amber-600 group-hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>'
icon3 = '<svg class="w-10 h-10 text-amber-600 group-hover:text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" /></svg>'

# -------------------------------------------------------------
# CATEGORY 1: FAMILY HOMESTAYS (16 LOCATIONS)
# -------------------------------------------------------------
family_locs = [
    ("mumbai", "Mumbai", "~85 km", "~1.5 - 2 Hours", "Smooth connectivity via Mumbai-Pune Expressway & Atal Setu", "images/v1774807173_04_y636xz.webp"),
    ("pune", "Pune", "~65 km", "~1 - 1.25 Hours", "Direct signal-free Expressway drive ascending into the hills", "images/v1772868264_1_wqosmq.webp"),
    ("navi-mumbai", "Navi Mumbai", "~70 km", "~1 Hour", "Smooth highway access via Kalamboli toll plaza onto Expressway", "images/v1774807173_04_y636xz.webp"),
    ("thane", "Thane", "~95 km", "~1.5 Hours", "Convenient bypass via Airoli and Shilphata directly onto Expressway", "images/v1774807173_04_y636xz.webp"),
    ("panvel", "Panvel", "~55 km", "~50 Mins", "Fastest gateway access directly starting at the Expressway entry", "images/v1774807173_04_y636xz.webp"),
    ("kharghar", "Kharghar", "~65 km", "~1 Hour", "Straight drive past Central Park onto the Sion-Panvel expressway", "images/v1774807173_04_y636xz.webp"),
    ("kalyan", "Kalyan", "~90 km", "~1.5 Hours", "Connect via Kalyan-Shil road directly to the highway corridor", "images/v1774807173_04_y636xz.webp"),
    ("dombivli", "Dombivli", "~85 km", "~1.25 Hours", "Smooth transit through Shilphata onto the Mumbai-Pune Expressway", "images/v1774807173_04_y636xz.webp"),
    ("airoli", "Airoli", "~85 km", "~1.25 Hours", "Swift link along Thane-Belapur corridor straight into the expressway", "images/v1774807173_04_y636xz.webp"),
    ("hinjewadi", "Hinjewadi", "~55 km", "~50 Mins", "Direct bypass entry onto Expressway avoiding all Pune city traffic", "images/v1772868264_1_wqosmq.webp"),
    ("wakad", "Wakad", "~55 km", "~50 Mins", "Direct jump from Bhumkar Chowk straight onto the Expressway", "images/v1772868264_1_wqosmq.webp"),
    ("baner", "Baner", "~60 km", "~1 Hour", "Bypass urban gridlock instantly along the Mumbai-Bengaluru bypass", "images/v1772868264_1_wqosmq.webp"),
    ("kharadi", "Kharadi", "~80 km", "~1.25 Hours", "Fast commute via Pune Ring Road and Expressway bypass corridor", "images/v1772868264_1_wqosmq.webp"),
    ("mumbai-airport", "Mumbai Airport", "~95 km", "~1.75 Hours", "Via Western Express Highway onto Santa Cruz-Chembur Link & Expressway", "images/v1774807173_04_y636xz.webp"),
    ("pune-airport", "Pune Airport", "~75 km", "~1.25 Hours", "Via Lohegaon ring road directly reaching the Pune-Mumbai highway", "images/v1772868264_1_wqosmq.webp"),
    ("navi-mumbai-airport", "Navi Mumbai Airport", "~60 km", "~50 Mins", "Express highway corridor via Panvel onto the mountain exit", "images/v1774807173_04_y636xz.webp"),
]

for loc_key, loc_name, dist, time_str, route_info, hero_img in family_locs:
    slug = f"homestay-near-{loc_key}-for-family"
    title = f"Homestay Near {loc_name} for Family | Private Pool Villa Lonavala"
    description = f"Looking for the best homestay near {loc_name} for family? Escape the city chaos and book our massive 4BHK private pool villas in Lonavala just {time_str} away. Kid & senior friendly with private chef."
    keywords = f"homestay near {loc_name.lower()} for family, family homestay near {loc_name.lower()}, best homestay near {loc_name.lower()} for family, 4bhk homestay near {loc_name.lower()} for family, private pool villa for family {loc_name.lower()}"
    canonical_url = f"https://retrofusion.in/{slug}"
    
    hero_h1_line1 = f"Homestay Near {loc_name}"
    hero_h1_line2 = "for Family"
    hero_subtext = f"Escape the city chaos. Discover our massive 4BHK luxury pool estates waiting for your family just {time_str} away in Lonavala."
    hero_btn_text = "Explore Family Escapes"
    
    intro_h2 = f"The Ultimate <span class=\"text-amber-600\">Family Getaway Near {loc_name}</span>"
    intro_p = f"When the fast pace and traffic of {loc_name} get overwhelming, your family deserves an authentic hill sanctuary. Our <strong>homestay near {loc_name} for family</strong> offers the most refreshing escape without the fatigue of a long journey. By hopping onto the Expressway, you trade city concrete for the lush greenery, clean mountain air, and absolute seclusion of your own private 4BHK estate in Lonavala. Complete with senior-friendly ground floor bedrooms, a sparkling private swimming pool with shallow kids' lounge, and wholesome home-cooked meals by our in-house chef."
    
    intro_features = [
        (icon1, "Scenic Drive", f"Swap urban horns for breathtaking Western Ghats mountain views on an easy {time_str} drive."),
        (icon2, "Kid & Senior Safe", "Ground-floor suites with zero stairs, anti-skid bathrooms, and private fenced lawns where toddlers play freely."),
        (icon3, "100% Private Estate", "Zero shared areas. Unwind in completely gated luxury estates featuring massive private pools and dedicated care.")
    ]
    
    reach_dist = dist
    reach_time = time_str
    reach_intro = f"Transitioning from {loc_name} to the pristine air of the Western Ghats is wonderfully swift."
    reach_steps = [
        (f"Departing {loc_name}", f"Head out via the direct arterial route onto the highway corridor ({route_info})."),
        ("Cruising the Expressway", "Merge onto the Expressway for a completely signal-free, scenic drive ascending through the misty hills."),
        ("Direct Estate Arrival", "Take the main Lonavala/Karla exit. Because our villas are just 10-15 minutes from the toll, you bypass crowded bazaar traffic entirely.")
    ]
    
    gallery_h2 = f"Family Luxury <span class=\"text-amber-600\">Near {loc_name}</span>"
    gallery_subtext = "Preview the serene family escapes and private pool spaces waiting just a short drive away."
    
    seo_h2 = f"Why Choose Our Homestay Near {loc_name} for Your Family Vacation?"
    seo_content_paragraphs = [
        f"Planning a family gathering with grandparents, parents, teenagers, and little children from {loc_name} often means booking separate hotel rooms on different floors, fighting over buffet timings, and sharing public pools with strangers.",
        f"At <strong>Retrofusion Luxury Homestays</strong>, you get an entire 4BHK private estate dedicated solely to your family. Grandparents can enjoy peaceful mornings on the garden veranda, kids can splash happily in the clean private pool, and everyone can bond over authentic, piping hot home-style meals prepared with love by our caretakers.",
        f"<h3>Senior-Citizen and Toddler Friendly Living</h3>",
        "Our luxury villas feature step-free ground floor bedrooms, non-slip flooring, and expansive manicured gardens. Parents can relax knowing the private swimming pool is clean, hygienic, and includes a shallow ledge designed specifically for young kids.",
        f"<h3>Authentic Home Dining & Pure Jain Food</h3>",
        "Say goodbye to standardized hotel buffets. Our resident private chef prepares fresh, wholesome meals tailored to your family's preferences — including strict Pure Jain, Pure Vegetarian, and mild food for toddlers.",
        f"Book directly with Retrofusion to guarantee best rates, personalized concierge care, and an unforgettable retreat at the premier <strong>homestay near {loc_name} for family</strong> vacations."
    ]
    
    faqs = [
        (f"How far is the homestay from {loc_name} and how long is the drive?", f"The property is located in Lonavala, roughly {dist} ({time_str} drive) from {loc_name}. The drive is smooth and completely signal-free along the Expressway."),
        ("Is the homestay suitable for elderly family members and toddlers?", "Yes, absolutely! Our villas feature spacious ground-floor bedrooms with step-free entrances, attached bathrooms with anti-skid tiles, and fenced gardens safe for young kids and seniors."),
        ("Can we get home-cooked pure veg or Jain meals for the family?", "Yes! Our in-house chefs specialize in pure vegetarian, Jain, and non-vegetarian home-style dishes prepared fresh with separate cookware."),
        ("How many family members can stay in a 4BHK villa?", "A 4BHK villa comfortably accommodates 12 to 20 family members with plush king beds, luxury extra rollaway mattresses, and spacious living spaces.")
    ]
    
    booking_title = f"Reserve Your <span class=\"text-amber-600\">Family Villa</span>"
    booking_subtext = f"Ready to escape {loc_name} for a memorable family weekend? Fill out the form below to check availability."
    booking_hidden_val = f"Homestay Near {loc_name} for Family"
    
    create_official_location_page(slug, title, description, keywords, canonical_url, hero_img, hero_h1_line1, hero_h1_line2, hero_subtext, hero_btn_text, intro_h2, intro_p, intro_features, reach_dist, reach_time, reach_intro, reach_steps, gallery_h2, gallery_subtext, seo_h2, seo_content_paragraphs, faqs, booking_title, booking_subtext, booking_hidden_val)

print("Finished generating Category 1 (Family Homestays)!")

# -------------------------------------------------------------
# CATEGORY 2: TEAM OUTING HOMESTAYS (8 LOCATIONS)
# -------------------------------------------------------------
team_locs = [
    ("mumbai", "Mumbai", "~85 km", "~1.5 - 2 Hours", "via Mumbai-Pune Expressway"),
    ("pune", "Pune", "~65 km", "~1 - 1.25 Hours", "via Expressway bypass corridor"),
    ("navi-mumbai", "Navi Mumbai", "~70 km", "~1 Hour", "via Kalamboli toll plaza onto Expressway"),
    ("thane", "Thane", "~95 km", "~1.5 Hours", "via Airoli - Shilphata bypass"),
    ("panvel", "Panvel", "~55 km", "~50 Mins", "direct Expressway gateway"),
    ("kharghar", "Kharghar", "~65 km", "~1 Hour", "via Sion-Panvel expressway"),
    ("hinjewadi", "Hinjewadi", "~55 km", "~50 Mins", "direct IT Park Expressway link"),
    ("kharadi", "Kharadi", "~80 km", "~1.25 Hours", "via Pune Ring Road to Expressway"),
]

for loc_key, loc_name, dist, time_str, route_info in team_locs:
    slug = f"homestay-near-{loc_key}-for-team-outing"
    title = f"Homestay Near {loc_name} for Team Outing | Corporate Offsite Villas"
    description = f"Host an energetic team outing near {loc_name} at Retrofusion Lonavala. 4BHK private pool estate, lawn team building, poolside BBQ, 300 Mbps Wi-Fi & GST invoice billing."
    keywords = f"homestay near {loc_name.lower()} for team outing, team outing places near {loc_name.lower()}, corporate offsite villa {loc_name.lower()}, team building homestay lonavala, private pool villa for team outing {loc_name.lower()}"
    canonical_url = f"https://retrofusion.in/{slug}"
    hero_img = "images/v1774810269_12_lo4gpx.webp"
    
    hero_h1_line1 = f"Homestay Near {loc_name}"
    hero_h1_line2 = "for Team Outing"
    hero_subtext = f"Energize your team away from office cubicles. Claim complete luxury and productivity at our colossal private pool estates in Lonavala just {time_str} from {loc_name}."
    hero_btn_text = "Plan Team Outing"
    
    intro_h2 = f"The Ultimate <span class=\"text-amber-600\">Corporate Retreat Near {loc_name}</span>"
    intro_p = f"Trade dull conference halls for fresh mountain breezes. Reserving a <strong>homestay near {loc_name} for team outing</strong> gives your colleagues an exclusive private estate where team bonding, strategy sessions, and celebration flow seamlessly together. Featuring high-speed 300 Mbps Wi-Fi, sprawling private lawns for team building games, a private swimming pool, and delicious chef-curated buffets."
    
    intro_features = [
        (icon1, "Team Building Lawn", "Expansive manicured green lawns perfect for cricket, tug-of-war, and outdoor leadership activities."),
        (icon2, "Aquatic Rejuvenation", "100% exclusive private swimming pool for pool volleyball, relaxation, and poolside celebrations."),
        (icon3, "GST Compliant Billing", "Official GST corporate tax invoicing provided for smooth corporate expense reimbursements.")
    ]
    
    reach_dist = dist
    reach_time = time_str
    reach_intro = f"Getting your team from {loc_name} to our private estates in Lonavala is remarkably fast and easy."
    reach_steps = [
        (f"Departure from {loc_name}", f"Assemble your team and join the highway corridor ({route_info})."),
        ("Smooth Expressway Run", "Enjoy a scenic drive through the Western Ghats with panoramic mountain vistas."),
        ("Direct Toll Bypass", "Take the Lonavala exit to arrive directly at our private gates without town market bottlenecks.")
    ]
    
    gallery_h2 = f"Corporate Luxury <span class=\"text-amber-600\">Near {loc_name}</span>"
    gallery_subtext = "Preview our spacious lounges, meeting areas, and private pool estates."
    
    seo_h2 = f"Why Companies Near {loc_name} Choose Retrofusion for Team Outings"
    seo_content_paragraphs = [
        f"Whether celebrating quarterly targets, welcoming new team members, or conducting annual strategy offsites, teams from {loc_name} deserve a private retreat that balances recreation and professional comfort.",
        f"At <strong>Retrofusion</strong>, your group enjoys complete estate privacy with four massive air-conditioned bedrooms, presentation-ready living rooms with large 4K Smart TVs, and blazing 300 Mbps fiber internet for hybrid check-ins.",
        f"<h3>Poolside Live BBQ & Chef Curated Buffets</h3>",
        "Our on-site culinary team prepares hot breakfast, multi-cuisine lunch buffets, evening high tea with snacks, and lively poolside barbecue dinners.",
        f"<h3>Official GST Corporate Invoicing</h3>",
        "We support corporate finance requirements with formal GST tax invoicing for all bookings, meal plans, and customized event setups."
    ]
    
    faqs = [
        (f"How long does it take to travel from {loc_name}?", f"The journey takes roughly {time_str} ({dist}) {route_info} directly to our gates in Lonavala."),
        ("Can we get official GST invoices for our corporate booking?", "Yes! We issue formal GST tax invoices with your company's legal name and GSTIN for all corporate offsite bookings."),
        ("What team building activities can be conducted at the villa?", "Our large private lawns are perfect for outdoor games like cricket, badminton, and tug-of-war. Indoors, teams enjoy snooker, carrom, and board games."),
        ("Is there high-speed internet for presentations?", "Yes, all villas have blazing-fast 300 Mbps fiber internet with seamless coverage across all rooms, lounges, and lawns.")
    ]
    
    booking_title = f"Reserve Your <span class=\"text-amber-600\">Team Outing Estate</span>"
    booking_subtext = f"Plan an unforgettable offsite for your colleagues from {loc_name}. Fill out the form below for corporate quotes."
    booking_hidden_val = f"Homestay Near {loc_name} for Team Outing"
    
    create_official_location_page(slug, title, description, keywords, canonical_url, hero_img, hero_h1_line1, hero_h1_line2, hero_subtext, hero_btn_text, intro_h2, intro_p, intro_features, reach_dist, reach_time, reach_intro, reach_steps, gallery_h2, gallery_subtext, seo_h2, seo_content_paragraphs, faqs, booking_title, booking_subtext, booking_hidden_val)

print("Finished generating Category 2 (Team Outing Homestays)!")

# -------------------------------------------------------------
# CATEGORY 3: WORKATION WITH WIFI (6 PAGES)
# -------------------------------------------------------------
workation_pages = [
    ("homestay-in-lonavala-with-wifi-for-workation", "Homestay in Lonavala with WiFi for Workation", "Lonavala", "~90 mins from Mumbai & 60 mins from Pune", "Central hill location in Lonavala"),
    ("homestay-near-mumbai-with-wifi-for-workation", "Homestay Near Mumbai with WiFi for Workation", "Mumbai", "~85 km (approx. 1.5 - 2 Hours)", "via Mumbai-Pune Expressway"),
    ("homestay-near-pune-with-wifi-for-workation", "Homestay Near Pune with WiFi for Workation", "Pune", "~65 km (approx. 1 Hour)", "via Expressway bypass"),
    ("4bhk-villa-near-mumbai-with-wifi-for-workation", "4BHK Villa Near Mumbai with WiFi for Workation", "Mumbai", "~85 km (approx. 1.5 - 2 Hours)", "via Mumbai-Pune Expressway"),
    ("4bhk-villa-near-pune-with-wifi-for-workation", "4BHK Villa Near Pune with WiFi for Workation", "Pune", "~65 km (approx. 1 Hour)", "via Expressway bypass"),
    ("private-pool-homestay-near-mumbai-with-wifi-for-workation", "Private Pool Homestay Near Mumbai with WiFi for Workation", "Mumbai", "~85 km (approx. 1.5 - 2 Hours)", "via Mumbai-Pune Expressway"),
]

for slug, page_title, ref_city, dist_str, route_info in workation_pages:
    title = f"{page_title} | 300 Mbps Fiber Internet & Private Pool"
    description = f"Work remotely surrounded by Lonavala hill views. 300 Mbps dual-band fiber WiFi, 100% power backup, private pool, comfortable work desks & hot meals on demand."
    keywords = f"{slug.replace('-', ' ')}, workation villa lonavala, work from home villa near mumbai, homestay with wifi lonavala, remote work homestay near pune"
    canonical_url = f"https://retrofusion.in/{slug}"
    hero_img = "images/v1770226533_N34_stewru.webp"
    
    hero_h1_line1 = page_title.split(" with ")[0]
    hero_h1_line2 = "with WiFi for Workation"
    hero_subtext = "Swap cramped home offices for breathtaking hill views. Enjoy seamless Zoom calls on 300 Mbps fiber internet, 100% power backup, and private pool relaxation."
    hero_btn_text = "Book Your Workation"
    
    intro_h2 = "The Ultimate <span class=\"text-amber-600\">Productive Workation in Lonavala</span>"
    intro_p = f"Remote work shouldn't mean staying trapped inside an apartment in {ref_city}. Booking a <strong>{page_title.lower()}</strong> gives you the perfect fusion of enterprise-grade connectivity and serene resort living. Take uninterrupted video meetings on 300 Mbps dual-band fiber internet, work from garden verandas, and unwind with an evening swim in your private pool."
    
    intro_features = [
        (icon1, "300 Mbps Fiber Wi-Fi", "Dual-band high-speed mesh routers across all bedrooms, living rooms, and poolside decks."),
        (icon2, "100% Power Security", "Heavy-duty inverter and generator backup guaranteeing zero drops during critical meetings."),
        (icon3, "Hot Meals on Demand", "Fresh tea, coffee, breakfast, and home-cooked meals served on your work schedule.")
    ]
    
    reach_dist = dist_str.split('(')[0].strip()
    reach_time = dist_str.split('(')[-1].replace(')', '') if '(' in dist_str else dist_str
    reach_intro = f"Traveling from {ref_city} up to your tranquil workation haven is amazingly swift."
    reach_steps = [
        (f"Easy Departure from {ref_city}", f"Hop onto the Expressway corridor ({route_info})."),
        ("Smooth Scenic Highway", "Enjoy signal-free driving up the Western Ghats in under two hours."),
        ("Fast Villa Arrival", "Arrive directly at your private gated villa, connect to high-speed fiber Wi-Fi, and start working.")
    ]
    
    gallery_h2 = "Workation Spaces <span class=\"text-amber-600\">& Private Pool</span>"
    gallery_subtext = "Explore the tranquil desks, serene verandas, and luxury bedrooms waiting for your workation."
    
    seo_h2 = "Why Book a Workation Villa in Lonavala with Retrofusion?"
    seo_content_paragraphs = [
        f"Whether you are a solo entrepreneur, a startup team, or a family balancing work and vacation, our <strong>{page_title.lower()}</strong> provides the ideal setup for sustained productivity.",
        "Take high-stakes client presentations with total confidence on our 300 Mbps fiber Wi-Fi backed by power generators. When your workday ends, step directly onto the sun deck, swim in your private pool, or enjoy quiet evening walks surrounded by mountain mist.",
        f"<h3>Long-Stay Discounts & Housekeeping Support</h3>",
        "We offer attractive weekly and monthly workation tariffs with inclusive daily housekeeping, fresh linen changes, and customized meal subscriptions."
    ]
    
    faqs = [
        ("How fast and reliable is the internet connection?", "We provide high-speed 300 Mbps fiber Wi-Fi with dual-band routers providing full coverage across all bedrooms, living rooms, and garden terraces. Complete power backup ensures zero connection drops."),
        ("Is the environment quiet enough for video conference calls?", "Yes! Our estates are located in tranquil residential and nature-surrounded pockets of Lonavala, far from highway honking, making them ideal for high-stakes video meetings."),
        ("Can we book long-term or weekly workations with discounted rates?", "Yes, we offer attractive weekly and monthly workation tariffs with inclusive housekeeping, high-speed Wi-Fi, and custom meal subscriptions."),
        ("What are the dining options during work hours?", "Our resident caretaker and chef serve piping hot tea, coffee, breakfast, and wholesome home-cooked meals right on your schedule so you never have to worry about cooking.")
    ]
    
    booking_title = f"Reserve Your <span class=\"text-amber-600\">Workation Estate</span>"
    booking_subtext = "Ready to elevate your work-from-home routine? Inquire below for availability and long-stay packages."
    booking_hidden_val = page_title
    
    create_official_location_page(slug, title, description, keywords, canonical_url, hero_img, hero_h1_line1, hero_h1_line2, hero_subtext, hero_btn_text, intro_h2, intro_p, intro_features, reach_dist, reach_time, reach_intro, reach_steps, gallery_h2, gallery_subtext, seo_h2, seo_content_paragraphs, faqs, booking_title, booking_subtext, booking_hidden_val)

print("Finished generating Category 3 (Workation with Wifi)!")

# -------------------------------------------------------------
# CATEGORY 4: REUNION PARTY WITH PRIVATE POOL (5 PAGES)
# -------------------------------------------------------------
reunion_pages = [
    ("private-pool-homestay-in-lonavala-for-reunion-party", "Private Pool Homestay in Lonavala for Reunion Party", "Lonavala", "~90 mins from Mumbai & 60 mins from Pune", "Central Lonavala Hill Location"),
    ("private-pool-homestay-near-mumbai-for-reunion-party", "Private Pool Homestay Near Mumbai for Reunion Party", "Mumbai", "~85 km (approx. 1.5 - 2 Hours)", "via Mumbai-Pune Expressway"),
    ("private-pool-homestay-near-pune-for-reunion-party", "Private Pool Homestay Near Pune for Reunion Party", "Pune", "~65 km (approx. 1 Hour)", "via Expressway bypass"),
    ("private-pool-4bhk-villa-near-mumbai-for-reunion-party", "Private Pool 4BHK Villa Near Mumbai for Reunion Party", "Mumbai", "~85 km (approx. 1.5 - 2 Hours)", "via Mumbai-Pune Expressway"),
    ("private-pool-4bhk-villa-near-pune-for-reunion-party", "Private Pool 4BHK Villa Near Pune for Reunion Party", "Pune", "~65 km (approx. 1 Hour)", "via Expressway bypass"),
]

for slug, page_title, ref_city, dist_str, route_info in reunion_pages:
    title = f"{page_title} | 4BHK Luxury Pool Estate"
    description = f"Host an unforgettable reunion party at Retrofusion Lonavala. 100% private pool, spacious party lawn, live BBQ, bonfire, music sound system & luxury suites for 15-25 guests."
    keywords = f"{slug.replace('-', ' ')}, reunion party villa lonavala, private pool villa for reunion near mumbai, 4bhk party villa near pune, college reunion homestay lonavala"
    canonical_url = f"https://retrofusion.in/{slug}"
    hero_img = "images/v1769868155_M08_qewdva.webp"
    
    hero_h1_line1 = page_title.split(" for ")[0]
    hero_h1_line2 = "for Reunion Party"
    hero_subtext = f"Reunite with old schoolmates, college buddies, or extended family in a colossal 4BHK private estate in Lonavala just a short drive from {ref_city}."
    hero_btn_text = "Plan Reunion Party"
    
    intro_h2 = f"Celebrate Lifelong Friendships <span class=\"text-amber-600\">in Complete Exclusivity</span>"
    intro_p = f"Reunion parties deserve a special venue where you can laugh loudly, reminisce over nostalgic memories, and celebrate late into the night without noise complaints from hotel staff. Reserving a <strong>{page_title.lower()}</strong> gives you an entire 4-bedroom luxury villa reserved strictly for your group — with a private pool, lawn for music, live barbecue, and four lavish en-suite master suites."
    
    intro_features = [
        (icon1, "100% Private Pool", "Crystal-clear, massive private swimming pool reserved strictly for your squad."),
        (icon2, "Live BBQ & Bonfire", "Enjoy fresh sizzling barbecue kebabs grilled poolside and cozy bonfire nights."),
        (icon3, "15 - 25 Guests Capacity", "Huge 4BHK layouts with plush king beds and spacious extra bedding to host large groups.")
    ]
    
    reach_dist = dist_str.split('(')[0].strip()
    reach_time = dist_str.split('(')[-1].replace(')', '') if '(' in dist_str else dist_str
    reach_intro = f"Convenient central location ensuring all friends from {ref_city} can gather effortlessly."
    reach_steps = [
        (f"Departure from {ref_city}", f"Connect directly with your group along the highway ({route_info})."),
        ("Scenic Hill Climb", "Drive up the smooth Expressway admiring the Western Ghats valleys."),
        ("Private Villa Check-in", "Pull into our private gated grounds with ample parking for multiple SUVs.")
    ]
    
    gallery_h2 = "Reunion Luxury <span class=\"text-amber-600\">& Private Party Lawns</span>"
    gallery_subtext = "Take a tour of the poolside decks, party lawns, and luxury suites waiting for your reunion."
    
    seo_h2 = "Why Retrofusion is the #1 Reunion Destination in Lonavala"
    seo_content_paragraphs = [
        f"When planning a school, college, or family reunion near {ref_city}, privacy is paramount. At Retrofusion, you don't share hallways, pools, or dining tables with strangers.",
        "Challenge friends to snooker and carrom tournaments, splash in the private pool, play your favorite music, and chat around the evening lawn bonfire until the early morning hours.",
        f"<h3>Custom Feast Buffets & Live Barbecue</h3>",
        "Our in-house culinary crew prepares customized feast buffets — from smoky live barbecue chicken and paneer tikkas to authentic biryanis and late-night snacks."
    ]
    
    faqs = [
        ("Can we play music and celebrate beside the pool?", "Yes! We provide sound systems for your private gathering. You can celebrate and enjoy music within reasonable community guidelines."),
        ("How many guests can stay together for a reunion?", "Our 4BHK villas comfortably accommodate 15 to 25 guests with plush king beds, high-quality extra bedding, and 4 spacious bathrooms."),
        ("Can you arrange custom cakes, decorations, or live BBQ?", "Yes! Our team can arrange festive party decorations, balloon arches, custom reunion cakes, and live poolside barbecue setups on advance request."),
        ("What indoor entertainment is available if it rains?", "We offer an indoor snooker/pool table, full-size carrom, classic board games, and 4K Smart TVs with streaming subscriptions.")
    ]
    
    booking_title = f"Reserve Your <span class=\"text-amber-600\">Reunion Villa</span>"
    booking_subtext = "Get direct villa rates and reserve your dates for an epic reunion party."
    booking_hidden_val = page_title
    
    create_official_location_page(slug, title, description, keywords, canonical_url, hero_img, hero_h1_line1, hero_h1_line2, hero_subtext, hero_btn_text, intro_h2, intro_p, intro_features, reach_dist, reach_time, reach_intro, reach_steps, gallery_h2, gallery_subtext, seo_h2, seo_content_paragraphs, faqs, booking_title, booking_subtext, booking_hidden_val)

print("Finished generating Category 4 (Reunion Party)!")

# -------------------------------------------------------------
# CATEGORY 5: CORPORATE / OFFICE / TEAM OUTING 4BHK VILLAS (6 PAGES)
# -------------------------------------------------------------
corp_pages = [
    ("4bhk-villa-near-mumbai-for-corporate-party", "4BHK Villa Near Mumbai for Corporate Party", "Mumbai", "Corporate Party", "~85 km (approx. 1.5 - 2 Hours)"),
    ("4bhk-villa-near-pune-for-corporate-party", "4BHK Villa Near Pune for Corporate Party", "Pune", "Corporate Party", "~65 km (approx. 1 Hour)"),
    ("4bhk-villa-near-mumbai-for-office-outing", "4BHK Villa Near Mumbai for Office Outing", "Mumbai", "Office Outing", "~85 km (approx. 1.5 - 2 Hours)"),
    ("4bhk-villa-near-pune-for-office-outing", "4BHK Villa Near Pune for Office Outing", "Pune", "Office Outing", "~65 km (approx. 1 Hour)"),
    ("4bhk-villa-near-mumbai-for-team-outing", "4BHK Villa Near Mumbai for Team Outing", "Mumbai", "Team Outing", "~85 km (approx. 1.5 - 2 Hours)"),
    ("4bhk-villa-near-pune-for-team-outing", "4BHK Villa Near Pune for Team Outing", "Pune", "Team Outing", "~65 km (approx. 1 Hour)"),
]

for slug, page_title, ref_city, event_type, dist_str in corp_pages:
    title = f"{page_title} | Private Pool & BBQ Estate"
    description = f"Book an executive {page_title} in Lonavala. 4BHK luxury private pool estate, spacious presentation lounge, 300 Mbps Wi-Fi, chef-cooked buffet & GST billing."
    keywords = f"{slug.replace('-', ' ')}, corporate villa lonavala, office outing villa near mumbai, executive retreat villa pune, private pool villa for company offsite"
    canonical_url = f"https://retrofusion.in/{slug}"
    hero_img = "images/v1768241694_1874704f-2b23-41a2-aa21-ca77ce4aaecd_ipao9k.jpg"
    
    hero_h1_line1 = f"4BHK Villa Near {ref_city}"
    hero_h1_line2 = f"for {event_type}"
    hero_subtext = f"Elevate your corporate culture with a private 4BHK hill estate in Lonavala just a quick drive from {ref_city}. Complete executive exclusivity, private pool, and GST billing."
    hero_btn_text = "Reserve Corporate Villa"
    
    intro_h2 = f"Executive Luxury <span class=\"text-amber-600\">for {event_type}s</span>"
    intro_p = f"High-performing teams require more than generic conference rooms in crowded commercial hotels. Reserving a <strong>{page_title.lower()}</strong> in Lonavala provides the ideal environment for executive strategy alignment, team building, and celebratory corporate gatherings with zero distractions."
    
    intro_features = [
        (icon1, "Executive Confidentiality", "Gated, standalone private 4BHK estates offering 100% privacy for confidential corporate meetings."),
        (icon2, "Aquatic & Lawn Recreation", "Private swimming pool and manicured lawns for relaxing decompression after strategy sessions."),
        (icon3, "Full GST Corporate Invoicing", "Formal GST tax invoices provided for seamless company accounting and reimbursement.")
    ]
    
    reach_dist = dist_str.split('(')[0].strip()
    reach_time = dist_str.split('(')[-1].replace(')', '') if '(' in dist_str else dist_str
    reach_intro = f"Effortless Expressway transit from {ref_city} straight to our private gates in Lonavala."
    reach_steps = [
        (f"Easy Departure from {ref_city}", "Assemble your colleagues and take the expressway corridor."),
        ("Fast Highway Drive", "Ascend through the Western Ghats on a smooth, scenic signal-free route."),
        ("Arrival at Private Estate", "Check into your private 4BHK villa with ample secure parking for all corporate vehicles.")
    ]
    
    gallery_h2 = f"Executive 4BHK <span class=\"text-amber-600\">Estates</span>"
    gallery_subtext = "Preview our spacious conference-ready lounges, private pools, and luxury master bedrooms."
    
    seo_h2 = f"Why Book a 4BHK Villa Near {ref_city} for Your {event_type}?"
    seo_content_paragraphs = [
        f"Our luxury 4BHK private estates in Lonavala provide spacious double-height living rooms with plush seating and high-speed fiber Wi-Fi for presentations, coupled with outdoor lawns for team activities and a private swimming pool for relaxation.",
        "We handle all corporate hospitality — from morning tea/coffee and custom breakfast buffets to live poolside barbecues and celebratory dinners.",
        f"<h3>Full GST Corporate Tax Billing</h3>",
        "We provide official GST invoices with your company's registered legal name and GSTIN for smooth accounting and corporate expense approval."
    ]
    
    faqs = [
        ("Can we get official GST invoices for our corporate booking?", "Yes, we issue formal GST tax invoices with your company's legal name and GSTIN for all corporate bookings."),
        ("Are there presentation and meeting facilities available?", "Yes, our air-conditioned living lounges feature large 4K Smart TVs with HDMI/screen-mirroring and 300 Mbps Wi-Fi for presentations."),
        ("How many team members can stay at a 4BHK villa?", "A 4BHK villa accommodates 15 to 25 members with king beds, premium extra rollaway mattresses, and spacious en-suite bathrooms."),
        ("What meal arrangements are available for office groups?", "Our in-house chef prepares customized corporate buffets including morning tea/coffee, hot breakfast, business lunch, high tea with snacks, and evening poolside barbecue.")
    ]
    
    booking_title = f"Reserve Your <span class=\"text-amber-600\">4BHK Corporate Villa</span>"
    booking_subtext = f"Plan an unforgettable {event_type.lower()} for your organization. Inquire below for dates and quotes."
    booking_hidden_val = page_title
    
    create_official_location_page(slug, title, description, keywords, canonical_url, hero_img, hero_h1_line1, hero_h1_line2, hero_subtext, hero_btn_text, intro_h2, intro_p, intro_features, reach_dist, reach_time, reach_intro, reach_steps, gallery_h2, gallery_subtext, seo_h2, seo_content_paragraphs, faqs, booking_title, booking_subtext, booking_hidden_val)

print("Finished generating Category 5 (Corporate 4BHK Villas)!")
print("ALL 41 OFFICIAL LOCATION PAGES SUCCESSFULLY GENERATED!")
