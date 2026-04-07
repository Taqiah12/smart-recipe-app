# smart-recipe-app
# App name: Smart Recipe App
# ---------------------------------------------
# Description : The Smart Recipe App allows users to input the ingredients they have and receive recipe suggestions. The app uses AI to generate recipes and suggest ingredient substitutions. It is designed for home cooks, students, and busy individuals who want to quickly prepare meals using available ingredients.

# ----------------------------------------------
# Team Members and roles :
# Taqiah - Frontend + API Integration/UI-UX
### Frontend Development & API Integration

# This project’s frontend was developed using HTML, CSS, and JavaScript, focusing on simplicity, usability, and seamless integration with the backend API.

### User Interface

#  Designed a responsive and visually appealing interface using HTML and CSS
# Implemented a modern UI with a glassmorphism card layout and background styling
# Created input fields and interactive buttons for user actions
# Dynamically updated the UI based on user input and API responses

### API Integration

# Integrated the frontend with backend REST APIs using the `fetch()` method

# Implemented the following endpoints:

  # `POST /recipes` → Sends user ingredients and receives AI-generated recipes
  # `GET /recipes` → Retrieves previously saved recipes from the database

# Configured dynamic API base URL:

  # Uses `localhost` during development
  # Switches to deployed backend URL in production

### Functionality Implemented

# Captures user input (ingredients) and sends it to the backend
# Displays AI-generated recipes dynamically on the page
# Fetches and displays saved recipes in a structured format
# Provides real-time feedback (loading messages, results display)

### ⚠️ Error Handling & Reliability

# Implemented robust error handling for:

  # Server-side errors (e.g., failed API responses)
  # Application-level errors (e.g., invalid data from backend)
# Added user-friendly error messages to improve user experience
# Included debugging logs (`console.error`) for troubleshooting during development and demo

### Environment Handling

# Implemented automatic switching between local and deployed environments:

# ```javascript
# const API_URL =
#  window.location.hostname === "localhost"
#    ? "http://localhost:5000"
#   : "https://smart-recipe-app-rpns.onrender.com";
# ```

### Testing & Validation

# Manually tested all API interactions:

  # Recipe generation flow
  # Saved recipes retrieval
# Verified correct data flow between frontend, backend, and database

### 👤 Contribution Summary

# Developed the complete frontend UI
# Integrated all backend APIs with the frontend
# Ensured smooth end-to-end user interaction
# Improved reliability through error handling and debugging support



# ------------------------------------------------------------------------------------------------------------------------




# Moeez - AI & Docker ( please if you are doing docker then it comes along with CI/CD + TESTING)
# Osama - Backend + database & Docker (please if you are doing docker then it comes along with CI/CD + TESTING)
# ----------------------------------------------
# Planned Features:
# Ingredient input form (non-AI)
# Recipe generation based on ingredients (AI-powered)

# Ingredient substitution suggestions (AI-powered)

# Display recipe details (steps, ingredients, nutrition) (non-AI)

# Save favorite recipes (non-AI)

# ----------------------------------------------
# Tech Stack:
# Frontend  : HTML, CSS, JavaScript
# Backend   : Python + Flask
# AI        : Google Gemini
# Database  : Supabase (PostgreSQL)
# Container : Docker
# CI/CD     : GitHub Actions
# Deployment: Render

# ----------------------------------------------
# Live URL:
# To be updated once deployment is complete

# ----------------------------------------------
# Backend Local Setup:
# cd backend
# python -m venv venv
# source venv/bin/activate  (Mac/Linux)
# venv\Scripts\activate     (Windows)
# pip install -r requirements.txt
# cp .env.example .env
# fill in SUPABASE_URL and SUPABASE_KEY in .env
# python app.py
# Health check: http://localhost:5000/health

# ----------------------------------------------
# Running Tests:
# cd backend
# pytest tests/ -v

# ----------------------------------------------
# Database Schema (Supabase):
# Table: recipes
# - id           : int8        (primary key, auto-increment)
# - ingredients  : text        (not null)
# - recipe       : text        (not null)
# - created_at   : timestamptz (default: now())