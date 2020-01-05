import os
import sys
from PIL import Image

copyfolder = sys.argv[1]
pastefolder= sys.argv[2]

if not os.path.exists(pastefolder):
	os.makedirs(pastefolder)

for photos in os.listdir(copyfolder):
	img =Image.open(f"{copyfolder}{photos}")
	cleanname = os.path.splitext(photos)[0]
	img.save(f"{pastefolder}{cleanname}.png","png")
	print("All done")