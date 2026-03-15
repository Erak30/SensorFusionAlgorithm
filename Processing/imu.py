import serial
import time
import numpy

class imu:
    def __init__(self):
        self.esp32 = serial.Serial(port='COM5', baudrate=115200, timeout=1)

        self.last_time = time.time()

        self.acc_roll = 0.0
        self.gyro_roll = 0.0

        self.acc_pitch = 0.0
        self.gyro_pitch = 0.0

    def calibrate(self):
        print("Calibrating...")
        gyro_offset_x = 0.0
        gyro_offset_y = 0.0
        gyro_offset_z = 0.0
        samples = 200
        for sample in range(samples):
            line = self.esp32.readline().decode('ascii').strip().split(',')
            gyro_offset_x += float(line[3])
            gyro_offset_y += float(line[4])
            gyro_offset_z += float(line[5])

        gyro_offset_x /= samples
        gyro_offset_y /= samples
        gyro_offset_z /= samples

        self.gyro_offset_x = gyro_offset_x
        self.gyro_offset_y = gyro_offset_y
        self.gyro_offset_z = gyro_offset_z

    def calculate(self):
        data = self.esp32.readline().decode('ascii').strip().split(',')

        accel_x = float(data[0])
        accel_y = float(data[1])
        accel_z = float(data[2])
        gyro_x = float(data[3])
        gyro_y = float(data[4])
        gyro_z = float(data[5])

        gyro_x = (gyro_x - self.gyro_offset_x) / 131
        gyro_y = (gyro_y - self.gyro_offset_y) / 131
        gyro_z = (gyro_z - self.gyro_offset_z) / 131

        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time

        self.acc_pitch = numpy.atan2(accel_y, accel_z) * 180 / numpy.pi
        self.gyro_pitch = gyro_x * delta_time

        self.acc_roll = numpy.atan2(accel_x, accel_z) * 180 / numpy.pi 
        self.gyro_roll = gyro_y * delta_time    
