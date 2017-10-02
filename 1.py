import pygame
from pygame.locals import *
from abc import ABCMeta, abstractmethod
class GameInstance(type, metaclass=ABCMeta):
    def __new__(cls, name, bases, attrs):
        attrs['__private'] = 'private value.'
        return super().__new__(cls, name, bases, attrs)
    @abstractmethod
    def Initialize(self): raise NotImplementedError()
    @abstractmethod
    def Finalize(self): raise NotImplementedError()
    @abstractmethod
    def Event(self, event): raise NotImplementedError()
    @abstractmethod
    def Draw(self, screen): raise NotImplementedError()

class GameState(metaclass=GameInstance):
#class GameState(metaclass=GameInstance, metaclass=ABCMeta):
#class GameState(GameInstance, metaclass=ABCMeta):
#    def __new__(cls, ):
#    def __init__(self, stateSwitcher, command):
    """
    @abstractmethod
    def Initialize(self): raise NotImplementedError()
    @abstractmethod
    def Finalize(self): raise NotImplementedError()
    @abstractmethod
    def Event(self, event): raise NotImplementedError()
    @abstractmethod
    def Draw(self, screen): raise NotImplementedError()
    """
    pass

class SelectState(GameState):
#    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Initialize(self): print('あみだくじ新規作成。')
    def Finalize(self): print('SelectState.Finalize')
    def Event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
    def Draw(self, screen): screen.fill((255,0,0))

s = SelectState()
print(dir(s))
