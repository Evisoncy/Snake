class juego:
    def isCollision(self,x1,y1,x2,y2):
        if x1 == x2:
            if y1 == y2:
                return True
        return False

    

    def isCollision2(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False