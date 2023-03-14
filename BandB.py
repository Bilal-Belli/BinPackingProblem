import heapq

def nextFit(objects,bin_size):
    # Initialize an empty list to store the bins
    bins = []
    # Initialize the index of current bin to 0
    bin_index = 0
    for object in objects:
        # If the current bin index is >= the number of bins in the list
        # we have to add a new bin to the list
        if bin_index >= len(bins):
            bins.append([])
        # If the current bin has enough space we add the object to this bin
        if(sum(bins[bin_index]) + object <= bin_size):
            bins[bin_index].append(object)
        # Otherwise, we start a new bin and we add the object
        else:
            bin_index += 1
            bins.append([object])
    return bins

def BinPacking_BB(objects,bin_size):
    # Get the number of objects
    n = len(objects)
    # Initial solution : initialize the lowerbound (minimum bins used)
    lower_bound = n / bin_size
    # Initialize the best solution to None
    solution = None
    # Initialize a priority queue
    priority_queue = [(lower_bound,   # lower bound
                        n,             # number of remaining objects
                        [],            # empty list for bins
                        objects)]      # list of remaining objects (initially we haven't pack any object yet)
    # While the priority queue is not empty
    cpt = 0
    elag = 0
    while priority_queue:
        # pop the state which has the lowest lower bound
        (lower_bound,number_of_remaining_objects,bins,remaining_objects) = heapq.heappop(priority_queue)
        # If the best solution has already been found and the lower bound of the current state is >= the number of bins used in that solution, we skip this state (i.e : on fait un elagage)
        if(solution is not None and lower_bound >= solution['number_of_bins_used']):
            elag += 1
            continue
        # If all the objects are packed, we have to check if the current solution is the best, if yes we sould update the solution
        if not remaining_objects:
            number_of_bins_used = len(bins) 
            if solution is None or number_of_bins_used < solution['number_of_bins_used']:
                # Update the solution
                solution = {
                    'number_of_bins_used' : number_of_bins_used,
                    'bins' : bins,
                }
        # Otherwise, branch by considering all possible bins to pack the next object and push this state to the priority queue
        else:
            object = remaining_objects[0] # get the object from the list of remaining objects
            for bin_index, bin in enumerate(bins):
                # if we can add the objects to one of the bins we have
                if sum(bin) + object <= bin_size: 
                    new_bins = bins[:] #update the new bins
                    new_bins[bin_index] = bin + [object] #add the object to the bin
                    new_remaining_objects = remaining_objects[1:] #update the remaining objects
                    #calculate the lower bound
                    lower_bound = len(new_remaining_objects) / bin_size + len(nextFit(new_remaining_objects,bin_size))
                    #push the state to the priority queue
                    heapq.heappush(priority_queue,(lower_bound,len(new_remaining_objects),new_bins,new_remaining_objects))
            # If we can't add the objects to one of the existant bins, we add one
            new_bins = bins + [[object]] #update the bins
            new_remaining_objects = remaining_objects[1:]
            # calculate the lower bound
            lower_bound = len(new_remaining_objects) / bin_size + len(nextFit(new_remaining_objects,bin_size))
            # push the state to the priority queue
            heapq.heappush(priority_queue,(lower_bound,len(new_remaining_objects),new_bins,new_remaining_objects))
        cpt += 1
    print(f"")
    print(f"Nombre d'iteration : {cpt}")
    print(f"Nombre d'elagage : {elag}")
    return solution