import pandas as pd
import os

# Ensure we write to the correct backend path
output_path = os.path.join("backend", "database", "recipes.csv")

data = {
    "Title": ["Garlic Butter Pasta", "Sugar Rice Delight"],
    "Ingredients": [
        "pasta, garlic, butter, salt",
        "white rice, sugar, pepper"
    ],
    "Instructions": [
        "Cook pasta, sauté garlic and butter, season with salt",
        "Cook white rice, add sugar and pepper"
    ],
    "Image_Name": ["garlic_pasta.jpg", "sweet_rice.jpg"],
    "Cleaned_Ingredients": [
        "pasta garlic butter salt",
        "white rice sugar pepper"
    ]
}

df = pd.DataFrame(data)
df.to_csv(output_path, index=False)
print(f"Sample recipe database created at: {output_path}")
