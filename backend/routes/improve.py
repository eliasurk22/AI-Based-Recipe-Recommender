import pandas as pd
from flask import Blueprint, request, jsonify
from database.db_loader import recipe_df

improve_bp = Blueprint("improve", __name__)

# Sample rule-based improvement function
def improve_recipe(recipe, category):
    health_swaps = {"butter": "olive oil", "sugar": "honey", "white rice": "brown rice"}
    taste_boosters = {"salt": "sea salt", "pepper": "smoked paprika", "garlic": "roasted garlic"}
    
    ingredients = recipe["Ingredients"].split(", ")
    improved_ingredients = []
    
    for ingredient in ingredients:
        if category == "health" and ingredient in health_swaps:
            improved_ingredients.append(health_swaps[ingredient])
        elif category == "taste" and ingredient in taste_boosters:
            improved_ingredients.append(taste_boosters[ingredient])
        else:
            improved_ingredients.append(ingredient)
    
    recipe["Improved_Ingredients"] = ", ".join(improved_ingredients)
    return recipe

@improve_bp.route("/improve", methods=["POST"])
def improve():
    data = request.json
    recipe_title = data.get("title")
    category = data.get("category")
    
    if not recipe_title or category not in ["health", "taste"]:
        return jsonify({"error": "Invalid request"}), 400

    recipe = recipe_df[recipe_df["Title"] == recipe_title].to_dict(orient="records")
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    improved_recipe = improve_recipe(recipe[0], category)
    return jsonify(improved_recipe)
