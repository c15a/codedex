from PIL import Image

jpg_image = Image.open("jhin1.jpg")
jpg_image2 = Image.open("jhin2.jpg")

jpg_image.save("jhin1.png")
jpg_image2.save("jhin2.png")