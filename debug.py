from pathlib import Path

all_images = []

for path in Path('datasets/OASIS/images').rglob('*.jpg'):
    all_images.append(str(path))

for path in Path('datasets/GAPED').rglob('*.bmp'):
    all_images.append(str(path))


print(all_images)
