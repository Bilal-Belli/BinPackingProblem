import copy
import itertools
import numpy as np
from collections import namedtuple
import time

Item = namedtuple("Item", ['id', 'size'])
Candidate = namedtuple("Candidate", ['items', 'fitness'])

#------------BIN-------------
def cost(bins):
    return len(bins)

class Bin(object):
    count = itertools.count()
    def __init__(self, capacity):
        self.id = next(Bin.count)
        self.capacity = capacity
        self.free_space = capacity
        self.items = []
        self.used_space = 0

    def add_item(self, item):
        self.items.append(item)
        self.free_space -= item.size
        self.used_space += item.size

    def remove_item(self, item_index):
        item_to_remove = self.items[item_index]
        del self.items[item_index]
        self.free_space += item_to_remove.size
        self.used_space -= item_to_remove.size

    def fits(self, item):
        return self.free_space >= item.size

    def __str__(self):
        items = [str(it) for it in self.items]
        items_string = '[' + ' '.join(items) + ']'
        return "Bin n° " + str(self.id) + " containing the " + \
            str(len(self.items)) + " following items : " + items_string + \
            " with " + str(self.free_space) + " free space."

    def __copy__(self):
        new_bin = Bin(self.capacity)
        new_bin.free_space = self.free_space
        new_bin.used_space = self.used_space
        new_bin.items = self.items[:]
        return new_bin

#-----------GA HEUR-----------

def nextfit(items, current_bins, capacity):
    bins = [copy.copy(b) for b in current_bins]
    if not bins:
        bin = Bin(capacity)
        bins.append(bin)
    for item in items:
        if item.size > capacity:
            continue
        if bin.fits(item):
            bin.add_item(item)
        else:
            bin = Bin(capacity)
            bin.add_item(item)
            bins.append(bin)
    return bins

def bestfit(items, current_bins, capacity):
    bins = [copy.copy(b) for b in current_bins]
    if not bins:
        bins = [Bin(capacity)]
    for item in items:
        if item.size > capacity:
            continue
        possible_bins = [bin for bin in bins if bin.fits(item)]
        if not possible_bins:
            bin = Bin(capacity)
            bin.add_item(item)
            bins.append(bin)
        else:
            index, free_space = min(enumerate(possible_bins), key=lambda it: it[1].free_space)
            possible_bins[index].add_item(item)
    return bins

def firstfit(items, current_bins, capacity):
    bins = [copy.copy(b) for b in current_bins]
    if not bins:
        bins = [Bin(capacity)]
    for item in items:
        if item.size > capacity:
            continue
        first_bin = next((bin for bin in bins if bin.free_space >= item.size), None)
        if first_bin is None:
            bin = Bin(capacity)
            bin.add_item(item)
            bins.append(bin)
        else:
            first_bin.add_item(item)
    return bins

def worstfit(items, current_bins, capacity):
    bins = [copy.copy(b) for b in current_bins]
    if not bins:
        bins = [Bin(capacity)]
    for item in items:
        if item.size > capacity:
            continue
        possible_bins = [bin for bin in bins if bin.fits(item)]
        if not possible_bins:
            bin = Bin(capacity)
            bin.add_item(item)
            bins.append(bin)
        else:
            index, free_space = max(enumerate(possible_bins), key=lambda it: it[1].free_space)
            possible_bins[index].add_item(item)
    return bins

#-----------GA------------

# step 01 : Create initial Population
def population_generator(items, capacity, population_size, greedy_solver):
    candidate = Candidate(items[:], fitness(items, capacity, greedy_solver))
    population = [candidate]
    new_items = items[:]
    for i in range(population_size - 1):
        np.random.shuffle(new_items)
        candidate = Candidate(new_items[:], fitness(new_items, capacity, greedy_solver))
        if candidate not in population:
            population.append(candidate)
    return population

# step 02 : calculate fitness for each candidate of this population
def fitness(candidate, capacity, greedy_solver):
    if greedy_solver == 'FF':
        return firstfit(candidate,[], capacity)
    elif greedy_solver == 'BF':
        return bestfit(candidate,[], capacity)
    return nextfit(candidate,[], capacity)

# step 03 : selection

# Selection par tournoi
def tournament_selection(population, tournament_selection_probability, k):
    candidates = [population[(np.random.randint(0, len(population) - 1))]]
    while len(candidates) < k:
        new_indiv = population[(np.random.randint(0, len(population) - 1))]
        if new_indiv not in candidates:
            candidates.append(new_indiv)
    ind = int(np.random.geometric(tournament_selection_probability, 1))
    while ind >= k:
        ind = int(np.random.geometric(tournament_selection_probability, 1))
    return candidates[ind]

