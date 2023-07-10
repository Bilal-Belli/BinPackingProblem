from testParameters import *
from BinPacking import BinPacking
from random import randint, gauss,shuffle,random
import copy
import math
import numpy as np
import time

def converterBP2WWO(solution:BinPacking):
    length_dimension_list = [solution.max_weight] * len(solution.bin_list)
    item_weight_list=[]
    position_list = []
    for bin_index in range(len(solution.bin_list)):
        i=0
        for item_exist in solution.bin_list[bin_index] :
            if item_exist==1:
                position_list.append(bin_index)
                item_weight_list.append(solution.item_weight_list[i])
            i+=1
    return position_list, length_dimension_list,item_weight_list

class WaterWaveOptimizer:
    def __init__(self, solutions: list[BinPacking],temperature = 50,alpha_temp=0.8):
        self.solutions = solutions
        self.alpha_temp = alpha_temp
        self.temperature = temperature
    class Wave:
        def __init__(self, problem: BinPacking, converter=converterBP2WWO,  wave_height=10, wave_length=0.5,alpha=1.01,beta=1.01):
            self.problem = problem
            self.position_list, self.length_dimension_list, self.item_weight_list = converter(problem)
            self.height = wave_height
            self.length = wave_length
            self.alpha =alpha
            self.beta = beta
            self.sol_opt = None
        def is_feasible(self):
            bins = {}
            for position, weight in zip(self.position_list, self.item_weight_list):
                if position in bins:
                    bins[position] += weight
                else:
                    bins[position] = weight
            for bin_index, bin_weight in bins.items():
                if bin_weight > self.problem.max_weight:
                    return False
            return True
        def fitness(self):
            return self.problem.number_of_items-len(set(self.position_list))
        def propagate_wave(self):
            x_new = self.copy()
            for d in range(len(self.position_list)):
                x_new.position_list[d] = int(self.position_list[d] + randint(-1, 1) * self.length_dimension_list[d] * self.length)
                if x_new.position_list[d] > x_new.length_dimension_list[d] or x_new.position_list[d] < 0:
                    x_new.position_list[d] = int(randint(0, x_new.length_dimension_list[d]))
            if x_new.is_feasible():
                return x_new
            else:
                return self
        """
        def refract_wave(self):
            x_new = self.copy()
            for d in range(len(self.position_list)):
                x_new.position_list[d] = gauss(0, 1)
            x_new.height = self.wave_height
        """
        def break_wave(self):
            x_new = self.copy()
            for d in range(len(self.position_list)):
                x_new.position_list[d] =int(self.position_list[d] + gauss(0, 4) * self.beta * len(self.position_list))%self.problem.number_of_items
            if x_new.is_feasible():
                return x_new
            else:
                return self
        def update_wave_length(self):
            fmin = sum(self.item_weight_list)/self.problem.max_weight
            fmax = self.problem.number_of_items
            self.length = self.length * self.alpha**(-(self.fitness() +  fmin) / (fmax - fmin))
        def copy(self):
            new_wave = copy.deepcopy(self)
            return new_wave
        def print_wave(self):
            bins = {}
            for position, weight in zip(self.position_list, self.item_weight_list):
                if position in bins:
                    bins[position].append(weight)
                else:
                    bins[position] = [weight]
            
            # print("Wave Details:")
            # for bin_index, item_weights in bins.items():
            #     print("Bin{}:".format(bin_index))
            #     print(", ".join(str(weight) for weight in item_weights))
            
            # print("Position List:", self.position_list)
            # print("item weights :",self.item_weight_list)
            # print("Length Dimension List:", self.length_dimension_list)
            # print("Height:", self.height)
            # print("Length:", self.length)
            # print("fitness : ",self.problem.number_of_items - self.fitness())
            # print("--------------------------------------")
            return self.problem.number_of_items - self.fitness(),bins
    def generate_waves(self) -> list[Wave]:
        waves=[]
        for solution in self.solutions:
            waves.append(self.Wave(problem=solution))
        return waves
    def optimize(self, max_iteration):
        i = 0 
        population = self.generate_waves()
        self.sol_opt = min(population, key=lambda x: x.fitness())
        while i < max_iteration: 
            for x_index in range(len(population)):
                x_new = population[x_index].propagate_wave()
                if x_new.fitness() - population[x_index].fitness() > 0:
                    if x_new.fitness() > self.sol_opt.fitness():
                        #x_new.break_wave()
                        self.sol_opt = x_new
                        population[x_index] = x_new
                    else:
                        """
                        instead of refracting the waves
                        x.height -= 1
                        if x.height == 0:
                            x_new = x.refract_wave()
                        """
                        u = random()
                        if u > math.e**((x_new.fitness() - population[x_index].fitness())/self.temperature):
                            population[x_index] = x_new
                        self.temperature=self.temperature*self.alpha_temp
            population[x_index].update_wave_length()
            i += 1
            # print("iteration : ",i)
        return self.sol_opt.print_wave()

def H_WWO_RS(benchmarkFileName):
    with open(benchmarkFileName, "r") as file:
        array = [int(x) for x in file.read().split()]

    # shuffle(array) # without order
    bin_packing_instance1= BinPacking(len(array), array, bin_size)
    bin_packing_instance1.first_fit()
    bin_packing_instance2 = BinPacking(len(array), array, bin_size)
    bin_packing_instance2.best_fit()
    bin_packing_instance3 = BinPacking(len(array), array, bin_size)
    bin_packing_instance3.next_fit()

    start_time = time.time()
    optimizer = WaterWaveOptimizer([bin_packing_instance1,bin_packing_instance2,bin_packing_instance3])

    sol_optimal,solution_bins = optimizer.optimize(100)

    stop_time = time.time()
    elapsed_time = stop_time - start_time
    return elapsed_time,sol_optimal,solution_bins