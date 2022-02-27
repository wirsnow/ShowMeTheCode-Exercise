import os
import sys
from pathlib import Path
from PIL import Image

pic_path = Path(sys.path[0], "picture")

def repicturesize(picname):
    change = Image.open(Path(pic_path, picname))
    w,h = change.size
    if w > 640:
        x = w/640.0
        w = 640
        h = int(h/x)
    if h>1136:
        x = h/1136.0
        h = 1136
        w = int(w/x)
    change.resize((w,h),Image.ANTIALIAS).save(Path(pic_path, "_" + picname))
def main():
    for _, _, i in os.walk(pic_path):
        for pic in i:
            repicturesize(pic)
if __name__ == "__main__":
    main()
