with open('ErgoSpace.html', 'r') as f:
    html = f.read()

# Fix the nested div structure
old_block = '''                </div>
            <div class="project-overview" style="margin-top: 48px;">
                <div class="overview-left">'''
new_block = '''                </div>
            </div>
            <div class="project-overview" style="margin-top: 48px;">
                <div class="overview-left">'''
html = html.replace(old_block, new_block)

# And remove the extra closing div at the end
old_end = '''                </div>
            </div>
            </div>
        </section>'''
new_end = '''                </div>
            </div>
        </section>'''
html = html.replace(old_end, new_end)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
