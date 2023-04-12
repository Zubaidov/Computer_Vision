import requests
from io import BytesIO
from PIL import Image

# set the number of images you want to download
num_images = 20

# set the desired width and height in pixels
width = 2048
height = 2048

# loop through the range of images you want to download
for i in range(num_images):
    try:
        # generate a random URL for the image
        url = f"https://source.unsplash.com/random/{width}x{height}"

        # make a request to the URL and get the image data
        response = requests.get(url)

        # create an image object from the image data
        img = Image.open(BytesIO(response.content))

        # save the image with a unique filename
        filename = f"image{i}.jpg"
        img.save(filename)

        print(f"Image {i+1} downloaded successfully!")

    except Exception as e:
        print(f"Error downloading image {i+1}: {e}")
