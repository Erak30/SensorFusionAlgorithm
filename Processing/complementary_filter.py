class complementary_filter: 
    def __init__(self, alpha=0.99):
        self.alpha = alpha
        self.pitch = 0.0
        self.roll = 0.0

    def calculate_pitch(self, gyro_pitch, acc_pitch):
        self.pitch = self.alpha * (self.pitch + gyro_pitch) + (1 - self.alpha) * acc_pitch

        if self.pitch > 180: 
            self.pitch -= 360
        elif self.pitch < -180:
            self.pitch += 360
        return self.pitch
    
    def calculate_roll(self, gyro_roll, acc_roll):
        self.roll = self.alpha * (self.roll - gyro_roll) + (1 - self.alpha) * acc_roll

        if self.roll > 180: 
            self.roll -= 360
        elif self.roll < -180:
            self.roll += 360
        return self.roll
