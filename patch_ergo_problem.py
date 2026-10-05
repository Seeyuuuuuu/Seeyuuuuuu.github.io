import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

problem_html = '''
        <!-- Problem Block -->
        <section class="responsive-block ergo-problem-block">
            <div class="ergo-problem-header">
                <h2>Problem</h2>
            </div>
            <div class="ergo-problem-grid">
                <div class="ergo-img-wrapper">
                    <img src="assets/Project-06/problem-1.png" alt="Working space problems" class="zoomable-img" data-gallery="ergo-problem">
                </div>
                <div class="ergo-img-wrapper">
                    <img src="assets/Project-06/problem-2.png" alt="Main reasons for using desk" class="zoomable-img" data-gallery="ergo-problem">
                </div>
            </div>
        </section>

        <!-- You May Also Like -->'''

html = html.replace('        <!-- You May Also Like -->', problem_html)

# Add css version bump (if it has one)
# Wait, let's just make sure ErgoSpace uses the latest CSS
# It might already have v=... let's replace it with v=59
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=59"', html)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

ergo_css = '''
/* ==========================================================================
   Project 06: ErgoSpace
   ========================================================================== */

.ergo-problem-block {
    margin-top: 80px;
    margin-bottom: 120px;
}

.ergo-problem-header h2 {
    font-size: 42px;
    font-weight: 800;
    font-style: italic;
    color: #E28864; /* Coral orange matching mockup */
    margin-bottom: 64px;
    letter-spacing: -0.5px;
}

.ergo-problem-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    align-items: center;
}

.ergo-img-wrapper {
    width: 100%;
}

.ergo-img-wrapper img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.4s ease, opacity 0.4s ease;
    cursor: zoom-in;
}

.ergo-img-wrapper img:hover {
    transform: translateY(-8px) scale(1.02);
    position: relative;
    z-index: 10;
}

@media (max-width: 1024px) {
    .ergo-problem-grid {
        grid-template-columns: 1fr;
        gap: 40px;
    }
}
'''

css += ergo_css

with open('style.css', 'w') as f:
    f.write(css)
