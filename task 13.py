import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temp_original = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

temp_spike = np.array([18.0, 20.0, 22.5, 35.0, 25.0, 25.5, 25.0])

ten_min_times = np.arange(8, 14 + 1/6, 1/6)
target_time = 10.5  

for temp_data, title in [(temp_original, "Original Data"), (temp_spike, "Parameter Changed (Spike at 11:00)")]:
    linear = interp1d(hours, temp_data, kind="linear")
    cubic = CubicSpline(hours, temp_data)
    print(f"--- {title} ---")
    print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
    print(f"Cubic estimate at 10:30:  {float(cubic(target_time)):.2f} C\n")
distance_km = np.array([0.0, 2.5, 5.0, 8.0, 10.0])
elevation_m = np.array([120.0, 145.0, 130.0, 190.0, 175.0])

linear_elev = interp1d(distance_km, elevation_m, kind="linear")
cubic_elev = CubicSpline(distance_km, elevation_m)

fine_distances = np.arange(0.0, 10.1, 0.5)
print("--- Real-World Case: Road Elevation Profile ---")
print(f"Estimated elevation at 4.2 km (Cubic): {float(cubic_elev(4.2)):.2f} meters")

plt.figure(figsize=(8, 5))
plt.scatter(distance_km, elevation_m, color="red", label="GPS Checkpoints", zorder=5)
plt.plot(fine_distances, linear_elev(fine_distances), "--", label="Linear Interpolation")
plt.plot(fine_distances, cubic_elev(fine_distances), label="Cubic Spline Profile", color="green")
plt.xlabel("Road Distance (km)")
plt.ylabel("Elevation (m)")
plt.title("Road Elevation Interpolation from Sparse GPS Checkpoints")
plt.legend()
plt.grid(True)
plt.show()