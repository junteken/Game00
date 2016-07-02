import pygame,sys, Global, UnitBase
from pygame.locals import *
from Global import *


rrr= UnitBase.ResourceExtractor()
rrr.GetSpriteInfoList('protoss_a.txt')
rrr.PrintList();
arbiter_sprite=rrr.GetSpriteInfo('arbiter')
print(arbiter_sprite)

zealot= UnitBase.Zealot()
Unit_group= pygame.sprite.RenderPlain(zealot.draw())

while 1:
    #?USER?INPUT
    deltat=clock.tick(30)
    for event in pygame.event.get():
        if hasattr(event, 'key'):
            print('key clicked')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            zealot.draw().position = pygame.mouse.get_pos()

            print('mouse clicked')
        else:
            continue
    #?RENDERING
    gScreen.fill((0,0,0))   
    Unit_group.update(deltat)
    Unit_group.draw(gScreen)
    pygame.display.flip()
