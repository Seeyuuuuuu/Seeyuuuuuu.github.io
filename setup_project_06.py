import re

# ==========================================
# 1. CREATE ErgoSpace.html
# ==========================================
with open('interior-archive.html', 'r') as f:
    html = f.read()

# Update SEO / Titles
html = re.sub(r'<title>.*?</title>', '<title>ErgoSpace - Siyu Li</title>', html)
html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="An ergonomic desk cabinet set featuring creative, collaborative, and privacy modules to reduce work fatigue.">', html)
html = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="ErgoSpace - Siyu Li">', html)
html = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="An ergonomic desk cabinet set featuring creative, collaborative, and privacy modules to reduce work fatigue.">', html)

# Update Hero Image
html = html.replace('assets/Project-05/Project-05_Cover.png', 'assets/Project-06/Project-06_Cover.jpg')
html = html.replace('alt="Spatial Visions hero"', 'alt="ErgoSpace hero"')

# Update Header
html = html.replace('<h1>Spatial Visions</h1>', '<h1>ErgoSpace: Modular Workstation</h1>')
html = html.replace('<p class="subtitle">A curated collection of photorealistic 3D interior renderings exploring light, material, and spatial atmosphere.</p>', '<p class="subtitle">An ergonomic desk cabinet set featuring creative, collaborative, and privacy modules to reduce work fatigue.</p>')

# Replace Overview Left
old_left_pattern = r'<div class="overview-left">.*?</div>\s*<div class="overview-right">'
new_left = '''<div class="overview-left">
                    <h3>Overview</h3>
                    <p>Completed as my 2023 graduation project, this design introduces a highly adaptable desk cabinet set tailored for modern, dynamic work environments. It contains creative, collaborative, and privacy modules that allow users to build a personalized workstation to suit their specific needs.</p>
                    <h3 style="margin-top: 32px;">The Challenge</h3>
                    <p>Modern professionals frequently switch between tasks that require deep focus, teamwork, or brainstorming, often leading to physical and mental strain. The challenge was to design a versatile furniture system that adapts to these diverse work modes while effectively addressing the prolonged work fatigue associated with traditional, static office setups.</p>
                    <h3 style="margin-top: 32px;">The Solution</h3>
                    <p>By seamlessly combining ergonomic knowledge with a modular architecture, I developed a customizable desk cabinet system that actively reduces people's work fatigue. The distinct modules—creative, collaborative, and privacy—can be easily reconfigured, empowering users to build their own workstation that supports their physical well-being and enhances productivity.</p>
                </div>
                <div class="overview-right">'''
html = re.sub(old_left_pattern, new_left, html, flags=re.DOTALL)

# Replace Overview Right
old_right_pattern = r'<div class="overview-right">.*?</div>\s*</div>\s*</section>'
new_right = '''<div class="overview-right">
                    <div class="meta-item">
                        <h4>My Role</h4>
                        <p>Industrial Designer</p>
                    </div>
                    <div class="meta-item">
                        <h4>Duration</h4>
                        <p>2023 (Graduation Project)</p>
                    </div>
                    <div class="meta-item">
                        <h4>Methods / Tools</h4>
                        <p>Rhino, KeyShot, AutoCAD, Adobe Illustrator</p>
                    </div>
                </div>
            </div>
        </section>'''
html = re.sub(old_right_pattern, new_right, html, flags=re.DOTALL)

# Remove all Project 5 blocks between </section> and <!-- You May Also Like -->
pattern_blocks = r'(</section>[\s\n]*)(<!-- Study Room Design -->.*?)(<!-- You May Also Like -->)'
html = re.sub(pattern_blocks, r'\1\3', html, flags=re.DOTALL)

# Write out ErgoSpace.html
with open('ErgoSpace.html', 'w') as f:
    f.write(html)


# ==========================================
# 2. UPDATE index.html
# ==========================================
with open('index.html', 'r') as f:
    index_html = f.read()

new_card = '''        <a href="ErgoSpace.html" class="gallery-item large">
            <img src="assets/Project-06/Project-06_Cover.jpg" alt="ErgoSpace: Modular Workstation" loading="lazy">
            <div class="overlay">
                <h3>ErgoSpace: Modular Workstation</h3>
                <p>An ergonomic desk cabinet set featuring creative, collaborative, and privacy modules to reduce work fatigue.</p>
            </div>
        </a>
        
    </main>'''

index_html = index_html.replace('    </main>', new_card)

with open('index.html', 'w') as f:
    f.write(index_html)
