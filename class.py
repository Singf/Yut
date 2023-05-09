class Team:
    def __init__(self):
        pass

class TeamA(Team):
    def __init__(self):
       pass
class TeamB(Team):
    def __init__(self):
        pass

class HorseA(TeamA):
    def __init__(self,x,y,together):
        self.x = x
        self.y = y
        self.together = together

    def locate(self):
        print('HorseA')
        print('x : %s' %self.x)
        print('y : %s' %self.y)
        print('together : %s' %self.together)
    
    
    
class HorseB(TeamB):
    def __init__(self,x,y,together):
        self.x = x
        self.y = y
        self.together = together

    def locate(self):
        print('HorseB')
        print('x : %s' %self.x)
        print('y : %s' %self.y)
        print('together : %s' %self.together)    




#class space:
 #   def __init__(self,x,y,):
  #      self.x = x
   #     self.y = y 
   #이게 맞나
        


a = HorseA(*[6,1,None])
b = HorseA(*[6,2,None])
c = HorseA(*[6,3,None])
d = HorseA(*[6,4,None])

q = HorseB(*[3,2,True])
w = HorseB(*[3,3,True])
e = HorseB(*[3,2,True])
r = HorseB(*[3,3,True])

a.locate()
q.locate()
