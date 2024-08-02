# Cars-Dataset
The "cars" dataset is a commonly used dataset in data analysis, data visualization. The cars dataset effectively demonstrates loading, inspecting, cleaning, filtering, and transforming data, highlighting the key steps in a data analysis workflow.

# Key Steps
Loading and Inspection: Loaded the dataset and performed initial inspection to understand its structure and dimensions.
Data Cleaning: Addressed missing values by filling them with the mode for categorical and numerical columns.
Data Filtering: Filtered out records with weight above 4000 to focus on lighter cars.
Data Transformation: Applied a transformation to increase the 'MPG_City' values by 3 units for all records.
Outcome: Enhanced data quality and prepared dataset for further analysis or modeling.






# How to use the code
# Step 1
Load the Dataset:
car = pd.read_csv(r"C:\Users\Admin\Downloads\file.csv"): Loads the dataset from the specified path.
# Step 2
Initial Data Inspection:
car.head(): Displays the first few rows.
car.shape: Shows the dimensions of the dataset.
# Step 3
Check for Missing Values:
car.isnull().sum(): Summarizes the count of missing values for each column before filling.

# Step 4
Fill Missing Values:
Loops through categorical and numerical columns to fill missing values with the mode (most frequent value).

# Step 5
Filter Data:
car = car[car['Weight'] <= 4000]: Filters out cars with a weight above 4000.

# Step 6

Transform Data:

car['MPG_City'] = car['MPG_City'].apply(lambda x: x + 3): Increases the MPG_City by 3 for all cars.

# Step 7

Final Data Inspection:

car.head(2): Displays the first few rows after modifications.
