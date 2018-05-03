class Sensor_Data:
    def __init__(self, has_data = True):
        self.has_data = has_data
        self.acc = [0.0, 0.0, 0.0]
        self.gyro = [0.0, 0.0, 0.0]
        self.ir = [0.0] * 64
        self.tof = 0.0
        
    def set_acc(self, acc):
        self.acc = acc

    def set_gyro(self, gyro):
        self.gyro = gyro

    def set_ir(self, ir):
        self.ir = ir

    def set_dist(self, tof):
        self.tof = tof
    
    def __str__(self):
        return "Gyrometer values: " + str(self.gyro) + "\n Acceleromter values: " + str(self.acc) +   "\n IR values: " + self.ir_str() +"\n ToF distance: " + str(self.tof) 

    def ir_str(self):
    	formatted_ir = ""
    	for i in range(len(self.ir)):
    		formatted_ir += str(self.ir[i]) + " "
    		if (i % 4) == 0:
    			formatted_ir += "\n"
    	return formatted_ir
