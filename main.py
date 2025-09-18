from PIL import Image
import os

def imageToAscii(filename):
    scale = 8
    ascii_chars = list(" $.'`^\",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$@%#*+=-:. ")

    rawImage = Image.open(filename).convert("RGB")
    rawImage_width = rawImage.size[0]
    rawImage_height = rawImage.size[1]
    width = int(rawImage_width/scale)
    aspectRatio = 0.5
    height = int(rawImage_height / scale * aspectRatio)
    resizedImage = rawImage.resize((width, height))

    pixels = resizedImage.getdata()
    chars = []
    for pixel in pixels:
        r, g, b = pixel
        brightness = int(sum(pixel)/3)
        char = ascii_chars[int(brightness / 255 * (len(ascii_chars) - 1))]
        chars.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")

    ascii_image = "\n".join("".join(chars[i:i + width]) for i in range(0, len(chars), width))

    print(ascii_image)


for file in os.listdir("."):
    if file.lower().endswith((".jpg", ".png")):
        imageToAscii(file)
