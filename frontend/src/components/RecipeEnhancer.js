import React, { useState } from "react";
import { improveRecipe } from "../api/recipeAPI";

function RecipeEnhancer() {
    const [title, setTitle] = useState("");
    const [category, setCategory] = useState("health");
    const [improvedRecipe, setImprovedRecipe] = useState(null);

    const handleImprove = async () => {
        const response = await improveRecipe(title, category);
        setImprovedRecipe(response);
    };

    return (
        <div>
            <h2>Improve Recipe</h2>
            <input type="text" placeholder="Recipe Title"
                value={title} onChange={(e) => setTitle(e.target.value)} />
            <select value={category} onChange={(e) => setCategory(e.target.value)}>
                <option value="health">Health</option>
                <option value="taste">Taste</option>
            </select>
            <button onClick={handleImprove}>Improve</button>

            {improvedRecipe && (
                <div>
                    <h3>Improved Recipe</h3>
                    <p><strong>Improved Ingredients:</strong> {improvedRecipe.Improved_Ingredients}</p>
                </div>
            )}
        </div>
    );
}

export default RecipeEnhancer;
