import tkinter as tk
from BandB import * 
import time

# fonction comme si ils sont déja implimmentées
# Define a function to update the result label
def binpackingfunctionBruteForce():
    result = 1111
    result = "Temp d'Execution: " + str(result)
    result_label.config(text=result)
def binpackingfunctionBranchAndBound():
    start_time = time.time()
    # Find the solution (minimum number of bins used & distribution of objects in the bins)
    solution,cpt,elag = BinPacking_BB(Objets,bin_size)
    end_time = time.time()
    elapsed_time = end_time - start_time

    for tableau in content_frame.winfo_children():
        tableau.destroy()
    couleurs = ["#f2f2f2", "#e6e6e6", "#d9d9d9", "#cccccc", "#bfbfbf"]
    # Créer une liste de tableaux avec des cases aléatoires
    for i , bin in enumerate(solution['bins']):
        couleur = couleurs[i % len(couleurs)]
        tableau = tk.Frame(content_frame, bd=1, relief="solid", bg=couleur)
        for j in range(len(bin)):
            tk.Label(tableau, text=f" {bin[j]} ", bd=1, relief="solid").pack(side="left", padx=5, pady=5, fill="x")
        tableau.pack(side="top", padx=10, pady=10, fill="x")

    result = f"{elapsed_time:.5f}"
    result2 = f"{solution['number_of_bins_used']}"
    result3 = f"{cpt}"
    result4 = f"{elag}"
    result = "Temp d'Execution: " + str(result)+ " s"
    result2 = "NB_bins Minimal: " + str(result2) 
    result3 = "NB_Itérations: " + str(cpt) 
    result4 = "NB_Elagages: " + str(elag) 
    result_label.config(text=result)
    result_label2.config(text=result2)
    result_label3.config(text=result3)
    result_label4.config(text=result4)

# Create a window object
window = tk.Tk()
# Add a title to the window
window.title("BinPacking - Projet OPT")
# Set the dimensions of the window
window.wm_state('zoomed')
window.resizable(False, False)
window.iconbitmap('icon.ico')

# Create a main frame
main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create frames inside the top frame
# Create a frame for the buttons
top_frame = tk.Frame(main_frame)
top_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Add two buttons to the frame
button1 = tk.Button(top_frame, text="Méthode Exacte", command=binpackingfunctionBruteForce)
button1.pack(side=tk.LEFT, padx=10, pady=10)
button2 = tk.Button(top_frame, text="Méthode Par Branch And Bound", command=binpackingfunctionBranchAndBound)
button2.pack(side=tk.LEFT, padx=10, pady=10)
# Center the frame horizontally
top_frame.place(relx=0.5, rely=0, anchor=tk.N)

# Create a frame for the output
output_frame = tk.Frame(main_frame)
output_frame.pack(side=tk.LEFT,  fill=tk.BOTH, expand=True)
# Create a label for the output
result_label = tk.Label(output_frame, text="Temp d'Execution: --",bg="#FFFF00")
result_label.pack(side=tk.LEFT)
result_label2 = tk.Label(output_frame, text="NB_bins Minimal: --",bg="#FFFF00")
result_label2.pack(side=tk.LEFT)
result_label3 = tk.Label(output_frame, text="NB_Itérations: --",bg="#FFFF00")
result_label3.pack(side=tk.LEFT)
result_label4 = tk.Label(output_frame, text="NB_Elagages: --",bg="#FFFF00")
result_label4.pack(side=tk.LEFT)
output_frame.place(relx=0.5, rely=0.1, anchor=tk.N)

# Create a frame for the bins content
content_frame = tk.Frame(main_frame, bd=1, relief="solid")
content_frame.pack(side=tk.LEFT, expand=True)
# Create a label for the content
content_frame.place(relx=0.5, rely=0.2, anchor=tk.N)

# Créer un cadre pour le tableau
tableau = tk.Frame(content_frame, bd=1, relief="solid")

# Ouvrir le fichier en mode lecture
with open("taillesObjets.txt", "r") as file:
    Objets = []
    # Lire le contenu ligne par ligne
    for ligne in file:
        # Convertir la ligne en nombre et ajouter à la liste
        taille = int(ligne.strip())
        Objets.append(taille)

# Test 
# Bin size
bin_size = 30

# Start the main event loop
window.mainloop()