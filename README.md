# Real-Time Orientation Tracking Using an MPU6050 IMU and Complementary Filtering

This project implements real-time orientation tracking of an MPU6050 IMU. It contains the orientation as calculated by the gyroscope, accelerometer and a sensor fusion algorithm (complementary filter) that combines input from both sensors.

![alt text](https://github.com/Erak30/Complementary-Filter/blob/master/complementary_filter.jpg?raw=true)

## Structure

This project contains two folders, one to process and visualize the data using Python, and the other to send the imu data from the microcontroller via serial data to be interpretted by the Python code.
