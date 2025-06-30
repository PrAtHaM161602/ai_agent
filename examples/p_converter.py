import PIL
from PIL import Image


def convert_to_black_and_white(image_path, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert('L')  # Convert to grayscale (black and white)
        img.save(output_path)
        print(f"Image successfully converted and saved to {output_path}")
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    input_image_path = "image.jpeg"  # Replace with the actual path to your image
    output_image_path = "black_and_white_image.png"  # Replace with the desired output path
    convert_to_black_and_white(input_image_path, output_image_path)
