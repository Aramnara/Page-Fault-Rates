import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated data for page replacement algorithms
# Workload Scenarios: Low, Medium, High
workload_scenarios = ['Low', 'Medium', 'High']

# Simulated page fault rates (in %)
data = {
    'FIFO': [15.6, 25.3, 35.8],
    'LRU': [10.5, 18.2, 28.7],
    'ARC': [8.7, 14.9, 22.1],
    'ML-based': [6.1, 9.8, 14.3]
}

# Create a DataFrame for better visualization
df = pd.DataFrame(data, index=workload_scenarios)

# Plotting the simulated data
plt.figure(figsize=(8, 6))
df.plot(kind='bar', figsize=(10, 6), colormap="viridis")
plt.title('Page Fault Rates Across Different Workload Scenarios')
plt.xlabel('Workload Scenarios')
plt.ylabel('Page Fault Rate (%)')
plt.xticks(rotation=0)
plt.legend(title='Algorithm')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Display the simulated data to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Simulated Page Fault Rates", dataframe=df)
