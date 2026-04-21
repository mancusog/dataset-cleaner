from pathlib import Path
from PIL import Image

FORMATS = ["*.jpg", "*.jpeg", "*.png", "*.webp"]

def get_images(folder: Path) -> list:
    images = []
    for fmt in FORMATS:
        images.extend(folder.glob(fmt))
    return images

def get_image_info(path: Path):
    img = Image.open(path)
    img_name = path.name
    img_size = img.size
    img_file_size = path.stat().st_size

    txt_path = path.parent / (path.stem + ".txt")
    has_caption = txt_path.exists()

    return img_name, img_size, img_file_size, has_caption

def print_info(folder: Path):
    images = get_images(folder)
    for img in images:
        img_name, img_size, img_file_size, has_caption = get_image_info(img)
        print(f"{img_name} | {img_size} | {img_file_size} bytes | caption: {has_caption}")

    