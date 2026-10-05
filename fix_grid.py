with open('ErgoSpace.html', 'r') as f:
    html = f.read()

target = '''        <!-- Problem Block -->
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

replacement = '''        <!-- Problem Block -->
        <section class="responsive-block ergo-problem-block">
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
        </section>'''

html = html.replace(target, replacement)
with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

target_css = '''.ergo-problem-block {
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
    align-items: flex-end;
}'''

replacement_css = '''.ergo-problem-block {
    margin-top: 80px;
    margin-bottom: 120px;
    /* Overrides the default gap: 80px and align-items from responsive-block if needed */
    gap: 40px;
    align-items: flex-end;
}

.ergo-problem-header h2 {
    font-size: 42px;
    font-weight: 800;
    font-style: italic;
    color: #E28864; /* Coral orange matching mockup */
    margin-bottom: 64px;
    letter-spacing: -0.5px;
}'''

css = css.replace(target_css, replacement_css)
css = css.replace('.ergo-problem-grid {', '.ergo-problem-block {') # Catch any media query references
with open('style.css', 'w') as f:
    f.write(css)
