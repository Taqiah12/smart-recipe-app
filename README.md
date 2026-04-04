# smart-recipe-app
# App name: Smart Recipe App
# ---------------------------------------------
# Description : The Smart Recipe App allows users to input the ingredients they have and receive recipe suggestions. The app uses AI to generate recipes and suggest ingredient substitutions. It is designed for home cooks, students, and busy individuals who want to quickly prepare meals using available ingredients.

# ----------------------------------------------
# Team Members and roles :
# Taqiah - Frontend + API Integration/UI-UX
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