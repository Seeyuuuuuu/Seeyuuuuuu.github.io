with open('ErgoSpace.html', 'r') as f:
    html = f.read()

# The second row is:
# <div class="project-overview" style="margin-top: 48px;">
#     <div class="overview-left">
#         <h3>The Challenge</h3>...
#     </div>
#     <div class="overview-right">
#         <h3>The Solution</h3>...
#     </div>
# </div>

# Replace that specific overview-right with overview-left
target = '''                <div class="overview-right">
                    <h3>The Solution</h3>'''
replacement = '''                <div class="overview-left">
                    <h3>The Solution</h3>'''

html = html.replace(target, replacement)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
