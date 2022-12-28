class Field():
    
    def __init__(self, length, width):
        self.field = []
        for meter_l in range(length):
            x_axis = []
            for meter_w in range(width):
                y_axis = []
                x_axis.append(y_axis)
            self.field.append(x_axis)
            
    def show(self):
        # the for loop allows you to iterate through each individual array/row/section within the map.
        # map(str, i) converts all the sectors within each section to a string and then,
        # ' '.join combines the individual items in a single string, and then each section gets printed one by one.
        for i in self.field:
            print(' '.join(map(str, i)))


    