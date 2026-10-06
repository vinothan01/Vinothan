from PIL import Image, ImageDraw, ImageFont

# Load the provided image
image_path = '/mnt/data/image.png'
original_image = Image.open(image_path)

# Prepare to add text annotations for length, width, and height
draw = ImageDraw.Draw(original_image)

# Define font and text color
try:
    font = ImageFont.truetype("arial", 20)  # Use a default font if Arial is not available
except IOError:
    font = ImageFont.load_default()

# Define positions for the labels
length_position = (200, 10)  # Top center for "Length"
width_position = (10, 100)   # Left center for "Width"
height_position = (200, 200) # Bottom center for "Height"

# Add text to the image
draw.text(length_position, "Length", fill="black", font=font)
draw.text(width_position, "Width", fill="black", font=font)
draw.text(height_position, "Height", fill="black", font=font)

# Save the annotated image
annotated_image_path = '/mnt/data/annotated_image.png'
original_image.save(annotated_image_path)

annotated_image_path