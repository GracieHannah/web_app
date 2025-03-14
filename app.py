import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    vehicle_df = pd.read_csv("vehicles_us.csv")
    return vehicle_df

vehicle_df = load_data()


st.title("Vehicle Sales Data Simulator")
st.header("Explore Vehicle Data")

st.markdown("""
This analysis will be used as a tool in a data simulator. This will accommodate 
the simulation of random events, allowing users to explore probabilities and 
outcomes in a visually interactive manner.This dashboard provides insights into 
vehicle data by displaying histograms and scatter plots.
Use the sidebar to filter or toggle visualizations.
""")

st.sidebar.header("Options")
show_histogram = st.sidebar.checkbox("Histogram: Model Year by Paint Color and Fuel", value=True)
show_scatter = st.sidebar.checkbox("Scatter Plot: Show Price vs. Odometer Scatter Plot", value=True)
show_bar = st.sidebar.checkbox("Bar Graph: Vehicle Manufacturer vs. Odometer", value=True)

st.subheader("Histogram: Model Year by Paint Color and Fuel")
hist_fig = px.histogram(
    vehicle_df,
    x="model_year",
    color="paint_color",
    facet_col="fuel",
    nbins=20,
    title="Distribution of Model Year by Paint Color and Fuel Type"
)
st.plotly_chart(hist_fig)

# 2. Conditional Scatter Plot: Price vs. Odometer by Condition
if show_scatter:
    st.subheader("Scatter Plot: Price vs. Odometer by Condition")
    scatter_fig = px.scatter(
        vehicle_df,
        x="odometer",
        y="price",
        color="condition",
        title="Price vs. Odometer by Condition"
    )
    st.plotly_chart(scatter_fig)

st.markdown("Adjust the options on the sidebar to explore the data further.")

# 3. Bar Chart: Vehicle Manufacturer vs. Odometer
vehicle_df = df.copy()
vehicle_df['manufacturer'] = vehicle_df['model'].str[:3]

st.header('Vehicle Manufacturer vs. Odometer')
st.write('The relationship between vehicle manufacturer and odometer is shown below.')
bar_fig = px.bar(
    vehicle_df, 
    x='manufacturer', 
    y='odometer', 
    color='odometer', 
    title='Vehicle Manufacturer vs. Odometer'
)
bar_fig.update_layout(
    yaxis=dict(range=[0, 300000]),
    plot_bgcolor='white'
)
st.plotly_chart(bar_fig)
```