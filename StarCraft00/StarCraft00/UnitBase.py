import Global, pygame, math

class UnitSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED=10
    MAX_REVERSE_SPEED=10
    ACCELERATION=2
    TURN_SPEED=5
    def __init__(self,image,position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image=pygame.image.load(image)
        #self.src_image.set_colorkey(pygame.Color(72,72,88,0))
        #self.rgb=self.src_image.get_at((0,0))
        self.position=position
        

    def update(self,deltat):
        # SIMULATION
        print("Update is called")
        self.image= self.src_image.subsurface(pygame.Rect(0,320,128,128)).convert()
        self.image.set_colorkey(pygame.Color(72,72,88))
        #self.image.set_colorkey(self.rgb)
        self.rect= self.position


class UnitBase(object):
    """UnitBase class"""
    name="N/A"

    #__SpriteList는 모든 객체가 공통으로 가지는 이미지 리소스이므로 class 변수(C++에서는 static에 해당)로 정의함    
    SpriteList= UnitSprite('protoss_a.png' , Global.gScreen.get_rect().center)
        
    def __init__(self, arg_name):
        #nonlocal __name,__SpriteList
        self.name=arg_name
        return super().__init__()

    def draw(self):
        raise NotImplementedError("UnitBase class must not be instantiated!!!")


class Protoss(UnitBase):
    """Protoss class"""

    def __init__(self, arg_name):                   
        return super().__init__(arg_name)

    def draw(self):        
        print('I am Protoss class',self.name)
        return SpriteList

    shield=0

class Zealot(Protoss):
    """Zealot class"""
    def __init__(sel):             
        return super().__init__('Zealot')

    def draw(self):
        print('I am {0} class'.format(self.name))
        return self.SpriteList

class ResourceExtractor:
    """ResourceExtractor class"""
    def draw(self):
        print('I am ResourceExtractor class')

    def GetSpriteList(name):
        print('GetSpriteLsit is called')

            