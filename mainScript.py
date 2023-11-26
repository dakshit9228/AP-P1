def mainScriptf(file_path):
    print("***********************************************************")
    print("Introduction Starts here ...")
    print("***********************************************************")
    print("""I delve into a Real estate dataset comprising attributes such as building construction dates, ownership 
    or leasing information, parking space counts, property types, building conditions, and geographical data. Despite
     the absence of property values, income levels, or population statistics, our analysis aims to uncover insights into 
     the real estate market's intricacies. We investigate property ownership trends, the influence of building age and 
     condition on utilization, regional variations in property types. By exploring these dimensions, we seek to provide a 
     comprehensive understanding of the factors shaping the real estate landscape, which can inform strategic decisions and 
     benefit property developers, investors, urban planners, policymakers, and researchers in the field.""")
    print("Introduction Ends here")
    print("Research Questions :")
    print(""""  
    1. What is the predominant mode of property use (ownership or leasing) across different property types, and how does this vary between states?
    
    \n2. Analyze the distribution of different property types within various States . Are certain property types more prevalent in specific areas?
    
    \n3. Is there a connection between the number of parking spaces available and the most commonly preferred property types?
    
    \n4. Is there any relation between the age of the bulding and the place?""")
    #Importing the libraries
    print("Importing the required libraries")
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import eda as ed
    import inferences as inf
    print("Finished : Importing the required libraries")
    pd.set_option('display.max_columns',None)
    import dataSummary as ds
    data=ds.dataSummary(file_path)
    data=ed.exploratoryDataAnalysis(data)
    inf.inferences(data)
    print("Inferences Ends here...")
    print("************************************")
    print("Conclusion : ")
    print("""In this comprehensive analysis of real estate data, a clear hierarchy of property prominence emerges, 
    with Washington City and Washington D.C. taking the lead, followed by Texas and California, at both the city and 
    state levels. The market leans heavily towards property leasing over ownership, particularly in California and Texas,
     while ownership dominates in Texas and Washington D.C. Interestingly, properties remain largely active, with few
      decommissioned, highlighting a focus on property maintenance. Missouri stands out for its high number of parking spaces, 
      while Maryland and American Samoa offer relatively fewer. The analysis also distinguishes between property types, 
      with buildings being more common in Texas and California, while structures are predominant in Texas, closely trailed by
       Washington D.C. Notably, Washington D.C. boasts the highest average property age at 51 years, reflecting its rich historical 
       character. These findings underscore the dynamic nature of property distribution, ownership trends, and property 
       characteristics, offering valuable insights for stakeholders in the ever-evolving real estate market.""")
    print("Conclusion Ends here...")
    print("********References*********")
    print("""
    https://catalog.data.gov/dataset/real-estate-across-the-united-states-rexus-inventory-building
    
    https://medium.com/@michael71314/python-lesson-29-more-things-you-can-do-with-matplotlib-bar-charts-matplotlib-pt-2-6db863ffb864
    
    https://ai.plainenglish.io/exploratory-data-analysis-eda-with-python-matplotlib-bb784e1d3dd3?gi=ce44d503cb73
    
    https://www.analyticsvidhya.com/blog/2021/02/introduction-to-exploratory-data-analysis-eda/""")
