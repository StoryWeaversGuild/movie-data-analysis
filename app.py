import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies_metadata.csv", low_memory=False)
    df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    df.dropna(subset=['budget', 'revenue', 'release_date'], inplace=True)
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df.dropna(subset=['release_date'], inplace=True)
    df['release_year'] = df['release_date'].dt.year
    df['profit'] = df['revenue'] - df['budget']
    return df

df = load_data()
st.write("Dataset shape:", df.shape)
st.write("Columns:", df.columns)
st.write("Sample data:", df.head())

st.title("Movie Data Analysis Dashboard")
option = st.sidebar.selectbox("Select Visualization", [
    "Ratings Distribution", 
    "Budget vs. Revenue", 
    "Top 10 Movies by Revenue", 
    "Total Profit by Year", 
    "Correlation Heatmap"
])

if option == "Ratings Distribution":
    st.write("Displaying Ratings Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['vote_average'], bins=20, kde=True, ax=ax)
    ax.set_title("Distribution of Movie Ratings")
    st.pyplot(fig)

elif option == "Budget vs. Revenue":
    st.write("Displaying Budget vs. Revenue")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='budget', y='revenue', alpha=0.5, ax=ax)
    ax.set_title("Budget vs. Revenue")
    st.pyplot(fig)

elif option == "Top 10 Movies by Revenue":
    st.write("Displaying Top 10 Movies by Revenue")
    top10 = df.nlargest(10, 'revenue')[['title', 'revenue']]
    fig, ax = plt.subplots()
    sns.barplot(data=top10, x='revenue', y='title', ax=ax)
    ax.set_title("Top 10 Movies by Revenue")
    st.pyplot(fig)

elif option == "Total Profit by Year":
    st.write("Displaying Total Profit by Year")
    profit_year = df.groupby('release_year')['profit'].sum().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(data=profit_year, x='release_year', y='profit', ax=ax)
    ax.set_title("Total Profit by Year")
    st.pyplot(fig)

elif option == "Correlation Heatmap":
    st.write("Displaying Correlation Heatmap")
    corr_cols = ['budget', 'revenue', 'vote_average', 'profit']
    corr = df[corr_cols].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)
