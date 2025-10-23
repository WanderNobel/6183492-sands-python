import numpy as np
import matplotlib.pyplot as plt

from signals import generate_sine_wave
t, wave = generate_sine_wave(1, 1, 0, 1)
plt.figure(1)
plt.plot(t, wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Signal')

from signals import generate_step_function
t = np.linspace(-1,1)
step = generate_step_function(t, 0)
plt.figure(2)
plt.plot(t, step)
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')
plt.title('Step Function')

from signals import generate_sine_wave
t, wave = generate_sine_wave(1, 1, 0.5, 1)
plt.figure(3)
plt.plot(t, wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time-Shifted Sinusoidal Signal')

from signals import generate_sine_wave
t, wave = generate_sine_wave(1, 1, 0.5, 2)
plt.figure(4)
plt.plot(t, wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Time-Shifted and Time-Scaled Sinusoidal Signal')
plt.show()