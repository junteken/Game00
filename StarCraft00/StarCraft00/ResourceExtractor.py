import pygame

class ResourceExtractor:
    """ResourceExtractor class"""    

    AllList=[]
    FileList=[]

    def __init__(self, filelist):
        self.FileList= filelist
        for filename in filelist:
            entirelist=[] #entirelist 구조 : {'unitname', Rect[0], Rect[1], Rect[2], ...Rect[N]}            
            file= open(filename+'.txt', 'r');
            #현재 읽어 들이는 unitname이랑 기존의 unitname을 비교해서 새로운 list item을 생성하기 위해 비교하는 변수
            unitname=self.GetUnitName(file.readline().split(' ')[0])
            templist=[]
            templist.append(unitname)

            for line in file:
                linestrlist=line.split(' ')
                if(unitname == self.GetUnitName(linestrlist[0])):
                    #기존꺼와 같은 경우 만들어놓은 list에 추가한다.  
                    templist.append(pygame.Rect(int(linestrlist[-4]), int(linestrlist[-3]), int(linestrlist[-2]), int(linestrlist[-1])))

                else:
                    #새로운 unit이 발견됨
                    entirelist.append(templist)
                    unitname= self.GetUnitName(linestrlist[0])
                    templist=list()
                    templist.append(unitname)
                    templist.append(pygame.Rect(int(linestrlist[-4]), int(linestrlist[-3]), int(linestrlist[-2]), int(linestrlist[-1])))

            entirelist.append(templist)
            self.AllList.append(entirelist)

    def GetUnitName(self, name):
        i=0
        for c in name:
            if(c.isdigit()):
                i+=1
        return name[:len(name)-i]


    def GetUnitPngFileName(self, unitname):
        index=0
        for al in self.AllList:
            for ll in al:                
                if(ll[0] == unitname):
                    return self.FileList[index]+'.png'
            index+=1
        raise RuntimeError('BeanzSoft : Can\'t find filename Sprite info with name')

    def GetSpriteInfo(self, unitname):
        for al in self.AllList:
            for ll in al:
                #if(ll[0].find(unitname)):
                if(ll[0] == unitname):
                    return ll
        raise RuntimeError('BeanzSoft : Can\'t find Sprite info with name')
        
    
    def PrintList(self):
        for ll in self.entirelist:
            print('unit={0}, RectListSize={1}'.format(ll[0], len(ll)))

    
