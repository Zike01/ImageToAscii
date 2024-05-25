from PIL import Image

ASCII_CHARS = "@#S%*+=-:. "  # black --> white


def resize_image(image, new_width=100):
    """resize image according to a new width"""
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def pixels_to_ascii(image):
    """Convert pixels to a string of ascii characters"""
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(new_width=100):
    # open an image from user input and convert to grayscale
    path = input("Path to image: ")
    
    try:
        img = Image.open("amongus.jpg").convert("L")
    except:
        print(f"{path} is not a valid pathname to an image")
    
    # convert image to ascii
    new_img_data = pixels_to_ascii(resize_image(img))
    
    # format 
    pixel_count = len(new_img_data)
    ascii_image = "\n".join(new_img_data[i:i+new_width] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)
    
    # save result 
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
        

if __name__ == "__main__":
    main()