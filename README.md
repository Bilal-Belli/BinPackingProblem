# Bin Packing Problem Optimization Algorithmes
This repository serves as a comprehensive collection of solutions and implementations for the Bin Packing 1D problem. It is a classic optimization problem where a set of items with varying sizes must be packed into a fixed number of bins, while minimizing wasted space.
## Code and Algorithmes
### Language & Framework
- The code is written in the Python language.
- The framework for the GUI is Tkinter.
### Features
- Most common methods for resolving this problem.
- Graphical user interface.
<div align="center">
   <img  width="683" src="https://github.com/Bilal-Belli/BinPackingProblem/assets/74218805/1efc6755-c0a3-47e0-9cbb-86325abd0527">
</div>

### List of Implimented Algorithmes
- Branch and bound.
- Best Fit.
- First Fit.
- Next Fit.
- Worst Fit
- Tabu Search.
- Genetic Algorithme.
- Hybridation WWO (water waves optimiser) and Simulated Annealing.
## Article (describe the hybridation schema)
### Research Paper
The available research paper document about our hybrid solution is written in 'French'. You can check it in this <a href="https://github.com/Bilal-Belli/BinPackingProblem/blob/main/ResearchPaper/OPT_SIQ1_EQUIPE02_RESEARCH_PAPER.pdf">link</a>.
### Benchmarking
- The resulting benchmark table is <a href="https://github.com/Bilal-Belli/BinPackingProblem/blob/main/benchmarks/TableBenchmarkingResults.xlsx">here</a>.
- We chose to conduct our test on 18 benchmarks, which are available <a href="https://github.com/Bilal-Belli/BinPackingProblem/tree/main/benchmarks">here</a>.
### Performances
#### Comparaison Fitness between (Exact solution, WWO, WWO with hybridation)
<div align="center">
   <img  width="683" src="https://github.com/Bilal-Belli/BinPackingProblem/assets/74218805/de5ba143-78a8-4ecf-a20b-ebc4149e1b01">
</div>

#### Comparaison Execution time between (WWO without hybridation and WWO with hybridation)
<div align="center">
   <img  width="683" src="https://github.com/Bilal-Belli/BinPackingProblem/assets/74218805/53cff904-e973-446d-a4ba-c4889ad61a4a">
</div>

### For Testing
- First, download or clone the repository.
- Second, ensure that you have installed the required libraries and fixed dependencies (path).
- There is a file named "testParameters.py". If you select another benchmarking file, you will need to make changes in this file (Bins max size and Number of objects).

### License
This repository is licensed under the MIT License.

### Thank you to the contributors
- 
- 
- 
- 
- 
