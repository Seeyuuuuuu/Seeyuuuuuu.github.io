import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

research_html = '''
        <!-- Research Block -->
        <section class="responsive-block ergo-research-block">
            <div class="ergo-col-left">
                <div class="ergo-section-header">
                    <h2>Observation</h2>
                </div>
                <div class="ergo-img-wrapper">
                    <img src="assets/Project-06/observation.png" alt="Observation" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-research">
                </div>
            </div>
            <div class="ergo-col-right">
                <div class="ergo-section-header">
                    <h2>User research</h2>
                </div>
                <div class="ergo-img-wrapper">
                    <img src="assets/Project-06/user-research.png" alt="User research" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-research">
                </div>
            </div>
        </section>

        <!-- You May Also Like -->'''

html = html.replace('        <!-- You May Also Like -->', research_html)

# Add css version bump
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=60"', html)

# Fix the header class in ErgoSpace.html for the previous block so we can use a shared one
html = html.replace('ergo-problem-header', 'ergo-section-header')

with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

# Update CSS classes
css = css.replace('.ergo-problem-header h2', '.ergo-section-header h2')

ergo_research_css = '''
.ergo-research-block {
    margin-bottom: 120px;
    gap: 40px;
    align-items: start;
}
'''
css += ergo_research_css

with open('style.css', 'w') as f:
    f.write(css)
