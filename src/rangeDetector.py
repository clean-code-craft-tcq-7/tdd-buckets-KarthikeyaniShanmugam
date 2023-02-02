class RangeDetector:
    def __init__(self):
        self.max_difference = 1

    def range_finder(self,samples):                    
        sub_list = []
        sub_list.append([samples[0]])
        sub_index = 0
        for i in range(1,len(samples)):
            if abs(samples[i] - samples[i-1]) > self.max_difference:
                sub_index = sub_index+1
                sub_list.append([])
            sub_list[sub_index].append(samples[i])
        return sub_list

    def counter(self,input_list):
        final_list = []
        for sub_list in input_list:
            print("sub_list: ", sub_list)
            final_list.append([[sub_list[0],sub_list[-1]],len(sub_list)])
        return final_list

    def range_and_readings_counter(self,periodic_samples):
        periodic_samples.sort()
        range_splitted_list = self.range_finder(periodic_samples)
        final_list = self.counter(range_splitted_list)

        return final_list

if __name__ == "__main__":
    detector = RangeDetector() 
    print(detector.range_and_readings_counter([3, 3, 5, 4, 10, 11, 12]))