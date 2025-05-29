from main_window import Ui_MainWindow
from PyQt5 import QtCore
from uservo import UartServoManager
import serial
import time

SERVO_PORT_NAME = 'COM5'
SERVO_BAUDRATE = 115200
SERVO_WAITTIME = 10000.00


class Robot:
    def __init__(self, ui: Ui_MainWindow):
        self.app_ui = ui
        self.uart = None
        self.uservo = None
        self.timer = QtCore.QTimer()
        self.servo_angle_list_current = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.servo_angle_list_zero_point = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.initConnect()

    def initConnect(self):
        self.timer.timeout.connect(self.timeoutEvent)
        self.app_ui.pushButton.clicked.connect(self.btnConnectServo)
        self.app_ui.pushButton_3.clicked.connect(self.fixAngle)
        self.app_ui.pushButton_4.clicked.connect(self.startwalk)
        self.app_ui.pushButton_5.clicked.connect(self.setInitialGait)
        self.app_ui.pushButton_6.clicked.connect(self.isOnline)

        self.app_ui.widget_1.ui.horizontalSlider.valueChanged.connect(self.setAngle_1)
        self.app_ui.widget_2.ui.horizontalSlider.valueChanged.connect(self.setAngle_2)
        self.app_ui.widget_3.ui.horizontalSlider.valueChanged.connect(self.setAngle_3)
        self.app_ui.widget_4.ui.horizontalSlider.valueChanged.connect(self.setAngle_4)
        self.app_ui.widget_5.ui.horizontalSlider.valueChanged.connect(self.setAngle_5)
        self.app_ui.widget_6.ui.horizontalSlider.valueChanged.connect(self.setAngle_6)
        self.app_ui.widget_7.ui.horizontalSlider.valueChanged.connect(self.setAngle_7)
        self.app_ui.widget_8.ui.horizontalSlider.valueChanged.connect(self.setAngle_8)
        self.app_ui.widget_9.ui.horizontalSlider.valueChanged.connect(self.setAngle_9)
        self.app_ui.widget_10.ui.horizontalSlider.valueChanged.connect(self.setAngle_10)
        self.app_ui.widget_11.ui.horizontalSlider.valueChanged.connect(self.setAngle_11)
        self.app_ui.widget_12.ui.horizontalSlider.valueChanged.connect(self.setAngle_12)

    def btnConnectServo(self):
        if self.uart is not None:
            return

        print('init uart...')
        self.uart = serial.Serial(port=SERVO_PORT_NAME, baudrate=SERVO_BAUDRATE,
                                  parity=serial.PARITY_NONE, stopbits=1,
                                  bytesize=8, timeout=0)
        self.uservo = UartServoManager(self.uart)
        print('init uart success.')

        for i in range(12):
            print(self.uservo.ping(i))

        self.timer.start(50)

    def print_textEdit(self, p_str):
        self.app_ui.textEdit.append(p_str)

    def timeoutEvent(self):
        """ query_angle """
        if self.uart is None:
            return
        self.uservo: UartServoManager

        for i in range(12):
            self.servo_angle_list_current[i] = self.uservo.query_servo_angle(i)
        #print(self.servo_angle_list_current)
        self.updateAngle()

    def updateAngle(self):
        self.app_ui.widget_1.ui.doubleSpinBox.setValue(self.servo_angle_list_current[0])
        self.app_ui.widget_2.ui.doubleSpinBox.setValue(self.servo_angle_list_current[1])
        self.app_ui.widget_3.ui.doubleSpinBox.setValue(self.servo_angle_list_current[2])
        self.app_ui.widget_4.ui.doubleSpinBox.setValue(self.servo_angle_list_current[3])
        self.app_ui.widget_5.ui.doubleSpinBox.setValue(self.servo_angle_list_current[4])
        self.app_ui.widget_6.ui.doubleSpinBox.setValue(self.servo_angle_list_current[5])
        self.app_ui.widget_7.ui.doubleSpinBox.setValue(self.servo_angle_list_current[6])
        self.app_ui.widget_8.ui.doubleSpinBox.setValue(self.servo_angle_list_current[7])
        self.app_ui.widget_9.ui.doubleSpinBox.setValue(self.servo_angle_list_current[8])
        self.app_ui.widget_10.ui.doubleSpinBox.setValue(self.servo_angle_list_current[9])
        self.app_ui.widget_11.ui.doubleSpinBox.setValue(self.servo_angle_list_current[10])
        self.app_ui.widget_12.ui.doubleSpinBox.setValue(self.servo_angle_list_current[11])

    def fixAngle(self):
        self.uservo: UartServoManager
        for i in range(12):
            self.servo_angle_list_zero_point[i] = self.servo_angle_list_current[i]
            self.uservo.set_servo_angle(i, self.servo_angle_list_current[i])

    # def startwalk(self):
    #     self.uservo: UartServoManager
    #     for i in range(12):
    #         self.servo_angle_list_zero_point[i] = self.servo_angle_list_current[i]
    #         self.uservo.set_servo_angle(i, self.servo_angle_list_current[i])
    #     self.uservo.set_servo_angle(9, self.servo_angle_list_zero_point[9] + 18, False, None, 8)
    #     #self.uservo.wait(SERVO_WAITTIME)
    #     print("左侧膝关节下降")
    #     self.uservo.set_servo_angle(8, self.servo_angle_list_zero_point[8] - 18, False, None, 8)
    #     self.uservo.wait(SERVO_WAITTIME)
    #     print("左侧髋关节前摆")
    #     self.uservo.set_servo_angle(3, self.servo_angle_list_zero_point[3] + 16, False, None, 8)
    #     self.uservo.wait(SERVO_WAITTIME)
    #     print("右侧膝关节下降")
    #     self.uservo.set_servo_angle(9, self.servo_angle_list_zero_point[9] - 10, False, None, 5)
    #     self.uservo.wait(SERVO_WAITTIME)
    #     print("左侧膝关节站立")
    #     self.uservo.set_servo_angle(2, self.servo_angle_list_zero_point[2] + 25, False, None, 13)
    #     #self.uservo.wait(SERVO_WAITTIME)
    #     print("右侧髋关节前摆")
    #     self.uservo.set_servo_angle(8, self.servo_angle_list_zero_point[8] + 10, False, None, 10)
    #     self.uservo.wait(SERVO_WAITTIME)
    #     print("左侧髋关节后摆")
    #     self.uservo.set_servo_angle(3, self.servo_angle_list_zero_point[3] - 8, False, None, 10)
    #     #self.uservo.wait(SERVO_WAITTIME)
    #     print("左侧膝关节下降")
    #     self.uservo.set_servo_angle(4, self.servo_angle_list_zero_point[4] - 25, False, None, 10)
    #     print("左侧踝关节下降")

    def startwalk(self):
        targetAngle = []
        fr = open('motion.txt')
        for line in fr.readlines():
            lineArr = []
            curLine = line.strip().split('\t')
            for i in range(12):
                lineArr.append(float(curLine[i]))
            targetAngle.append(lineArr)
        t_s = time.time()
        for i in range(13):
            for j in range(12):
                t_a = time.time()
                flag = self.uservo.set_servo_angle(j, targetAngle[i][j], False, 40)
                #if(flag):
                    #print(self.uservo.query_servo_angle(j))
            # t_s = time.time()
            #self.uservo.wait(t_a)
            # t_e = time.time()
            # print(t_e - t_s)
            print("第"+ str(i) +"次角度:" )
            print("目标角度:")
            print(targetAngle[i])
            currentAngle = []
            for u in range(12):
                currentAngle.append(self.uservo.query_servo_angle(u))
            print("实际角度:")
            print(currentAngle)
            print("\n")
        self.uservo.wait()
        endAngle = []
        for v in range(12):
            endAngle.append(self.uservo.query_servo_angle(v))
        print("最终角度:")
        print(endAngle)
        t_e = time.time()
        print(t_e - t_s)
        # for u in range(12):
        #     print(self.uservo.query_servo_angle(u))




    def setInitialGait(self):
        self.uservo.set_servo_angle(0, 14, False, None, 10)
        self.uservo.set_servo_angle(1, -3, False, None, 10)
        self.uservo.set_servo_angle(2, 21, False, None, 10)
        self.uservo.set_servo_angle(3, 14, False, None, 10)
        self.uservo.set_servo_angle(4, 92, False, None, 10)
        self.uservo.set_servo_angle(5, -136, False, None, 10)
        self.uservo.set_servo_angle(6, -4, False, None, 10)
        self.uservo.set_servo_angle(7, 3, False, None, 10)
        self.uservo.set_servo_angle(8, -36, False, None, 10)
        self.uservo.set_servo_angle(9, 37, False, None, 10)
        self.uservo.set_servo_angle(10, -11, False, None, 10)
        self.uservo.set_servo_angle(11, -85, False, None, 10)

    def isOnline(self):
        print("在线状态:")
        for i in range(12):
            is_online = self.uservo.ping(i)
            print("舵机ID={} 是否在线: {}".format(i, is_online))

    def setAngle_1(self, value):
        self.servo_angle_list_current[0] = self.servo_angle_list_zero_point[0] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(0, self.servo_angle_list_current[0])

    def setAngle_2(self, value):
        self.servo_angle_list_current[1] = self.servo_angle_list_zero_point[1] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(1, self.servo_angle_list_current[1])

    def setAngle_3(self, value):
        self.servo_angle_list_current[2] = self.servo_angle_list_zero_point[2] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(2, self.servo_angle_list_current[2])

    def setAngle_4(self, value):
        self.servo_angle_list_current[3] = self.servo_angle_list_zero_point[3] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(3, self.servo_angle_list_current[3])

    def setAngle_5(self, value):
        self.servo_angle_list_current[4] = self.servo_angle_list_zero_point[4] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(4, self.servo_angle_list_current[4])

    def setAngle_6(self, value):
        self.servo_angle_list_current[5] = self.servo_angle_list_zero_point[5] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(5, self.servo_angle_list_current[5])

    def setAngle_7(self, value):
        self.servo_angle_list_current[6] = self.servo_angle_list_zero_point[6] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(6, self.servo_angle_list_current[6])

    def setAngle_8(self, value):
        self.servo_angle_list_current[7] = self.servo_angle_list_zero_point[7] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(7, self.servo_angle_list_current[7])

    def setAngle_9(self, value):
        self.servo_angle_list_current[8] = self.servo_angle_list_zero_point[8] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(8, self.servo_angle_list_current[8])

    def setAngle_10(self, value):
        self.servo_angle_list_current[9] = self.servo_angle_list_zero_point[9] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(9, self.servo_angle_list_current[9])

    def setAngle_11(self, value):
        self.servo_angle_list_current[10] = self.servo_angle_list_zero_point[10] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(10, self.servo_angle_list_current[10])

    def setAngle_12(self, value):
        self.servo_angle_list_current[11] = self.servo_angle_list_zero_point[11] + 1 * value
        if self.uart is None:
            return
        self.uservo.set_servo_angle(11, self.servo_angle_list_current[11])
