import React, { useState } from "react";
import { getRecommendedRecipes } from "../api/recipeAPI";

function RecipeInput({ setRecipes }) {
    const [ingredients, setIngredients] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const ingredientList = ingredients.split(",").map(ing => ing.trim());
        const response = await getRecommendedRecipes(ingredientList);
        setRecipes(response.recipes || []);
    };

    return (
        <div>
            <h2>Enter Ingredients</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="e.g., tomato, cheese, pasta"
                    value={ingredients} onChange={(e) => setIngredients(e.target.value)} />
                <button type="submit">Get Recipes</button>
            </form>
        </div>
    );
}

export default RecipeInput;
