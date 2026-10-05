import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

details_html = '''
        <!-- Details Block -->
        <section class="responsive-block ergo-details-block">
            <div class="ergo-col-left">
                <div class="ergo-section-header">
                    <h2>Ergonomic research</h2>
                </div>
                <div class="ergo-img-wrapper">
                    <img src="assets/Project-06/ergonomic-research.png" alt="Ergonomic research" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-details">
                </div>
            </div>
            <div class="ergo-col-right">
                <div class="ergo-section-header">
                    <h2>Mindmap</h2>
                </div>
                <div class="ergo-img-wrapper ergo-mindmap-img">
                    <img src="assets/Project-06/mindmap.png" alt="Mindmap" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-details">
                </div>
                <div class="ergo-section-header" style="margin-top: 80px;">
                    <h2>Design point</h2>
                </div>
                <div class="ergo-img-wrapper ergo-design-point-img">
                    <img src="assets/Project-06/design-point.png" alt="Design points" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-details">
                </div>
            </div>
        </section>

        <!-- You May Also Like -->'''

html = html.replace('        <!-- You May Also Like -->', details_html)

# Add css version bump
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=68"', html)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

ergo_details_css = '''
/* Ergo Details Block */
.ergo-details-block {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: stretch;
    margin-bottom: 120px;
}

.ergo-details-block .ergo-col-left,
.ergo-details-block .ergo-col-right {
    display: flex;
    flex-direction: column;
    height: 100%;
}

.ergo-details-block .ergo-col-left .ergo-img-wrapper:last-child,
.ergo-details-block .ergo-col-right .ergo-img-wrapper:last-child {
    margin-top: auto;
}

@media (max-width: 1024px) {
    .ergo-details-block {
        grid-template-columns: 1fr;
    }
}
'''
css += ergo_details_css

with open('style.css', 'w') as f:
    f.write(css)
