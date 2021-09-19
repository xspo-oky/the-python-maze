#!/usr/bin/env python3

"""
The Python Maze

This is a simple maze game made in preperation to my GCSE project.

Author: Jack Jones
School: Stover School
Year: 11
Teacher: Ben Kerr
"""

import pygame
from pygame import mixer
import math
import sys
import time
import logging

# logging.basicConfig(filename='./log/info.log', filemode='w', format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.basicConfig(filename='./log/error.log', filemode='w', format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logging.basicConfig(filename='./log/debug.log', filemode='w', format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# initializing the constructor
pygame.init()
mixer.init()
logging.debug('constructor initialized')
stage = 1
logging.debug('stage variable set to 1')

# DEFINING GLOBAL VARIABLES

class widgetSettings:
    button = pygame.Rect(0,0,0,0)

class colours:
    white = (255, 255, 255)
    black = (0, 0, 0)
    grey = (90, 90, 90)

class images:
    bg = pygame.image.load('./images/bg/bg2.jpg')
    bgImgResize = pygame.transform.scale(bg, (1280,720))
    icon = pygame.image.load('./images/icon/the-python-maze-icon.png')
    welcomeBg = pygame.image.load('./images/bg/welcome.png')
    startButtonInactive = pygame.image.load('./images/buttons/start-inactive.png')
    startButtonActive = pygame.image.load('./images/buttons/start-active.png')
    quitButtonInactive = pygame.image.load('./images/buttons/quit-inactive.png')
    quitButtonActive = pygame.image.load('./images/buttons/quit-active.png')
    audioOn = pygame.image.load('./images/buttons/audio-on.png')
    audioOff = pygame.image.load('./images/buttons/audio-off.png')

class windowSettings:
    res = 1280, 720
    font = pygame.font.Font('./font/pixel-font.ttf', 30)

class settings:
    fps = 10
    fpsClock = pygame.time.Clock()
    speed = 3
    musicVolume = 0.7
    clock = pygame.time.Clock()
    mouse_pos = ""
    mixer.music.load('./sounds/music.mp3')
    mixer.music.set_volume(musicVolume)

class player:
    playerImg = pygame.image.load('./images/user/knight.png')
    playerImgResize = pygame.transform.scale(playerImg, (100, 100))
    playerX = 200
    playerY = 200
    playerX_change = 0
    playerY_change = 0

class widgets:
    # defining button structure
    def button(x,y,w,inactiveImage,activeImage,action=None):
        h = math.ceil(w/2.33)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        widgetSettings.button.width = w
        widgetSettings.button.height = h
        widgetSettings.button.x = x
        widgetSettings.button.y = y
        inactiveImageResize = pygame.transform.scale(inactiveImage, (w,h))
        activeImageResize = pygame.transform.scale(activeImage, (w,h))
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            window.blit(activeImageResize, (x,y))
            if click[0] == 1 and action != None:
                action()
        else:
            window.blit(inactiveImageResize, (x,y))
    # defining text box structure
    def textBox(msg,x,y,w,h,borderWidth,borderRadius,borderTopLeftRadius,borderTopRightRadius,borderBottomLeftRadius,borderBottomRightRadius,borderColour,adjustX,adjustY,colour,textColour):
        widgetSettings.button.width = w
        widgetSettings.button.height = h
        widgetSettings.button.x = x
        widgetSettings.button.y = y
        pygame.draw.rect(window, colour, (x,y,w,h))
        pygame.draw.rect(window, borderColour, (x-1,y-1,w+4,h+4), borderRadius, borderTopLeftRadius, borderTopRightRadius, borderBottomLeftRadius, borderBottomRightRadius)
        text = windowSettings.font.render(msg, True, textColour)
        center = ((x+(w/2)-adjustX)), y+((h/2)-adjustY)
        window.blit(text,center)

logging.debug('classes loaded')

# creates the screen and changes icon and initialized font
window = pygame.display.set_mode(windowSettings.res)
mixer.music.play()
audio = "on"
pygame.font.init()
icon = pygame.display.set_icon(images.icon)
if audio == "on":
    audioButton = "on"
elif audio == "off":
    audioButton = "off"

logging.debug('screen loaded, icon changed and initialized font')

def events():
    # keydown events
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.playerX_change -= settings.speed
            logging.debug('k_left pressed')
        elif event.key == pygame.K_RIGHT:
            player.playerX_change += settings.speed
            logging.debug('k_right pressed')
        elif event.key == pygame.K_UP:
            player.playerY_change -= settings.speed
            logging.debug('k_up pressed')
        elif event.key == pygame.K_DOWN:
            player.playerY_change += settings.speed
            logging.debug('k_down pressed')
    # keyup events
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            player.playerX_change = 0
            player.playerY_change = 0
            logging.debug('keyup (k_left,k_right,k_up,k_down)')
logging.debug('events function loaded')

def playerxy(x, y):
    window.blit(player.playerImgResize, (x, y))
logging.debug('playerxy function loaded')

def quitGame():
    logging.debug('GAME CLOSED')
    running = False
    pygame.quit()
    quit()
logging.debug('quitGame function loaded')

def gameStart():
    stage = 2
    logging.debug('stage set to 2')
logging.debug('gameStart function loaded')

def audioOn():
    mixer.music.unpause()
    audio = "on"

def audioOff():
    mixer.music.pause()
    audio = "off"

# runtime welcome screen
def welcome():

    mouse = pygame.mouse.get_pos()
    logging.debug('mouse variable assigned')
    window.blit(images.welcomeBg, (0, 0))
    logging.debug("background blit'd")
    pygame.display.set_caption('The Python Maze - Welcome')
    logging.debug("title set to 'The Python Maze - Welcome'")
    widgets.button(110,320,300,images.startButtonInactive,images.startButtonActive,gameStart)
    logging.debug('start button loaded')
    widgets.button(110,480,300,images.quitButtonInactive,images.quitButtonActive,quitGame)
    logging.debug('quit button loaded')
    if audioButton == "on":
        widgets.button(-20,60,170,images.audioOn,images.audioOn,audioOff)
    elif audioButton == "off":
        widgets.button(-20,60,170,images.audioOff,images.audioOff,audioOn)
    logging.debug('buttons loaded')

# main game screen
def main():
    window.blit(images.bgImgResize, (0, 0))
    logging.debug('background for main loaded')
    pygame.display.set_caption('The Python Maze')
    logging.debug("title set to 'The Python Maze'")
    playerxy(player.playerX, player.playerY)
    logging.debug('playerxy function called')

# RUNTIME
running = True
logging.debug('running variable set to True')
while running:
    logging.debug('stage = {}'.format(stage))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        events()
    logging.debug('quit event loaded inside loop')

    window.fill(colours.black)
    logging.debug('window fill set to colour-black')

    if stage == 1:
        welcome()
        logging.debug('welcome function called')
    elif stage == 2:
        main()
        logging.debug('main function called')

    # x change borders
    player.playerX += player.playerX_change
    if player.playerX <= 0:
        player.playerX = 0
    elif player.playerX >= 1100:
        player.playerX = 1100
    logging.debug('x change borders set')
    # y change borders
    player.playerY += player.playerY_change
    if player.playerY <= -12:
        player.playerY = -12
    elif player.playerY >= 535:
        player.playerY = 535
    logging.debug('y change borders set')

    pygame.display.update()
    logging.debug('display updated')
    settings.fpsClock.tick(settings.fps)