import csv
from email import header
def csvFormatter(inputList):
    output_string = ""
    output_string += (str("Range" + ","+ "Readings"))
    output_string += "\n"
    for item in inputList:
        output_string += "{}-{},{}".format(str(item[0]),str(item[1]), item[2])
        output_string += "\n"
    return output_string