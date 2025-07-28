print("Welcome to the Electrical Load Analyzer")
import pandas as pd

# Load CSV
data = pd.read_csv("data.csv")

# Preview
print("\n=== Raw Electrical Usage Data ===")
print(data)

# Calculate total energy used in kWh
data['Total_kWh'] = (data['Watts'] * data['Hours Used per Day'] * data['Days Used']) / 1000

# Define average cost per kWh
COST_PER_KWH = 0.15 #roughly the avg cost per KWH
data['Estimated Cost'] = data['Total_kWh'] * COST_PER_KWH

# Print results
print("\n=== Energy Usage Summary ===")
print(data[['Device', 'Total_kWh', 'Estimated Cost']])

# Print total household usage and cost
total_kwh = data['Total_kWh'].sum()
total_cost = data['Estimated Cost'].sum()

print(f"\nTotal Monthly Usage: {total_kwh:.2f} kWh")
print(f"Total Estimated Cost: ${total_cost:.2f}")