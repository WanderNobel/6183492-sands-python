import numpy as np 

def generate_sine_wave(frequency, duration, time_shift, time_scale):
    """
    This function generates a sine wave signal

    Parameters:
        frequency (float) : Frequency of the sine wave in Hertz
        duration (float) : Duration of the signal in seconds
        time_shift (float) : Time shift applied to the sin wave in seconds
        time_scale (float) : Scaling factor applied to the time axis

    Returns:
        tuple : (t, wave)
        t : Time array from 0 to duration with 100 points
        wave: sine wave values
    """
    t = np.linspace(0, duration, 100)
    wave = np.sin(2 * np.pi * frequency * t * time_scale + time_shift)
    return t, wave 

def generate_step_function(t, step_time):
    """
    This function generates a step function signal

    Parameters:
        t (float) : Time values at which the step function is evaluated in seconds
        step_time (float) : The time at which the step transition occurs in seconds

    Returns:
        numpy.ndarray : step funtion values: 0 for t < step time, 1 for t > step_time.
    """"
    return np.where(t < step_time, 0, 1)


