#!/usr/bin/python3
# -*-coding: utf8 -*-

import sys
import pygame
import random

pygame.init()

# Screen creation:
screen = pygame.display.set_mode((300, 300))


class Lab(list):

    """Labyrinth Class."""

    def __init__(self, fichier):
        """Constructor of this class"""
        self.fichier = fichier
        self.lab = []
        self.l_wall = []
        self.l_none = []
        self.config = 0
        self.wall = pygame.image.load('floor-tiles-20x20.png').convert()

    def generate_lab(self):
        """generate the labyrinth"""

        with open(self.fichier, "r") as fichier:
            config = []
            for raw in fichier:
                raw_lab = []
                for lettre in raw:
                    if lettre != '\n':
                        raw_lab.append(lettre)
                config.append(raw_lab)
            self.config = config

    def display_lab(self):
        """diplay the labyrinth, add rectangles of walls to l_wall and blacks rectangles to the l_none"""

        x = 0
        for row in self.config:
            y = 0
            for column in row:
                if column == 'm':
                    screen.blit(self.wall, (x * 20, y * 20), (100, 0, 20, 20))
                    self.l_wall.append(screen.blit(self.wall, (x * 20, y * 20), (100, 0, 20, 20)))
                if column == 'x':
                    screen.blit(self.wall, (x * 20, y * 20), (380, 0, 20, 20))
                    self.l_none.append(screen.blit(self.wall, (x * 20, y * 20), (380, 0, 20, 20)))
                if column == 'D':
                    screen.blit(self.wall, (x * 20, y * 20), (160, 20, 20, 20))
                if column == 'A':
                    screen.blit(self.wall, (x * 20, y * 20), (160, 20, 20, 20))
                y += 1
            x += 1


class Player(pygame.sprite.Sprite):
    """Player Class."""

    def __init__(self, departure):
        """Constructor of this class"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('MacGyver.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.speed_right = [20, 0]
        self.speed_left = [-20, 0]
        self.speed_up = [0, -20]
        self.speed_down = [0, 20]
        self.pos = self.rect.move(departure)
        self.obj1 = False
        self.obj2 = False

    def move_right(self):
        """move the player on the right."""

        self.pos = self.pos.move(self.speed_right)
        if self.pos.right >= 280:
            self.pos.right = 280

    def move_left(self):
        """move the player on the left."""

        self.pos = self.pos.move(self.speed_left)
        if self.pos.left <= 0:
            self.pos.left = 20

    def move_up(self):
        """move the player on the top."""

        self.pos = self.pos.move(self.speed_up)
        if self.pos.top <= 0:
            self.pos.top = 20

    def move_down(self):
        """move the player on the bottom."""

        self.pos = self.pos.move(self.speed_down)
        if self.pos.bottom >= 280:
            self.pos.bottom = 280

    def draw_me(self):
        """draw player."""

        screen.blit(self.image, self.pos)


class Labobject(pygame.sprite.Sprite):
    """Class for labyrinth objects."""

    def __init__(self, image, list):
        """Constructor of this class"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = random.choice(list)

    def my_rect(self):
        """return the rectangle of the object."""

        return screen.blit(self.image, self.pos)

    def erase_me(self):
        """clears the object on the screen"""

        self.image.fill((0, 0, 0, 0))


class Guardian(pygame.sprite.Sprite):
    """Class for the labyrinth guardian."""

    def __init__(self, arrival):
        """Constructor of this class"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Gardien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = self.rect.move(arrival)

    def erase_me(self):
        """clears the guardian on the screen."""

        self.rect = self.image.fill((0, 0, 0, 0))

    def my_rect(self):
        """return the rect of the object."""

        return screen.blit(self.image, self.pos)