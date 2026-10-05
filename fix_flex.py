with open('style.css', 'r') as f:
    css = f.read()

target = '''.ergo-analysis-block .ergo-col-right {
    display: flex;
    flex-direction: column;
}'''

replacement = '''.ergo-analysis-block .ergo-col-left,
.ergo-analysis-block .ergo-col-right {
    display: flex;
    flex-direction: column;
    height: 100%;
}

.ergo-analysis-block .ergo-col-left .ergo-img-wrapper {
    margin-top: auto; /* Pushes left image to the absolute bottom */
}'''

css = css.replace(target, replacement)
with open('style.css', 'w') as f:
    f.write(css)

import re
with open('ErgoSpace.html', 'r') as f:
    html = f.read()
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=67"', html)
with open('ErgoSpace.html', 'w') as f:
    f.write(html)
