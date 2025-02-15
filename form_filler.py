import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the form image using OpenCV
image_path = "test.png"  
form_image = cv2.imread(image_path)

# Convert to grayscale for better OCR detection
gray = cv2.cvtColor(form_image, cv2.COLOR_BGR2GRAY)

# Apply OCR to detect text positions
custom_oem_psm_config = r'--oem 3 --psm 6'  
data = pytesseract.image_to_data(gray, config=custom_oem_psm_config, output_type=pytesseract.Output.DICT)

# ✅ Convert OpenCV (NumPy array) to PIL Image for drawing
pil_image = Image.fromarray(cv2.cvtColor(form_image, cv2.COLOR_BGR2RGB))

# Create a drawing object
draw = ImageDraw.Draw(pil_image)
font = ImageFont.load_default()  

# Iterate through detected text boxes
for i in range(len(data['text'])):
    text = data['text'][i].strip()
    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]

    # Check for empty text fields
    if text == "":  
        print(f"Filling empty field at ({x}, {y}) with 'Nathan'")
        draw.text((x + 5, y + 5), "Nathan", fill=(0, 0, 0), font=font)  

# ✅ Convert PIL image back to OpenCV format (if needed)
form_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# Save the modified image
output_path = "filled_form.png"
cv2.imwrite(output_path, form_image)

# Show the modified form
pil_image.show()

print(f"Form successfully filled and saved as '{output_path}'.")