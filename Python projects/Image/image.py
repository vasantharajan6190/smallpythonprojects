from PIL import Image,ImageFilter

img = Image.open("./sample.jpg")
img.thumbnail((300,10))
img.save("sample24,png","png")
img.show()