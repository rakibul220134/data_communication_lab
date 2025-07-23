import numpy as np
import matplotlib.pyplot as plt

# Input binary data
data = "1011001"
bit_duration = 1  # seconds per bit
sample_rate = 1000  # samples per second
t = np.linspace(0, len(data) * bit_duration, len(data) * sample_rate)

# Carrier frequencies and parameters
f_carrier = 5  # 5Hz
amp_high = 1
amp_low = 0.1  # For ASK 0
f_low = 3
f_high = 7
phase_0 = 0
phase_1 = np.pi

# Generate signals
ask = np.zeros(len(t))
fsk = np.zeros(len(t))
psk = np.zeros(len(t))

for i, bit in enumerate(data):
    start = i * sample_rate
    end = (i + 1) * sample_rate
    time_segment = t[start:end]

    # ASK: Amplitude changes
    amplitude = amp_high if bit == '1' else amp_low
    ask[start:end] = amplitude * np.sin(2 * np.pi * f_carrier * time_segment)

    # FSK: Frequency changes
    freq = f_high if bit == '1' else f_low
    fsk[start:end] = np.sin(2 * np.pi * freq * time_segment)

    # PSK: Phase changes
    phase = phase_1 if bit == '1' else phase_0
    psk[start:end] = np.sin(2 * np.pi * f_carrier * time_segment + phase)

# Plotting
plt.figure(figsize=(14, 10))

plt.subplot(3, 1, 1)
plt.plot(t, ask, color='blue')
plt.title("Amplitude Shift Keying (ASK)")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, fsk, color='green')
plt.title("Frequency Shift Keying (FSK)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, psk, color='red')
plt.title("Phase Shift Keying (PSK)")
plt.grid(True)

plt.xlabel("Time (s)")
plt.tight_layout()
plt.show()
