import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

# The block to move
solution_block = '''<h3 style="margin-top: 32px;">The Solution</h3>
                    <p>By seamlessly combining ergonomic knowledge with a modular architecture, I developed a customizable desk cabinet system that actively reduces people's work fatigue. The distinct modules—creative, collaborative, and privacy—can be easily reconfigured, empowering users to build their own workstation that supports their physical well-being and enhances productivity.</p>'''

# Remove from overview-left
html = html.replace(solution_block + '\n                </div>', '                </div>')

# Add to overview-right (after the meta-items)
target_right = '''                    <div class="meta-item">
                        <h4>Methods / Tools</h4>
                        <p>Rhino, KeyShot, AutoCAD, Adobe Illustrator</p>
                    </div>'''

new_right = target_right + '\n                    ' + solution_block

html = html.replace(target_right, new_right)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
