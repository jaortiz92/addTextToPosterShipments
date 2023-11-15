import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from .guides import Guides
from .imageGuide import ImageGuide
from .constants import Constants
from .utils import Utils

class App:
    def __init__(self) -> None:
        self.open_files()
        self.fit()
        


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
        self.guides: DataFrame = Guides().guides

    def fit(self) -> None:
        '''
            Use guide's data to add texts

            Parameters
            ----------
            None

            Returns
            -------
            None
        '''
        imagens: int = len(self.guides)
        print('Se crearan {} imagenes'.format(imagens))
        for i in self.guides.index:
            print('Generando imagen {} de {}'.format(i + 1, imagens))
            ImageGuide(
                self.guides.loc[i, 'NOMBRE'],
                self.guides.loc[i, 'TRANSPORTADORA'],
                self.guides.loc[i, 'GUIA'],
                self.guides.loc[i, 'FECHA'],
            )
        print('Proceso Completado')


