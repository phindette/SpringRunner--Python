from constantes import *

class Point:

    def __init__(self,x,y,etat):
        self.x = x
        self.y = y
        self.etat = etat

    def setEtat(self,etat):
        self.etat = etat

    def getEtat(self):
        return self.etat

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def estSolide(self,x,y):
        return x == self.x and y == self.y and self.etat == SOLIDE

    #return true si c'est le même
    def equal(self,point):
        return point.getx == self.getx and point.gety == self.gety and point.etat == self.etat 
