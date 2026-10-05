with open('style.css', 'r') as f:
    css = f.read()

target = '''.ergo-details-block .ergo-col-left .ergo-img-wrapper:last-child,
.ergo-details-block .ergo-col-right .ergo-img-wrapper:last-child {
    margin-top: auto;
}'''

css = css.replace(target, '')

with open('style.css', 'w') as f:
    f.write(css)

import re
with open('ErgoSpace.html', 'r') as f:
    html = f.read()
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=69"', html)
with open('ErgoSpace.html', 'w') as f:
    f.write(html)
