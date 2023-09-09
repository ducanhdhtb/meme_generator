from Exceptions import InvalidFilePath
from PIL import Image, ImageFont, ImageDraw
import random
import os

class MemeEngine:
    """
    Class to generate actual meme files.

    Attributes:
        temp_dir (str): The directory path where produced meme files are stored.

    Methods:
        __init__(self, path):
            Initializes the MemeEngine instance with a directory path.

        make_meme(self, img_path, text, author, width=500) -> str:
            Generate a meme with the given image, text, and author.

    """

    def __init__(self, path):
        """
        Initializes the meme engine with a directory path where produced meme files are stored.

        Args:
            path (str): The directory path for storing generated meme files.

        """
        self.temp_dir = path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Generate a meme with the given image, text, and author.

        Args:
            img_path (str): The path to the source image file.
            text (str): The text to be added to the meme.
            author (str): The author's name to be added to the meme.
            width (int, optional): The width of the generated meme image (default is 500).

        Returns:
            str: The path to the generated meme image.

        Raises:
            InvalidFilePath: If the image path is invalid.

        """
        out_path = os.path.join(self.temp_dir, f"{random.randint(0, 1000000)}.png")

        if width >= 500:
            width = 500

        try:
            with Image.open(img_path) as img:
                ratio = img.height / img.width
                height = int(width * ratio)
                img = img.resize((int(width), height))
                font_size = int(height / 20)

                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("./_data/arial.ttf", font_size)

                cordinate_x = random.randint(0, int(img.width / 4))
                cordinate_y = random.randint(0, int(img.height - font_size * 2))

                draw.text((cordinate_x, cordinate_y), text, font=font, fill=(0, 0, 0))
                draw.text((int(cordinate_x * 1.2), cordinate_y + font_size), " - " + author, font=font)
                img.save(out_path)

        except (OSError, IOError):
            raise InvalidFilePath("Invalid image path")

        return out_path
