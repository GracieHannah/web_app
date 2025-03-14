import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

df['manufacturer'] = df['model'].str[:3].str.lower()

st.title("Vehicle Data Dashboard")
st.header("Explore Vehicle Data")

st.markdown("""
This dashboard provides insights into vehicle data by displaying histograms and scatter plots.
Use the sidebar to filter or toggle visualizations.
""")

st.sidebar.header("Options")
show_scatter = st.sidebar.checkbox("Show Price vs. Odometer Scatter Plot", value=True)

st.subheader("Histogram: Model Year by Paint Color and Fuel")
hist_fig = px.histogram(
    df,
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
        df,
        x="odometer",
        y="price",
        color="condition",
        title="Price vs. Odometer by Condition"
    )
    st.plotly_chart(scatter_fig)

st.markdown("Adjust the options on the sidebar to explore the data further.")



st.header('Vehicle manufacturer vs odometer')
st.write('The relationship between vehicle manufacturer and odometer is shown below.')
vehicle_df['manufacturer'] = vehicle_df['model'].str[:3]
fig=px.bar(vehicle_df, x='manufacturer', y='odometer', color='odometer', title='Vehicle manufacturer vs odometer')
fig.update_layout(yaxis=dict(range=[0,300000]))
fig.update_layout(
    plot_bgcolor='white'
)
fig.show()
st.plotly_chart(fig)    

