// Hotel Nightingale — Base Script
// Mobile nav toggle, sticky navbar scroll effect, alert dismissal

document.addEventListener('DOMContentLoaded', function () {
    // Mobile nav toggle
    const menuToggle = document.getElementById('menuToggle');
    const navMenu = document.getElementById('navMenu');

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function () {
            menuToggle.classList.toggle('active');
            navMenu.classList.toggle('open');
        });

        navMenu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                menuToggle.classList.remove('active');
                navMenu.classList.remove('open');
            });
        });
    }

    // Sticky navbar scroll effect
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 40) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Alert dismissal
    document.querySelectorAll('.alert-close').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const alert = btn.closest('.alert');
            if (alert) {
                alert.style.opacity = '0';
                setTimeout(function () {
                    alert.remove();
                }, 300);
            }
        });
    });

    // Auto-dismiss alerts after 6 seconds
    document.querySelectorAll('.alert').forEach(function (alert) {
        setTimeout(function () {
            alert.style.opacity = '0';
            setTimeout(function () {
                alert.remove();
            }, 300);
        }, 6000);
    });
});
