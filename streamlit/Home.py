import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
df = pd.read_csv('../data/final_data.csv', parse_dates=['date'])
df.sort_values(by='date', inplace=True)

# Streamlit app title and page configuration
st.set_page_config(page_title="Working Hours Dashboard", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: Working Hours Dashboard")
st.markdown("##")

# ---- Sidebar for Filtering Years ----
st.sidebar.header("Filter Years for Visual Calendar")
selected_years = st.sidebar.multiselect("Select Years", df['date'].dt.year.unique(), default=None)

# Filter data based on selected years
filtered_df = df[df['date'].dt.year.isin(selected_years)]

# ---- Mainpage ----

# Create pivot table for main heatmap and bar plot
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
sum_working_hours_per_month = df.groupby(['year', 'month'])['total_time_hour'].sum()
df_result = sum_working_hours_per_month.reset_index()
pivot_result = df_result.pivot_table(index='year', columns='month', values='total_time_hour', fill_value=0)

# Create main heatmap using Streamlit's native plotting function
st.subheader('Working Hours Heatmap')
fig, ax = plt.subplots(figsize=(10, 3))
sns.heatmap(pivot_result, annot=True, fmt=".1f", cmap='YlGnBu', linewidths=0.5, ax=ax)
ax.set_title('Working Hours Heatmap (Year-wise)')
ax.set_xlabel('Month')
ax.set_ylabel('Year')
st.pyplot(fig)


# Create main bar plot
st.subheader('Total Working Hours per Month')
fig_bar, ax_bar = plt.subplots(figsize=(10, 4))
pivot_result.plot(kind='bar', stacked=True, ax=ax_bar)
plt.title('Total Working Hours per Month (Year-wise)')
plt.xlabel('Month')
plt.ylabel('Working Hours')
plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))
plt.xticks(rotation=0)
st.pyplot(fig_bar)

# ---- Visual Calendar Heatmap ----
grouped_df = filtered_df.groupby(filtered_df['date'].dt.year)

for year, year_data in grouped_df:
    min_date = year_data['date'].min()
    max_date = year_data['date'].max()
    all_dates = pd.date_range(start=min_date, end=max_date)
    calendar_df = pd.DataFrame({'date': all_dates})
    calendar_df = pd.merge(calendar_df, year_data[['date', 'total_time_hour']], on='date', how='left')
    calendar_df['total_time_hour'].fillna(0, inplace=True)
    calendar_pivot = calendar_df.pivot_table(index=calendar_df['date'].dt.month,
                                            columns=calendar_df['date'].dt.day,
                                            values='total_time_hour',
                                            fill_value=0)

    # Create the Visual Calendar Heatmap using Streamlit's native plotting function
    st.subheader(f'Visual Calendar - Working Hours ({year})')
    fig_calendar, ax_calendar = plt.subplots(figsize=(15, 5))
    sns.heatmap(calendar_pivot, cmap='coolwarm', annot=True, fmt=".1f", linewidths=0.5, cbar=False, ax=ax_calendar)
    ax_calendar.set_xlabel('Day')
    ax_calendar.set_ylabel('Month')
    ax_calendar.set_title(f'Visual Calendar - Working Hours ({year})')
    st.pyplot(fig_calendar)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
