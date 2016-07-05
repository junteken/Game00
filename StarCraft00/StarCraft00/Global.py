import pygame, ResourceExtractor

gScreen=pygame.display.set_mode((1024,768))
clock=pygame.time.Clock()

gRsrcExtractor=ResourceExtractor.ResourceExtractor(['protoss_a', 'protoss_b', 'protoss_c'])

gCmdList=['IDLE', 'SELECT', 'MOVE', 'ATTACK']
gCmdListInt=(0, 1, 2, 3)
gCmdListDict=dict(zip(gCmdList, gCmdListInt))

