from PIL import Image

# Open the image
img = Image.open("jhin1.png")
img2 = Image.open("jhin2.png")

# Resize the image
resized_img = img.resize((500, 500))  # Provide the new dimensions
resized_img2 = img2.resize((500, 500))

# Save the resized image
resized_img.save("jhin1_resize.png")
resized_img2.save("jhin2_resize.png")