// Hotel Nightingale — Gallery Script
// Category filter tabs and image lightbox

document.addEventListener('DOMContentLoaded', function () {
    const filterButtons = document.querySelectorAll('.filter-pill');
    const galleryCards = document.querySelectorAll('.gallery-card');

    filterButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            filterButtons.forEach(function (btn) {
                btn.classList.remove('active');
            });
            button.classList.add('active');

            const filter = button.getAttribute('data-filter');

            galleryCards.forEach(function (card) {
                if (filter === 'all' || card.getAttribute('data-category') === filter) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });

    // Lightbox
    const lightboxModal = document.getElementById('lightboxModal');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const lightboxClose = document.querySelector('.lightbox-close');

    function openLightbox(card) {
        const img = card.querySelector('img');
        const title = card.querySelector('h3');

        if (lightboxImg && img) {
            lightboxImg.src = img.src;
            lightboxImg.alt = img.alt;
        }
        if (lightboxCaption && title) {
            lightboxCaption.textContent = title.textContent;
        }
        if (lightboxModal) {
            lightboxModal.classList.add('open');
        }
        document.body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        if (lightboxModal) {
            lightboxModal.classList.remove('open');
        }
        document.body.style.overflow = '';
    }

    galleryCards.forEach(function (card) {
        card.addEventListener('click', function () {
            openLightbox(card);
        });
    });

    if (lightboxClose) {
        lightboxClose.addEventListener('click', closeLightbox);
    }

    if (lightboxModal) {
        lightboxModal.addEventListener('click', function (event) {
            if (event.target === lightboxModal) {
                closeLightbox();
            }
        });
    }

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && lightboxModal && lightboxModal.classList.contains('open')) {
            closeLightbox();
        }
    });
});
