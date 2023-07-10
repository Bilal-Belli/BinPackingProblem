class BinPacking:
    def __init__(self, number_of_items, item_weight_list, max_weight):
        self.number_of_items = number_of_items
        self.item_weight_list = item_weight_list
        self.bin_list = [[0] * number_of_items for _ in range(number_of_items)]
        self.max_weight = max_weight
    
    def bin_weight(self,i):
        s=0
        for j in range(self.number_of_items):
            s = s + self.bin_list[i][j] * self.item_weight_list[j]
        return s
    
    def is_feasible_solution(self):
        bin_weights = [sum([self.item_weight_list[j] * self.bin_list[i][j] for j in range(self.number_of_items)]) 
            for i in range(self.number_of_items)]
        return all(weight <= self.max_weight for weight in bin_weights)
    
    def function_to_maximize(self):
        return sum(1 for row in self.bin_list if all(elem == 0 for elem in row))
    
    def function_to_minimize(self):
        return self.number_of_items - self.function_to_maximize()
    
    def first_fit(self):
        for item_index in range(self.number_of_items):
            for bin_index in range(self.number_of_items):
                if self.bin_weight(bin_index) + self.item_weight_list[item_index] <= self.max_weight:
                    self.bin_list[bin_index][item_index] = 1
                    break

    def next_fit(self):
        current_bin_index = 0
        for item_index in range(self.number_of_items):
            if self.bin_weight(current_bin_index) + self.item_weight_list[item_index] <= self.max_weight:
                self.bin_list[current_bin_index][item_index] = 1
            else:
                current_bin_index += 1
                self.bin_list[current_bin_index][item_index] = 1

    def best_fit(self):
        bin_capacities = [self.max_weight] * self.number_of_items
        for item_index in range(self.number_of_items):
            best_bin_index = -1
            min_remaining_capacity = float('inf')
            for bin_index in range(self.number_of_items):
                remaining_capacity = bin_capacities[bin_index] - self.item_weight_list[item_index]
                if remaining_capacity >= 0 and remaining_capacity < min_remaining_capacity:
                    best_bin_index = bin_index
                    min_remaining_capacity = remaining_capacity
            if best_bin_index != -1:
                self.bin_list[best_bin_index][item_index] = 1
                bin_capacities[best_bin_index] -= self.item_weight_list[item_index]

    def first_fit_decreasing(self):
        sorted_items = sorted(range(self.number_of_items), key=lambda x: self.item_weight_list[x], reverse=True)
        for item_index in sorted_items:
            bin_index = 0
            while bin_index < self.number_of_items:
                if self.bin_weight(bin_index) + self.item_weight_list[item_index] <= self.max_weight:
                    self.bin_list[bin_index][item_index] = 1
                    break
                bin_index += 1
            else:
                # Start a new bin if no bin can accommodate the item
                self.bin_list[bin_index][item_index] = 1

    def print_solution(self):
        for bin in self.bin_list:
            items_in_bin = [self.item_weight_list[i] for i, item in enumerate(bin) if item == 1]
            print("Weights of items in bin:", items_in_bin)