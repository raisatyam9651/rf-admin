<?php
$pageTitle = "4BHK Villa Near Mumbai for Family | Private Pool Homestay Lonavala";
$pageDescription = "Book a luxury 4BHK villa near Mumbai for your family vacation. Located in Lonavala with private swimming pool, garden lawn, home-cooked meals, and games.";
$pageKeywords = "4bhk villa near mumbai for family, family villa with private pool near mumbai, 4 bedroom villa lonavala for family, luxury homestay for family get together mumbai";
$pageRobots = "index, follow";
$canonicalUrl = "https://retrofusion.in/4bhk-villa-near-mumbai-for-family";
$ogTitle = "4BHK Villa Near Mumbai for Family | Retrofusion Luxury Homestays";
$ogDescription = "The ultimate multi-generational family retreat near Mumbai. Luxury 4BHK private pool villas in Lonavala with kid-friendly lawns, games, and fresh home-style dining.";
$ogImage = "https://retrofusion.in/images/family_villa_lonavala_hero.webp";

include 'includes/header.php';

$num1 = rand(1, 9);
$num2 = rand(1, 9);
$_SESSION['captcha_answer'] = $num1 + $num2;
?>

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LodgingBusiness",
      "@id": "https://retrofusion.in/#lodging",
      "name": "Retrofusion Luxury Homestays & Private Villas",
      "url": "https://retrofusion.in/4bhk-villa-near-mumbai-for-family",
      "telephone": "+91 8999036644",
      "priceRange": "₹₹₹",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Old Mumbai Pune Highway, Near Karla Caves & Wax Museum",
        "addressLocality": "Lonavala",
        "addressRegion": "Maharashtra",
        "postalCode": "410401",
        "addressCountry": "IN"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 18.7557,
        "longitude": 73.4091
      },
      "description": "Exclusive 4BHK private pool villas in Lonavala designed for family getaways from Mumbai. Features senior-friendly ground floor bedrooms, kid-safe swimming pools, home-style food, and lush gardens."
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://retrofusion.in/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Family Villas",
          "item": "https://retrofusion.in/4bhk-villa-near-mumbai-for-family"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Is the 4BHK villa suitable for elderly family members and toddlers?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, our villas feature ground-floor bedrooms with step-free access, western attached bathrooms, anti-skid pool decks, and fenced gardens safe for young kids and seniors."
          }
        },
        {
          "@type": "Question",
          "name": "How far is the villa from Mumbai?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Retrofusion villas are located in Lonavala, roughly 85 to 95 km from Mumbai (approx. 90 to 120 minutes via the Mumbai-Pune Expressway or Atal Setu)."
          }
        },
        {
          "@type": "Question",
          "name": "Can we get home-cooked pure veg or Jain meals for the family?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes! Our in-house chefs specialize in pure vegetarian, Jain, and non-vegetarian home-style Maharashtrian and North Indian dishes prepared fresh."
          }
        },
        {
          "@type": "Question",
          "name": "How many family members can sleep comfortably in a 4BHK villa?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A 4BHK villa comfortably accommodates 12 to 20 family members with king beds, premium extra rollaway mattresses, and spacious living spaces."
          }
        }
      ]
    }
  ]
}
</script>

<!-- Hero Section -->
<section class="relative pt-32 pb-20 md:pt-40 md:pb-28 bg-luxury-black text-white overflow-hidden">
    <div class="absolute inset-0 z-0">
        <img src="images/family_villa_lonavala_hero.webp" alt="4BHK Villa Near Mumbai for Family" class="w-full h-full object-cover opacity-35 filter brightness-75 scale-105 transition-transform duration-1000">
        <div class="absolute inset-0 bg-gradient-to-t from-luxury-black via-luxury-black/70 to-transparent"></div>
    </div>
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 max-w-5xl text-center">
        <span class="inline-block px-4 py-1.5 rounded-full bg-gold/20 border border-gold/40 text-gold text-xs uppercase tracking-widest font-medium mb-4">
            Private Multi-Generational Retreat
        </span>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-serif font-bold text-white mb-6 leading-tight">
            4BHK Villa Near <span class="text-gold">Mumbai</span> for Family
        </h1>
        <p class="text-base sm:text-lg text-gray-300 max-w-3xl mx-auto mb-8 font-light leading-relaxed">
            Escape city noise and treat your family to an exclusive 4BHK holiday in Lonavala. Gated private estates with private pool, kid-safe lawns, indoor games, senior-friendly rooms, and warm home-cooked meals.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="#inquiry-form" class="w-full sm:w-auto px-8 py-3.5 rounded-full bg-gold text-luxury-black font-semibold text-sm hover:bg-gold-light transition duration-300 shadow-lg shadow-gold/20">
                Check Family Availability
            </a>
            <a href="https://wa.me/918999036644?text=Hi%2C%20I%20am%20looking%20for%20a%204BHK%20villa%20near%20Mumbai%20for%20a%20family%20getaway." target="_blank" class="w-full sm:w-auto px-8 py-3.5 rounded-full border border-white/30 text-white font-medium text-sm hover:bg-white/10 transition duration-300 flex items-center justify-center gap-2">
                <span>WhatsApp Concierge</span>
            </a>
        </div>
    </div>
