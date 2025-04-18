import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set page configuration
st.set_page_config(page_title="Ocean Temperature Impact Visualizer", layout="wide")

# Title and description
st.title("Ocean Temperature Impact Visualizer")
st.markdown("""
This app visualizes ocean temperature trends and their ecological impacts.
The data is simulated for demonstration, showing average sea surface temperatures from 1980 to 2025.
""")

# Generate sample data
years = np.arange(1980, 2026)
np.random.seed(42)
temperatures = 26 + 0.02 * (years - 1980) + np.random.normal(0, 0.2, len(years))
data = pd.DataFrame({"Year": years, "Temperature (°C)": temperatures})

# Plot temperature trend
st.subheader("Ocean Temperature Trend (1980–2025)")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data["Year"], data["Temperature (°C)"], color="blue", label="Sea Surface Temperature")
ax.axhline(y=28, color="red", linestyle="--", label="Coral Bleaching Threshold (28°C)")
ax.set_xlabel("Year")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Simulated Ocean Temperature Trend")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Calculate and display impacts
st.subheader("Ecological Impacts")
mean_temp = data["Temperature (°C)"].mean()
recent_temp = data["Temperature (°C)"].iloc[-1]

impacts = []
if recent_temp > 28:
    impacts.append("**Coral Bleaching**: High risk due to temperatures exceeding 28°C.")
if recent_temp > 27.5:
    impacts.append("**Sea Level Rise**: Accelerated due to thermal expansion and ice melt.")
if mean_temp > 26.5:
    impacts.append("**Marine Ecosystem Stress**: Increased stress on fish and plankton populations.")

if impacts:
    for impact in impacts:
        st.markdown(impact)
else:
    st.markdown("No significant impacts detected based on current temperature thresholds.")

# Sidebar for user interaction
st.sidebar.header("Settings")
temp_threshold = st.sidebar.slider(
    "Set Coral Bleaching Threshold (°C)", min_value=26.0, max_value=30.0, value=28.0, step=0.1
)
st.sidebar.markdown("Adjust the threshold to see how it affects impact detection.")

# Update plot with user-defined threshold
st.subheader("Custom Threshold Analysis")
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(data["Year"], data["Temperature (°C)"], color="blue", label="Sea Surface Temperature")
ax2.axhline(y=temp_threshold, color="orange", linestyle="--", label=f"Custom Threshold ({temp_threshold}°C)")
ax2.set_xlabel("Year")
ax2.set_ylabel("Temperature (°C)")
ax2.set_title("Temperature with Custom Threshold")
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

# Display data table
st.subheader("Data Table")
st.dataframe(data.tail(10))  # Show last 10 years