import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import eda as ed
def inferences(data):
    print("**************************************************")
    print("Inferences Starts here...")
    print("Having completed the Exploratory Data Analysis phase, we will now move forward with the analysis required to address our research questions.")
    print("**************************************************")
    print(">>>>>>Inference 1 : What is the predominant mode of property use (ownership or leasing) across different property types, and how does this vary between states? >>>>>>>>> ")
    # Filter the data for leased properties
    leased_data = data[data['Owned/Leased'] == 'LEASED']
    # Group the leased data by 'State' and count the occurrences
    leased_counts = leased_data['Bldg State'].value_counts()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(12, 6))
    plt.bar(leased_counts.index, leased_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Leased Properties by State')
    plt.xticks(rotation=45)  # Rotate state labels for better readability
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("Findings : Here it says that most number of properties has been leased in the state of California(CA) followed by Texas (TX)")
    # Filter the data for Owned properties
    owned_data = data[data['Owned/Leased'] == 'OWNED']
    # Group the Owned data by 'State' and count the occurrences
    owned_counts = owned_data['Bldg State'].value_counts()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(12, 6))
    plt.bar(owned_counts.index, owned_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Owned Properties by State')
    plt.xticks(rotation=45)  # Rotate state labels for better readability
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("""Findings : If we look into the owned properties, Texas stood at first followed by Washington(DC) So 
    finally as California and Texas are the states with most number of properties being leased and Texas, Washington Dc 
    are the top 2 states with more no of properties being owned by rather leasing.""")
    print("**************************************************")
    print(">>>>>>Inference 2 : Analyze the distribution of different property types within various States . Are certain property types more prevalent in specific areas?")
    # Filter the data for building type of properties
    bulding = data[data['Property Type'] == 'BUILDING']
    # Group the building data by 'State' and count the occurrences
    bulding_counts = bulding['Bldg State'].value_counts()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(20, 15))
    plt.bar(bulding_counts.index, bulding_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Property type - Bulding by State')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Display the plot
    plt.show()


    # Filter the data for Structure type of properties
    structure = data[data['Property Type'] == 'STRUCTURE']
    # Group the Structure data by 'State' and count the occurrences
    structure_counts = structure['Bldg State'].value_counts()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(20, 15))
    plt.bar(structure_counts.index, structure_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Property type - Structure by State')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("Findings : Property type Buildings are more in Texas followed by California while in Structures type Texas again topped it followed by Washington DC.")
    print("**************************************************")
    print(">>>>>>Inference 3 : Is there a connection between the number of parking spaces available and the most commonly preferred property types?")
    # Group the data by 'Property Type' and calculating the average number of parking spaces
    average_spaces_by_property_type = data.groupby('Property Type')['Total Parking Spaces'].mean()
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    average_spaces_by_property_type.plot(kind='bar', color='lightblue')
    plt.xlabel('Property Type')
    plt.ylabel('Total Parking Spaces')
    plt.title('Total Parking Spaces by Property Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("Findings : It is clear that property type of structure has more number of parking spaces than building type")
    print("**************************************************")
    print(">>>>>>Inference 4 : Is there any relation between the age of the building and the place?")
    import datetime as dt
    #lets calculate the age of the property using the construction date of the property
    current_date = dt.datetime.now()
    # current_year = current_date.year
    #As datset has a date attribute lets convert its data type into date type
    #data['Construction Date']=data['Construction Date'].replace('1/0/1900', '1/1/1900') #as we have some data issues fixed it manually as it is only one data obervation
    data['Construction Date'] = pd.to_datetime(data['Construction Date'])
    data['Property Age'] =(current_date - data['Construction Date']).dt.days // 365  # Calculate age in year
    # Print the DataFrame with the property age
    #print(df[['Construction Date', 'Property Age']])
    print(data.head())
    #Group the data by 'State' and calculate the average age for each state
    average_age_by_state = data.groupby('Bldg State')['Property Age'].mean()
    # Creating a bar plot using Matplotlib
    plt.figure(figsize=(12, 6))
    average_age_by_state.plot(kind='bar', color='lightblue')
    plt.xlabel('State')
    plt.ylabel('Property Average Age')
    plt.title('Average Age of Properties by State')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Display the plot
    plt.show()
    print("Findings : From te above plots, Interestingly I found that Washington DC has average property age of 51 years being the highest so mostly of the old properties were located in the Washington DC.")
