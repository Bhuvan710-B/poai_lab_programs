"""
Experiment 3B - Fuzzy Inference System
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement a simple fuzzy inference system that sets a fan speed
    from the room temperature.

Requirements:
    pip install numpy scikit-fuzzy matplotlib

Run:
    python 3B_fuzzy_inference.py
    (A window with the membership-function plots opens first; close it and
     the result is printed. On a machine without a display, run
     `MPLBACKEND=Agg python 3B_fuzzy_inference.py` to skip the window.)

Steps:
    1. Define the input (temperature) and output (fan speed) universes.
    2. Define triangular membership functions (Low / Medium / High).
    3. Plot the membership functions.
    4. Fuzzification: find how much 28 C belongs to Low / Medium / High.
    5. Rules:  Low temp -> Low fan,  Medium -> Medium,  High -> High.
    6. Defuzzification: centroid of the combined fan-speed sets -> crisp value.

Output (computed by this program; 28 C is 0.2 Medium and 0.8 High):
    Temperature: 28°C
    Fuzzified fan speed: 7.56

NOTE: The lab manual's recorded output shows 6.00 for this same code, but
this program prints 7.56. See the README.
"""

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Step 1: Fuzzy variables (input: temperature, output: fan speed)
temperature = np.arange(0, 41, 1)   # 0 to 40 degrees Celsius
fan_speed = np.arange(0, 11, 1)     # 0 to 10

# Step 2: Triangular membership functions [left foot, peak, right foot]
temp_low = fuzz.trimf(temperature, [0, 0, 20])
temp_medium = fuzz.trimf(temperature, [10, 20, 30])
temp_high = fuzz.trimf(temperature, [20, 30, 40])

fan_low = fuzz.trimf(fan_speed, [0, 0, 5])
fan_medium = fuzz.trimf(fan_speed, [2, 5, 8])
fan_high = fuzz.trimf(fan_speed, [5, 10, 10])

# Step 3: Visualise the membership functions
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(temperature, temp_low, label="Low")
plt.plot(temperature, temp_medium, label="Medium")
plt.plot(temperature, temp_high, label="High")
plt.title("Temperature Membership Functions")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Degree")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(fan_speed, fan_low, label="Low")
plt.plot(fan_speed, fan_medium, label="Medium")
plt.plot(fan_speed, fan_high, label="High")
plt.title("Fan Speed Membership Functions")
plt.xlabel("Fan Speed")
plt.ylabel("Membership Degree")
plt.legend()

plt.tight_layout()
plt.show()

# Step 4: Fuzzification of a crisp temperature input
temperature_input = 28  # Example temperature in °C

temp_low_level = fuzz.interp_membership(temperature, temp_low, temperature_input)
temp_medium_level = fuzz.interp_membership(temperature, temp_medium, temperature_input)
temp_high_level = fuzz.interp_membership(temperature, temp_high, temperature_input)

# Step 5: Apply the fuzzy rules
#   Rule 1: If temperature is Low,    fan speed is Low
#   Rule 2: If temperature is Medium, fan speed is Medium
#   Rule 3: If temperature is High,   fan speed is High
fan_low_level = temp_low_level
fan_medium_level = temp_medium_level
fan_high_level = temp_high_level

# Step 6: Defuzzification - combine the weighted output sets, take the centroid
aggregated = (fan_low * fan_low_level
              + fan_medium * fan_medium_level
              + fan_high * fan_high_level)
fan_output = fuzz.defuzz(fan_speed, aggregated, "centroid")

# Step 7: Print the result
print(f"Temperature: {temperature_input}°C")
print(f"Fuzzified fan speed: {fan_output:.2f}")
