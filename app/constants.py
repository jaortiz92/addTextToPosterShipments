from typing import Tuple


class Constants:
    # PATH
    IN: str = './in/'
    BASE: str = 'base/'
    OUT: str = './out/'

        # In
    IMAGE_PATH: str = IN + BASE + 'ARTE-SIN-TITULOS.png'
    FONT_HI_PATH: str = IN + BASE + 'Raleway-Regular.ttf'
    FONT_NAME_PATH: str = IN + BASE + 'Raleway-SemiBoldItalic.ttf'
    FONT_TRANSPORT_PATH: str = IN + BASE + 'Raleway-Regular.ttf'
    FONT_GUIDE_PATH: str = IN + BASE + 'Century-Gothic-Bold.ttf'
    FONT_TITLE_PATH: str = IN + BASE + 'Raleway-SemiBold.ttf'
    FONT_DATE_PATH: str = IN + BASE + 'Raleway-Regular.ttf'
    FILE_TO_WORK: str = IN + 'Guias.xlsx'
        # Out
        
    # Default
    IMAGE_SIZE: Tuple[int] = (1200, 1800)

    # Parameters
        # Axis
    Y_NAME: int = 210
    Y_TRANSPORT: int = 485
    Y_GUIDE: int = 550
    Y_DATE: int = 640
        # Color
    COLOR_NAME: Tuple[int] = (39, 49, 121)
    COLOR_TRANSPORT: Tuple[int] = (246, 255, 255)
    COLOR_GUIDE: Tuple[int] = (246, 255, 255)
    COLOR_DATE: Tuple[int] = (246, 255, 255)
        # Size
    SIZE_NAME: int = 80
    SIZE_TRANSPORT: int = 60
    SIZE_GUIDE: int = 70
    SIZE_DATE: int = 60
        # Title
    TITLE_NAME: str = 'Hola '
    TITLE_TRANSPORT: str = 'Transportadora: '
    TITLE_GUIDE: str = 'Guía # '
    TITLE_DATE: str = 'Fecha de envío: '