</section>

<!-- Route & Distance Guide from Mumbai -->
<section class="py-12 bg-luxury-charcoal/40 border-y border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-5xl">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">From Mumbai / BKC</p>
                <p class="text-xl sm:text-2xl font-bold text-gold">~85 km</p>
                <p class="text-gray-400 text-xs mt-1">~1.5 - 2h drive</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">Family Capacity</p>
                <p class="text-xl sm:text-2xl font-bold text-gold">12 – 20 Pax</p>
                <p class="text-gray-400 text-xs mt-1">4 En-Suite Bedrooms</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">Kid & Senior Friendly</p>
                <p class="text-xl sm:text-2xl font-bold text-white">Safe & Secure</p>
                <p class="text-gray-400 text-xs mt-1">Ground floor suites & lawn</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">Culinary Service</p>
                <p class="text-xl sm:text-2xl font-bold text-white">Veg & Jain</p>
                <p class="text-gray-400 text-xs mt-1">Fresh home-cooked meals</p>
            </div>
        </div>
    </div>
</section>

<!-- Editorial Section -->
<section class="py-20 bg-luxury-black text-gray-300">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl leading-relaxed">
        <div class="space-y-6">
            <h2 class="text-2xl sm:text-4xl font-serif font-bold text-white tracking-wide">
                The Perfect Family Sanctuary Away from Mumbai’s Hectic Pace
            </h2>
            <p>
                Planning a family gathering with grandparents, parents, teenagers, and little children in a standard hotel often means booking separate rooms on different floors, fighting over restaurant timings, and sharing public pools with strangers.
            </p>
            <p>
                At <strong>Retrofusion Luxury Homestays</strong> in Lonavala, you get an entire 4BHK private estate dedicated solely to your family. Grandparents can enjoy serene mornings on the garden veranda, kids can splash happily in the clean private pool, teens can challenge each other on the snooker table, and everyone can bond over authentic, piping hot home-style meals prepared with love by our caretakers.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-gold font-serif text-lg font-semibold mb-2">Senior & Child Friendly</h3>
                    <p class="text-sm text-gray-400">Step-free ground floor bedrooms, gentle steps, shaded sit-outs, and secure enclosed grounds give complete peace of mind.</p>
                </div>
                <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-gold font-serif text-lg font-semibold mb-2">Fresh Home-Cooked Food</h3>
                    <p class="text-sm text-gray-400">Enjoy customized family dining: pure veg, Jain options, Maharashtrian specialties, tawa chapatis, and fresh snacks on demand.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Villa Showcase -->
<section class="py-20 bg-luxury-charcoal/20 border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-6xl">
        <div class="text-center mb-16">
            <span class="text-gold text-xs uppercase tracking-widest font-semibold">Handpicked Family Stays</span>
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Our Signature 4BHK Family Villas</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1773076226_27_ipqwdd.webp" alt="Retro Visawa Family Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Retro Visawa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Mountain-view infinity pool, indoor pool table, open garden, and spacious family living areas.</p>
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
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Family Villa FAQs</h2>
        </div>
        <div class="space-y-4">
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>What is the driving time from Mumbai?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Via the Mumbai-Pune Expressway or Atal Setu from South/Central Mumbai, driving time is typically between 90 minutes and 2 hours depending on departure time.
                </p>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>Is the pool safe for children?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Yes, our pools feature shallow zones and gradual depth transitions suitable for family relaxation, with crystal-clear filtration maintained daily.
                </p>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>Can we use the villa kitchen to cook baby food?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Yes, families have access to the kitchen for boiling milk, preparing infant cereals, or warming food. Our staff is also delighted to assist.
                </p>
            </details>
        </div>
    </div>
</section>

<!-- Inquiry Form -->
<section id="inquiry-form" class="py-20 bg-luxury-charcoal/30 border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-3xl">
        <div class="bg-luxury-black p-8 sm:p-12 rounded-3xl border border-white/10 shadow-2xl">
            <div class="text-center mb-8">
                <span class="text-gold text-xs uppercase tracking-widest font-semibold">Reserve Family Vacation</span>
                <h2 class="text-2xl sm:text-3xl font-serif font-bold text-white mt-2">Book Your 4BHK Family Villa</h2>
                <p class="text-gray-400 text-sm mt-2">Get direct villa rates, seasonal packages, and instant date confirmation.</p>
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
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Number of Family Members</label>
                        <input type="number" name="guests" min="1" placeholder="e.g. 14 (Adults + Kids)" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
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
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Family Notes / Dietary Requests</label>
                    <textarea name="message" rows="3" placeholder="Tell us if you need pure veg/Jain food, senior room on ground floor, or baby food support..." class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition"></textarea>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Security Verification: <?php echo "$num1 + $num2 = ?"; ?> *</label>
                    <input type="number" name="captcha" required placeholder="Enter total" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                </div>
                <button type="submit" class="w-full py-4 rounded-xl bg-gold text-luxury-black font-bold uppercase tracking-wider text-sm hover:bg-gold-light transition duration-300 shadow-lg shadow-gold/20">
                    Send Family Booking Inquiry
                </button>
            </form>
        </div>
    </div>
</section>

<?php include 'includes/footer.php'; ?>
