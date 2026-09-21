import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm

logger = logging.getLogger(__name__)

ROOMS = [
    {
        'slug': 'the-nightingale-suite',
        'name': 'The Nightingale Suite',
        'tagline': 'Our signature crown jewel',
        'price': 126000,
        'capacity': 2,
        'size_sqm': 85,
        'bed': '1 King Bed',
        'features': [
            'Private terrace with skyline view',
            'Freestanding soaking tub',
            'Personal concierge butler',
            'Champagne welcome service',
        ],
        'image': 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'slug': 'garden-terrace-room',
        'name': 'Garden Terrace Room',
        'tagline': 'Serene and light-filled',
        'price': 64000,
        'capacity': 2,
        'size_sqm': 55,
        'bed': '1 Queen Bed',
        'features': [
            'Private garden-view terrace',
            'Rainfall shower',
            'Complimentary minibar',
            'Egyptian cotton linens',
        ],
        'image': 'https://images.unsplash.com/photo-1611906655387-4353b60b587f?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'slug': 'executive-panorama-room',
        'name': 'Executive Panorama Room',
        'tagline': 'Refined comfort, elevated views',
        'price': 82500,
        'capacity': 3,
        'size_sqm': 62,
        'bed': '1 King or 2 Twin Beds',
        'features': [
            'Floor-to-ceiling city views',
            'Executive lounge access',
            'Nespresso coffee bar',
            'Marble ensuite bathroom',
        ],
        'image': 'https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'slug': 'royal-heritage-suite',
        'name': 'Royal Heritage Suite',
        'tagline': 'Timeless grandeur',
        'price': 166000,
        'capacity': 4,
        'size_sqm': 110,
        'bed': '1 King Bed + Living Room',
        'features': [
            'Separate living and dining area',
            'Private plunge pool access',
            '24-hour butler service',
            'Grand piano lounge',
        ],
        'image': 'https://images.unsplash.com/photo-1590490359683-658d3d23f972?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'slug': 'wellness-retreat-room',
        'name': 'Wellness Retreat Room',
        'tagline': 'A sanctuary for rest',
        'price': 72000,
        'capacity': 2,
        'size_sqm': 58,
        'bed': '1 Queen Bed',
        'features': [
            'In-room aromatherapy diffuser',
            'Direct spa wing access',
            'Yoga mat & wellness kit',
            'Herbal tea welcome tray',
        ],
        'image': 'https://images.unsplash.com/photo-1618773928121-c32242e63f39?auto=format&fit=crop&w=1200&q=80',
    },
    {
        'slug': 'skyline-penthouse',
        'name': 'Skyline Penthouse',
        'tagline': 'The pinnacle of indulgence',
        'price': 246000,
        'capacity': 4,
        'size_sqm': 150,
        'bed': '2 King Beds',
        'features': [
            'Panoramic wraparound terrace',
            'Private rooftop jacuzzi',
            'Dedicated events butler',
            'Bespoke in-suite dining',
        ],
        'image': 'https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=1200&q=80',
    },
]

GALLERY_ITEMS = [
    {
        'title': 'The Nightingale Suite',
        'category': 'rooms',
        'category_label': 'Rooms & Suites',
        'image': 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'Garden Terrace Room',
        'category': 'rooms',
        'category_label': 'Rooms & Suites',
        'image': 'https://images.unsplash.com/photo-1611906655387-4353b60b587f?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'The Lantern Room',
        'category': 'dining',
        'category_label': 'Dining & Lounge',
        'image': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'Rooftop Champagne Bar',
        'category': 'dining',
        'category_label': 'Dining & Lounge',
        'image': 'https://images.unsplash.com/photo-1470337458703-46ad1756a187?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'Serenity Spa',
        'category': 'wellness',
        'category_label': 'Wellness & Spa',
        'image': 'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'Infinity Pool',
        'category': 'wellness',
        'category_label': 'Wellness & Spa',
        'image': 'https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'Grand Facade',
        'category': 'architecture',
        'category_label': 'Architecture & Grounds',
        'image': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'The Grand Lobby',
        'category': 'architecture',
        'category_label': 'Architecture & Grounds',
        'image': 'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?auto=format&fit=crop&w=1000&q=80',
    },
    {
        'title': 'Sculpted Gardens',
        'category': 'architecture',
        'category_label': 'Architecture & Grounds',
        'image': 'https://images.unsplash.com/photo-1551918120-9739cb430c6d?auto=format&fit=crop&w=1000&q=80',
    },
]


def home(request):
    context = {
        'featured_rooms': ROOMS[:3],
        'preview_gallery': GALLERY_ITEMS[:6],
    }
    return render(request, 'core/home.html', context)


def rooms(request):
    context = {
        'rooms': ROOMS,
    }
    return render(request, 'core/rooms.html', context)


def gallery(request):
    context = {
        'gallery_items': GALLERY_ITEMS,
    }
    return render(request, 'core/gallery.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = f"New {data['inquiry_type'].title()} Inquiry from {data['full_name']}"
            body = (
                f"Full Name: {data['full_name']}\n"
                f"Email: {data['email']}\n"
                f"Phone: {data['phone'] or 'Not provided'}\n"
                f"Inquiry Type: {data['inquiry_type']}\n"
                f"Check-in: {data['check_in'] or 'Not specified'}\n"
                f"Check-out: {data['check_out'] or 'Not specified'}\n"
                f"Guests: {data['guests'] or 'Not specified'}\n\n"
                f"Message:\n{data['message']}"
            )
            try:
                send_mail(
                    subject=subject,
                    message=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.HOTEL_CONTACT_EMAIL],
                    fail_silently=False,
                )
                send_mail(
                    subject='We have received your inquiry — Hotel Nightingale',
                    message=(
                        f"Dear {data['full_name']},\n\n"
                        "Thank you for reaching out to Hotel Nightingale. "
                        "Our concierge team has received your inquiry and will "
                        "respond within 24 hours.\n\n"
                        "Warm regards,\nHotel Nightingale Concierge Team"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[data['email']],
                    fail_silently=False,
                )
                messages.success(
                    request,
                    'Thank you for your inquiry. Our concierge team will be in touch shortly.',
                )
            except Exception:
                logger.exception('Failed to send contact form emails')
                messages.error(
                    request,
                    'We could not send your inquiry at this time. Please try again later or call us directly.',
                )
            return redirect('contact')
    else:
        initial = {
            'check_in': request.GET.get('check_in'),
            'check_out': request.GET.get('check_out'),
            'guests': request.GET.get('guests', 2),
        }
        form = ContactForm(initial=initial)

    return render(request, 'core/contact.html', {'form': form})
