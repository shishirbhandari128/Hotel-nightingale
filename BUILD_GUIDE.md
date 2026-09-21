# AI Implementation Prompt & Specification: Hotel Nightingale Website

> **Instruction for the Implementing AI Agent:**  
> You are acting as a Senior Full-Stack Django Developer and Luxury UI/UX Designer. Your objective is to build the complete frontend and backend for **Hotel Nightingale**, a luxury boutique hotel website, according to the specifications below.
> 
> **Important Implementation Rule:**  
> Do not bundle all styles or scripts into single monolithic files. Maintain strict modularity: `base.html` must define `{% block extra_css %}` and `{% block extra_js %}`. Each distinct page must use its own dedicated CSS and JS files in `static/css/` and `static/js/`.

---

## 1. Project Context & Workspace Layout

* **Project Root:** `d:\Hotel Nightingale`
* **Django Project App:** `Hotel_Nightingale`
* **Core Application:** `core` (already registered in `INSTALLED_APPS`)
* **Target Directory Architecture:**

```text
d:\Hotel Nightingale\
├── Hotel_Nightingale\
│   ├── settings.py                 # Update: Static, Media, Email configurations
│   └── urls.py                     # Update: Include core.urls and static media routes
├── core\
│   ├── forms.py                    # Create: Contact & reservation inquiry form
│   ├── views.py                    # Update: Views for home, rooms, gallery, contact
│   └── urls.py                     # Update: URL patterns (home, rooms, gallery, contact)
├── templates\
│   ├── base.html                   # Create: Master layout (Header, Nav, Messages, Footer)
│   └── core\
│       ├── home.html               # Create: Hero, quick booking, story, featured suites
│       ├── rooms.html              # Create: Full accommodations list & room details
│       ├── gallery.html            # Create: Filterable photo gallery & lightbox
│       └── contact.html            # Create: Contact info & interactive form
└── static\
    ├── css\
    │   ├── base.css                # Create: Design tokens, typography, nav, footer, alerts
    │   ├── home.css                # Create: Hero, booking bar, story, preview cards
    │   ├── rooms.css               # Create: Room suites grid and amenity badges
    │   ├── gallery.css             # Create: Masonry gallery grid and lightbox modal
    │   └── contact.css             # Create: Split-panel contact & inquiry form styles
    ├── js\
    │   ├── base.js                 # Create: Mobile nav toggle, scroll effects, alert close
    │   ├── gallery.js              # Create: Category filter tabs and image lightbox
    │   └── contact.js              # Create: Date validation and form enhancements
    └── images\
        └── gallery\                # Directory for static hotel imagery
```

---

## 2. Design System & Aesthetics Specification

The visual identity must feel like a 5-star boutique retreat (quiet luxury, serene, timeless):

1. **Color Tokens:**
   * **Midnight Navy (`#0B131F` / `#111C2B`):** Header, dark banners, footer, deep contrast.
   * **Warm Alabaster (`#FAF8F5` / `#F4EFEA`):** Page backgrounds (avoid sterile `#FFFFFF` backgrounds).
   * **Pure White (`#FFFFFF`):** Cards, form containers, elevated surfaces.
   * **Champagne Gold (`#C5A880` / Hover: `#B3956B`):** Primary brand accent, CTA buttons, badges, icons.
   * **Text Colors:** Primary text in Deep Charcoal (`#1E293B`); secondary text in Muted Slate (`#64748B`).
   * **Borders:** Subtle warm hairlines (`#E8E2D9`).

2. **Typography (Google Fonts):**
   * **Headings:** `Cormorant Garamond` (Serif, weights: 400, 500, 600, 700).
   * **Body & Inputs:** `Plus Jakarta Sans` (Sans-serif, weights: 300, 400, 500, 600).
   * **Eyebrows / Subheadings:** Uppercase, letter-spaced `0.2em`, small font size (`0.75rem`).

---

## 3. Detailed Implementation Tasks

### Task 1: Django Settings Configuration (`Hotel_Nightingale/settings.py`)
- **Static & Media:**
  - Configure `STATICFILES_DIRS = [BASE_DIR / 'static']` and `STATIC_ROOT = BASE_DIR / 'staticfiles'`.
  - Configure `MEDIA_URL = '/media/'` and `MEDIA_ROOT = BASE_DIR / 'media'`.
