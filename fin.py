import pygame
from constantes import *
import game
import inputbox
import highscores
import texte

surfaceW = LARGEURFENETRE #Dimension de la fenêtre / Largeur
surfaceH = HAUTEURFENETRE #Dimension de la fenêtre / Longueur

class Fin :
    """ Création et gestion des boutons d'un menu """
    def __init__(self, application, *groupes) :
        self.highscores = highscores.Highscores()
        self.pseudo = ''
        self.score = 11
        self.couleurs = dict(
            normal=(0, 200, 0),
            survol=(0, 200, 200),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        # noms des menus et commandes associées
        items = (
            ('REJOUER', application.jeu),
            ('CLASSEMENT', application.regles),
            ('QUITTER', application.quitter)
        )
        x = surfaceW/2
        y = surfaceH/2 -100
        self._boutons = []
        #champ de saisie:
        self.boxInfo = inputbox.InputBox(x-250,y,250,50,self,"Entrez votre pseudo :")
        self.box = inputbox.InputBox(x,y,200,50,self,'',True)
        clock = pygame.time.Clock()
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                self.box.handle_event(event)
            self.box.update()
            #screen = pygame.display.set_mode((640, 480))
            application.fenetre.fill(COULEURMENU)
            self.boxInfo.draw(application.fenetre)
            self.box.draw(application.fenetre)
            pygame.display.flip()
            clock.tick(30)

        for texte, cmd in items :
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                200,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
            for groupe in groupes :
                groupe.add(mb)
        #champ nb points:
        mb = MenuChampsPts(str(self.score),self.couleurs['normal'],font,x,y-(120*4),400,50)
        for groupe in groupes :
            groupe.add(mb)
        #Ajout du joueur dans le classement.
        self.highscores.addHighscore(self.score,self.pseudo)
        self.highscores.displayHighscores()
    def update(self, events) :
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons :
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur) :
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche :
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else :
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else :
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self) :
        pygame.mouse.set_cursor(*pygame.cursors.arrow) # initialisation du pointeur



class MenuBouton(pygame.sprite.Sprite) :
    """ Création d'un simple bouton rectangulaire """
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande) :
        super().__init__()
        self._commande = commande

        self.image = pygame.Surface((largeur, hauteur))
        self.image.fill(COULEURMENU)
        #self.image.fill(COULEURMENU)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur/2, hauteur/2)

        self.dessiner(couleur)

    def dessiner(self, couleur) :
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self) :
        # Appel de la commande du bouton
        self._commande()

