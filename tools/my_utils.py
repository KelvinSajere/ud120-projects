from math import log2 as log
def entropy_calculator(wieghted_averages):
    total_weight = sum(wieghted_averages)
    index_0 = wieghted_averages[0]/total_weight
    index_1 = wieghted_averages[1]/total_weight
    return [-index_0* log(index_0),-index_1 * log(index_1)]

print(entropy_calculator([2,2]))