import re
with open('style.css') as f: css = f.read()
css = css.replace('''.ergo-mindmap-area > img {
    position: absolute;
    inset: 0;''', '''.ergo-mindmap-area > img {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: -24px; /* let the mindmap dip slightly into the gap above "Design point" */''')
css = css.replace('''.ergo-design-point-group {
    padding-top: 40px;
}

.ergo-design-point-group .ergo-section-header h2 {
    margin-bottom: 32px;
}''', '''.ergo-design-point-group {
    position: relative;
    z-index: 2;
    padding-top: 0;
}

.ergo-design-point-group .ergo-section-header h2 {
    margin-bottom: 24px;
}''')
with open('style.css','w') as f: f.write(css)
with open('ErgoSpace.html') as f: html = f.read()
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=72"', html)
with open('ErgoSpace.html','w') as f: f.write(html)
