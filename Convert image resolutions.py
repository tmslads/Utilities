# Give it a folder with images and it'll give you images of a resolution you choose

import os
import time
import concurrent.futures
from PIL import Image


pics = r"C:\Users\Uncle Sam\Desktop\New folder"
output = r"C:\Users\Uncle Sam\Desktop\New folder\converted"
os.mkdir(output)
images = os.listdir(pics)
print(images)
new_size = (1920, 1080)

start = time.perf_counter()

# Takes img from org_assets, resizes, then saves it in sep folder.
def resizer(image):
    name = os.path.basename(image)[:-4]  # Gets name of file
    img = Image.open(f"{pics}\\{image}")
    img = img.resize(new_size, Image.ANTIALIAS)
    img.save(f"{output}\\{name}.jpg", quality=95)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(resizer, images)  # map(func, iterable)

end = time.perf_counter()
# Using threading this completes in ~0.8s, otherwise the code took over 3s to complete
print(end-start)
print("done")
