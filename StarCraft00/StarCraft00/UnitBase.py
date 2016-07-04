import Global, pygame

class UnitSprite(pygame.sprite.Sprite):    
    def __init__(self,image,spriteinfo):
        pygame.sprite.Sprite.__init__(self)
        self.spriteinfoList= spriteinfo
        self.spritename=spriteinfo[0]
        self.currentFrame=1 #list의 1번부터 Rect객체이므로
        self.src_image=pygame.image.load(image)
        self.image= self.src_image.subsurface(spriteinfo[self.currentFrame]).convert()
        self.position= Global.gScreen.get_rect().center
        #self.src_image.set_colorkey(pygame.Color(72,72,88,0))
        #self.rgb=self.src_image.get_at((0,0))
        #self.position=position
        

    def update(self,deltat):
        # SIMULATION        
        self.currentFrame+=1
        if(self.currentFrame >= len(self.spriteinfoList) ):
            self.currentFrame=1
        self.image= self.src_image.subsurface(self.spriteinfoList[self.currentFrame]).convert()
        self.image.set_colorkey(pygame.Color(72,72,88))
        #self.image.set_colorkey(self.rgb)
        self.rect= self.position


class UnitBase(object):
    """UnitBase class"""
    name="N/A"
        
    def __init__(self, arg_name):
        #nonlocal __name,__SpriteList
        self.name=arg_name
        self.state= Global.gCmdListInt[0] #생성시 Idle state로 setting
        self.stateObject= [IdleState(), SelectState(), MoveState(), AttackState()]
        return super().__init__()

    def draw(self):
        raise NotImplementedError("UnitBase class must not be instantiated!!!")
    

class Protoss(UnitBase):
    """Protoss class"""

    def __init__(self, arg_name):                   
        return super().__init__(arg_name)

    def draw(self):        
        print('I am Protoss class',self.name)        

    shield=0

class Zealot(Protoss):
    """Zealot class"""
    
    #__SpriteList는 모든 객체가 공통으로 가지는 이미지 리소스이므로 class 변수(C++에서는 static에 해당)로 정의함    
    def __init__(self):
        self.name= 'zealot'        
        #해당 unit의 전체 sprite list를 가지는 변수
        self.SpriteList= UnitSprite( Global.gRsrcExtractor.GetUnitPngFileName(self.name), Global.gRsrcExtractor.GetSpriteInfo(self.name))
        #초기에는 전체 sprite list를 모두 그려주게 된다.
        self.drawList= self.SpriteList
        return super().__init__('zealot')

    def draw(self):
        print('I am {0} class'.format(self.name))
        self.StatusUpdate()
        return self.drawList

    def StatusUpdate(self):
        #자신의 상태에 맞게 행동을 계속 해야한다.
        print('I am {0} class'.format(self.name))

    def Move(self, targetXY, targetOb):
        print('Move cmd received')

    def Attack(self,targetXY, targetOb):
        print('Attack cmd received')

    def Select(self,fake_arg1, fake_arg2):
        print('Select cmd received')

    def Idle(self,fake_arg1, fake_arg2):
        print('UnSelect cmd received')

    CmdOpList=[Idle, Select, Move, Attack]

    def HandleCmd(self, Cmd, Unit, targetXY, targetOb):
        self.stateObject[self.state].handleInput(Cmd, self, targetXY, targetOb)

#gCmdList=['IDLE', 'SELECT', 'MOVE', 'ATTACK']
class IdleState(object):
    """UnitState class"""
    def handleInput(self, Cmd, Unit, targetXY, targetOb):
        if(Cmd == Global.gCmdList[Global.gCmdListDict['SELECT']]):#idle state는 오직 select state로만 이동 가능하다.
            Unit.state= Global.gCmdListDict[Cmd]
            Unit.CmdOpList[Unit.state](Unit, targetXY, targetOb)


class SelectState(object):
    """UnitState class"""
    def handleInput(self, Cmd, Unit, targetXY, targetOb):        
        Unit.state= Global.gCmdListDict[Cmd] #select state는 모든 state로 이동 가능
        Unit.CmdOpList[Unit.state](Unit, targetXY, targetOb)
        

class MoveState(object):
    """UnitState class"""
    def handleInput(self, Cmd, Unit, targetXY, targetOb):
        if(Cmd == Global.gCmdList[Global.gCmdListDict['ATTACK']]):#move state는 cmd를 받아서 갈수 있는 state는 오직 ATTACK만 가능
            Unit.state= Global.gCmdListDict[Cmd]
            Unit.CmdOpList[Unit.state](Unit, targetXY, targetOb)

class AttackState(object):
    """UnitState class"""
    def handleInput(self, Cmd, Unit, targetXY, targetOb):
        if(Cmd == Global.gCmdList[Global.gCmdListDict['MOVE']]):#attck state는 cmd를 받아서 갈수 있는 state는 오직 MOVE만 가능
            Unit.state= Global.gCmdListDict[Cmd]
            Unit.CmdOpList[Unit.state](Unit, targetXY, targetOb)