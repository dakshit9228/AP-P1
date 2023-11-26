import pandas as pd
import numpy as np

def dataSummary(data_url):
    """
    My data has 18 columns and 8770 rows of data.

    ** Attributes : **

    Location Code : location code

    Region Code ; region code of building

    Bldg Address1 : address1 of building

    Bldg Address2 : address2 of building

    Bldg City :city of building

    Bldg County :county of building

    Bldg State :state of building

    Bldg Zip :ZIP code of building

    Congressional District :District of building

    Bldg Status :Status of building

    Property Type :TYpe of properTY

    Bldg ANSI Usable :Ansi usable

    Total Parking Spaces :Parking spaces

    Owned/Leased :Leased or Owned

    Construction Date : Date of bulding construction

    Historical Type : Historical type

    Historical Status : Historical Status

    ABA Accessibility Flag : Flag"""
    print("*******************************************************")
    print("*******************************************************")
    print("Data Summary Starts here...")
    print("*******************************************************")
    print( """
    My data has 18 columns and 8770 rows of data.
    
    ** Attributes : **
    
    Location Code : location code
    
    Region Code ; region code of building
    
    Bldg Address1 : address of building
    
    Bldg Address2 : address of building
    
    Bldg City :city of building
    
    Bldg County :county of building
    
    Bldg State :state of building
    
    Bldg Zip :ZIP code of building
    
    Congressional District :District of building
    
    Bldg Status :Status of building
    
    Property Type :TYpe of properTY
    
    Bldg ANSI Usable :Ansi usable
    
    Total Parking Spaces :Parking spaces
    
    Owned/Leased :Leased or Owned
    
    Construction Date : Date of bulding construction
    
    Historical Type : Historical type
    
    Historical Status : Historical Status
    
    ABA Accessibility Flag : Flag
            """)
    print("*******************************************************")
    print("Fetching the data from the github")
    print("*******************************************************")
    data=pd.read_csv(data_url)
    print("Data fetching Finished")
    print("*******************************************************")
    print("Displaying the data")
    print("*******************************************************")
    print(data)
    print("*******************************************************")
    print("Checking the data shape")
    print("*******************************************************")
    print(data.shape)
    print(f"Data has {data.shape[1]} columns and {data.shape[0]} rows. We hold the required columns and will drop the unwanted columns as move on to future")
    print("*******************************************************")
    print("Checking the data types of the attributes")
    print("*******************************************************")
    print(data.info())
    print("*******************************************************")
    print("Data Summary Ends here...")
    print("*******************************************************")
    return data
