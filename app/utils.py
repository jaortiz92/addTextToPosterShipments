import re
from re import Match
from typing import List
import pandas as pd
from pandas.core.frame import DataFrame
from .constants import Constants
from typing import Tuple
from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile
from PIL.ImageFont import FreeTypeFont


class Utils():

    @classmethod
    def generate_size(
            cls, text_one: str, text_two: str,
            font_one:FreeTypeFont, font_two:FreeTypeFont
        ) -> Tuple[int]:
        '''
            Estimate text size

            Parameters
            ----------
            text_one: str
                Text One to use
            text_two: str
                Text Two to use
            font_one:FreeTypeFont
                Font One to use with text one
            font_two:FreeTypeFont
                Font Two to use with text two

            Returns
            -------
            tuple(int):
                [0]: Size width in pixels
                [1]: Size height in pixels
                [2]: Size width in pixels to text One
        '''
        size_one: Tuple[int] = font_one.getbbox(text_one)
        size_two: Tuple[int] = font_two.getbbox(text_two)

        return (
            size_one[2] + size_two[2],
            max(size_one[3], size_two[3]),
            size_one[2],
        )
    
    @classmethod
    def generate_center_value(
            cls, width: int
        ) -> int:
        '''
            Calculate pixel to center value

            Parameters
            ----------
            width: int
                Width to text

            Returns
            -------
            int:
                Value 
        '''
        return int((Constants.IMAGE_SIZE[0] - width)/ 2)

    @classmethod
    def save_image(
            cls, name: str, image: PngImageFile
        ) -> None:
        '''
            Save image with new text in the folder

            Parameters
            ----------
            name: str
                Name to image's file
            image: PngImageFile
                Image

            Returns
            -------
            None
        '''
        image.save(Constants.OUT + name + '.png')