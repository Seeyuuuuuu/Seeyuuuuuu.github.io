with open('ErgoSpace.html', 'r') as f:
    html = f.read()

html = html.replace('<div class="project-overview" style="margin-top: 48px;">', '<div class="project-overview" style="margin-top: 80px;">')

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
