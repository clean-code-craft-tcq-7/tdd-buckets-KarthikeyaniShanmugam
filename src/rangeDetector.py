from src.configuration import *
def detectRange(samples): 
    sub_list = []
    sub_list.append([samples[0]])
    sub_index = 0
    for i in range(1,len(samples)):
        if abs(samples[i] - samples[i-1]) > max_difference:
            sub_index = sub_index+1
            sub_list.append([])
        sub_list[sub_index].append(samples[i])
    return sub_list