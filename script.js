document.addEventListener('DOMContentLoaded', () => {
    const backToTopBtn = document.getElementById('backToTop');

    const header = document.querySelector('.header');

    // Show/hide back to top button and header divider based on scroll position
    window.addEventListener('scroll', () => {
        if (window.scrollY > 0) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        if (window.scrollY > 300) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    // Smooth scroll to top when button is clicked
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenuClose = document.querySelector('.mobile-menu-close');
    const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

    if (mobileMenuBtn && mobileMenuClose && mobileMenuOverlay) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenuOverlay.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        });

        mobileMenuClose.addEventListener('click', () => {
            mobileMenuOverlay.classList.remove('active');
            document.body.style.overflow = '';
        });

        mobileNavLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuOverlay.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // Project & About Hero Smooth Snap Logic
    const snapTarget = document.querySelector('.project-info') || document.querySelector('.about-content');
    if (snapTarget) {
        let isSnapping = false;
        let snapComplete = false;
        let releaseTimeout;
        
        window.addEventListener('wheel', (e) => {
            if (isSnapping) {
                e.preventDefault(); // Block scrolling during animation
                
                // If animation has finished but user is still scrolling (e.g. trackpad momentum),
                // we keep resetting the lock until they completely stop for 100ms.
                if (snapComplete) {
                    clearTimeout(releaseTimeout);
                    releaseTimeout = setTimeout(() => {
                        isSnapping = false;
                        snapComplete = false;
                    }, 100);
                }
                return;
            }
            
            // If near the very top and scrolling down
            if (window.scrollY < 20 && e.deltaY > 0) {
                e.preventDefault();
                isSnapping = true;
                snapComplete = false;
                
                const targetPosition = snapTarget.getBoundingClientRect().top + window.scrollY;
                
                // Slow scroll (1.2 seconds) to target
                smoothScrollTo(targetPosition, 1200);
            }
        }, { passive: false });

        function smoothScrollTo(targetPosition, duration) {
            const startPosition = window.scrollY;
            const distance = targetPosition - startPosition;
            let startTime = null;

            function animation(currentTime) {
                if (startTime === null) startTime = currentTime;
                const timeElapsed = currentTime - startTime;
                const progress = Math.min(timeElapsed / duration, 1);
                
                // Ease-in-out curve
                const ease = progress < 0.5 
                    ? 2 * progress * progress 
                    : -1 + (4 - 2 * progress) * progress;

                window.scrollTo(0, startPosition + distance * ease);

                if (timeElapsed < duration) {
                    requestAnimationFrame(animation);
                } else {
                    snapComplete = true;
                    // Initial release timeout in case there's no residual momentum
                    releaseTimeout = setTimeout(() => {
                        isSnapping = false;
                        snapComplete = false;
                    }, 200);
                }
            }

            requestAnimationFrame(animation);
        }
    }

    // Protect Images: Disable Right-Click and Dragging
    document.addEventListener('contextmenu', (e) => {
        if (e.target.tagName === 'IMG') {
            e.preventDefault();
        }
    });

    document.addEventListener('dragstart', (e) => {
        if (e.target.tagName === 'IMG') {
            e.preventDefault();
        }
    });
});
