const BASE_URL = "http://localhost:5000";

export const getRecommendedRecipes = async (ingredients) => {
    const response = await fetch("http://127.0.0.1:5000/api/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ingredients })
    });
    return response.json();
};

export const improveRecipe = async (title, category) => {
    const response = await fetch("http://localhost:5000/api/improve",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, category })
    });
    return response.json();
};

export const analyzeHealth = async (title) => {
    const response = await fetch("http://localhost:5000/api/improve",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title })
    });
    return response.json();
};
