% Data from the table
benchmarks = {'BPP\_50\_50\_0.1\_0.7\_7', 'BPP\_50\_400\_0.2\_0.8\_4', 'BPP\_100\_750\_0.2\_0.7\_0', 'BPP\_200\_1000\_0.2\_0.8\_8', 'BPP\_300\_50\_0.1\_0.7\_0', 'BPP\_500\_50\_0.1\_0.7\_2', 'BPP\_750\_500\_0.2\_0.8\_8', 'BPP\_750\_750\_0.2\_0.8\_9', 'BPP\_750\_1000\_0.2\_0.8\_9', 'BPP\_1000\_50\_0.1\_0.7\_1', 'BPP\_1000\_125\_0.2\_0.8\_9', 'BPP\_1000\_150\_0.2\_0.8\_9', 'BPP\_1000\_200\_0.2\_0.8\_9', 'BPP\_1000\_300\_0.2\_0.8\_9', 'BPP\_1000\_400\_0.2\_0.8\_9', 'BPP\_1000\_500\_0.2\_0.8\_9', 'BPP\_1000\_750\_0.2\_0.8\_9', 'BPP\_1000\_1000\_0.1\_0.7\_0'};
solutionExact = [23, 36, 45, 110, 129, 198, 385, 385, 394, 391, 498, 525, 508, 516, 504, 510, 523, 397];
solutionWWO = [31, 41, 64, 145, 181, 276, 529, 532, 540, 544, 695, 712, 697, 700, 702, 707, 718, 563];
solutionHybrid = [29, 40, 59, 136, 173, 257, 527, 530, 525, 517, 683, 699, 680, 685, 669, 687, 702, 528];

% Create the grouped bar plot
figure;
bar([solutionExact', solutionWWO', solutionHybrid']);

% Set plot labels and title
xticks(1:length(benchmarks));
xticklabels(benchmarks);
xlabel('Benchmark');
ylabel('Solution');
title('Comparison of Solutions for each Benchmark');
legend('Solution Exact', 'Solution WWO sans Hybridation', 'Solution Hybridation');

% Customize plot appearance
grid on;
set(gca, 'FontSize', 10);
set(gca, 'FontWeight', 'bold');
xtickangle(45);

% Adjust figure size if needed
set(gcf, 'Position', [100, 100, 1000, 500]);
