from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
from PIL.ImageFont import FreeTypeFont
from .constants import Constants
from .utils import Utils

class ImageGuide:
    def __init__(
            self, name: str, transporter: str, guide: str, date: str
        ) -> None:
        self.name: str = name
        self.transporter: str = transporter
        self.guide: str = guide
        self.date: str = date
        self.open_image()
        self.add_texts()
        Utils.save_image(self.name, self.image)

    def open_image(self) -> None:
        '''
            Open image to use

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        self.image: PngImageFile = Image.open(Constants.IMAGE_PATH)
        self.draw: ImageDraw.ImageDraw = ImageDraw.Draw(self.image)

    def add_texts(self) -> None:
        '''
            add all texts to image

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        # Name
        self.add_one_text(
            Constants.FONT_HI_PATH,
            Constants.FONT_NAME_PATH,
            Constants.SIZE_NAME,
            Constants.TITLE_NAME,
            self.name,
            Constants.Y_NAME,
            Constants.COLOR_NAME
        )

        #Transport
        self.add_one_text(
            Constants.FONT_TITLE_PATH,
            Constants.FONT_TRANSPORT_PATH,
            Constants.SIZE_TRANSPORT,
            Constants.TITLE_TRANSPORT,
            self.transporter,
            Constants.Y_TRANSPORT,
            Constants.COLOR_TRANSPORT
        )

        #Guide
        self.add_one_text(
            Constants.FONT_GUIDE_PATH,
            Constants.FONT_GUIDE_PATH,
            Constants.SIZE_GUIDE,
            Constants.TITLE_GUIDE,
            self.guide,
            Constants.Y_GUIDE,
            Constants.COLOR_GUIDE
        )

        #Date
        self.add_one_text(
            Constants.FONT_TITLE_PATH,
            Constants.FONT_DATE_PATH,
            Constants.SIZE_DATE,
            Constants.TITLE_DATE,
            self.date,
            Constants.Y_DATE,
            Constants.COLOR_DATE
        )

    def add_one_text(
            self, font_path_one: str, font_path_two: str,
            size: int, text_one: str, text_two: str,
            y_value: int, color: Tuple[int]
        ) -> None:
        '''
            font_path_one: str
                Path to text one's font
            font_path_two: str
                Path to text two's font
            size: int
                Size to text's font
            text_one: str
                Text one
            text_two: str
                Text two
            y_value: int
                Position to y in the image
            color: Tuple[int]
                Color to use in the text

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''

        font_one: FreeTypeFont = ImageFont.truetype(font_path_one, size)
        
        font_two: FreeTypeFont = ImageFont.truetype(font_path_two, size)
        
        sizes: Tuple[int] = Utils.generate_size(
            text_one, text_two,
            font_one, font_two,
        )

        x_name: int = Utils.generate_center_value(sizes[0])

        self.draw.text(
            (x_name, y_value),
            text_one,
            font=font_one,
            fill=color
        )

        self.draw.text(
            (x_name + sizes[2], y_value),
            text_two,
            font=font_two,
            fill=color
        )