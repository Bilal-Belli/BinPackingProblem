import tkinter as tk
from BandB import *
from FirstFit import *
from NextFit import *
from BestFit import *
from WorstFit import *
from testParameters import *
import random
import time

# fonction comme si ils sont déja implimmentées
# Define a function to update the result label
# 1:
def binpackingfunctionBruteForce():
    # nothing
    result = 1111
    # result = "Temp d'Execution: " + str(result)
    # result_label.config(text=result)
# 2:
def binpackingfunctionBranchAndBound():
    start_time = time.time()
    # Find the solution (minimum number of bins used & distribution of objects in the bins)
    minBoxes, solution = branchAndBound(nb_objets, bin_size, Objets)
    end_time = time.time()
    elapsed_time = end_time - start_time
    for tableau in bins_frame.winfo_children():
        tableau.destroy()
    couleurs = ["#f2f2f2", "#e6e6e6", "#d9d9d9", "#cccccc", "#bfbfbf"]
    # Créer une liste de tableaux avec des cases aléatoires
    for i, bin in enumerate(solution):
        if bin:
            couleur = couleurs[i % len(couleurs)]
            tableau = tk.Frame(bins_frame, bd=1, relief="solid", bg=couleur)
            for j in range(len(bin)):
                tk.Label(tableau, text=f" {bin[j]} ", bd=1, relief="solid").pack(side="left", padx=5, pady=5, fill="x")
            tableau.pack(side="top", padx=10, pady=10, fill="x")
    bins_frame.update_idletasks()
    content_canvas.config(scrollregion=content_canvas.bbox(tk.ALL))
    result = f"{elapsed_time:.5f}"
    result2 = f"{minBoxes}"
    result  = "Temp d'Execution: " + str(result)+ " s"
    result2 = "NB_bins Minimal: " + str(minBoxes) 
    result_label.config(text=result)
    result_label2.config(text=result2)
# 3:
def binpackingfunctionFirstFit():
    Set = []
    for i in range(0,nb_objets):
        c = Objets[i]
        l = Item() 
        l.setWeight(c)
        Set.append(l) 
    SetFF = list(Set)
    BinFF = [Bin()]
    start_time = time.time()
    FF = FirstFit(SetFF,BinFF)
    FF.packItems()
    minBoxes, solution = FF.returnFF()
    end_time = time.time()
    elapsed_time = end_time - start_time
    for tableau in bins_frame.winfo_children():
        tableau.destroy()
    couleurs = ["#f2f2f2", "#e6e6e6", "#d9d9d9", "#cccccc", "#bfbfbf"]
    # Créer une liste de tableaux avec des cases aléatoires
    for i, bin in enumerate(solution):
        if bin:
            couleur = couleurs[i % len(couleurs)]
            tableau = tk.Frame(bins_frame, bd=1, relief="solid", bg=couleur)
            for j in range(len(bin)):
                tk.Label(tableau, text=f" {bin[j]} ", bd=1, relief="solid").pack(side="left", padx=5, pady=5, fill="x")
            tableau.pack(side="top", padx=10, pady=10, fill="x")
    bins_frame.update_idletasks()
    content_canvas.config(scrollregion=content_canvas.bbox(tk.ALL))
    result = f"{elapsed_time:.5f}"
    result2 = f"{minBoxes}"
    result  = "Temp d'Execution: " + str(result)+ " s"
    result2 = "NB_bins Minimal: " + str(minBoxes) 
    result_label.config(text=result)
    result_label2.config(text=result2)
# 4:
def binpackingfunctionBestFit():
    Set = []
    for i in range(0,nb_objets):
        c = Objets[i]
        l = Item() 
        l.setWeight(c)
        Set.append(l) 
    SetBF = list(Set)
    BinBF = [Bin()]
    start_time = time.time()
    BF = BestFit(SetBF,BinBF)
    BF.packItems()
    minBoxes, solution = BF.returnBF()
    end_time = time.time()
    elapsed_time = end_time - start_time
    for tableau in bins_frame.winfo_children():
        tableau.destroy()
    couleurs = ["#f2f2f2", "#e6e6e6", "#d9d9d9", "#cccccc", "#bfbfbf"]
    # Créer une liste de tableaux avec des cases aléatoires
    for i, bin in enumerate(solution):
        if bin:
            couleur = couleurs[i % len(couleurs)]
            tableau = tk.Frame(bins_frame, bd=1, relief="solid", bg=couleur)
            for j in range(len(bin)):
                tk.Label(tableau, text=f" {bin[j]} ", bd=1, relief="solid").pack(side="left", padx=5, pady=5, fill="x")
            tableau.pack(side="top", padx=10, pady=10, fill="x")
    bins_frame.update_idletasks()
    content_canvas.config(scrollregion=content_canvas.bbox(tk.ALL))
    result = f"{elapsed_time:.5f}"
    result2 = f"{minBoxes}"
    result  = "Temp d'Execution: " + str(result)+ " s"
    result2 = "NB_bins Minimal: " + str(minBoxes) 
    result_label.config(text=result)
    result_label2.config(text=result2)
