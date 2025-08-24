from PIL import Image

filenames = ['oscar1.jpg', 'oscar2.jpg', 'oscar3.jpg', 'oscar4.jpg']
images = []

# Take size and mode from the first image
with Image.open(filenames[0]) as im:
    target_size = im.size
    mode = im.mode

# Resize and convert all images
for filename in filenames:
    with Image.open(filename) as im:
        resized = im.resize(target_size).convert(mode)
        images.append(resized)

# Save as animated GIF
images[0].save(
    'oscar.gif',
    save_all=True,               # <-- important for GIF
    append_images=images[1:],    # add remaining frames
    duration=500,                # 500ms per frame
    loop=0                       # infinite loop
)