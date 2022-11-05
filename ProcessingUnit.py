class Processing_Unit:
    def _init_(Wifi_Module,Communication_Channel, Camera_Control_Unit, Sensor_Control_Unit):
        self.Wifi_Module = Wifi_Module
        self.Communication_Channel = Communication_Channel
        self.Camera_Control_Unit = Camera_Control_Unit
        self.Sensor_Control_Unit = Sensor_Control_Unit
    def Recieve(x):
        print('Processing Unit recieves order information from supervisor or recieves signals from signals')
    def Transmit(x):
        print('Processing Unit Transmits info to Kiva Robot')
    def Path_Planning(x):
        print('Processing Unit constructs a map when location of the order is detected by sensors')
    def AvoidObstacles(x):
        print('Processing Unit stops the robot and avoids obstacles if there is any in this path and then looks for another path')
    def PerformsSystemscheck():
        print('Processing unit performs full systems check on all components')