import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Blueprint, request, jsonify
from database.db_loader import recipe_df

recommend_bp = Blueprint("recommend", __name__)

def recommend_recipes(ingredients):
    ingredient_texts = recipe_df["Cleaned_Ingredients"].astype(str)
    user_input = " ".join(ingredients)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(ingredient_texts)
    user_vector = vectorizer.transform([user_input])

    cosine_similarities = (tfidf_matrix * user_vector.T).toarray().flatten()

    # Set a similarity threshold to filter out irrelevant results
    threshold = 0.1  # Adjust this value as needed
    valid_indices = np.where(cosine_similarities >= threshold)[0]
    sorted_indices = valid_indices[np.argsort(cosine_similarities[valid_indices])[::-1]]

    recommendations = recipe_df.iloc[sorted_indices][["Title", "Ingredients", "Instructions", "Image_Name"]].to_dict(orient="records")
    return recommendations[:5]  # Return top 5 only if they meet the threshold


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    ingredients = data.get("ingredients", [])

    # Strip whitespace and remove empties
    ingredients = [ing.strip() for ing in ingredients if ing.strip()]

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    results = recommend_recipes(ingredients)
    return jsonify({"recipes": results})

