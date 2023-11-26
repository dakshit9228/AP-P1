import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def exploratoryDataAnalysis(data):
    print("******************************************************")
    print("Exploratory Data Analysis Starts here ....")
    print("""To begin this phase of the research, our first step entails performing a summary statistics 
    analysis for each of the variables in our dataset, with the objective of identifying potential outliers 
    or missing values that may have an impact on our findings. Subsequently, we will showcase visual analyses 
    for each attribute, utilizing both Matplotlib and Seaborn for data visualization.""")
    print("******************************************************")
    print("I am dropping some of the not required columns from the existing data set")
    data=data.drop(['Location Code','Region Code','Bldg Address1','Bldg Address2','Bldg Zip','Congressional District','Bldg ANSI Usable','Historical Type','Historical Status','ABA Accessibility Flag '],axis=1)
    print("Displaying the columns after dropping the unwanted columns")
    print(data.columns)
    print("""Having accomplished the data import and the removal of extraneous attributes, our next crucial step involves a 
    meticulous examination of the dataset for any instances of missing values. The identification and appropriate handling 
    of null values are of paramount importance, as they have the potential to impact the overall integrity and trustworthiness 
    of our research results.""")
    print("Checking for the frequency of missing values in each column")
    print(data.isnull().sum())
    print("From the above results it was evident that there are no missing data in our data set")
    print("**********************************************************")
    print("**********************************************************")
    print("Statistical summary of the numerical columns in the data set ")
    print("**********************************************************")
    print(data.describe())
    print(""""The describe method in pandas offers a comprehensive summary of data distribution characteristics for 
    each attribute. It presents key statistical metrics, including the mean, median (50%), and quartile values (25% and 75%), 
    allowing us to discern central tendencies and variations within the data. Furthermore, the method provides the standard 
    deviation, offering insights into the spread and dispersion of data points for each attribute.""")
    print("**********************************************************")
    print("Properties by city:")
    print("__________________________________________________________")
    # Get the top 5 cities by count because we have large number of city which cannot be visualized
    top_cities = data['Bldg City'].value_counts().head(5)
    # Create a bar plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_cities.index, y=top_cities.values, palette='viridis')
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.title('Seaborn - Top 5 Cities by Count')
    plt.xticks(rotation=45)  # Rotate city labels for better readability
    plt.tight_layout()
    # Display the plot
    plt.show()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(top_cities.index, top_cities.values, color='skyblue')
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.title('Matplotlib - Top 5 Cities by Count')
    plt.xticks(rotation=45)  # Rotate city labels for better readability
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("Findings : It shows that Washington city stood at top notch with highest number of properties in the Unites States of America followed by the Laredo city.")
    print("**********************************************************")
    print("Properties by County:")
    print("__________________________________________________________")
    # Get the top 10 county by count because we have large number of counties which cannot be visualized
    top_county = data['Bldg County'].value_counts().head(10)
    # Create a bar plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_county.index, y=top_county.values, palette='viridis')
    plt.xlabel('County')
    plt.ylabel('Count')
    plt.title('Seaborn - Top 10 County by Count')
    plt.xticks(rotation=45)  # Rotate city labels for better readability
    plt.tight_layout()
    # Display the plot
    plt.show()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(top_county.index, top_county.values, color='skyblue')
    plt.xlabel('County')
    plt.ylabel('Count')
    plt.title('Matplotlib - Top 10 County by Count')
    plt.xticks(rotation=45)  # Rotate county labels for better readability
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("Findings : Even in case of county level District of columbia and Montgomery has highest number of properties.")
    print("**********************************************************")
    print("Properties by State:")
    print("__________________________________________________________")
    plt.figure(figsize=(25, 6))
    ax = data['Bldg State'].value_counts().plot(kind="bar")
    ax.set_title('Properties by States using Matplotlib')
    plt.show()
    plt.figure(figsize=(25, 6))
    ax = sns.countplot(x='Bldg State', data=data,palette='viridis')
    ax.set_title('Properties by States using Seaborn')
    plt.show()
    print("Findings : As per the above plots it conveys that if we look by the state, Texas has highest no of properties followed by the California.")
    print("**********************************************************")
    print("Building Status:")
    print("__________________________________________________________")
    #using matplotlib
    plt.figure(figsize=(8, 6))
    ax = data['Bldg Status'].value_counts().plot(kind="bar")
    ax.set_title('Properties by Status using Matplotlib')
    plt.show()
    #using seaborn
    plt.figure(figsize=(8, 6))
    ax = sns.countplot(x='Bldg Status', data=data,palette='viridis')
    ax.set_title('Properties by Status using Seaborn')
    plt.show()
    print("Findings : Most of the building are active and very less buildings were decommissioned as oer the above plots")
    print("**********************************************************")
    print("Parking Spaces by State:")
    print("__________________________________________________________")
    #using matplotlib
    # Group the data by 'State' and calculate the average number of spaces
    average_spaces_by_state = data.groupby('Bldg State')['Total Parking Spaces'].mean()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(12, 6))
    average_spaces_by_state.plot(kind='bar')
    plt.xlabel('State')
    plt.ylabel('Average Number of Spaces')
    plt.title('Average Number of Spaces by State')
    plt.xticks(rotation=45)  # Rotate state labels for better readability
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("Findings : So Missouri(MS) has more number of parking spaces followed by the Maryland(MD) and American Samoa(AS) is the place with very less number of parking spaces.")
    print("**********************************************************")
    print("Ownership:")
    print("__________________________________________________________")
    #using matplotlib
    plt.figure(figsize=(8, 6))
    ax = data['Owned/Leased'].value_counts().plot(kind="bar")
    ax.set_title('Properties by Ownership using Matplotlib')
    plt.show()
    #using seaborn
    plt.figure(figsize=(8, 6))
    ax = sns.countplot(x='Owned/Leased', data=data,palette='viridis')
    ax.set_title('Properties by Ownership using Seaborn')
    plt.show()
    print("Findings : It is interesting that most of the properties are being leased than being owned.")
    print("EDA Ends here....")
    return data

