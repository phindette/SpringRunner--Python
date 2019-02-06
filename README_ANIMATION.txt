Deso c'est un peu long, dans l'idéal il aurait fallu crée une classe mère ObjetAnimé et
en faire hériter toute les classe d'objet avec une animation, ca aurait éco pas mal

Pour chaques classes d'objets ayant des animations, il faut rajouter :

-> >>Dans le .py de la classe concernée
-> import animation
-> from animation import *
-> from constantes import *

--> >>Dans la définition de la classe concernée

---> >>Dans le def __init__(self,game)
----> self.animation = "VALEUR PAR DEFAUT" // string identifiant l'animation en cours
----> self.index = 0 // indice de l'animation en cours
----> self.spritesCollection = initTabSprites(nbAnimations) // Crée un dictionnaire de tableau pour contenir tout les sprites de l'objet 
----> // Crée un dictionnaire de tableau pour contenir tout les sprites de l'objet
----> //POUR CHAQUE SPRITESHEETS UTILISEES ajoutez la ligne suivante :
----> self.NOMSPRITESHEET = SpriteSheet("NOMFICHIER.png")
----> self.charger_image()
----> self.image = self.spritesCollection[0][0] 
----> // ici choisir dans spritesCollection l'animation et la frame voulue par défaut
----> self.rect = self.image.get_rect()
        
----> self.rect.center = (0, HAUTEURFENETRE - 60)
----> // ... fin du __init__

---> >>Dans charger image //ne doit contenir que les lignes suivantes
----> // POUR CHAQUE TABLEAU DANS spritesCollection ajouter :
----> LoadSprites(self.spritesCollection[I],SPRITESHEET,NB,LARGEUR,HAUTEUR)
----> // Découpe les sprites et les répartie dans spritesCollection
----> // I = numéro de l'animation concernée
----> // SPRITESHEET = Spritesheet concernée (ex : self.spritesDebout)
----> // NB = nombres de frames différentes de l'animation
----> // LARGEUR et HAUTEUR = largeur et hauteur DE CHAQUE FRAME de l'animation (pas de la spritsheet)
----> // exemple : LoadSprites(self.spritesCollection[2],self.spritesMarche,8,35,60)
----> // ici on load les sprites de marche (vers la droite car pas inverted) dans spritesCollection[2]
----> // cette spritesheet doit être découpée en 8 rectangles de 35x60 px
----> // utilisez loadSpritesInverted à la place de loadSprites pour mirror la spritesheet verticalement

---> >>Dans le def update(self)
----> // Voilà l'exemple pour le personnage. pour chaque animation différente, il faut vérifier
----> // l'animation en cours, puis si l'index ne pointe pas hors de la range de l'animation en cours.
----> // Si c'est le cas on le remet à 0. Enfin, on actualise self.image avec l'image de l'animation correspondante.
----> // ici, SR veut dire Still Right et SL Still Left
----> self.index += 1
----> if self.animation == "SR":
-----> if self.index >= len(self.spritesCollection[0]):
------> self.index = 0
-----> self.image = self.spritesCollection[0][self.index]
----> elif self.animation == "SL":
-----> if self.index >= len(self.spritesCollection[2]):
------> self.index = 0
-----> self.image = self.spritesCollection[1][self.index]
----> elif ...

----> >>Dans chaque déclenchement d'un evènement lié à un changement d'animation
----> self.animation = "NOMANIM" 
----> // ex : self.animation = "R" pour l'animation de marche à droite quand la 
----> // touche d est pressée