import numpy as np 

def generate_sine_wave(frequency, duration, sample_rate):
    samples = duration * sample_rate 
    t = np.linspace(0, duration, samples)
    wave = np.sin(2 * np.pi * frequency * t)
    return wave 

def generate_step_function(t, step_time):
    return np.where(t < step_time, 0, 1)

