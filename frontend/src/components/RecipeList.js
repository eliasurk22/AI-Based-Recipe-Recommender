import React from "react";

function RecipeList({ recipes }) {
    return (
        <div>
            <h2>Recommended Recipes</h2>
            {recipes.length === 0 ? (
                <p>No recipes found.</p>
            ) : (
                <ul>
                    {recipes.map((recipe, index) => (
                        <li key={index}>
                            <h3>{recipe.Title}</h3>
                            <p><strong>Ingredients:</strong> {recipe.Ingredients}</p>
                            <p><strong>Instructions:</strong> {recipe.Instructions}</p>
                            <img src={`/images/${recipe.Image_Name}`} alt={recipe.Title} width="150" />
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default RecipeList;
