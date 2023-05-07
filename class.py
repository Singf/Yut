class Horse:
    def __init__(self,x,y,together):
        self.x = x
        self.y = y
        self.together = together

    def locate(self):
        print('x : %s' %self.x)
        print('y : %s' %self.y)
        print('together : %s' %self.together)
    


a = Horse(*[6,1,None])

a.locate()




