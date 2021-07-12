class juego:
    def isCollision(self,x1,y1,x2,y2):
        if x1 == x2:
            if y1 == y2:
                return True
        return False

    def isCollision2(self,x1,y1,x2,y2,x3,y3):
        if x1 == x2:
            if y1 == y2:
                if x2==x3:
                    if y2==y3:
                     return True
        return False