import pandas as pd
import os

# Load CSV dataset
def load_recipes(csv_path = os.path.join(os.path.dirname(__file__), "recipes.csv")):
    df = pd.read_csv(csv_path)
    required_columns = {"Title", "Ingredients", "Instructions", "Image_Name", "Cleaned_Ingredients"}
    
    if not required_columns.issubset(df.columns):
        raise ValueError("CSV must contain 'Title', 'Ingredients', 'Instructions', 'Image_Name', 'Cleaned_Ingredients'")
    
    return df

# Load data once and keep in memory for efficiency
recipe_df = load_recipes()
