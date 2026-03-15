import matplotlib.pyplot as plt

class plot:
    def __init__(self):
        self.window_size = 100
        self.pitch_values1 = []
        self.pitch_values2 = []
        self.pitch_values3 = []

        self.roll_values1 = []
        self.roll_values2 = []
        self.roll_values3 = []

        plt.ion()
        self.fig, (self.ax1,self.ax2) = plt.subplots(2)
        self.fig.set_size_inches(8, 4)
        plt.subplots_adjust(hspace = 1.0, wspace = 0.5, right = 0.7)

        self.ax1.set_title('pitch')
        self.ax1.set_ylabel('angle (degrees)')

        self.ax2.set_title('roll')
        self.ax2.set_ylabel('angle (degrees)')

        self.line1, = self.ax1.plot(self.pitch_values1)
        self.line2, = self.ax1.plot(self.pitch_values2)
        self.line3, = self.ax1.plot(self.pitch_values3)
        self.ax1.legend([self.line1, self.line2, self.line3], ['complementary filter', 'accelerometer', 'gyroscope'], bbox_to_anchor=[1.05, 0.5], loc='center left', borderaxespad=0.)
        #self.ax1.legend([self.line1, self.line2, self.line3], ['complementary filter', 'accelerometer', 'gyroscope'], bbox_to_anchor=(0., -1.02, 1., .102), loc='lower left', mode="expand", borderaxespad=0., ncols=3)


        self.ax1.set_ylim(-180, 180)
        self.ax1.set_xlim(0, self.window_size)

        self.line4, = self.ax2.plot(self.roll_values1)
        self.line5, = self.ax2.plot(self.roll_values2)
        self.line6, = self.ax2.plot(self.roll_values3)
        self.ax2.legend([self.line1, self.line2, self.line3], ['complementary filter', 'accelerometer', 'gyroscope'], bbox_to_anchor=[1.05, 0.5], loc='center left', borderaxespad=0.)

#       self.ax2.legend([self.line4, self.line5, self.line6], ['complementary filter', 'accelerometer', 'gyroscope'])


        self.ax2.set_ylim(-180, 180)
        self.ax2.set_xlim(0, self.window_size)

        plt.show(block=False)

    def update(self, pitch1, pitch2, pitch3, roll1, roll2, roll3):

        self.pitch_values1.append(pitch1)
        self.pitch_values2.append(pitch2)
        self.pitch_values3.append(pitch3)

        self.roll_values1.append(roll1)
        self.roll_values2.append(roll2)
        self.roll_values3.append(roll3)

        x = range(len(self.pitch_values1))

        self.line1.set_data(x[-self.window_size:], self.pitch_values1[-self.window_size:])
        self.line2.set_data(x[-self.window_size:], self.pitch_values2[-self.window_size:])
        self.line3.set_data(x[-self.window_size:], self.pitch_values3[-self.window_size:])

        self.line4.set_data(x[-self.window_size:], self.roll_values1[-self.window_size:])
        self.line5.set_data(x[-self.window_size:], self.roll_values2[-self.window_size:])
        self.line6.set_data(x[-self.window_size:], self.roll_values3[-self.window_size:])

        if len(x) > self.window_size:
            self.ax1.set_xlim(len(x)-self.window_size, len(x))
            self.ax2.set_xlim(len(x)-self.window_size, len(x))


        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
