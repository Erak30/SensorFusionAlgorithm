import imu
import complementary_filter
import plot

mpu = imu.imu()
filter1 = complementary_filter.complementary_filter(0.95)
filter2 = complementary_filter.complementary_filter(0.0)
filter3 = complementary_filter.complementary_filter(1.0)
mpu.calibrate()
graphs = plot.plot()

while 1:
    try:
        mpu.calculate()
        pitch1 = filter1.calculate_pitch(mpu.gyro_pitch, mpu.acc_pitch)
        pitch2 = filter2.calculate_pitch(mpu.gyro_pitch, mpu.acc_pitch)
        pitch3 = filter3.calculate_pitch(mpu.gyro_pitch, mpu.acc_pitch)

        roll1 = filter1.calculate_roll(mpu.gyro_roll, mpu.acc_roll)
        roll2 = filter2.calculate_roll(mpu.gyro_roll, mpu.acc_roll)
        roll3 = filter3.calculate_roll(mpu.gyro_roll, mpu.acc_roll)


        print("roll: " + "{:.2f}".format(roll1) + " pitch: " + "{:.2f}".format(pitch1))
        graphs.update(pitch1, pitch2, pitch3, roll1, roll2, roll3)
    except KeyboardInterrupt:
        print("Exiting...")
        break
