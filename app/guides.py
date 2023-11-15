import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from .constants import Constants

class Guides:
    def __init__(self) -> None:
        self.open_files()
        self.clean_file()


    def open_files(self) -> None:
        '''
            Open files to use

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        self.guides: DataFrame = pd.read_excel(
            Constants.FILE_TO_WORK,
            dtype={
                'GUIA': str
            }
        )

    def clean_file(self) -> None:
        '''
        This function clean guides file

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.guides['NOMBRE']: Series = self.guides['CLIENTE'].apply(
            lambda x: str(x).title().split()[0]
        )

        self.guides['TRANSPORTADORA']: Series = self.guides['TRANSPORTADORA'].apply(
            lambda x: str(x).upper()
        )

        self.guides['FECHA']: Series = self.guides['FECHA'].dt.strftime('%m/%d/%Y')
