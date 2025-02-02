from weasyprint import HTML

# Convert to PDF
HTML(filename="example.html").write_pdf("pof.pdf")

print("PDF generated successfully!")