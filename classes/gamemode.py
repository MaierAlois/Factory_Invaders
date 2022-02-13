# from character import *
from element import *


class GameMode:
    
    def __init__(self, colsElement, nbCols = 4):
        self._colsElement = [[] for x in range(nbCols)]
        
    def addElement(self, element):
        self._colsElement.append(element)
        
    def delElement(self, element):
        element.destroy()
        self._colsElement.remove(element)