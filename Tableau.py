


class Joueur:
    def __init__(self, name, licence, points):
        self.name = name
        self.licence = licence
        self.points = points
        self.player = [self.name, self.licence, self.points]


class Tableau:
    def __init__(self, nomFichier):
        self.nomFichier = nomFichier
        file = open(nomFichier)
        data = file.read()
        self.tableau = Tableau.get_tableau(self, data)

    def get_tableau(self, data):
        tableau = data.split('\n')
        matrice = []
        for infos in tableau:
            infosJoueur = infos[1:len(infos) - 1]
            tabInfos = infosJoueur.split(',')
            print(tabInfos)
            if self.nomFichier == 'data.txt':
                objetJoueur = Joueur(tabInfos[0].replace("\'", ""),
                                     tabInfos[1].replace("\'", "").lstrip(),
                                     tabInfos[2].replace("\'", "").lstrip())
                matrice.append(objetJoueur.player)
            else:
                nomJoueur = tabInfos[2]
                objetRencontre = Rencontres(tabInfos[0].replace("\'", ""),
                                            tabInfos[1].replace("\'", "").replace(" ", ""),
                                            nomJoueur[2:len(nomJoueur)].replace("\'", ""))
                matrice.append(objetRencontre.rencontre)
        return matrice

    def afficher(self):
        for infos in self.tableau:
            print(infos)

    def modifierData(self):
        stringFile = ""
        file = open(self.nomFichier, "w")
        for i in range(len(self.tableau) - 1):
            string = str(self.tableau[i]) + "\n"
            stringFile += string
        stringFile += str(self.tableau[len(self.tableau) - 1])
        file.write(stringFile)
        file.close()

    def ajouterJoueur(self):
        nom = input("Nom du joueur?")
        prenom = input("prenom du joueur?")
        licence = input("n° de licence?")
        points = input("points officiels?")
        player = Joueur(nom + ' ' + prenom, str(licence), str(points))
        self.tableau.append(player.player)

    def triRencontre(self, joueur:str) -> list:
        """
        :param joueur: string
        :type joueur: str
        :return: ca retourne une liste des rencontres du joueur demande
        """
        rencontres_du_joueur = []
        for item in self.tableau:
            if item[2] == joueur:
                rencontres_du_joueur.append(item)
        a_joue_dans_equipe = []
        for rencontre in rencontres_du_joueur:
            a_joue_dans_equipe.append(int(rencontre[1]))
        a_joue_dans_equipe.sort()
        return a_joue_dans_equipe







class Rencontres():
    def __init__(couille, date, numero_equipe, joueur):
        couille.date = date
        couille.numero_equipe = numero_equipe
        couille.joueur = joueur
        couille.rencontre = [couille.date, couille.numero_equipe, couille.joueur]

#joueur = Tableau('data.txt')
#joueur.modifierData()

#rencontre = Tableau('rencontres.txt')
#rencontre.triRencontre("Beauvais Liam")


