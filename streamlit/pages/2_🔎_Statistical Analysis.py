import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Load the CSV data
df = pd.read_csv('./data/final_data.csv', parse_dates=['date'])
df.sort_values(by='date', inplace=True)

# Streamlit app title and page configuration
st.set_page_config(page_title="Statistical Analysis", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: Statistical Analysis ")
st.markdown("##")

# Sidebar for year selection
st.sidebar.header("Filter by Year")
years = st.sidebar.multiselect("Select years", df['date'].dt.year.unique(), default=df['date'].dt.year.unique())

# Filter data based on selected years
filtered_df = df[df['date'].dt.year.isin(years)]

# Scatter Plot
st.subheader('Scatter Plot of Working Hours')
string = 'A scatter plot of working hours and dates is a graphical representation that shows the relationship between the amount of time spent working (in hours) and specific dates.'
st.markdown(string, help=None)
fig, ax = plt.subplots(figsize=(16, 6))
ax.scatter(filtered_df['date'], filtered_df['total_time_hour'])
locator = mdates.MonthLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)
st.pyplot(fig)

# Histogram Plot
st.subheader('Histogram of Working Hours')
string = 'Histograms are commonly used to understand the distribution of a continuous variable, such as working hours, and to identify patterns, trends, and central tendencies in the data. They provide insights into how data is spread out and help identify clusters, gaps, and outliers.'
st.markdown(string, help=None)
fig, ax = plt.subplots(figsize=(15, 6), dpi=80)
ax.hist(filtered_df['total_time_hour'], bins=60, color='skyblue', edgecolor='black')
ax.set_ylabel('Days')
ax.set_xlabel('Working Hours')
ticks = np.arange(4, 13, 0.5)
ax.set_xticks(ticks)
detailed_ticks = np.arange(4, 13, 0.5)
ax.set_xticklabels(detailed_ticks)
st.pyplot(fig)

# Density Plot with Mean and Median Lines
st.subheader('Density Plot of Working Hours')
string = 'Density plot visualize the distribution of a continuous variable data points. Unlike a histogram, which uses bars to approximate the frequency of data within specific intervals (bins), a density plot represents the probability density function of the data.'
st.markdown(string, help=None)

# Check if the data is valid for plotting
if not filtered_df['total_time_hour'].empty and not filtered_df['total_time_hour'].isnull().all():
    fig, ax = plt.subplots(figsize=(15, 6), dpi=80)
    ax = filtered_df['total_time_hour'].plot(kind='density', color='blue')
    ax.axvline(filtered_df['total_time_hour'].mean(), color='red', linestyle='dashed', label='Mean')
    ax.axvline(filtered_df['total_time_hour'].median(), color='green', linestyle='dashed', label='Median')
    ticks = np.arange(4, 14, 0.5)
    ax.set_xticks(ticks)
    detailed_ticks = [tick if tick % 1 == 0 else '' for tick in ticks]
    ax.set_xticklabels(detailed_ticks)
    ax.set_xlim(4, 13)
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("No valid data available for density plot.")

# Average Total Time Trend Over Months
st.subheader('Average Total Time Trend Over Months')
filtered_df.loc[:, 'month'] = filtered_df['date'].dt.month
monthly_avg_total_time = filtered_df.groupby('month')['total_time_hour'].mean()

fig_line, ax_line = plt.subplots(figsize=(15, 6))
ax_line.plot(monthly_avg_total_time.index, monthly_avg_total_time.values, marker='o', linestyle='-')
ax_line.set_xlabel('Month')
ax_line.set_ylabel('Average Total Time (hours)')
ax_line.set_title('Trend of Total Time over the Months')
ax_line.set_xticks(range(1, 13))
ax_line.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax_line.grid(True)
st.pyplot(fig_line)


# Boxplot of Total Time by Year
st.subheader('Distribution of Total Time by Year')
st.write('A boxplot of total time by year is a graphical representation used to display the distribution of a continuous variable, such as "total time" (e.g., working hours) across different years. It provides insights into the central tendency, spread, and potential outliers within each years dataset.')
fig_boxplot, ax_boxplot = plt.subplots(figsize=(10, 6))
sns.boxplot(x=df['date'].dt.year, y=df['total_time_hour'], ax=ax_boxplot)
ax_boxplot.set_xlabel('Year')
ax_boxplot.set_ylabel('Total Time (hours)')
ax_boxplot.set_title('Distribution of Total Time by Year')
ax_boxplot.grid(True)
st.pyplot(fig_boxplot)
multi_line_text = """
**Box (Interquartile Range, IQR)**: The central part of the boxplot consists of a rectangle (the "box") that represents the interquartile range (IQR), which spans from the first quartile (25th percentile) to the third quartile (75th percentile) of the data. This region contains 50% of the data points for each year.

**Median Line**: Inside the box, a line is drawn to represent the median value of the data for each year. The median is the value that separates the lower 50% of the data from the upper 50%.

**Whiskers**: Lines (whiskers) extend vertically from the edges of the box to indicate the extent of the data beyond the IQR. These lines usually represent a range of 1.5 times the IQR. Data points outside this range are often considered as potential outliers and are plotted individually as points beyond the whiskers.

**Outliers**: Any data points that fall beyond the whiskers are plotted as individual points and are considered outliers. Outliers can signify unusual or extreme values that might warrant further investigation.

By constructing a boxplot of total time by year, you can compare the distribution of working hours for different years, identify any shifts in central tendencies or changes in variability, and detect any unusual observations that might require special attention.
"""

st.markdown(multi_line_text)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)