import Global, pygame, math

class UnitSprite(pygame.sprite.Sprite):    
    def __init__(self,image,position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image=pygame.image.load(image)
        #self.src_image.set_colorkey(pygame.Color(72,72,88,0))
        #self.rgb=self.src_image.get_at((0,0))
        #self.position=position
        

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

    shield=0

class Zealot(Protoss):
    """Zealot class"""
        
    #__SpriteList는 모든 객체가 공통으로 가지는 이미지 리소스이므로 class 변수(C++에서는 static에 해당)로 정의함
        
    SpriteList= UnitSprite('protoss_a.png' , Global.gScreen.get_rect().center)

    def __init__(self):             
        self.SpriteList= UnitSprite('protoss_a.png' , Global.gScreen.get_rect().center)
        return super().__init__('Zealot')

    def draw(self):
        print('I am {0} class'.format(self.name))
        return self.SpriteList

class ResourceExtractor:
    """ResourceExtractor class"""    

    def __init__(self):        
        self.entirelist=[] #entirelist 구조 : {'unitname', Rect[0], Rect[1], Rect[2], ...Rect[N]}

    def GetUnitName(self, name):
        i=0
        for c in name:
            if(c.isdigit()):
                i+=1
        return name[:len(name)-i]

    def GetSpriteInfoList(self, filename):
        print('GetSpriteInfoList is called')
        file= open(filename, 'r');
        #현재 읽어 들이는 unitname이랑 기존의 unitname을 비교해서 새로운 list item을 생성하기 위해 비교하는 변수
        unitname=self.GetUnitName(file.readline().split(' ')[0])
        templist=[]
        templist.append(unitname)

        for line in file:
            linestrlist=line.split(' ')
            if(unitname == linestrlist[0][:-4]):
                #기존꺼와 같은 경우 만들어놓은 list에 추가한다.  
                templist.append(pygame.Rect(int(linestrlist[-4]), int(linestrlist[-3]), int(linestrlist[-2]), int(linestrlist[-1])))

            else:
                #새로운 unit이 발견됨
                self.entirelist.append(templist)
                unitname= linestrlist[0][:-4]
                templist=list()
                templist.append(unitname)
    
    def PrintList(self):
        for ll in self.entirelist:
            print('unit={0}, RectListSize={1}'.format(ll[0], len(ll)))

    
