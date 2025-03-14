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
outcomes in a visually interactive manner. This dashboard provides insights into 
vehicle data by displaying histograms and scatter plots.
Use the sidebar to filter or toggle visualizations.
""")

st.sidebar.header("Options")
show_histogram = st.sidebar.checkbox("Model Year by Paint Color and Fuel", value=True)
show_scatter = st.sidebar.checkbox("Show Price vs. Odometer Scatter Plot", value=True)
show_hist2 = st.sidebar.checkbox("Vehicle Manufacturer vs. Odometer", value=True)
show_scatter2 = st.sidebar.checkbox("Vehicle model year vs price", value=True)


if show_histogram:
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


lower_bound = vehicle_df['price'].quantile(0.01)
upper_bound = vehicle_df['price'].quantile(0.99)
clean_df = vehicle_df[
    (vehicle_df['price'] >= lower_bound) &
    (vehicle_df['price'] <= upper_bound)
]

if show_hist2:
    st.subheader("Price Distribution")
    hist2_fig = px.histogram(
        clean_df,
        x="price",
        color="price",
        title="Price Distribution"
    )
    st.plotly_chart(hist2_fig)

vehicle_df['manufacturer'] = vehicle_df['model'].str[:3]

if show_scatter2:
    st.subheader("Vehicle model year vs price")
    scatter2_fig = px.scatter(
        vehicle_df,
        x="model",
        y="price",
        color="manufacturer",
        title="Vehicle model vs Price"
    )
    scatter2_fig.update_layout(
        xaxis={'categoryorder':'category ascending'}
    )
    scatter2_fig.update_xaxis(tickangle=45)

    st.plotly_chart(scatter2_fig)
