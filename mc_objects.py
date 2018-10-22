#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This is use to define the classe object
"""
import pygame

class McObjects():
    """
        This class is used to represent the objects that McGyver
        need to take
    """
    x_o, y_o = 0, 0

    def __init__(self, x_o, y_o, image, window):
        """
            Creating the object with coordinates, image and the window
        """
        self.x_o = x_o
        self.y_o = y_o
        self.image = image
        self.window = window

    def placeobj(self, wsol, wmurv, hmurh):
        """
            Placing the object according to the coordinates
        """
        self.window.blit(self.image, (self.x_o * wsol + wmurv * 2 / 3,
                                      self.y_o * wsol + hmurh * 2 / 3))

    def get_rect(self, wgrd, wwallv, hwallh):
        """
            Function that return the rectangle representing the object
        """    
        x = self.x_o * wgrd + wwallv * 2 / 3
        y = self.y_o * wgrd + hwallh * 2 / 3
        return pygame.Rect(x, y, wwallv, hwallh)

