from pathlib import Path
from dataset_cleaner.reporting import get_images
from PIL import Image

def rename_images(folder, config):
    images = get_images(folder)
    temp_paths = []
    for i, img in enumerate(images, start=1):
        temp = folder / f"__temp_{i}{img.suffix}"
        img.rename(temp)
        temp_paths.append(temp)
    for i, temp in enumerate(temp_paths, start=1):
        final = folder / (str(i) + temp.suffix)
        temp.rename(final)

def crop_images(folder, config):
    ratio_split = config.aspect_ratio.split(":")
    target_ratio = int(ratio_split[0]) / int(ratio_split[1])
    output_folder = folder / "cropped"
    output_folder.mkdir(exist_ok=True)

    images = get_images(folder)
    for img_path in images:
        pil_img = Image.open(img_path)
        width, height = pil_img.size
        img_ratio = width / height
        if abs (img_ratio - target_ratio) > 0.01:
            new_width = height * target_ratio
            left = (width - new_width) // 2
            right = left + new_width
            top = 0
            bottom = height
            cropped_img = pil_img.crop((left, top, right, bottom))
            cropped_img.save(output_folder / img_path.name)
        else:
            pass