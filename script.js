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

// Lightbox Gallery Logic
document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('imageLightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const closeBtn = document.querySelector('.lightbox-close');
    const prevBtn = document.querySelector('.lightbox-prev');
    const nextBtn = document.querySelector('.lightbox-next');
    
    if (lightbox && lightboxImg) {
        const allZoomableImages = Array.from(document.querySelectorAll('.zoomable-img, .trevo-blueprint-img, .synergy-img, .project-gallery img, .projecting-main-img, .conversion-img-wrapper img, .ecosystem-phones img, .empowering-bg, .woman-img, .visual-foundation-image img, .lowering-phones img'));
        
        let currentGroup = [];
        let currentIndex = 0;
        
        const updateArrowVisibility = () => {
            if (!prevBtn || !nextBtn) return;
            if (currentGroup.length <= 1) {
                prevBtn.style.display = 'none';
                nextBtn.style.display = 'none';
                return;
            }
            prevBtn.style.display = 'block';
            nextBtn.style.display = 'block';
            
            if (currentIndex === 0) {
                prevBtn.classList.add('disabled');
            } else {
                prevBtn.classList.remove('disabled');
            }
            
            if (currentIndex === currentGroup.length - 1) {
                nextBtn.classList.add('disabled');
            } else {
                nextBtn.classList.remove('disabled');
            }
        };

        const updateLightboxImage = (index) => {
            lightboxImg.style.opacity = 0.5;
            setTimeout(() => {
                const currentImg = currentGroup[index];
                lightboxImg.src = currentImg.src;
                if (currentImg.classList.contains('trevo-blueprint-img') || currentImg.classList.contains('needs-white-bg')) {
                    lightboxImg.classList.add('lightbox-white-bg');
                } else {
                    lightboxImg.classList.remove('lightbox-white-bg');
                }
                lightboxImg.style.opacity = 1;
            }, 150);
        };

        allZoomableImages.forEach((img) => {
            img.style.cursor = 'zoom-in';
            img.addEventListener('click', () => {
                const galleryName = img.getAttribute('data-gallery');
                if (galleryName) {
                    currentGroup = Array.from(document.querySelectorAll(`img[data-gallery="${galleryName}"]`));
                } else {
                    currentGroup = [img];
                }
                
                currentIndex = currentGroup.indexOf(img);
                
                updateArrowVisibility();
                
                if (img.classList.contains('trevo-blueprint-img') || img.classList.contains('needs-white-bg')) {
                    lightboxImg.classList.add('lightbox-white-bg');
                } else {
                    lightboxImg.classList.remove('lightbox-white-bg');
                }
                
                lightbox.style.display = 'flex';
                setTimeout(() => {
                    lightbox.classList.add('show');
                }, 10);
                lightboxImg.src = currentGroup[currentIndex].src;
                document.body.style.overflow = 'hidden';
            });
        });
        
        const closeLightbox = () => {
            lightbox.classList.remove('show');
            setTimeout(() => {
                lightbox.style.display = 'none';
            }, 300);
            document.body.style.overflow = 'auto';
        };
        
        const showNext = (e) => {
            if (e) e.stopPropagation();
            if (currentGroup.length > 1 && currentIndex < currentGroup.length - 1) {
                currentIndex++;
                updateLightboxImage(currentIndex);
                updateArrowVisibility();
            }
        };

        const showPrev = (e) => {
            if (e) e.stopPropagation();
            if (currentGroup.length > 1 && currentIndex > 0) {
                currentIndex--;
                updateLightboxImage(currentIndex);
                updateArrowVisibility();
            }
        };

        if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
        if (nextBtn) nextBtn.addEventListener('click', showNext);
        if (prevBtn) prevBtn.addEventListener('click', showPrev);
        
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                closeLightbox();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (lightbox.classList.contains('show')) {
                if (e.key === 'Escape') closeLightbox();
                if (e.key === 'ArrowRight' && currentGroup.length > 1 && currentIndex < currentGroup.length - 1) showNext();
                if (e.key === 'ArrowLeft' && currentGroup.length > 1 && currentIndex > 0) showPrev();
            }
        });
    }
});
