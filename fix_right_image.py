import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

# We need to add a class to the right image wrapper in the Analysis block
target_html = '''<div class="ergo-img-wrapper">
                    <img src="assets/Project-06/market-analysis.png" alt="Market analysis" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-analysis">
                </div>'''
replacement_html = '''<div class="ergo-img-wrapper right-analysis-img">
                    <img src="assets/Project-06/market-analysis.png" alt="Market analysis" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-analysis">
                </div>'''

html = html.replace(target_html, replacement_html)

# Also bump css
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=66"', html)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

# Add the right-analysis-img class
css += '''
.right-analysis-img {
    width: 85%; /* Make the image smaller to save vertical space */
}
'''
with open('style.css', 'w') as f:
    f.write(css)
