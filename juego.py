class juego:
    def isCollision(self,x1,y1,x2,y2):
        if x1 == x2:
            if y1 == y2:
                return True
        return False