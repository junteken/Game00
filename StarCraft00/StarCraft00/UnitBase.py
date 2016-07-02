import Global, pygame, math

class UnitSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED=10
    MAX_REVERSE_SPEED=10
    ACCELERATION=2
    TURN_SPEED=5
    def __init__(self,image,position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image=pygame.image.load(image)
        self.position=position
        self.speed=self.direction=0
        self.k_left=self.k_right=self.k_down=self.k_up=0

    def update(self,deltat):
        # SIMULATION
        self.speed+=(self.k_up+self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed =-self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        x,y=self.position
        rad=self.direction*math.pi/180
        x+=-self.speed*math.sin(rad)
        y+=-self.speed*math.cos(rad)
        self.position=(x,y)
        self.image=pygame.transform.rotate(self.src_image,self.direction)
        self.rect=self.image.get_rect()
        self.rect.center=self.position


class UnitBase(object):
    """UnitBase class"""
    name="N/A"
        
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
    #__SpriteList는 모든 객체가 공통으로 가지는 이미지 리소스이므로 class 변수(C++에서는 static에 해당)로 정의함    
    SpriteList= UnitSprite('car.png' , Global.gScreen.get_rect().center)

    def __init__(sel):             
        return super().__init__('Zealot')

    def draw(self):
        print('I am {0} class'.format(self.name))
        return self.SpriteList

