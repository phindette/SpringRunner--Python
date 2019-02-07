import pygame

class Highscores:
    def __init__(self):
        self.self = self

    def displayHighscores(self):
        f=open("highscores.txt","r")
        contenu=f.read()
        print(contenu)

    def addHighscore(self,score, joueur):
        f=open("highscores.txt","r")
        contenu=f.readlines()
        str1=contenu[len(contenu)-1]
        li = str1.split(':',1)
        li = [li[0].split(' ') , li[1].split(' ')]
        lowscore=int(li[1][0])
        if lowscore<score :
            for x in contenu:
                li = x.split(':',1)
                li = [li[0].split(' ') , li[1].split(' ')]
                if score > int(li[1][0]) :
                    li[0][0]=joueur
                    li[1][0]=str(score)
                    for y in reversed(range(contenu.index(x)+1,len(contenu)-1)):
                        contenu[y]=contenu[y-1]
                    contenu[contenu.index(x)]=li[0][0]+'          score :'+li[1][0]+' points\n'
                    break
            f.close()
            f=open("highscores.txt","w+")
            for x in contenu :
                f.write(x)
            f.close()
            '''self.displayHighscores()
        else:
            self.displayHighscores()'''
