from rembg import remove
from PIL import Image
import io

# Define input and output paths
input_path = 'input_image.jpg'
output_path = 'output_image.png'

# Open the image
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the result
# Note: Output is saved as PNG to preserve transparency
output_image.save(output_path)

print(f"Success! Background removed and saved to {output_path}")