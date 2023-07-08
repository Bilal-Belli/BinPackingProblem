from testParameters import *
import random
from random import shuffle
import time

class Heuristic:
    @staticmethod
    def apply(item, bins):
        return bins
class FirstFit(Heuristic):
    @staticmethod
    def apply(item, bins):
        b = next((b for b in bins if b.can_add_item(item)), None)
        if not b:
            b = Bin(bins[0].capacity)
            bins.append(b)
        b.add_item(item)
        return bins
class BestFit(Heuristic):
    @staticmethod
    def apply(item, bins):
        valid_bins = (b for b in bins if b.can_add_item(item))
        sorted_bins = sorted(valid_bins, key=lambda x: x.filled_space(), reverse=True)
        if sorted_bins:
            b = sorted_bins[0]
        else:
            b = Bin(bins[0].capacity)
            bins.append(b)
        b.add_item(item)
        return bins
class NextFit(Heuristic):
    @staticmethod
    def apply(item, bins):
        b = bins[-1]
        if not b.add_item(item):
            b = Bin(bins[0].capacity)
            bins.append(b)
            b.add_item(item)
        return bins
class WorstFit(Heuristic):
    @staticmethod
    def apply(item, bins):
        valid_bins = (b for b in bins if b.can_add_item(item))
        sorted_bins = sorted(valid_bins, key=lambda x: x.filled_space())
        if sorted_bins:
            b = sorted_bins[0]
        else:
            b = Bin(bins[0].capacity)
            bins.append(b)
        b.add_item(item)
        return bins
class Bin:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
    def add_item(self, new_item):
        if self.can_add_item(new_item):
            self.items.append(new_item)
            return True
        return False
    def can_add_item(self, new_item):
        return new_item.size <= self.open_space()
    def filled_space(self):
        return sum(item.size for item in self.items)
    def open_space(self):
        return self.capacity - self.filled_space()
    def fitness(self):
        return (self.filled_space() / self.capacity) ** 2
    def showBinContent(self):
        for singleItem in self.items:
            singleItem.showItemSize()
class MoveOperator:
    @staticmethod
    def apply(items, choices):
        return items
class Remove(MoveOperator):
    @staticmethod
    def apply(items, choices):
        num_removals = random.randrange(len(items))
        for _ in range(num_removals):
            to_remove = random.randrange(len(items))
            items = items[:to_remove] + items[to_remove + 1:]
        return items
class Add(MoveOperator):
    @staticmethod
    def apply(items, choices):
        num_inserts = random.randrange(len(items) + 1)
        for _ in range(num_inserts):
            to_insert = random.randrange(len(items))
            items = items[:to_insert] + random.choice(choices) + items[to_insert:]
        return items
class Change(MoveOperator):
    @staticmethod
    def apply(items, choices):
        num_changes = random.randrange(len(items)+1)
        items = list(items)
        for _ in range(num_changes):
            to_change = random.randrange(len(items))
            items[to_change] = random.choice(choices)
        return "".join(items)
class Swap(MoveOperator):
    @staticmethod
    def apply(items, choices):
        num_swaps = random.randrange(len(items))
        items = list(items)
        for _ in range(num_swaps):
            idx1, idx2 = random.randrange(len(items)), random.randrange(len(items))
            items[idx1], items[idx2] = items[idx2], items[idx1]
        return "".join(items)
class Item:
    def __init__(self, size):
        self.size = size
    def showItemSize(self):
        print(self.size)
