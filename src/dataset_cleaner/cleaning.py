from pathlib import Path
from dataset_cleaner.reporting import get_images

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