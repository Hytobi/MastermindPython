#PLOUVIN Patrice
#05/02/2018


lesCouleurs = ['violet', 'jaune', 'rouge', 'orange',
'rose', 'bleu foncée', 'bleu clair', 'vert', 'vide'] #Couleurs dans le jeu

ESSAIS = 10 # Nombres d'essais maximum

class Proposition():
    '''Contient le code d'une proposition'''

    def __init__(self,prop):
        '''Fonction qui initialise la class
           Argument : self --- class --- une proposition
                      prop --- list(int) --- liste de couleur caracterisé par un entier
           Retour : None'''
        self.__nb1 = prop[0]  # Initialise chaque couleur
        self.__nb2 = prop[1]
        self.__nb3 = prop[2]
        self.__nb4 = prop[3]

    
    def calcule_bp_mp(self, code):
        '''Fonction qui retourn le nombre de couleur bien placés et mal placés dans le code
           Argument : self --- class --- une proposition
                      code --- list(int) --- liste des entier représentant des couleurs
           Retour : tuple(int,int) --- tuple(nb bien placés, nb mal placés)'''
        listeProp = [self.__nb1, self.__nb2, self.__nb3, self.__nb4] # La proposition
        bien_places = 0   # Initialiste les bien placés à 0
        mal_places  = 0   # Initialiste les mal placés à 0
        redon = []        # Crée une liste pour éviter les redondance

        for i in range(4) : # Un code se compose de 4 couleurs
            
            if listeProp[i] in code and code[i] == listeProp[i] and listeProp[i] not in redon:        # Si la couleur est dans le code et à la même place
                bien_places +=1                     # On ajoute 1 au bien placés
                redon.append(listeProp[i])          # Mise à jour de la liste des redondances

            elif listeProp[i] in code and listeProp[i] not in redon:    # Si la couleur est dans le code et pas à la même place
                mal_places += 1                     # On ajoute 1 au mal placés
                redon.append(listeProp[i])          # Mise à jour de la liste des redondances
        return (bien_places, mal_places)


    

    def str(self):
        '''Méthode qui qui retourne une chaîne de caractéres d'entier qui code les couleurs
           Arguments : self --- class --- Proposition
           Retour : str --- entier codant les couleurs'''
        return '[' + str(self.__nb1) + ', ' + str(self.__nb2) + ', ' + str(self.__nb3) + ', ' + str(self.__nb4) + ']'
    
    def __str__(self):
        '''Méthode qui affiche une chaîne de caractéres d'entier qui code les couleurs
           Arguments : self --- class --- Proposition
           Retour : Affiche les entiers codant les couleurs'''
        print(self.str())
        


class Mastermind():
    '''qui contient la modélisation du jeu général.
    Elle permettra ultérieurement
    de gérer une partie où c’est l’ordinateur qui ’joue’.'''

    def __init__(self, nb_couleur=6, taille_code=4):
        '''Méthode qui initialise la class.
           Argument : self --- class --- Mastermind
                      nb_couleur --- int --- nombre de couleur dans le jeu
                      taille_code --- int --- nombre de valeurs dans un code
           Retour : None'''
        self.__nb_couleur = nb_couleur
        
        self.__taille_code = taille_code

        self.__mystere = None


    def dim(self):
        '''Méthode qui return la taille du code
           Argument : self --- class --- Mastermind
           Retour : self.__taille_code --- int --- La taille du code'''
        return self.__taille_code


    def lancer(self):
        '''Méthode qui génére aléatoirement un code secret.
           Argument : self --- class --- Mastermind
           Retour : None'''
        
        from random import randint
        code = []
        for i in range(self.__nb_couleur):
            code.append(randint(0, self.__nb_couleur))

        self.__mystere = Proposition(code)

    def bp_mp(self, code):
        '''Fonction qui retourn le nombre de couleur bien placés et mal placés dans
           le code passé en paramètre par rapport au mystère du Mastermind
           Argument : self --- class --- Mastermind
                      code --- list(int) --- liste des entier représentant des couleurs
           Retour : tuple(int,int) --- tuple(nb bien placés, nb mal placés)'''
        listeProp = [self.__nb1, self.__nb2, self.__nb3, self.__nb4] # La proposition
        bien_places = 0   # Initialiste les bien placés à 0
        mal_places  = 0   # Initialiste les mal placés à 0
        redon = []        # Crée une liste pour éviter les redondance

        for i in range(4) : # Un code se compose de 4 couleurs
            
            if listeProp[i] in code and code[i] == listeProp[i] and listeProp[i] not in redon:        # Si la couleur est dans le code et à la même place
                bien_places +=1                     # On ajoute 1 au bien placés
                redon.append(listeProp[i])          # Mise à jour de la liste des redondances

            elif listeProp[i] in code and listeProp[i] not in redon:    # Si la couleur est dans le code et pas à la même place
                mal_places += 1                     # On ajoute 1 au mal placés
                redon.append(listeProp[i])          # Mise à jour de la liste des redondances
        return (bien_places, mal_places)



if __name__ == '__main__' :
    mm = Mastermind()
    ## pour g´ en´ erer un code secret :
    mm.lancer()
    cpt = 1
    bp, mp = 0, 0
    while (cpt < 10) and (bp != mm.dim()) :
        print("Tour "+str(cpt))
        rep = eval(input("Votre proposition ? "))
        bp,mp = mm.bp_mp(rep)
        print("La réponse est ",bp,"bien placés et ",mp,"mal placés.")
        cpt += 1
    ## end of while
    if (bp,mp) == (mm.dim(),0) :
        print("Bravo, la partie est finie, vous avez gagn´ e.")












    







    
