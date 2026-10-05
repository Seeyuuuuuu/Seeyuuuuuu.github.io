import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

analysis_html = '''
        <!-- Analysis Block -->
        <section class="responsive-block ergo-research-block">
            <div class="ergo-col-left">
                <div class="ergo-section-header">
                    <h2>Project workflow</h2>
                    <p class="ergo-subtitle">——Take designers as an example</p>
                </div>
                <div class="ergo-img-wrapper">
                    <img src="assets/Project-06/project-workflow.png" alt="Project workflow" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-analysis">
                </div>
            </div>
            <div class="ergo-col-right">
                <div class="ergo-section-header">
                    <h2>Market analysis</h2>
                </div>
                <div class="ergo-img-wrapper">
                    <img src="assets/Project-06/market-analysis.png" alt="Market analysis" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-analysis">
                </div>
                <div class="ergo-findings">
                    <h3>Findings</h3>
                    <ul>
                        <li>At present, the most <strong>commonly used</strong> desks today are traditional multi-person desks.</li>
                        <li><strong>Existing</strong> offices desks <strong>cannot meet</strong> the individual working <strong>needs</strong> of employees.</li>
                        <li>The desks need to meet people's needs for <strong>cooperation, storage, creativity, privacy,</strong> etc.</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- You May Also Like -->'''

html = html.replace('        <!-- You May Also Like -->', analysis_html)

# Add css version bump
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=62"', html)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)

with open('style.css', 'r') as f:
    css = f.read()

ergo_analysis_css = '''
.ergo-subtitle {
    font-style: italic;
    color: #92a2a8;
    font-size: 16px;
    margin-top: -50px;
    margin-bottom: 50px;
}

.ergo-findings {
    margin-top: 64px;
}

.ergo-findings h3 {
    font-size: 32px;
    font-weight: 800;
    font-style: italic;
    color: #E28864;
    margin-bottom: 24px;
    letter-spacing: -0.5px;
}

.ergo-findings ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.ergo-findings li {
    position: relative;
    padding-left: 20px;
    margin-bottom: 20px;
    font-size: 15px;
    line-height: 1.6;
    color: #777;
}

.ergo-findings li::before {
    content: '●';
    position: absolute;
    left: 0;
    color: #E28864;
    font-size: 14px;
    top: 0;
}

.ergo-findings li strong {
    color: #333;
    font-weight: 700;
}
'''
css += ergo_analysis_css

with open('style.css', 'w') as f:
    f.write(css)
