from src.rangeCounter import *
from src.rangeDetector import *
from src.sorter import *
from src.validator import *
from src.outputFormatter import *
def range_and_readings_counter(periodic_samples):
    valid = getValidation(periodic_samples)
    if not(valid):
        return []

    sortedSamples = getSort(periodic_samples)
    rangeSubsets = detectRange(sortedSamples)
    finalList = []
    for subset in rangeSubsets:
        finalList.append(counter(subset))
    print(csvFormatter(finalList))
    return finalList
            