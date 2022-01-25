import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from Tableau import Tableau, Joueur, Rencontres


def brulage_tableau(numeros_equipe) -> str:
    string = ""
    if len(numeros_equipe) == 0:
        return "aucune rencontres enregistrees"
    for team in range(1, 6):
        encounters_nb = numeros_equipe.count(team)
        if encounters_nb != 0:
            string += str(encounters_nb) + " matchs en equipe " + str(team) + " ,"
    return string[0:len(string) - 1]


# -------------------------------------------------------------------------


def add_encounter():  # AJOUTER Rencontre
    new_window = tkinter.Toplevel(window)
    var = IntVar()
    new_window.geometry("600x550")

    label_date = Label(new_window, text="date de la rencontre(xx/xx/xxxx)")
    date_entry = Entry(new_window, width=50)
    label_team_nb = Label(new_window, text="joue dans l'equipe")
    cadre = Frame(new_window)
    r1 = Radiobutton(cadre, text="equipe1", variable=var, value=1)
    r2 = Radiobutton(cadre, text="equipe2", variable=var, value=2)
    r3 = Radiobutton(cadre, text="equipe3", variable=var, value=3)
    r4 = Radiobutton(cadre, text="equipe4", variable=var, value=4)
    r5 = Radiobutton(cadre, text="equipe5", variable=var, value=5)

    label_noms = Label(new_window, text="NOMS ET PRENOMS SANS ACCENTS NI MAJUSCULES")
    label_nom1 = Label(new_window, text="joueur numero 1")
    nom_entry1 = Entry(new_window, width=50)
    label_nom2 = Label(new_window, text="joueur numero 2")
    nom_entry2 = Entry(new_window, width=50)
    label_nom3 = Label(new_window, text="joueur numero 3")
    nom_entry3 = Entry(new_window, width=50)
    label_nom4 = Label(new_window, text="joueur numero 4")
    nom_entry4 = Entry(new_window, width=50)
    label_example = Label(new_window, text="AJOUTER RENCONTRE")

    def data_send():
        encounter1 = Rencontres(date_entry.get(), var.get(), nom_entry1.get())
        encounter2 = Rencontres(date_entry.get(), var.get(), nom_entry2.get())
        encounter3 = Rencontres(date_entry.get(), var.get(), nom_entry3.get())
        encounter4 = Rencontres(date_entry.get(), var.get(), nom_entry4.get())
        if check_data([encounter1.rencontre, encounter2.rencontre, encounter3.rencontre, encounter4.rencontre]):
            ping_encounters.tableau.append(encounter1.rencontre)
            ping_encounters.tableau.append(encounter2.rencontre)
            ping_encounters.tableau.append(encounter3.rencontre)
            ping_encounters.tableau.append(encounter4.rencontre)
            ping_encounters.modifierData()
            messagebox.showinfo("Statut Ajout", "Formulaire Envoye!")

    button_example = Button(new_window, text="Enregistrer", command=data_send)

    label_date.pack(pady=(50, 10))
    date_entry.pack()
    label_team_nb.pack(pady=(50, 10))
    cadre.pack()
    r1.pack(padx=5, side=LEFT)
    r2.pack(padx=5, side=LEFT)
    r3.pack(padx=5, side=LEFT)
    r4.pack(padx=5, side=LEFT)
    r5.pack(padx=5, side=LEFT)
    label_noms.pack(pady=(50, 10))
    label_nom1.pack()
    nom_entry1.pack()
    label_nom2.pack()
    nom_entry2.pack()
    label_nom3.pack()
    nom_entry3.pack()
    label_nom4.pack()
    nom_entry4.pack()
    label_example.pack(pady=(30, 10))
    button_example.pack()

    def check_data(players) -> bool:  # appel fonction pasLeDroit pour "est brule" et "va etre brule"
        for player in players:
            if not_the_right(Tableau.triRencontre(ping_encounters, player[2]), player[1], 0):
                messagebox.showinfo("ERREUR", player[2] + " ne peut pas jouer en equipe " + player[1] + " !")
                return False
            if not_the_right(Tableau.triRencontre(ping_encounters, player[2]), player[1], 1):
                messagebox.showinfo("ATTENTION", player[2] +
                                    " ne pourra plus jouer dans  une equipe en dessous de l'equipe " + player[1])
        return True

    def not_the_right(team_nb, asked_nb,
                     mod):  # check si les joueurs peuvent jouer dans l'equipe"numero_demande"
        if len(team_nb) == 2:
            if asked_nb > team_nb[1]:
                if mod == 0:
                    return True
            if asked_nb < team_nb[1]:
                if mod == 1:
                    if team_nb[0] != team_nb[1]:
                        return True
            return False

        if len(team_nb) < 2:
            return False
        count = 1
        temp = team_nb[0]
        for i in range(1, len(team_nb)):
            if count == 2:
                if temp < int(asked_nb):
                    if mod == 1:
                        if temp == int(asked_nb):
                            return False
                    return True
                return False
            if team_nb[i] == temp:
                count += 1
            else:
                if mod == 0:
                    count -= 1
                temp = team_nb[i]
        return False


