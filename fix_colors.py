with open('ErgoSpace.html', 'r') as f:
    html = f.read()

target = '''            <div class="project-overview" style="margin-top: 48px;">
                <div class="overview-left">
                    <h3>The Challenge</h3>
                    <p>Modern professionals frequently switch between tasks that require deep focus, teamwork, or brainstorming, often leading to physical and mental strain. The challenge was to design a versatile furniture system that adapts to these diverse work modes while effectively addressing the prolonged work fatigue associated with traditional, static office setups.</p>
                </div>
                <div class="overview-left">
                    <h3>The Solution</h3>
                    <p>By seamlessly combining ergonomic knowledge with a modular architecture, I developed a customizable desk cabinet system that actively reduces people's work fatigue. The distinct modules—creative, collaborative, and privacy—can be easily reconfigured, empowering users to build their own workstation that supports their physical well-being and enhances productivity.</p>
                </div>
            </div>'''

replacement = '''            <div class="project-overview" style="margin-top: 48px;">
                <div class="overview-left">
                    <h3 style="color: #1a1a1a;">The Challenge</h3>
                    <p style="color: #444;">Modern professionals frequently switch between tasks that require deep focus, teamwork, or brainstorming, often leading to physical and mental strain. The challenge was to design a versatile furniture system that adapts to these diverse work modes while effectively addressing the prolonged work fatigue associated with traditional, static office setups.</p>
                </div>
                <div class="overview-left">
                    <h3 style="color: #1a1a1a;">The Solution</h3>
                    <p style="color: #444;">By seamlessly combining ergonomic knowledge with a modular architecture, I developed a customizable desk cabinet system that actively reduces people's work fatigue. The distinct modules—creative, collaborative, and privacy—can be easily reconfigured, empowering users to build their own workstation that supports their physical well-being and enhances productivity.</p>
                </div>
            </div>'''

html = html.replace(target, replacement)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
