% Data from the table
benchmarks = {'BPP\_50\_50\_0.1\_0.7\_7', 'BPP\_50\_400\_0.2\_0.8\_4', 'BPP\_100\_750\_0.2\_0.7\_0', 'BPP\_200\_1000\_0.2\_0.8\_8', 'BPP\_300\_50\_0.1\_0.7\_0', 'BPP\_500\_50\_0.1\_0.7\_2', 'BPP\_750\_500\_0.2\_0.8\_8', 'BPP\_750\_750\_0.2\_0.8\_9', 'BPP\_750\_1000\_0.2\_0.8\_9', 'BPP\_1000\_50\_0.1\_0.7\_1', 'BPP\_1000\_125\_0.2\_0.8\_9', 'BPP\_1000\_150\_0.2\_0.8\_9', 'BPP\_1000\_200\_0.2\_0.8\_9', 'BPP\_1000\_300\_0.2\_0.8\_9', 'BPP\_1000\_400\_0.2\_0.8\_9', 'BPP\_1000\_500\_0.2\_0.8\_9', 'BPP\_1000\_750\_0.2\_0.8\_9', 'BPP\_1000\_1000\_0.1\_0.7\_0'};
T_exWWO = [0.42, 0.52, 1.41, 4.86, 9.93, 26.15, 63.69, 64, 65, 121, 129, 120, 118, 116, 137, 116, 116, 116];
T_exHybrid = [0.47, 0.4, 1.5, 4.7, 9.8, 28, 67, 64.3, 67, 115, 131, 121, 123, 117, 135, 126, 131, 125];

% Create the grouped bar plot
figure;
bar([T_exWWO', T_exHybrid'], 'grouped');

% Set plot labels and title
xticks(1:length(benchmarks));
xticklabels(benchmarks);
xlabel('Benchmark');
ylabel('Execution Time (T_{ex})');
title('Comparison of T_{ex} WWO sans Hybridation and T_{ex} Hybridation for different Benchmarks');

% Add legend
legend('T_{ex} WWO sans Hybridation', 'T_{ex} Hybridation');

% Customize plot appearance
grid on;
set(gca, 'FontSize', 10);
set(gca, 'FontWeight', 'bold');
xtickangle(45);

% Adjust figure size if needed
set(gcf, 'Position', [100, 100, 1000, 500]);
