import matplotlib.pyplot as plt

from signals import generate_sine_wave
wave = generate_sine_wave(5, 2, 100)

#print(wave[:10])
plt.plot(wave)
plt.show()