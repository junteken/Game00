import pygame,sys, Global, UnitBase
from pygame.locals import *
from Global import *


zealot= UnitBase.Zealot()
Unit_group= pygame.sprite.RenderPlain(zealot.draw())

while 1:
    #?USER?INPUT
    deltat=clock.tick(30)
    for event in pygame.event.get():
        if hasattr(event, 'key'):            
            if event.key==K_RIGHT: zealot.HandleCmd(gCmdList[0], zealot, '10, 10', 'hydra')
            elif event.key == K_LEFT: zealot.HandleCmd(gCmdList[1], zealot, '10, 10', 'hydra')
            elif event.key == K_UP: zealot.HandleCmd(gCmdList[2], zealot, '10, 10', 'hydra')
            elif event.key == K_DOWN: zealot.HandleCmd(gCmdList[3], zealot, '10, 10', 'hydra')
            elif event.key == K_ESCAPE: sys.exit(0)
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
