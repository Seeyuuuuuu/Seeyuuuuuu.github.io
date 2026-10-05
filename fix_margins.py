with open('style.css', 'r') as f:
    css = f.read()

target = '''.ergo-findings h3 {
    font-size: 32px;
    font-weight: 800;
    font-style: italic;
    color: #E28864;
    margin-bottom: 16px;
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
    margin-bottom: 14px;
    font-size: 13.5px;
    line-height: 1.5;
    color: #777;
}'''

replacement = '''.ergo-findings h3 {
    font-size: 32px;
    font-weight: 800;
    font-style: italic;
    color: #E28864;
    margin-bottom: 12px;
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
    margin-bottom: 8px;
    font-size: 13.5px;
    line-height: 1.4;
    color: #777;
}'''

css = css.replace(target, replacement)
with open('style.css', 'w') as f:
    f.write(css)

import re
with open('ErgoSpace.html', 'r') as f:
    html = f.read()
html = re.sub(r'href="style\.css(\?v=\d+)?"', 'href="style.css?v=65"', html)
with open('ErgoSpace.html', 'w') as f:
    f.write(html)
