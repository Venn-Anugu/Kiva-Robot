class sensors:
    def _init_(LIDAR_Sensor, IR_sensor,Camera):
        self.LIDAR_Sensor = LIDAR_Sensor
        self.IR_sensor = IR_sensor
        self.Camera = Camera
    def ReadBarcodes(x):
        print('Sensors scan and read barcodes to find the order position')
    def LocatePosition(x):
        print('Sensors locate the position of the order and send its info to Processing unit')
    def MeasureDistance(x):
        print('Sensors measure the distance after finding the order and send its closest pod')
    def Detectbstacles(x):
        print('IR sensors determine the surface and detect obstacles')
    def CapturesVisuals(x):
        print('Camera gives visuals access to the robots')