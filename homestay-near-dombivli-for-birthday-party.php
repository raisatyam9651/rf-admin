<?php
$pageTitle = "Homestay Near Dombivli for Birthday Party | Private Pool Villa Lonavala";
$pageDescription = "Host a high-energy birthday party at a private pool homestay near Dombivli. Located in Lonavala with private swimming pool, barbecue, party lawn, and luxury suites.";
$pageKeywords = "homestay near dombivli for birthday party, birthday party villa near dombivli, pool villa dombivli east west palava city, birthday celebration stay lonavala";
$pageRobots = "index, follow";
$canonicalUrl = "https://retrofusion.in/homestay-near-dombivli-for-birthday-party";
$ogTitle = "Homestay Near Dombivli for Birthday Party | Retrofusion Villas Lonavala";
$ogDescription = "Celebrate your birthday with complete privacy and luxury. 4BHK private pool villas in Lonavala just 1h 45m from Dombivli and Palava. Pool, DJ music, BBQ & party lawns.";
$ogImage = "https://retrofusion.in/images/private_pool_villa_lonavala_hero.webp";

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
      "url": "https://retrofusion.in/homestay-near-dombivli-for-birthday-party",
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
      "description": "Luxurious 4BHK private pool villas in Lonavala, roughly 1h 45m drive from Dombivli and Palava City, tailored for exceptional birthday celebrations, family parties, and pool bashes."
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
          "name": "Birthday Party Villas",
          "item": "https://retrofusion.in/homestay-in-lonavala-for-birthday-party.php"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "Homestay Near Dombivli for Birthday Party",
          "item": "https://retrofusion.in/homestay-near-dombivli-for-birthday-party"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How far is Retrofusion homestay from Dombivli?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The drive from Dombivli (via Kalyan-Shilphata Road or Nilje / Palava to the Mumbai-Pune Expressway) is around 90-95 km, taking roughly 1 hour 45 minutes."
          }
        },
        {
          "@type": "Question",
          "name": "Can we arrange a private pool party for the birthday celebration?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes! Every villa comes with a private swimming pool reserved strictly for your group, complete with deck recliners and Bluetooth audio setups."
          }
        },
        {
          "@type": "Question",
          "name": "Are fresh meals and barbecue arranged at the villa?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, our culinary team prepares live barbecue dishes, Indian breads, traditional Maharashtrian specialties, and multi-course buffets tailored to your event."
          }
        },
        {
          "@type": "Question",
          "name": "What is the guest sleeping capacity?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our 4BHK villas can comfortably accommodate 15 to 25 people with extra mattresses and spacious en-suite bedrooms."
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
        <img src="images/private_pool_villa_lonavala_hero.webp" alt="Homestay Near Dombivli for Birthday Party" class="w-full h-full object-cover opacity-35 filter brightness-75 scale-105 transition-transform duration-1000">
        <div class="absolute inset-0 bg-gradient-to-t from-luxury-black via-luxury-black/70 to-transparent"></div>
    </div>
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10 max-w-5xl text-center">
        <span class="inline-block px-4 py-1.5 rounded-full bg-gold/20 border border-gold/40 text-gold text-xs uppercase tracking-widest font-medium mb-4">
            Under 1h 45m from Dombivli & Palava
        </span>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-serif font-bold text-white mb-6 leading-tight">
            Homestay Near <span class="text-gold">Dombivli</span> for Birthday Party
        </h1>
        <p class="text-base sm:text-lg text-gray-300 max-w-3xl mx-auto mb-8 font-light leading-relaxed">
            Trade crowded city banquet rooms for an exclusive hill station birthday experience. Private pools, sprawling party lawns, live barbecue grills, and luxury 4BHK bedrooms in Lonavala.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <a href="#inquiry-form" class="w-full sm:w-auto px-8 py-3.5 rounded-full bg-gold text-luxury-black font-semibold text-sm hover:bg-gold-light transition duration-300 shadow-lg shadow-gold/20">
                Reserve Birthday Dates
            </a>
            <a href="https://wa.me/918999036644?text=Hi%2C%20I%20am%20from%20Dombivli%20and%20looking%20for%20a%20birthday%20party%20villa%20in%20Lonavala." target="_blank" class="w-full sm:w-auto px-8 py-3.5 rounded-full border border-white/30 text-white font-medium text-sm hover:bg-white/10 transition duration-300 flex items-center justify-center gap-2">
                <span>Chat on WhatsApp</span>
            </a>
        </div>
    </div>
</section>

<!-- Route & Distance Guide from Dombivli -->
<section class="py-12 bg-luxury-charcoal/40 border-y border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-5xl">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">From Dombivli East / West</p>
                <p class="text-xl sm:text-2xl font-bold text-gold">~92 km</p>
                <p class="text-gray-400 text-xs mt-1">~1h 45m drive</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">From Palava / Nilje</p>
                <p class="text-xl sm:text-2xl font-bold text-gold">~85 km</p>
                <p class="text-gray-400 text-xs mt-1">Fast Shilphata bypass</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">Villa Features</p>
                <p class="text-xl sm:text-2xl font-bold text-white">Private Pool</p>
                <p class="text-gray-400 text-xs mt-1">Snooker & Party Lawn</p>
            </div>
            <div class="p-4 rounded-xl bg-white/5 border border-white/10">
                <p class="text-gray-400 text-xs uppercase tracking-wider mb-1">Group Size</p>
                <p class="text-xl sm:text-2xl font-bold text-white">12 – 25 Pax</p>
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
                An Exclusive Birthday Celebration Just a Short Drive Away
            </h2>
            <p>
                Whether you live in Dombivli East, Manpada, or Palava City, booking banquet halls in town often brings the frustrations of restricted party hours, limited guest privacy, and zero holiday atmosphere. A quick drive onto the expressway brings you straight into the scenic beauty of Lonavala.
            </p>
            <p>
                <strong>Retrofusion Luxury Homestays</strong> gives you the keys to an entire private villa designed for fun and celebration. Splash in the pool, gather around the barbecue grill for sizzling kebabs, listen to your favorite beats, and cut the birthday cake under the open sky with your closest people.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
                <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-gold font-serif text-lg font-semibold mb-2">Bespoke Birthday Decorations</h3>
                    <p class="text-sm text-gray-400">We set up festive balloon backdrops, neon signage, and fairy lighting around the swimming pool before you arrive.</p>
                </div>
                <div class="bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-gold font-serif text-lg font-semibold mb-2">Private Pool & Game Lounge</h3>
                    <p class="text-sm text-gray-400">Enjoy full pool privacy, indoor snooker/pool tables, board games, and manicured lawns for fun family games.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Villa Showcase -->
<section class="py-20 bg-luxury-charcoal/20 border-t border-white/5">
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-6xl">
        <div class="text-center mb-16">
            <span class="text-gold text-xs uppercase tracking-widest font-semibold">Featured Properties</span>
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Birthday Villas Near Dombivli</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1773076226_27_ipqwdd.webp" alt="Retro Visawa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Retro Visawa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Mountain-view infinity pool, indoor 8-ball pool table, terrace party deck, and capacity for 15-25 guests.</p>
                    <a href="/retro-viswa-lonavala" class="text-gold text-sm font-semibold hover:underline">Explore Villa &rarr;</a>
                </div>
            </div>
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1774810269_12_lo4gpx.webp" alt="Neo Retro Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Neo Retro Villa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Glass-walled luxury villa featuring plunge pool, designer lounge, and modern birthday vibes.</p>
                    <a href="/neo-retro" class="text-gold text-sm font-semibold hover:underline">Explore Villa &rarr;</a>
                </div>
            </div>
            <div class="bg-luxury-black rounded-2xl overflow-hidden border border-white/10 hover:border-gold/50 transition duration-300">
                <img src="images/v1769868155_M08_qewdva.webp" alt="Retro Villa" class="w-full h-56 object-cover">
                <div class="p-6">
                    <h3 class="text-xl font-serif font-bold text-white mb-2">Retro Villa (4BHK)</h3>
                    <p class="text-gray-400 text-sm mb-4">Lush green garden surroundings, tranquil private pool, vintage charm, and delicious local food.</p>
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
            <span class="text-gold text-xs uppercase tracking-widest font-semibold">Answers to Common Questions</span>
            <h2 class="text-3xl sm:text-4xl font-serif font-bold text-white mt-2">Frequently Asked Questions</h2>
        </div>
        <div class="space-y-4">
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>What is the quickest route from Dombivli to Lonavala?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Take Kalyan-Shilphata Road through Palava onto the Taloja bypass, then merge onto the Mumbai-Pune Expressway at Kalamboli. Total driving time is typically under 1 hour 45 minutes.
                </p>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>Can we bring outside beverages and celebratory snacks?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Yes, outside drinks and snacks are welcomed with no corkage charges. Large refrigerators, ice setups, and dining glassware are provided.
                </p>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl p-5 [&_summary::-webkit-details-marker]:hidden cursor-pointer">
                <summary class="flex justify-between items-center text-white font-medium">
                    <span>Is Wi-Fi and generator backup available?</span>
                    <span class="text-gold group-open:rotate-180 transition-transform duration-300">&darr;</span>
                </summary>
                <p class="text-gray-400 text-sm mt-3 leading-relaxed">
                    Yes, all Retrofusion villas have high-speed broadband Wi-Fi and automatic power backup so your party music, lighting, and entertainment never pause.
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
                <span class="text-gold text-xs uppercase tracking-widest font-semibold">Reserve Your Party</span>
                <h2 class="text-2xl sm:text-3xl font-serif font-bold text-white mt-2">Book Your Birthday Homestay</h2>
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
                        <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Number of Guests</label>
                        <input type="number" name="guests" min="1" placeholder="e.g. 15" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
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
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Preferred Villa</label>
                    <select name="villa" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                        <option value="Any Villa" class="bg-luxury-black">Any Available Villa</option>
                        <option value="Retro Visawa" class="bg-luxury-black">Retro Visawa (Infinity Pool & Snooker)</option>
                        <option value="Neo Retro Villa" class="bg-luxury-black">Neo Retro Villa (Ultra Luxury)</option>
                        <option value="Retro Villa" class="bg-luxury-black">Retro Villa (Vintage Garden Retreat)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Special Requirements / Decoration</label>
                    <textarea name="message" rows="3" placeholder="Tell us if you want BBQ, cake, balloon decorations, or special meals..." class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition"></textarea>
                </div>
                <div>
                    <label class="block text-xs uppercase tracking-wider text-gray-400 mb-2">Math Verification: <?php echo "$num1 + $num2 = ?"; ?> *</label>
                    <input type="number" name="captcha" required placeholder="Enter total" class="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white focus:outline-none focus:border-gold transition">
                </div>
                <button type="submit" class="w-full py-4 rounded-xl bg-gold text-luxury-black font-bold uppercase tracking-wider text-sm hover:bg-gold-light transition duration-300 shadow-lg shadow-gold/20">
                    Send Inquiry
                </button>
            </form>
        </div>
    </div>
</section>

<?php include 'includes/footer.php'; ?>
