import matplotlib.pyplot as plt

from signals import generate_sine_wave
wave = generate_sine_wave(5, 2, 100)
plt.plot(wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Signal')
plt.show()