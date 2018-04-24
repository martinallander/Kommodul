class Sensor_Data:
    def __init__(self, acceleromter, gyrometer, ir, tof):
        self.acceleromter = acceleromter
        self.gyrometer = gyrometer
        self.ir = ir
        self.tof = tof
    def __str__(self):
        return "Gyrometer values: " + str(self.gyrometer) + "\n Acceleromter values: " + str(self.acceleromter) +   "\n IR values: " + self.ir_str() +"\n ToF distance: " + str(self.tof) 
    def ir_str(self):
    	formatted_ir = ""
    	for i in range(len(self.ir)):
    		formatted_ir += str(self.ir[i]) + " "
    		if (i % 4) == 0:
    			formatted_ir += "\n"
    	return formatted_ir