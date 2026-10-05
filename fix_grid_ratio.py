with open('style.css', 'r') as f:
    css = f.read()

target = '''.ergo-research-block {
    margin-bottom: 120px;
    gap: 40px;
    align-items: start;
}'''

replacement = '''.ergo-research-block {
    margin-bottom: 120px;
    gap: 40px;
    align-items: start;
}

/* Add an asymmetric grid modifier for the Analysis block */
.ergo-analysis-block {
    display: grid;
    grid-template-columns: 55fr 45fr;
    gap: 60px;
    align-items: stretch; /* So left and right columns share the exact same height */
    margin-bottom: 120px;
}

.ergo-analysis-block .ergo-col-right {
    display: flex;
    flex-direction: column;
}

.ergo-analysis-block .ergo-findings {
    margin-top: auto; /* Pushes the findings to the bottom */
}

@media (max-width: 1024px) {
    .ergo-analysis-block {
        grid-template-columns: 1fr;
    }
}
'''

css = css.replace(target, replacement)

with open('style.css', 'w') as f:
    f.write(css)

with open('ErgoSpace.html', 'r') as f:
    html = f.read()

html = html.replace('<section class="responsive-block ergo-research-block">', '<section class="responsive-block ergo-analysis-block">', 1)

with open('ErgoSpace.html', 'w') as f:
    f.write(html)
