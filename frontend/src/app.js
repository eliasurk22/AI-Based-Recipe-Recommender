import React, { useState } from "react";
import RecipeInput from "./components/RecipeInput";
import RecipeList from "./components/RecipeList";
import RecipeEnhancer from "./components/RecipeEnhancer";
import "./styles/App.css";

function App() {
    const [recipes, setRecipes] = useState([]);

    return (
        <div className="app-container">
            <h1>AI Recipe Recommender</h1>
            <RecipeInput setRecipes={setRecipes} />
            <RecipeList recipes={recipes} />
            <RecipeEnhancer />
        </div>
    );
}

export default App;
