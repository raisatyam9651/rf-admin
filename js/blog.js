document.addEventListener('DOMContentLoaded', () => {
    const blogContainer = document.getElementById('blog-container');

    if (!blogContainer) return;

    // Hardcoded latest blog posts since WP API is no longer active
    const posts = [
        {
            title: "Top 20 Lonavala Tourist Places You Must Visit in 2025",
            link: "/blogs/lonavala-tourist-places",
            excerpt: "Discover the top 20 Lonavala tourist places to explore in 2025. From scenic viewpoints and historic...",
            imageUrl: "/blogs/images/Best-Tourist-Point-in-Lonavala-Top-Attractions-1024x559.webp"
        },
        {
            title: "Best Places to Stay in Lonavala for Family",
            link: "/blogs/best-places-to-stay-in-lonavala-for-family",
            excerpt: "Planning a family trip to Lonavala? Discover the best family-friendly homestays with private pools...",
            imageUrl: "/blogs/images/Top-Rated-Family-Homestay-in-Lonavala.webp"
        },
        {
            title: "Pawna Lake Camping Lonavala: Complete Guide",
            link: "/blogs/pawna-lake-camping-lonavala-complete-guide-with-stay-option",
            excerpt: "Experience the ultimate weekend getaway with our complete guide to Pawna Lake camping in Lonavala...",
            imageUrl: "/blogs/images/Pawna-Lake-Camping-Lonavala.webp"
        }
    ];

    blogContainer.innerHTML = ''; // Clear loading state

    posts.forEach(post => {
        const cardHTML = `
            <div class="w-[85vw] sm:w-full flex-shrink-0 snap-start h-full">
                <article class="h-full bg-white rounded-2xl shadow-md overflow-hidden hover:shadow-xl transition-all duration-300 group hover:-translate-y-2 flex flex-col border border-stone-100">
                    <!-- Image -->
                    <div class="relative h-56 sm:h-64 flex-shrink-0 overflow-hidden bg-stone-100">
                        <img src="${post.imageUrl}" alt="${post.title}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
                    </div>
                    <!-- Content -->
                    <div class="p-6 flex-1 flex flex-col justify-between">
                        <div>
                            <h3 class="text-xl font-bold text-stone-900 mb-3 font-display leading-tight group-hover:text-amber-700 transition-colors line-clamp-2">
                                ${post.title}
                            </h3>
                            <p class="text-stone-500 text-sm leading-relaxed mb-4 line-clamp-3">
                                ${post.excerpt}
                            </p>
                        </div>
                        <a href="${post.link}" class="inline-flex items-center text-stone-900 font-semibold text-sm hover:text-amber-700 transition-colors mt-auto">
                            Read More <svg class="w-3 h-3 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                            </svg>
                        </a>
                    </div>
                </article>
            </div>
        `;
        blogContainer.insertAdjacentHTML('beforeend', cardHTML);
    });
});
