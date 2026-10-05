import re
with open('ErgoSpace.html') as f: html = f.read()
start = html.index('<!-- Details Block -->')
end = html.index('<!-- You May Also Like -->')
new_block = '''<!-- Details Block -->
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
                <div class="ergo-mindmap-area">
                    <div class="ergo-section-header">
                        <h2>Mindmap</h2>
                    </div>
                    <img src="assets/Project-06/mindmap.png" alt="Mindmap" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-details">
                </div>
                <div class="ergo-design-point-group">
                    <div class="ergo-section-header">
                        <h2>Design point</h2>
                    </div>
                    <div class="ergo-img-wrapper ergo-design-point-img">
                        <img src="assets/Project-06/design-point.png" alt="Design points" class="zoomable-img needs-flat-white-bg" data-gallery="ergo-details">
                    </div>
                </div>
            </div>
        </section>

        '''
html = html[:start] + new_block + html[end:]
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=71"', html)
with open('ErgoSpace.html','w') as f: f.write(html)

with open('style.css') as f: css = f.read()
css = css.replace('''    grid-template-columns: 65fr 35fr;
    gap: 60px;
    align-items: stretch;
    margin-bottom: 120px;
}''', '''    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: stretch;
    margin-bottom: 120px;
}''')
css += '''
/* Mindmap fills all leftover height of the right column, anchored top-right.
   The image is absolutely positioned so it never adds height to the row:
   the left column defines the row height. */
.ergo-mindmap-area {
    position: relative;
    flex: 1;
    min-height: 0;
}

.ergo-mindmap-area .ergo-section-header {
    position: relative;
    z-index: 2;
    pointer-events: none;
}

.ergo-mindmap-area > img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    object-position: top right;
    cursor: zoom-in;
}

.ergo-design-point-group {
    padding-top: 40px;
}

.ergo-design-point-group .ergo-section-header h2 {
    margin-bottom: 32px;
}

@media (max-width: 1024px) {
    .ergo-mindmap-area > img {
        position: static;
        height: auto;
    }
}
'''
with open('style.css','w') as f: f.write(css)
