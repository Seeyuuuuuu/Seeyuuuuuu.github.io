import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

target_html = '''<div class="ergo-col-right">
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
            </div>'''

replacement_html = '''<div class="ergo-col-right">
                <div class="ergo-section-header">
                    <h2>Mindmap</h2>
                </div>
                <div class="ergo-img-wrapper ergo-mindmap-img">
                    <img src="assets/Project-06/mindmap.png" alt="Mindmap" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-details">
                </div>
                <div class="ergo-design-point-group" style="margin-top: auto; padding-top: 80px;">
                    <div class="ergo-section-header">
                        <h2>Design point</h2>
                    </div>
                    <div class="ergo-img-wrapper ergo-design-point-img">
                        <img src="assets/Project-06/design-point.png" alt="Design points" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-details">
                    </div>
                </div>
            </div>'''

html = html.replace(target_html, replacement_html)
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=70"', html)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

target_css = '''.ergo-details-block {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: stretch;
    margin-bottom: 120px;
}'''

replacement_css = '''.ergo-details-block {
    display: grid;
    grid-template-columns: 65fr 35fr;
    gap: 60px;
    align-items: stretch;
    margin-bottom: 120px;
}'''

css = css.replace(target_css, replacement_css)

with open('style.css', 'w') as f:
    f.write(css)
