with open('ErgoSpace.html', 'r') as f:
    html = f.read()

target1 = 'class="zoomable-img" data-gallery="ergo-problem"'
replacement1 = 'class="zoomable-img needs-flat-white-bg" data-gallery="ergo-problem"'

html = html.replace(target1, replacement1)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
