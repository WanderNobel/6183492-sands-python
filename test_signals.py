import numpy as np

from signals import generate_sine_wave
def test_generate_sine_wave():
    t, wave = generate_sine_wave(1, 1, 0, 1)
    assert len(t) == 100
    assert len(wave) == 100
    assert t[0] == 0 
    assert np.all(wave >= -1) and np.all(wave <= 1)

    t, wave = generate_sine_wave(1, 1, 0.5, 1)
    assert len(t) == 100
    assert len(wave) == 100
    assert t[0] == 0 
    assert np.all(wave >= -1) and np.all(wave <= 1)

    t, wave = generate_sine_wave(1, 1, 0.5, 2)
    assert len(t) == 100
    assert len(wave) == 100
    assert t[0] == 0 
    assert np.all(wave >= -1) and np.all(wave <= 1)
    
from signals import generate_step_function
def test_generate_step_function():
    t = np.linspace(-1,1)
    step = generate_step_function(t, 0)
    assert len(t) == 50
    assert len(step) == 50
    assert t[0] == -1
    assert np.all(step[t < 0] == 0) and np.all(step[t < 0] == 0)