class MenuChampsPts(pygame.sprite.Sprite):
    def __init__(self,score,couleur, font, x, y, largeur, hauteur):
        super().__init__()
        self.image = pygame.Surface((largeur,hauteur))
        self.image.fill(COULEURMENU)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.texte = font.render(str("Vous avez "+score+" points"),True,(0,0,0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur/2,hauteur/2)
        self.dessiner(couleur)

    def dessiner(self, couleur) :
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

class Jeu :
    """ Simulacre de l'interface du jeu """
    def __init__(self, jeu, *groupes) :
        self._fenetre = jeu.fenetre
        jeu.fond = (0, 0, 0)

        from itertools import cycle
        couleurs = [(0, 48, i) for i in range(0, 256, 15)]
        couleurs.extend(sorted(couleurs[1:-1], reverse=True))
        self._couleurTexte = cycle(couleurs)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.creerTexte()
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (surfaceW/2, surfaceH/2)
        # Création d'un event
        self._CLIGNOTER = pygame.USEREVENT + 1
        pygame.time.set_timer(self._CLIGNOTER, 80)

    def creerTexte(self) :
        self.texte = self._font.render(
            'LE JEU EST EN COURS D\'EXÉCUTION',
            True,
            next(self._couleurTexte)
        )

    def update(self, events) :
        self._fenetre.blit(self.texte, self.rectTexte)
        for event in events :
            if event.type == self._CLIGNOTER :
                self.creerTexte()
                break

    def detruire(self) :
        pygame.time.set_timer(self._CLIGNOTER, 0) # désactivation du timer
#enfaite ici c'est classement :)
class Regles  :
    def __init__(self, regles, *groupes):
        self._fenetre = regles.fenetre

        #Ma version :

        f=open("highscores.txt","r")
        #chope le premier mot (pseudo)
        l = []
        for ligne in f:
            ligne = ligne.replace('\n','')
            l.append(ligne)
        for x in range (1,len(l)):
            if x == 1:
                self.l1 = texte.Texte(regles,str(x)+" "+l[x-1],LARGEURFENETRE/2 -200,100,400)
            if x == 2:
                self.l2 = texte.Texte(regles,str(x)+" "+l[x-1],LARGEURFENETRE/2 -200,200,400)
            if x == 3:
                self.l3 = texte.Texte(regles,str(x)+" "+l[x-1],LARGEURFENETRE/2 -200,300,400)
            if x == 4:
                self.l4 = texte.Texte(regles,str(x)+" "+l[x-1],LARGEURFENETRE/2 -200,400,400)
            if x == 5:
                self.l5 = texte.Texte(regles,str(x)+" "+l[x-1],LARGEURFENETRE/2 -200,500,400)
            if x == 6:
                self.l6 = texte.Texte(regles,str(x)+" "+l[x-1],LARGEURFENETRE/2 -200,600,400)
            if x == 7:
                self.l7 = texte.Texte(regles,str(x)+" "+l[x-1],LARGEURFENETRE/2 -200,700,400)



    def update(self, events) :
        self._fenetre.blit(self.l1.textSurf, self.l1.rect)
        self._fenetre.blit(self.l2.textSurf, self.l2.rect)
        self._fenetre.blit(self.l3.textSurf, self.l3.rect)
        self._fenetre.blit(self.l4.textSurf, self.l4.rect)
        self._fenetre.blit(self.l5.textSurf, self.l5.rect)
        self._fenetre.blit(self.l6.textSurf, self.l6.rect)
        self._fenetre.blit(self.l7.textSurf, self.l7.rect)
        '''for event in events :
            if event.type == self._CLIGNOTER :
                self.creerTexte()
                break'''

    def detruire(self) :
            pygame.time.set_timer(self._CLIGNOTER, 0) # désactivation du timer



class Application :
    """ Classe maîtresse gérant les différentes interfaces du jeu """
    def __init__(self) :
        pygame.init()
        pygame.display.set_caption("SpringRunner")
        self.fond = (COULEURMENU)

        self.fenetre = pygame.display.set_mode((surfaceW,surfaceH))
        # Groupe de sprites utilisé pour l'affichage
        self.les_sprites = pygame.sprite.Group()
        self.textes = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self) :
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.les_sprites.empty()
        except AttributeError:
            pass

    def menu(self) :
        # Affichage du menu
        self._initialiser()
        self.ecran = Fin(self, self.les_sprites)

    def jeu(self) :
        # Affichage du jeu
        self._initialiser()
        print("tamer")
        #self.ecran = Jeu(self, self.les_sprites)
        g = game.Game()
        while g.enCours:
            g.nouvellePartie()
        pygame.quit()

    def regles(self):
        #Affichage des règles
        self._initialiser()
        self.ecran = Regles(self, self.les_sprites)
        #pygame.init()
        #self.ecran = pygame.display.set_mode((surfaceW,surfaceH))
        #pygame.display.set_caption("Règles")
        #self.clock = pygame.time.Clock()

    def quitter(self) :
        self.statut = False

    def update(self) :
        events = pygame.event.get()

        for event in events :
            if event.type == pygame.QUIT :
                self.quitter()
                return

        self.fenetre.fill(self.fond)
        self.ecran.update(events)
        self.les_sprites.update()
        self.les_sprites.draw(self.fenetre)
        pygame.display.update()

    def startFin(self):
        app = Application()
        app.menu()
        clock = pygame.time.Clock()
        while app.statut :
            app.update()
            clock.tick(30)

        pygame.quit()