class TabuSearch:
    heuristic_map = {
        "f": FirstFit,
        "n": NextFit,
        "w": WorstFit,
        "b": BestFit,
    }
    movers = [Add, Change, Remove, Swap] 
    def __init__(self, capacity, items, MAX_COMBINATION_LENGTH=10, MAX_ITERATIONS=5000, MAX_NO_CHANGE = 1000):
        """
        Creates an instance that can run the tabu search algorithm.
        :param capacity: The capacity of a bin.
        :param items: The items that have to be packed in bins.
        """
        self.MAX_COMBINATION_LENGTH = MAX_COMBINATION_LENGTH
        self.MAX_ITERATIONS = MAX_ITERATIONS
        self.MAX_NO_CHANGE = MAX_NO_CHANGE
        self.bin_capacity = capacity
        self.items = items
        self.fitness = 0
        self.bins = [Bin(capacity)]
        self.tabu_list = set()
    def run(self):
        """
        Runs the tabu search algorithm and returns the results at the end of the process.
        :return: (num_iterations, num_no_changes, chosen_combination)
        """
        combination = "".join(
            [random.choice(list(self.heuristic_map.keys())) for _ in range(random.randrange(self.MAX_COMBINATION_LENGTH) or 1)])
        self.bins = self.generate_solution(combination)
        self.fitness = sum(b.fitness() for b in self.bins) / len(self.bins)
        self.tabu_list.add(combination)
        current_iteration = 0
        num_no_change = 0
        while num_no_change < self.MAX_NO_CHANGE and current_iteration < self.MAX_ITERATIONS:
            new_combination = self.apply_move_operator(combination)
            while len(new_combination) > self.MAX_COMBINATION_LENGTH :
                new_combination = self.apply_move_operator(new_combination)
            if new_combination not in self.tabu_list:
                self.tabu_list.add(new_combination)
                solution = self.generate_solution(new_combination)
                fitness = sum(b.fitness() for b in solution) / len(solution)
                if fitness > self.fitness:
                    self.bins = solution
                    self.fitness = fitness
                    num_no_change = 0
                    combination = new_combination
            current_iteration += 1
            num_no_change += 1
        return current_iteration, num_no_change, combination
    def run2(self,AGsol):
        """
        Runs the tabu search algorithm and returns the results at the end of the process.
        :return: (num_iterations, num_no_changes, chosen_combination)
        """
        combination = AGsol.best_solution.pattern
        self.bins =self.generate_solution(combination) 
        self.fitness = AGsol.best_solution.fitness
        self.tabu_list.add(combination)
        current_iteration = 0
        num_no_change = 0
        while num_no_change < self.MAX_NO_CHANGE and current_iteration < self.MAX_ITERATIONS:
            new_combination = self.apply_move_operator(combination)
            while len(new_combination) > self.MAX_COMBINATION_LENGTH :
                new_combination = self.apply_move_operator(new_combination)
            if new_combination not in self.tabu_list:
                self.tabu_list.add(new_combination)
                solution = self.generate_solution(new_combination)
                fitness = sum(b.fitness() for b in solution) / len(solution)
                if fitness > self.fitness:
                    self.bins = solution
                    self.fitness = fitness
                    num_no_change = 0
                    combination = new_combination
                current_iteration += 1
            else : 
                current_iteration += 1
                num_no_change += 1
        return current_iteration, num_no_change, combination
    def run3(self,chromosome):
        """
        Runs the tabu search algorithm and returns the results at the end of the process.
        :return: (num_iterations, num_no_changes, chosen_combination)
        """
        combination = chromosome.pattern
        self.bins =self.generate_solution(combination) 
        self.fitness = chromosome.fitness
        self.tabu_list.add(combination)
        current_iteration = 0
        num_no_change = 0
        while num_no_change < self.MAX_NO_CHANGE and current_iteration < self.MAX_ITERATIONS:
            new_combination = self.apply_move_operator(combination)
            while len(new_combination) > self.MAX_COMBINATION_LENGTH :
                new_combination = self.apply_move_operator(new_combination)
            if new_combination not in self.tabu_list:
                self.tabu_list.add(new_combination)
                solution = self.generate_solution(new_combination)
                fitness = sum(b.fitness() for b in solution) / len(solution)
                if fitness > self.fitness:
                    self.bins = solution
                    self.fitness = fitness
                    num_no_change = 0
                    combination = new_combination
                current_iteration += 1
            else : 
                current_iteration += 1
                num_no_change += 1
        return current_iteration, num_no_change, combination
    def generate_solution(self, pattern):
        """
        Generates a candidate solution based on the pattern given.
        :param pattern: A pattern indicating the order in which heuristics need to be applied to get the solution.
        :return: A list of bins to serve as a solution.
        """
        solution = [Bin(self.bin_capacity)]
        pattern_length = len(pattern)
        for idx, item in enumerate(self.items):
            h = pattern[idx % pattern_length]
            solution = self.heuristic_map[h].apply(item, solution)
        return solution
    def apply_move_operator(self, pattern):
        """
        Applies a random move operator to the given pattern.
        :param pattern: The pattern to apply the move operator to.
        :return: The pattern after the move operator has been applied.
        """
        return random.choice(self.movers).apply(pattern, list(self.heuristic_map.keys()))

def RT(fileName):
    boxContent=[]
    # Ouvrir le fichier en mode lecture
    with open(fileName, "r") as file:
        Objets = []
        for ligne in file:
            taille = int(ligne.strip())
            Objets.append(taille)
        num_items = nb_objets
        capacity = bin_size
        items = Objets
        items = [Item(size=int(i)) for i in items]
    # Perform 1 independent iterations. (on peut la changer si veut exécuter  successivement en ce script en changent 1 par le nombre d'expériances)
    for iteration in range(1):
        # print('Iteration numéro: '+ iteration)
        # Randomize the order of the items in the item list.
        shuffle(items)
        thing = TabuSearch(capacity, items)
        start_time = time.time()
        total_iterations, stagnation, combination = thing.run()
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # the result bins content
        for singleBin in thing.bins:
            newBoxContent=[]
            for singleItem in singleBin.items:
                newBoxContent.append(singleItem.size)
            boxContent.append(newBoxContent)
    return elapsed_time,len(thing.bins),boxContent

# Pour le test en ce fichier
# RT()