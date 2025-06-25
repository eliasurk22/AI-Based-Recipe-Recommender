from flask import Blueprint, request, jsonify
from database.db_loader import recipe_df

health_bp = Blueprint("health", __name__)

# Sample nutritional analysis function
def analyze_health(recipe):
    unhealthy_ingredients = {"sugar": "High sugar content", "butter": "High in saturated fats", "salt": "Excess sodium"}
    
    ingredients = recipe["Ingredients"].split(", ")
    health_warnings = [unhealthy_ingredients[ing] for ing in ingredients if ing in unhealthy_ingredients]
    
    return {"health_score": 100 - (len(health_warnings) * 10), "warnings": health_warnings}

@health_bp.route("/health", methods=["POST"])
def analyze():
    data = request.json
    recipe_title = data.get("title")
    
    if not recipe_title:
        return jsonify({"error": "Recipe title is required"}), 400
    
    recipe = recipe_df[recipe_df["Title"] == recipe_title].to_dict(orient="records")
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    health_data = analyze_health(recipe[0])
    return jsonify(health_data)
