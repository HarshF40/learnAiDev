import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    original_image = Image.open(arg).convert("RGBA")  # Convert to RGBA to handle transparency
    base_image = Image.new("RGBA", original_image.size, (255, 255, 255, 255))  # Create a white background
    # Paste the original image onto the white background
    base_image.paste(original_image, (0, 0), original_image)  # Use original as mask
    images.append(base_image)
    
base_image = images[0]
for i in range(1, len(images)):
    images[i] = images[i].resize(base_image.size, Image.LANCZOS)
    
images[0].save(
    "catGif.gif", save_all = True, append_images = images[1:], duration=500, loop=0
)