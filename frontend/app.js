async function getRecipe() {
  const ingredients = document.getElementById("ingredients").value;
  const resultDiv = document.getElementById("result");

  if (!ingredients) {
    alert("Please enter ingredients!");
    return;
  }

  resultDiv.classList.remove("hidden");
  resultDiv.innerHTML = "⏳ Generating recipe...";

  const API_URL =
  window.location.hostname === "localhost"
    ? "http://localhost:5000"
    : "https://your-render-url.onrender.com"; // update later


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