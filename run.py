import matplotlib.pyplot as plt

from signals import generate_sine_wave
wave = generate_sine_wave(5, 2, 100)
plt.plot(wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Signal')
plt.show()

from signals import generate_step_function(t, step_time)
t = np.linspace(-1,1)
step = generate_step_function(t, 0)
plt.plot(t, step)
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.title('Step Function')
plt.show()