- **Email Backend (Development Mode):**
  - Set `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'` so dispatched emails print clearly to the console during development.
  - Set `DEFAULT_FROM_EMAIL = 'Hotel Nightingale <concierge@hotelnightingale.com>'`.
  - Define `HOTEL_CONTACT_EMAIL = 'reservations@hotelnightingale.com'`.

---

### Task 2: Contact Form (`core/forms.py`)
Create a Django `Form` class named `ContactForm` with:
- **Fields:**
  - `full_name`: CharField with max length 120, placeholder, required.
  - `email`: EmailField, required.
  - `phone`: CharField, optional, max length 30.
  - `inquiry_type`: ChoiceField (General Inquiry, Room Reservation, Events, Concierge).
  - `check_in`: DateField (HTML5 `type="date"`), optional.
  - `check_out`: DateField (HTML5 `type="date"`), optional.
  - `guests`: IntegerField (min: 1, max: 10, default: 2).
  - `message`: Textarea with 5 rows, required.
  - `honeypot`: Hidden CharField for automated bot/spam detection (`clean_honeypot` raises ValidationError if populated).
- Apply appropriate CSS classes (`form-input`, `form-select`, `form-textarea`) in form widgets.

---

### Task 3: Views & Email Dispatch (`core/views.py`)
Implement the following views with mock data structures (to be migrated to database models later):
1. **`home(request)`**:
   - Provides featured suites (top 3 rooms) and preview gallery items (top 6 images).
   - Renders `core/home.html`.
2. **`rooms(request)`**:
   - Provides full list of rooms/suites with pricing, capacity, dimensions, features, and images.
   - Renders `core/rooms.html`.
3. **`gallery(request)`**:
   - Provides gallery items tagged with categories (`rooms`, `dining`, `wellness`, `architecture`).
   - Renders `core/gallery.html`.
4. **`contact(request)`**:
   - Supports both `GET` and `POST`.
   - On `GET`: Pre-populates dates/guests if query parameters are passed from the home quick-booking bar.
   - On `POST`: Validates `ContactForm`.
     - When valid: Sends formatted notification email to `HOTEL_CONTACT_EMAIL` via `django.core.mail.send_mail`.
     - Sends a polite acknowledgment confirmation email to the guest.
     - Adds a Django success message via `django.contrib.messages.success`.
     - Redirects back to `contact`.
     - If email dispatch fails, catches exception and logs a user-friendly error message via `messages.error`.

---

### Task 4: URL Routing (`core/urls.py` & `Hotel_Nightingale/urls.py`)
- **`core/urls.py`**:
  - `path('', views.home, name='home')`
  - `path('rooms/', views.rooms, name='rooms')`
  - `path('gallery/', views.gallery, name='gallery')`
  - `path('contact/', views.contact, name='contact')`
- **`Hotel_Nightingale/urls.py`**:
  - Include `core.urls`.
  - Add static and media URL patterns when `settings.DEBUG` is True.

---

### Task 5: Master Layout (`templates/base.html`)
- HTML5 document with Google Fonts and FontAwesome 6 CDN.
- Global announcement strip with phone, email, and social links.
- Fixed/sticky glassmorphic navbar (`#navbar`) with brand logo/crest, navigation links, and "Book Your Stay" CTA.
- Responsive mobile menu button (`#menuToggle`) and drawer menu (`#navMenu`).
- Django `messages` alert display container with dismiss buttons.
- Comprehensive footer with brand summary, quick links, amenities list, contact details, and copyright.
- **Strict Asset Slots:**
  - `<link rel="stylesheet" href="{% static 'css/base.css' %}">`
  - `{% block extra_css %}{% endblock %}` in `<head>`
  - `<script src="{% static 'js/base.js' %}"></script>`
  - `{% block extra_js %}{% endblock %}` right before `</body>`

---

### Task 6: Page Templates
Each template extends `base.html` and imports its specific CSS/JS files:

1. **`templates/core/home.html`**:
   - Injects `static/css/home.css`.
   - Hero section with high-contrast background overlay, luxury headline, and CTAs.
   - Quick booking bar (check-in date, check-out date, guests selector) submitting `GET` to the contact/inquiry page.
   - Story / Heritage section highlighting hotel history and signature highlights.
   - Featured Suites 3-column card grid with price badges and amenity tags.
   - Teaser gallery section with button linking to the full gallery.

2. **`templates/core/rooms.html`**:
   - Injects `static/css/rooms.css`.
   - Page banner with title and tagline.
   - Detailed vertical or grid layout of all suites with room dimensions, guest capacity, included amenities checklists, pricing, and direct inquiry buttons.

