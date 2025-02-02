import markdown

with open("example.md", "r") as md_file:
    md_text = md_file.read()
    html_text = markdown.markdown(md_text)

with open("example.html", "w") as html_file:
    html_file.write(html_text)

print("Markdown converted to HTML!")