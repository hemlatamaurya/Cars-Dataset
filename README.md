# Cars-Dataset
The "cars" dataset is a commonly used dataset in data analysis, data visualization, and machine learning. It contains information about different car models, including various attributes such as miles per gallon (MPG), horsepower, weight, and more. This dataset is often used in educational contexts and for demonstrating techniques in data science because it is relatively simple and easy to understand.

# Common Attributes in the Cars Dataset

MPG (Miles Per Gallon): A measure of fuel efficiency.
Cylinders: Number of cylinders in the engine.
Displacement: Engine displacement.
Horsepower: Power of the engine.
Weight: Weight of the car.
Acceleration: Time taken to accelerate from 0 to a certain speed.
Model Year: Year the car model was released.
Origin: Country of origin (e.g., USA, Europe, Japan).

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
