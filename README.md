# **🎬 Movie Data Analysis Dashboard**

This project is an interactive web application built with **Streamlit** that allows users to explore and visualize a dataset of movie metadata. It provides several different visualizations to analyze trends in movie ratings, budgets, revenues, and profits over time.

## **✨ Features**

The dashboard offers the following interactive visualizations, selectable from a sidebar menu:

* **Ratings Distribution**: A histogram showing the distribution of average movie ratings.  
* **Budget vs. Revenue**: A scatter plot to visualize the relationship between a movie's budget and its revenue.  
* **Top 10 Movies by Revenue**: A bar chart displaying the 10 highest-grossing movies.  
* **Total Profit by Year**: A line chart illustrating the trend of total movie profits over the years.  
* **Correlation Heatmap**: A heatmap showing the correlation between key numerical features like budget, revenue, vote\_average, and profit.

## **📊 Dataset**

The application uses the movies\_metadata.csv dataset. The data is loaded and preprocessed to handle missing values and to create new features like release\_year and profit for analysis.

*The data loading is cached using @st.cache\_data for improved performance on subsequent runs.*

## **📦 Dependencies**

To run this application, you will need the following Python libraries:

* **streamlit**: For creating the interactive web dashboard.  
* **pandas**: For data manipulation and analysis.  
* **matplotlib**: For creating static, animated, and interactive visualizations.  
* **seaborn**: For making statistical graphics.

You can install these dependencies using pip:

pip install streamlit pandas matplotlib seaborn

## **🚀 How to Run the Application**

1. **Prepare your data**: Make sure you have the movies\_metadata.csv file inside a data/ directory in your project folder.  
2. **Save the code**: Save the provided script as app.py.  
3. **Run from the terminal**: Open your terminal or command prompt, navigate to the project directory, and run the following command:  
   streamlit run app.py

4. **View the dashboard**: A new tab should open in your web browser with the interactive dashboard. You can then use the sidebar to switch between the different visualizations.

## **📁 File Description**

* **app.py**: The main Python script containing the Streamlit application code. It handles data loading, preprocessing, and the generation of all visualizations.  
* **data/movies\_metadata.csv**: The dataset file containing the movie information used for the analysis.