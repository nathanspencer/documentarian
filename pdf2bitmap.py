import pypdfium2
import numpy as np

# Load the PDF
pdf = pypdfium2.PdfDocument("test.pdf")

# Render the first page to a NumPy array
page = pdf[0]
bitmap = page.render().to_numpy()

# Save raw bitmap data to a text file
with open("oncology-request-form.txt", "w") as file:
    # Write the shape
    file.write(f"Shape: {bitmap.shape}\n")
    
    # Write the raw pixel values (flattened for easier reading)
    np.savetxt(file, bitmap.reshape(-1, bitmap.shape[-1]), fmt="%d", delimiter=" ")