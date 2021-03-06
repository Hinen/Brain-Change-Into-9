# -*- coding: utf-8 -*-

from tkinter import *
from datetime import *
import os

def importPyGame(errCount):
    try:
        if errCount < 2:
            import pygame
    except ImportError:
        print("Installing PyGame")
        os.system('pip install pygame')
        importPyGame(errCount + 1)

importPyGame(0)

from Script.Utility.SceneManager import *

class GameManager():
    _win = None

    _dt = 0
    _nowScene = None

    def __init__(self, win):
        self._win = win
        self._win.title("뇌를 9로 바꾸는 변환기")
        self._win.geometry("800x600")
        self._win.resizable(0, 0)

        # event bind
        self._win.bind('<Key>', self.pressKeyHandler)

        # scene init
        SceneManager.get(self._win, self.sceneChange).sceneChange(SceneType.INTRO)

        self.gameLoop()

    def sceneChange(self, newScene):
        if self._nowScene is not None:
            self._nowScene.destroy()

        self._nowScene = newScene

    def pressKeyHandler(self, key):
        self._nowScene.pressKeyHandler(key)

    def gameLoop(self):
        # calc dt
        now = datetime.now().timestamp()
        if self._dt == 0:
            self._dt = now

        updateDt = now - self._dt
        self._dt = now

        # scene update
        self._nowScene.update(updateDt)

        # loop
        self._win.after(10, self.gameLoop)

_win = Tk()
_gameManager = GameManager(_win)
_win.mainloop()