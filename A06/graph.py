import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("graph.csv")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df["x"], df["y"], marker="*", color="purple")
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = cos(x)")
plt.grid(True)

# Save image
plt.savefig("graph.png", dpi=300)