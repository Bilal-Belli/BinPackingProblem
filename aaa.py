import tkinter as tk
import random

# Fonction qui met à jour les tableaux
def mettre_a_jour_tableaux():
    # Générer un nombre aléatoire de tableaux (entre 3 et 5)
    nombre_tableaux = random.randint(3, 5)
    
    # Supprimer les anciens tableaux (s'il y en a)
    for tableau in fenetre.winfo_children():
        tableau.destroy()
    
    # Créer une liste de tableaux avec des cases aléatoires
    for i in range(nombre_tableaux):
        tableau = tk.Frame(fenetre, bd=1, relief="solid")
        cases = random.randint(3, 7)
        for j in range(cases):
            tk.Label(tableau, text=f"Tableau {i} - Case {j}", bd=1, relief="solid").pack(side="left", padx=5, pady=5, fill="x")
        tableau.pack(side="top", padx=10, pady=10, fill="x")

# Créer une fenêtre principale
fenetre = tk.Tk()
fenetre.title("Tableaux Dynamiques")

# Créer un bouton pour mettre à jour les tableaux
bouton = tk.Button(fenetre, text="Mettre à jour", command=mettre_a_jour_tableaux)

# Pack le bouton dans la fenêtre
bouton.pack(side="bottom", pady=10)

# Mettre à jour les tableaux initiaux
mettre_a_jour_tableaux()

# Lancer la boucle principale
fenetre.mainloop()