# sélection par roue de roulette.
def roulette_wheel_selection(population):
    max = sum([len(e.fitness) for e in population])
    pick = np.random.uniform(0, max)
    current = max
    for item in population:
        current -= len(item.fitness)
        if current < pick:
            return item

# Selection par rang
def rank_selection(population):
    length = len(population)
    rank_sum = length * (length + 1) / 2
    pick = np.random.uniform(0, rank_sum)
    current = 0
    i = length
    for item in population:
        current += i
        if current > pick:
            return item
        i -= 1

# Stochastic Universal Sampling (SUS)
def SUS(population, n):
    selected = []
    pointers = []
    max = sum([len(e.fitness) for e in population])
    distance = max / n
    start = np.random.uniform(0, distance)
    for i in range(n):
        pointers.append(start + i * distance)
    for pointer in pointers:
        current = 0
        for item in population:
            current += len(item.fitness)
            if current > pointer:
                selected.append(item)
    return selected

# step 04 : crossover

def crossover(parent1, parent2):
    taken = [False] * len(parent1)
    child = []
    i = 0
    while i < len(parent1):
        element = parent1[i]
        if not taken[element.id]:
            child.append(element)
            taken[element.id] = True
        element = parent2[i]
        if not taken[element.id]:
            child.append(element)
            taken[element.id] = True
        i += 1
    return child

# step 05 : mutation
def mutation(member, capacity, greedy_solver):
    member_items = member.items
    a = np.random.randint(0, len(member_items) - 1)
    b = np.random.randint(0, len(member_items) - 1)
    while a == b:
        b = np.random.randint(0, len(member_items) - 1)
    c = member_items[a]
    member_items[a] = member_items[b]
    member_items[b] = c
    member = Candidate(member_items, fitness(member_items, capacity, greedy_solver))
    return member

#################### GENETIC ALGORITHM ################################
def genetic_algorithm(weights, capacity, population_size, generations, k, tournament_selection_probability, crossover_probability, mutation_probability, greedy_solver, allow_duplicate_parents, selection_method):
    items = [Item]
    items = [ Item(i,weights[i]) for i in range(len(weights))]

    population = population_generator(items, capacity, population_size, greedy_solver)
    best_solution = fitness(items, capacity, greedy_solver)
    i = 0

    while i < generations:
        new_generation = []
        best_child = best_solution
        for j in range(population_size):
            if selection_method == 'SUS':
                first_parent = SUS(population, 1)[0].items
                second_parent = SUS(population, 1)[0].items
                if not allow_duplicate_parents:
                    while first_parent == second_parent:
                        second_parent = SUS(population, 1)[0].items
            elif selection_method == 'TS':
                first_parent = tournament_selection(population, tournament_selection_probability, k).items
                second_parent = tournament_selection(population, tournament_selection_probability, k).items
                if not allow_duplicate_parents:
                    while first_parent == second_parent:
                        second_parent = tournament_selection(population, tournament_selection_probability, k).items
            elif selection_method == 'RW':
                first_parent = roulette_wheel_selection(population).items
                second_parent = roulette_wheel_selection(population).items
                if not allow_duplicate_parents:
                    while first_parent == second_parent:
                        second_parent = roulette_wheel_selection(population).items
            elif selection_method == 'RS':
                first_parent = rank_selection(population).items
                second_parent = rank_selection(population).items
                if not allow_duplicate_parents:
                    while first_parent == second_parent:
                        second_parent = rank_selection(population).items
            else:
                return

            child = crossover(first_parent, second_parent)
            child = Candidate(child[:], fitness(child, capacity, greedy_solver))

            prob = np.random.rand()
            if prob <= mutation_probability:
                child = mutation(child, capacity, greedy_solver)

            if len(child.fitness) < len(best_child):
                best_child = child.fitness
            new_generation.append(child)

        if len(best_child) < len(best_solution):
            best_solution = best_child
        population = [Candidate(p.items[:], p.fitness) for p in new_generation]
        population.sort(key=lambda candidate: len(candidate.fitness), reverse=True)
        i += 1

    return len(best_solution), [[item.size for item in bin.items] for bin in best_solution]

def AG(benchmarkFileName):
    with open(benchmarkFileName, "r") as ifile:
        bin_capacity = int(ifile.readline())
        items_length = int(ifile.readline())
        items = []
        for i in range(items_length):
            line = ifile.readline().strip()
            if line:
                items.append(int(line))
        start_time = time.time()
        best_length, solution = genetic_algorithm(items, bin_capacity, 50, 50, 2, 0.7, 0.3, 0.4, 'FF', False, 'TS')
        end_time = time.time()
        execution_time = end_time - start_time
    
    return execution_time,best_length,solution

# Pour le test en ce fichier
# AG()