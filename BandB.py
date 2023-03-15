import heapq

def nextFit(objects,bin_size):
    # Initialiser une liste vide pour stocker les "bins" bacs
    bins = []
    # Initialiser l'index du bin courant à 0
    bin_index = 0
    for object in objects:
        # Si l'index de bac actuel est >= le nombre de bacs dans la liste
        # nous devons ajouter un nouveau bac à la liste
        if bin_index >= len(bins):
            bins.append([])
        # Si le bac actuel a suffisamment d'espace, nous ajoutons l'objet à ce bac
        if(sum(bins[bin_index]) + object <= bin_size):
            bins[bin_index].append(object)
        # Sinon, on commence un nouveau bin et on ajoute l'objet
        else:
            bin_index += 1
            bins.append([object])
    return bins

def BinPacking_BB(objects,bin_size):
    # Obtenir le nombre d'objets
    n = len(objects)
    # Solution initiale : initialiser la borne inférieure (bins minimum utilisés)
    lower_bound = n / bin_size
    # Initialiser la meilleure solution à Aucun
    solution = None
    # Initialiser une file d'attente prioritaire
    priority_queue = [(lower_bound,   # borne inférieure
                        n,             # nombre d'objets restants
                        [],            # liste vide pour les bacs
                        objects)]      # liste des objets restants (initialement nous n'avons encore emballé aucun objet)
    # Tant que la file d'attente prioritaire n'est pas vide
    cpt = 0
    elag = 0
    while priority_queue:
        # pop l'état qui a la borne inférieure la plus basse
        (lower_bound,number_of_remaining_objects,bins,remaining_objects) = heapq.heappop(priority_queue)
        # Si la meilleure solution a déjà été trouvée et que la borne inférieure de l'état actuel est >= le nombre de bacs utilisés dans cette solution, nous sautons cet état (c'est-à-dire : on fait un elagage)
        if(solution is not None and lower_bound >= solution['number_of_bins_used']):
            elag += 1
            continue
        # Si tous les objets sont emballés, il faut vérifier si la solution actuelle est la meilleure, si oui il faut mettre à jour la solution
        if not remaining_objects:
            number_of_bins_used = len(bins) 
            if solution is None or number_of_bins_used < solution['number_of_bins_used']:
                # Mettre à jour la solution
                solution = {
                    'number_of_bins_used' : number_of_bins_used,
                    'bins' : bins,
                }
        # Sinon, branchez en considérant tous les bacs possibles pour emballer l'objet suivant et poussez cet état vers la file d'attente prioritaire
        else:
            object = remaining_objects[0] # récupérer l'objet dans la liste des objets restants
            for bin_index, bin in enumerate(bins):
                # si nous pouvons ajouter les objets à l'un des bacs que nous avons
                if sum(bin) + object <= bin_size: 
                    new_bins = bins[:] # mettre à jour les nouveaux bacs
                    new_bins[bin_index] = bin + [object] # ajouter l'objet à la bin
                    new_remaining_objects = remaining_objects[1:] # mettre à jour les objets restants
                    # calculer la borne inférieure
                    lower_bound = len(new_remaining_objects) / bin_size + len(nextFit(new_remaining_objects,bin_size))
                    # pousser l'état vers la file d'attente prioritaire
                    heapq.heappush(priority_queue,(lower_bound,len(new_remaining_objects),new_bins,new_remaining_objects))
            # Si nous ne pouvons pas ajouter les objets à l'un des bacs existants, nous en ajoutons un
            new_bins = bins + [[object]] # mettre à jour les bacs
            new_remaining_objects = remaining_objects[1:]
            # calculer la borne inférieure
            lower_bound = len(new_remaining_objects) / bin_size + len(nextFit(new_remaining_objects,bin_size))
            # pousser l'état vers la file d'attente prioritaire
            heapq.heappush(priority_queue,(lower_bound,len(new_remaining_objects),new_bins,new_remaining_objects))
        cpt += 1
    return solution,cpt,elag