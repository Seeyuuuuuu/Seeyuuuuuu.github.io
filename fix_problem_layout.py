import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

target = '''        <!-- Problem Block -->
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
        </section>'''

replacement = '''        <!-- Problem Block -->
        <section class="responsive-block ergo-problem-block">
            <div class="ergo-problem-grid">
                <div class="ergo-col-left">
                    <div class="ergo-problem-header">
                        <h2>Problem</h2>
                    </div>
                    <div class="ergo-img-wrapper">
                        <img src="assets/Project-06/problem-1.png" alt="Working space problems" class="zoomable-img" data-gallery="ergo-problem">
                    </div>
                </div>
                <div class="ergo-col-right">
                    <div class="ergo-img-wrapper">
                        <img src="assets/Project-06/problem-2.png" alt="Main reasons for using desk" class="zoomable-img" data-gallery="ergo-problem">
                    </div>
                </div>
            </div>
        </section>'''

html = html.replace(target, replacement)
with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

# I need to change align-items from center to flex-end in .ergo-problem-grid
css = css.replace('.ergo-problem-grid {\n    display: grid;\n    grid-template-columns: 1fr 1fr;\n    gap: 40px;\n    align-items: center;\n}', '.ergo-problem-grid {\n    display: grid;\n    grid-template-columns: 1fr 1fr;\n    gap: 40px;\n    align-items: flex-end;\n}')

with open('style.css', 'w') as f:
    f.write(css)
