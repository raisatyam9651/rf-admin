$faqHtml = @"
<!-- ===== FAQ SECTION ===== -->
<section class="py-16 bg-stone-50 border-t border-stone-200">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-display font-bold text-[#0F2A24] mb-8 text-center">Frequently Asked Questions</h2>
    <div class="space-y-6">
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-stone-100">
        <h3 class="text-xl font-bold text-[#0F2A24] mb-2">Do you provide high-speed internet for presentations?</h3>
        <p class="text-stone-600">Yes, our villas are equipped with high-speed Fiber Wi-Fi to ensure seamless presentations, video conferencing, and uninterrupted connectivity for your team.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-stone-100">
        <h3 class="text-xl font-bold text-[#0F2A24] mb-2">Are there dedicated breakout rooms for strategy sessions?</h3>
        <p class="text-stone-600">Absolutely. Alongside massive double-height living rooms, we offer multiple quiet zones and outdoor seating arrangements that function perfectly as breakout areas for smaller team discussions.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-stone-100">
        <h3 class="text-xl font-bold text-[#0F2A24] mb-2">Is renting a private villa more cost-effective than a resort?</h3>
        <p class="text-stone-600">Yes. When booking for corporate groups of 10-25+ people, renting an entire luxury villa offers significant cost-per-head efficiency compared to booking individual rooms and banquet halls at 3-star resorts, while providing vastly superior privacy.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-stone-100">
        <h3 class="text-xl font-bold text-[#0F2A24] mb-2">Do you provide GST invoicing for corporate bookings?</h3>
        <p class="text-stone-600">Yes, we provide fully compliant B2B GST invoicing and customized billing solutions tailored for corporate expense policies.</p>
      </div>
    </div>
  </div>
</section>
"@

$faqSchema = @"
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do you provide high-speed internet for presentations?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, our villas are equipped with high-speed Fiber Wi-Fi to ensure seamless presentations, video conferencing, and uninterrupted connectivity for your team."
      }
    },
    {
      "@type": "Question",
      "name": "Are there dedicated breakout rooms for strategy sessions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Alongside massive double-height living rooms, we offer multiple quiet zones and outdoor seating arrangements that function perfectly as breakout areas for smaller team discussions."
      }
    },
    {
      "@type": "Question",
      "name": "Is renting a private villa more cost-effective than a resort?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. When booking for corporate groups of 10-25+ people, renting an entire luxury villa offers significant cost-per-head efficiency compared to booking individual rooms and banquet halls at 3-star resorts, while providing vastly superior privacy."
      }
    },
    {
      "@type": "Question",
      "name": "Do you provide GST invoicing for corporate bookings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, we provide fully compliant B2B GST invoicing and customized billing solutions tailored for corporate expense policies."
      }
    }
  ]
}
</script>
"@

Get-ChildItem -Filter "*for-corporate-party.php" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    
    if ($content -notmatch 'FAQ SECTION') {
        $content = $content -replace '<\?php include ''includes/footer.php''; \?>', "`n`$faqHtml`n`n<?php include 'includes/footer.php'; ?>"
        $content = $content -replace '</script>\s*<style>', "</script>`n`$faqSchema`n<style>"
        
        # Replace the literal `$faqHtml` strings back with the variable content (powershell replace weirdness fix)
        $content = $content.Replace('`$faqHtml', $faqHtml)
        $content = $content.Replace('`$faqSchema', $faqSchema)

        Set-Content -Path $_.FullName -Value $content -NoNewline
    }
}