# ---------------------------------------------------------------------------------

def add_player():  # AJOUTER JOUEUR
    new_window = tkinter.Toplevel(window)
    new_window.geometry("400x400")

    label_nom = Label(new_window, text="Nom et prenom sans accents et tout en minuscule")
    nom_entry = Entry(new_window, width=50)
    label_licence = Label(new_window, text="numero licence")
    licence_entry = Entry(new_window, width=50)
    label_points = Label(new_window, text="nombre de points")
    points_entry = Entry(new_window, width=50)
    label_example = Label(new_window, text="AJOUTER JOUEUR")

    def send_form():
        objet_joueur = Joueur(nom_entry.get(), licence_entry.get(), points_entry.get())
        ping_players.tableau.append(objet_joueur.player)
        ping_players.modifierData()
        messagebox.showinfo("Statut Ajout", "Formulaire Envoye!")

    button_example = Button(new_window, text="Enregistrer", command=send_form)

    label_licence.pack(pady=(30, 0))
    licence_entry.pack()
    label_points.pack(pady=(30, 0))
    points_entry.pack()
    label_nom.pack(pady=(30, 0))
    nom_entry.pack()
    label_example.pack(pady=(30, 0))
    button_example.pack()


# --------------------------------------------------------------------------------

window = Tk()  # main loop
window.geometry("1500x700")
window.title("Pour le Club")

ping_players = Tableau("data.txt")
ping_encounters = Tableau("rencontres.txt")

players_tab = Treeview(window, columns=('joueur', 'licence', 'points', 'peut_jouer'))
players_tab.column("# 1", anchor=CENTER, stretch=NO, width=200)
players_tab.heading('joueur', text='Nom du joueur')
players_tab.column("# 2", anchor=CENTER, stretch=NO, width=200)
players_tab.heading('licence', text='licence')
players_tab.column("# 3", anchor=CENTER, stretch=NO, width=200)
players_tab.heading('points', text='points')
players_tab.column("# 4", anchor=CENTER, stretch=NO, width=500)
players_tab.heading('peut_jouer', text='peut jouer en equipe')
players_tab['show'] = 'headings'
encounters_tab = Treeview(window, columns=('joueur', 'licence', 'points'))
encounters_tab.column("# 1", anchor=CENTER, stretch=NO, width=300)
encounters_tab.heading('joueur', text='Date de la rencontre')
encounters_tab.column("# 2", anchor=CENTER, stretch=NO, width=300)
encounters_tab.heading('licence', text='joue dans l\'equipe')
encounters_tab.column("# 3", anchor=CENTER, stretch=NO, width=300)
encounters_tab.heading('points', text='nom prenom sans accents et majuscules')
encounters_tab['show'] = 'headings'


def actualiser():
    encounters_tab.delete(*encounters_tab.get_children())
    players_tab.delete(*encounters_tab.get_children())
    encounter_display()
    players_display()


cadre_btn = Frame(window)
add_player_btn = Button(cadre_btn, text="AJOUTER JOUEUR", command=add_player)
add_encounter_btn = Button(cadre_btn, text="AJOUTER RENCONTRE", command=add_encounter)
btn_reload = Button(cadre_btn, text="ACTUALISER", command=actualiser)


def players_display():
    for players_list in ping_players.tableau:  # tableau des joueurs
        print(players_list[0])
        players_tab.insert('', 'end', values=(
            players_list[0], players_list[1], players_list[2],
            brulage_tableau(ping_encounters.triRencontre(players_list[0]))))


def encounter_display():
    encounters_tab.insert('', 'end', values=(  # tableau des rencontres
        ping_encounters.tableau[0][0], ping_encounters.tableau[0][1], ping_encounters.tableau[0][2]))
    for i in range(1, len(ping_encounters.tableau)):
        if ping_encounters.tableau[i][0] == ping_encounters.tableau[i - 1][0]:
            if ping_encounters.tableau[i][1] == ping_encounters.tableau[i - 1][1]:
                encounters_tab.insert('', 'end', values=(
                    '', '', ping_encounters.tableau[i][2]))
            else:
                encounters_tab.insert('', 'end', values=(
                    '', ping_encounters.tableau[i][1], ping_encounters.tableau[i][2]))
        else:
            encounters_tab.insert('', 'end', values=(
                ping_encounters.tableau[i][0], ping_encounters.tableau[i][1], ping_encounters.tableau[i][2]))


encounter_display()
players_display()

players_tab.pack(padx=10, pady=50)
encounters_tab.pack(padx=10, pady=(0, 50))

cadre_btn.pack(pady=10)
btn_reload.pack(padx=10, pady=(0, 10), side=LEFT)
add_encounter_btn.pack(padx=10, pady=(0, 10), side=LEFT)
add_player_btn.pack(padx=10, pady=(0, 10), side=LEFT)
window.mainloop()
