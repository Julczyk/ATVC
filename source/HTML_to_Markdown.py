import html2text

def html_to_markdown(html_text):
    # Initialize the HTML to Markdown converter
    converter = html2text.HTML2Text()
    
    # Optionally, set the conversion options (e.g., remove_links=True to remove links)
    # converter.ignore_links = True

    # Convert the HTML to Markdown
    markdown_text = converter.handle(html_text)
    
    return markdown_text

# Example HTML text
html_text = """
<p>This is a <a href="https://example.com">link</a>.</p>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<h2>Header 2</h2>
<p>Some text.</p>
"""

# Convert HTML to Markdown
markdown_text = html_to_markdown(html_text)
print(markdown_text)