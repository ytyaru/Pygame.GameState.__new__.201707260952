import pygame
from pygame.locals import *
from abc import ABCMeta, abstractmethod
class GameState(type, metaclass=ABCMeta):
    __stateSwitcher = None
    __command = None
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        attrs['__private'] = 'private value.'
        for a in args: print(a)
        for k,v in kwargs.items(): print(k,v)
        attrs['__stateSwitcher'] = cls.__NewStateSwitcher()
        attrs['__command'] = cls.__NewCommand()
        return super().__new__(cls, name, bases, attrs)
    @classmethod
    def __NewStateSwitcher(cls):
        if not cls.__stateSwitcher: cls.__stateSwitcher = 'StateSwitcher'
        return cls.__stateSwitcher
    @classmethod
    def __NewCommand(cls):
        if not cls.__command: cls.__command = 'Command'
        return cls.__command

    @abstractmethod
    def Initialize(self): raise NotImplementedError()
    @abstractmethod
    def Finalize(self): raise NotImplementedError()
    @abstractmethod
    def Event(self, event): raise NotImplementedError()
    @abstractmethod
    def Draw(self, screen): raise NotImplementedError()

class SelectState(metaclass=GameState):
    def Initialize(self): print('あみだくじ新規作成。')
    def Finalize(self): print('SelectState.Finalize')
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
    def Draw(self, screen): screen.fill((255,0,0))

s = SelectState()
print(dir(s))
