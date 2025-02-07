#!/usr/bin/env python3
import pygame
from pygame.locals import *

pygame.init()
resolution = 480, 320
screen_mode = HWSURFACE
title = "Mangala"
fps = 20
color_black = 0, 0, 0
color_blue = 0, 0, 255
color_white = 255, 255, 255
color_red = 255, 0, 0
screen = pygame.display.set_mode(resolution, screen_mode)
pygame.display.set_caption(title)
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 35)
en = 60
boy = 60


def new_hole(x, y):
    return pygame.Rect(x, y, en, boy)


hk1 = [None] * 6
hk2 = [None] * 6
for i in range(0, 6):
    hk1[i] = new_hole(en * (i + 1), 180)
    hk2[i] = new_hole(en * (i + 1), 0)


def new_game():
    global s, first_player, game_ended
    s = ([4] * 6 + [0]) * 2
    first_player = True
    game_ended = False


new_game()


def hazne(count, x, y, k):
    kboy = k * boy
    pygame.draw.rect(screen, color_blue, (x, y, en, kboy))
    pygame.draw.rect(screen, color_white, (x, y, en, kboy), 1)
    text = font.render(str(count), 1, color_black)
    yx, yy = text.get_size()
    screen.blit(text, (x + en / 2 - yx / 2, y + kboy / 2 - yy / 2))


def create():
    hazne(s[6], 0, boy, 2)
    hazne(s[13], 60 * 7, boy, 2)
    for i in range(0, 6):
        ii = 5 - i
        hazne(s[ii], en * (i + 1), 0, 1)
        hazne(s[i + 7], en * (i + 1), 180, 1)
    if first_player:
        sirametin = "1"
    else:
        sirametin = "2"
    oyuncuyazi1 = font2.render("1.", 1, color_white)
    oyuncuyazi2 = font2.render("2.", 1, color_white)
    bilgi_yazi = font2.render(
        "Hamle sirasi " + sirametin + ". oyuncuda", 1, color_white
    )
    bx, by = bilgi_yazi.get_size()
    bilgi_yazi2 = font2.render("Y: Yeni Oyun ESC: Cikis", 1, color_white)
    bx2, by2 = bilgi_yazi2.get_size()
    screen.blit(oyuncuyazi1, ((resolution[0] - 35) / 2, 145))
    screen.blit(oyuncuyazi2, ((resolution[0] - 35) / 2, 60))
    screen.blit(bilgi_yazi, ((resolution[0] - bx) / 2, boy * 4 + 8))
    screen.blit(bilgi_yazi2, ((resolution[0] - bx2) / 2, boy * 4 + by + 16))


def end_of_game():
    if s[13] > s[6]:
        state = "Oyunu 1. oyuncu kazandi."
    elif s[13] < s[6]:
        state = "Oyunu 2. oyuncu kazandi."
    else:
        state = "Oyun berabere."

    end_text1 = font2.render(state, 1, color_red)
    x1, y1 = end_text1.get_size()
    end_text2 = font2.render(
        "1. Oyuncu: " + str(s[13]) + " 2. Oyuncu: " + str(s[6]), 1, color_blue
    )
    x2, y2 = end_text2.get_size()
    end_text3 = font2.render("Y: Yeni Oyun ESC: Cikis", 1, color_white)
    x3, y3 = end_text3.get_size()
    screen.blit(end_text1, ((resolution[0] - x1) / 2, (resolution[1] - y2) / 2 - y1))
    screen.blit(end_text2, ((resolution[0] - x2) / 2, (resolution[1] - y2) / 2))
    screen.blit(end_text3, ((resolution[0] - x3) / 2, (resolution[1] - y2) / 2 + y2))


timer = pygame.time.Clock()
is_end = False
while not is_end:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_end = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                is_end = True
            elif event.key == K_y:
                new_game()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if first_player:
                    for i in range(0, 6):
                        if hk1[i].collidepoint(event.pos):
                            gg = s[i + 7]
                            if gg != 0:
                                for jj in range(1, gg + 1):
                                    s[(i + 7 + jj) % 14] += 1
                                    s[i + 7] = 0
                                son = (i + 7 + jj) % 14
                                if son == 13:
                                    first_player = True
                                else:
                                    if son in range(0, 6):
                                        if s[son] % 2 == 0:
                                            s[13] += s[son]
                                            s[son] = 0
                                    else:
                                        if s[son] == 1:
                                            s[13] += s[12 - son] + 1
                                            s[son] = 0
                                            s[12 - son] = 0
                                    first_player = False
                                if sum(s[7:-1]) == 0:
                                    s[13] += sum(s[:6])
                                    s[:6] = [0] * 6
                                    game_ended = True
                else:
                    for i in range(0, 6):
                        if hk2[i].collidepoint(event.pos):
                            gg = s[5 - i]
                            if gg != 0:
                                for jj in range(1, gg + 1):
                                    s[(5 - i + jj) % 14] += 1
                                    s[5 - i] = 0
                                son = (5 - i + jj) % 14
                                if son == 6:
                                    first_player = False
                                else:
                                    if son in range(7, 13):
                                        if s[son] % 2 == 0:
                                            s[6] += s[son]
                                            s[son] = 0
                                    else:
                                        if s[son] == 1:
                                            s[6] += s[12 - son] + 1
                                            s[son] = 0
                                            s[12 - son] = 0
                                    first_player = True
                                if sum(s[:6]) == 0:
                                    s[6] += sum(s[7:-1])
                                    s[7:-1] = [0] * 6
                                    game_ended = True
    screen.fill(color_black)
    if game_ended == False:
        create()
    else:
        end_of_game()
    pygame.display.flip()
    timer.tick(fps)