3. **`templates/core/gallery.html`**:
   - Injects `static/css/gallery.css` and `static/js/gallery.js`.
   - Page banner.
   - Filter pill buttons (`All`, `Rooms & Suites`, `Dining & Lounge`, `Wellness & Spa`, `Architecture & Grounds`).
   - Responsive photo grid with hover overlays and titles.
   - Lightbox modal markup (`#lightboxModal`) with full-screen dark backdrop, close button, image preview, and caption.

4. **`templates/core/contact.html`**:
   - Injects `static/css/contact.css` and `static/js/contact.js`.
   - Page banner.
   - Two-column layout:
     - Left column: Hotel concierge details, physical address, direct phone lines, emails, and check-in/out policies.
     - Right column: Clean Django form with CSRF token, honeypot field, field error highlights, and submit button.

---

### Task 7: Modular Stylesheets (`static/css/`)
Build separate, well-documented stylesheets:

1. **`base.css`**:
   - CSS variables (`--color-*`, `--font-*`, `--shadow-*`, `--transition`).
   - Modern reset and box-sizing.
   - Typography hierarchies (`h1`-`h6`, `.eyebrow`, `.lead-text`).
   - Button styles (`.btn-gold`, `.btn-outline-light`, `.btn-outline-dark`).
   - Sticky navbar styling with backdrop blur and mobile toggle styles.
   - Django alert toast cards (`.alert-success`, `.alert-error`).
   - Multi-column footer and copyright strip.
2. **`home.css`**:
   - Hero container, cinematic overlay, and typography.
   - Quick booking bar grid and input styles.
   - Story 2-column grid and floating heritage badge.
   - Room preview cards with hover zoom and floating price tags.
   - Teaser photo grid.
3. **`rooms.css`**:
   - Detailed accommodations cards, amenities checklists with check icons, and reservation call-to-actions.
4. **`gallery.css`**:
   - Filter button pill styling and active state indicators.
   - Masonry/grid layout for image cards with zoom on hover.
   - Lightbox modal styling (fixed position, backdrop blur, centered image, caption, close icon).
5. **`contact.css`**:
   - Split-panel grid layout.
   - Dark luxury theme for the info card with gilded icons.
   - White card container for the form with subtle shadows.
   - Inputs, select dropdowns, textareas, focus rings, and red validation error notices.

---

### Task 8: Modular JavaScript (`static/js/`)
1. **`base.js`**:
   - Hamburger menu toggle: opens/closes mobile navigation drawer.
   - Sticky navbar scroll handler: decreases navbar padding and adds drop-shadow on scroll.
   - Alert close listener: dismisses alert toasts on click.
2. **`gallery.js`**:
   - Filter buttons click handler: filters cards by `data-category` attribute.
   - Lightbox click handler: populates `#lightboxImg` and `#lightboxCaption`, opens modal.
   - Lightbox close handlers: modal close button, backdrop click, and `Escape` key listener.
3. **`contact.js`**:
   - Sets minimum check-in date to today (`new Date().toISOString().split('T')[0]`).
   - Dynamically updates check-out minimum date to at least 1 day after the selected check-in date.

---

### Task 9: Static Images & Fallbacks
- Create `static/images/` and `static/images/gallery/`.
- Ensure all template `<img>` tags have fallback `onerror` URLs pointing to curated Unsplash luxury architecture/hotel images, ensuring the UI looks rich immediately even before local photo assets are added.

---

## 4. Verification & Acceptance Criteria

When implementation is complete, the AI agent must verify:

1. **Navigation:** All links (`/`, `/rooms/`, `/gallery/`, `/contact/`) resolve with HTTP 200.
2. **Template Separation:** Inspecting the DOM of `/gallery/` shows `base.css` + `gallery.css` and `base.js` + `gallery.js`, without loading unnecessary `home.css` or `contact.css`.
3. **Interactive Features:**
   - Gallery filter buttons toggle visibility of cards seamlessly.
   - Clicking an image opens the Lightbox; pressing `ESC` or clicking the backdrop closes it.
   - Quick booking bar on the home page submits dates to `/contact/` and auto-fills the form fields.
4. **Email Dispatch:** Submitting the contact form:
   - Displays a green success banner on `/contact/`.
   - Outputs the formatted email with sender, recipient, and inquiry details to the running Django development terminal.
5. **Responsiveness:** Test layouts on mobile (< 768px) and desktop (> 1024px) for proper grid collapsing and hamburger menu function.