# 5:
def binpackingfunctionWorstFit():
    Set = []
    for i in range(0,nb_objets):
        c = Objets[i]
        l = Item() 
        l.setWeight(c)
        Set.append(l) 
    SetWF = list(Set)
    BinWF = [Bin()]
    start_time = time.time()
    WF = WorstFit(SetWF,BinWF)
    WF.packItems()
    minBoxes, solution = WF.returnWF()
    end_time = time.time()
    elapsed_time = end_time - start_time
    for tableau in bins_frame.winfo_children():
        tableau.destroy()
    couleurs = ["#f2f2f2", "#e6e6e6", "#d9d9d9", "#cccccc", "#bfbfbf"]
    # Créer une liste de tableaux avec des cases aléatoires
    for i, bin in enumerate(solution):
        if bin:
            couleur = couleurs[i % len(couleurs)]
            tableau = tk.Frame(bins_frame, bd=1, relief="solid", bg=couleur)
            for j in range(len(bin)):
                tk.Label(tableau, text=f" {bin[j]} ", bd=1, relief="solid").pack(side="left", padx=5, pady=5, fill="x")
            tableau.pack(side="top", padx=10, pady=10, fill="x")
    bins_frame.update_idletasks()
    content_canvas.config(scrollregion=content_canvas.bbox(tk.ALL))
    result = f"{elapsed_time:.5f}"
    result2 = f"{minBoxes}"
    result  = "Temp d'Execution: " + str(result)+ " s"
    result2 = "NB_bins Minimal: " + str(minBoxes) 
    result_label.config(text=result)
    result_label2.config(text=result2)
# 6:
def binpackingfunctionNextFit():
    Set = []
    for i in range(0,nb_objets):
        c = Objets[i]
        l = Item() 
        l.setWeight(c)
        Set.append(l) 
    SetNF = list(Set)
    BinNF = [Bin()]
    start_time = time.time()
    NF = NextFit(SetNF,BinNF)
    NF.packItems()
    minBoxes, solution = NF.returnNF()
    end_time = time.time()
    elapsed_time = end_time - start_time
    for tableau in bins_frame.winfo_children():
        tableau.destroy()
    couleurs = ["#f2f2f2", "#e6e6e6", "#d9d9d9", "#cccccc", "#bfbfbf"]
    # Créer une liste de tableaux avec des cases aléatoires
    for i, bin in enumerate(solution):
        if bin:
            couleur = couleurs[i % len(couleurs)]
            tableau = tk.Frame(bins_frame, bd=1, relief="solid", bg=couleur)
            for j in range(len(bin)):
                tk.Label(tableau, text=f" {bin[j]} ", bd=1, relief="solid").pack(side="left", padx=5, pady=5, fill="x")
            tableau.pack(side="top", padx=10, pady=10, fill="x")
    bins_frame.update_idletasks()
    content_canvas.config(scrollregion=content_canvas.bbox(tk.ALL))
    result = f"{elapsed_time:.5f}"
    result2 = f"{minBoxes}"
    result  = "Temp d'Execution: " + str(result)+ " s"
    result2 = "NB_bins Minimal: " + str(minBoxes) 
    result_label.config(text=result)
    result_label2.config(text=result2)
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
# button1 = tk.Button(top_frame, text="Méthode Exacte", command=binpackingfunctionBruteForce)
# button1.pack(side=tk.LEFT, padx=10, pady=10)
button2 = tk.Button(top_frame, text="Méthode Par Branch And Bound", command=binpackingfunctionBranchAndBound)
button2.pack(side=tk.LEFT, padx=10, pady=10)
button3 = tk.Button(top_frame, text="Méthode First Fit", command=binpackingfunctionFirstFit)
button3.pack(side=tk.LEFT, padx=10, pady=10)
button4 = tk.Button(top_frame, text="Méthode Best Fit", command=binpackingfunctionBestFit)
button4.pack(side=tk.LEFT, padx=10, pady=10)
button5 = tk.Button(top_frame, text="Méthode Worst Fit", command=binpackingfunctionWorstFit)
button5.pack(side=tk.LEFT, padx=10, pady=10)
button6 = tk.Button(top_frame, text="Méthode Next Fit", command=binpackingfunctionNextFit)
button6.pack(side=tk.LEFT, padx=10, pady=10)
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
output_frame.place(relx=0.5, rely=0.1, anchor=tk.N)

# Create a frame for the bins content
content_frame = tk.Frame(main_frame, bd=1, relief="solid")
content_frame.pack(side=tk.LEFT, expand=True)
# Create a label for the content
content_label = tk.Label(content_frame, text="Bins Content")
content_label.pack(side=tk.TOP, padx=10, pady=10)

# Create a canvas for the bins content
content_canvas = tk.Canvas(content_frame, bd=0, highlightthickness=0)
content_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar for the canvas
content_scrollbar = tk.Scrollbar(content_frame, orient=tk.VERTICAL, command=content_canvas.yview)
content_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
content_canvas.config(yscrollcommand=content_scrollbar.set)

# Create a frame inside the canvas to hold the bins
bins_frame = tk.Frame(content_canvas)
content_canvas.create_window((0, 0), window=bins_frame, anchor=tk.NW)

# Créer un cadre pour le tableau
tableau = tk.Frame(bins_frame, bd=1, relief="solid")

# Ouvrir le fichier en mode lecture
with open("benchMark4heuristics.txt", "r") as file:
    Objets = []
    # Lire le contenu ligne par ligne
    for ligne in file:
        # Convertir la ligne en nombre et ajouter à la liste
        taille = int(ligne.strip())
        Objets.append(taille)

# Update the canvas scroll region after adding the bins
bins_frame.update_idletasks()
content_canvas.config(scrollregion=content_canvas.bbox(tk.ALL))
# Start the main event loop
window.mainloop()