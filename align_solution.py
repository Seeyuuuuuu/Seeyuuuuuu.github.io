import re

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

# 1. Extract The Challenge block and remove it from the first overview-left
challenge_block = '''<h3 style="margin-top: 32px;">The Challenge</h3>
                    <p>Modern professionals frequently switch between tasks that require deep focus, teamwork, or brainstorming, often leading to physical and mental strain. The challenge was to design a versatile furniture system that adapts to these diverse work modes while effectively addressing the prolonged work fatigue associated with traditional, static office setups.</p>'''
html = html.replace(challenge_block, '')

# 2. Extract The Solution block and remove it from the first overview-right
solution_block = '''<h3 style="margin-top: 32px;">The Solution</h3>
                    <p>By seamlessly combining ergonomic knowledge with a modular architecture, I developed a customizable desk cabinet system that actively reduces people's work fatigue. The distinct modules—creative, collaborative, and privacy—can be easily reconfigured, empowering users to build their own workstation that supports their physical well-being and enhances productivity.</p>'''
html = html.replace(solution_block, '')

# Also remove the margin-top: 32px from both since they are now at the top of their own row
challenge_block = challenge_block.replace('<h3 style="margin-top: 32px;">', '<h3>')
solution_block = solution_block.replace('<h3 style="margin-top: 32px;">', '<h3>')

# 3. Create the new Row 2
new_row = f'''
            <div class="project-overview" style="margin-top: 48px;">
                <div class="overview-left">
                    {challenge_block.strip()}
                </div>
                <div class="overview-right">
                    {solution_block.strip()}
                </div>
            </div>'''

# 4. Insert the new row immediately after the first project-overview ends
pattern = r'(<div class="project-overview">.*?\s*</div>\s*</div>)'
html = re.sub(pattern, r'\1' + new_row, html, flags=re.DOTALL)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
