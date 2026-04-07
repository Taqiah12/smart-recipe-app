// Declare API_URL at the top so all functions can use it
const API_URL =
  window.location.hostname === "localhost"
    ? "http://localhost:5000"
    : "https://your-render-url.onrender.com"; // update later


async function getRecipe() {
  const ingredients = document.getElementById("ingredients").value;
  const resultDiv = document.getElementById("result");

  if (!ingredients) {
    alert("Please enter ingredients!");
    return;
  }

  resultDiv.classList.remove("hidden");
  resultDiv.innerHTML = "⏳ Generating recipe...";




  try {
    
const response = await fetch(`${API_URL}/recipes`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ ingredients })
    });

    const data = await response.json();

    resultDiv.innerHTML = `
      <h2>🍽 Recipe</h2>
      <p>${data.recipe}</p>
    `;
  } catch (error) {
    resultDiv.innerHTML = "⚠️ Failed to fetch recipe. Try again.";
  }
}
// Function to load saved recipes
async function loadRecipes() {
  const resultDiv = document.getElementById("result");

  resultDiv.classList.remove("hidden");
  resultDiv.innerHTML = "⏳ Loading saved recipes...";

  try {
    const res = await fetch(`${API_URL}/recipes`);
    const data = await res.json();

    if (!data.recipes || data.recipes.length === 0) {
      resultDiv.innerHTML = "No recipes saved yet.";
      return;
    }

    resultDiv.innerHTML = data.recipes.map(r => `
      <div class="card">
        <p><b>Ingredients:</b> ${r.ingredients}</p>
        <pre>${r.recipe}</pre>
      </div>
    `).join("");

  } catch (error) {
    resultDiv.innerHTML = "⚠️ Failed to load recipes.";
  }
}