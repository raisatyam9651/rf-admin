<?php
$pageTitle = "4BHK Villa Near Pune Airport for Family | Private Pool Homestay Lonavala";
$pageDescription = "Book a luxury 4BHK family villa near Pune Airport (PNQ). Just 80 minutes to Lonavala featuring private swimming pool, garden lawn, indoor games, and home-cooked meals.";
$pageKeywords = "4bhk villa near pune airport for family, family villa with private pool near pnq, 4 bedroom villa lonavala for family fly in pune, luxury homestay for family reunion viman nagar";
$pageRobots = "index, follow";
$canonicalUrl = "https://retrofusion.in/4bhk-villa-near-pune-airport-for-family";
$ogTitle = "4BHK Villa Near Pune Airport for Family | Retrofusion Luxury Homestays";
$ogDescription = "Under 80 minutes from Pune Airport (PNQ). Rent an exclusive 4BHK private pool villa in Lonavala with senior-friendly rooms, kids play area, snooker, and hot home-style meals.";
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
      "url": "https://retrofusion.in/4bhk-villa-near-pune-airport-for-family",
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
      "description": "Premium 4BHK private pool villas in Lonavala located approximately 1 hour 20 minutes from Pune International Airport (PNQ), tailored for family reunions and vacations with outstation arrivals."
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
          "item": "https://retrofusion.in/4bhk-villa-near-pune-airport-for-family"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How far is the 4BHK family villa from Pune Airport (PNQ)?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Retrofusion Villas in Lonavala are approximately 72 km from Pune Airport (Lohegaon / Viman Nagar), taking about 1 hour 20 minutes via the Pune-Mumbai Expressway bypass."
          }
        },
        {
          "@type": "Question",
          "name": "Can you coordinate airport transfers for outstation family members?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, our concierge team can organize private cabs or tempo travelers for convenient pickup from PNQ arrivals straight to the villa doorstep."
          }
        },
        {
          "@type": "Question",
          "name": "Is the property suitable for elderly parents and young kids?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, our properties feature ground floor bedrooms with step-free access, ensuite western bathrooms, shallow pool zones, and enclosed garden lawns safe for children."
          }
        },
        {
          "@type": "Question",
          "name": "What is the sleeping capacity of the 4BHK villa?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our 4BHK villas comfortably lodge 12 to 20 family members with 4 air-conditioned master bedrooms and premium extra mattresses."
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
        <img src="images/family_villa_lonavala_hero.webp" alt="4BHK Villa Near Pune Airport for Family" class="w-full h-full object-cover opacity-35 filter brightness-75 scale-105 transition-transform duration-1000">
        <div class="absolute inset-0 bg-gradient-to-t from-luxury-black via-luxury-black/70 to-transparent"></div>
    </div>
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 max-w-5xl text-center">
        <span class="inline-block px-4 py-1.5 rounded-full bg-gold/20 border border-gold/40 text-gold text-xs uppercase tracking-widest font-medium mb-4">
            Under 80 Mins from PNQ Airport
        </span>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-serif font-bold text-white mb-6 leading-tight">
            4BHK Villa Near <span class="text-gold">Pune Airport</span> for Family
        </h1>
        <p class="text-base sm:text-lg text-gray-300 max-w-3xl mx-auto mb-8 font-light leading-relaxed">
            Planning a multi-generational family vacation where relatives fly into Pune? Escape city hotels and settle into a private 4BHK pool villa surrounded by the verdant Western Ghats in Lonavala.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="#inquiry-form" class="w-full sm:w-auto px-8 py-3.5 rounded-full bg-gold text-luxury-black font-semibold text-sm hover:bg-gold-light transition duration-300 shadow-lg shadow-gold/20">
                Reserve Family Dates
            </a>
            <a href="https://wa.me/918999036644?text=Hi%2C%20our%20family%20is%20landing%20at%20Pune%20Airport%20and%20looking%20for%20a%204BHK%20villa." target="_blank" class="w-full sm:w-auto px-8 py-3.5 rounded-full border border-white/30 text-white font-medium text-sm hover:bg-white/10 transition duration-300 flex items-center justify-center gap-2">
                <span>WhatsApp Concierge</span>
            </a>
        </div>
    </div>
</section>

<!-- Route & Distance Guide from PNQ -->
<section class="py-12 bg-luxury-charcoal/40 border-y border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-5xl">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">From PNQ Terminal</p>
                <p class="text-xl sm:text-2xl font-bold text-gold">~72 km</p>
                <p class="text-gray-400 text-xs mt-1">~1h 20m drive</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">From Viman Nagar / Kalyani</p>
                <p class="text-xl sm:text-2xl font-bold text-gold">~70 km</p>
                <p class="text-gray-400 text-xs mt-1">Direct expressway bypass</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">Amenities</p>
                <p class="text-xl sm:text-2xl font-bold text-white">Private Pool</p>
                <p class="text-gray-400 text-xs mt-1">Lawn & indoor games</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">Family Capacity</p>
                <p class="text-xl sm:text-2xl font-bold text-white">12 – 20 Pax</p>
                <p class="text-gray-400 text-xs mt-1">4 En-Suite Bedrooms</p>
            </div>
        </div>
    </div>
</section>

<!-- Editorial Section -->
<section class="py-20 bg-luxury-black text-gray-300">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl leading-relaxed">
        <div class="space-y-6">
            <h2 class="text-2xl sm:text-4xl font-serif font-bold text-white tracking-wide">
                A Refreshing Hill Getaway for Families Arriving at Pune Airport
            </h2>
            <p>
                When relatives fly into Pune Airport from across India or overseas, staying in busy city hotels in Viman Nagar or Koregaon Park often means spending your precious vacation time navigating traffic.
            </p>
            <p>
                In just 80 minutes along the expressway bypass, your whole family arrives at <strong>Retrofusion Luxury Homestays</strong> in Lonavala. Enjoy private swimming pools, breezy garden verandas, and large living rooms where memories are made. Our dedicated cooks serve fresh, customized home-cooked meals so you can concentrate on spending quality time together.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-gold font-serif text-lg font-semibold mb-2">Senior & Child Friendly</h3>
                    <p class="text-sm text-gray-400">Ground-floor master bedrooms, safe enclosed gardens, and clean pool waters make it ideal for multi-generational families.</p>
                </div>
                <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-gold font-serif text-lg font-semibold mb-2">Homely Fresh Meals</h3>
                    <p class="text-sm text-gray-400">Fresh breakfast, tea/coffee snacks, pure veg, Jain, and non-veg curries cooked just the way your family likes it.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Villa Showcase -->
<section class="py-20 bg-luxury-charcoal/20 border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-6xl">
        <div class="text-center mb-16">
            <span class="text-gold text-xs uppercase tracking-widest font-semibold">Luxury Properties</span>
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Family Villas Near Pune Airport</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1773076226_27_ipqwdd.webp" alt="Retro Visawa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Retro Visawa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Mountain-view infinity pool, indoor pool table, open garden, and sprawling family balconies.</p>
                    <a href="/retro-viswa-lonavala" class="text-gold text-sm font-semibold hover:underline">Explore Villa &rarr;</a>
                </div>
            </div>
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1774810269_12_lo4gpx.webp" alt="Neo Retro Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Neo Retro Villa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Modern contemporary architecture, private plunge pool, cozy lounges, and luxury bedrooms.</p>
                    <a href="/neo-retro" class="text-gold text-sm font-semibold hover:underline">Explore Villa &rarr;</a>
                </div>
            </div>
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1769868155_M08_qewdva.webp" alt="Retro Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Retro Villa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Quiet boutique homestay surrounded by tall trees, peaceful garden, and crystal private swimming pool.</p>
                    <a href="/retro-villas" class="text-gold text-sm font-semibold hover:underline">Explore Villa &rarr;</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Accordion -->
<section class="py-20 bg-luxury-black border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl">
        <div class="text-center mb-12">
            <span class="text-gold text-xs uppercase tracking-widest font-semibold">Helpful Information</span>
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Frequently Asked Questions</h2>
        </div>
        <div class="space-y-4">
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>What is the best route from Pune Airport to the villa?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    From PNQ, take the airport road toward Vishrantwadi / Katraj-Dehu Road bypass, join the Pune-Mumbai Expressway, and exit at Lonavala. Total driving time is around 1 hour 20 minutes.
                </p>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>Can we get personalized meals for grandparents and children?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Yes, our cooks prepare mild, low-spice meals, khichdi, pure vegetarian, and Jain foods tailored to seniors and toddlers.
                </p>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>Is power backup available in case of outages?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Yes, heavy-duty inverter and generator backup systems guarantee uninterrupted lighting, air conditioning, refrigeration, and Wi-Fi throughout your family vacation.
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
                <p class="text-gray-400 text-sm mt-2">Direct booking rates, seasonal packages, and instant date confirmation.</p>
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
                        <option value="Any Villa" class="bg-luxury-black">Any Available Villa</option>
                        <option value="Retro Visawa" class="bg-luxury-black">Retro Visawa (Infinity Pool & Snooker)</option>
                        <option value="Neo Retro Villa" class="bg-luxury-black">Neo Retro Villa (Ultra Luxury)</option>
                        <option value="Retro Villa" class="bg-luxury-black">Retro Villa (Vintage Garden Retreat)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Special Requests & Flight Details</label>
                    <textarea name="message" rows="3" placeholder="Tell us if you need airport pickup, ground-floor senior room, or pure veg/Jain food..." class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition"></textarea>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Verification: <?php echo "$num1 + $num2 = ?"; ?> *</label>
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
