with open('ErgoSpace.html', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<!-- Research Block -->' in line:
        # The next section should be ergo-research-block
        lines[i+1] = lines[i+1].replace('ergo-analysis-block', 'ergo-research-block')
    if '<!-- Analysis Block -->' in line:
        # The next section should be ergo-analysis-block
        lines[i+1] = lines[i+1].replace('ergo-research-block', 'ergo-analysis-block')

with open('ErgoSpace.html', 'w') as f:
    f.writelines(lines)
