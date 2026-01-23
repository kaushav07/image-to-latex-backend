# Image → LaTeX Converter

Convert handwritten or printed math equations from images into clean LaTeX using AI.

This project includes:
- A FastAPI backend
- A simple HTML/CSS/JavaScript frontend

This README can be used **as-is for both frontend and backend repositories**.

---

## Live Deployment

Backend API:  
https://image-to-latex-backend.onrender.com

Frontend:  
https://image-to-latex.vercel.app

---

## What This Project Does

- Upload an image containing a math equation
- Converts the equation into LaTeX
- Shows image preview before processing
- Displays generated LaTeX
- One click copy functionality

---

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- AI: OpenAI API
- Deployment: Render

---

## API Key & Security

The OpenAI API key is stored locally in a `.env` file and is **not committed to GitHub**.

For deployment, the key is added using **Render Environment Variables**.

---

## Example Equations to Test

- `x = (-b ± √(b² − 4ac)) / 2a`
- `∫₀^∞ e^{-x²} dx = √π / 2`
- `∑_{i=1}^{n} i = n(n+1)/2`
- `a² + b² = c²`

---

## 📄 License
This project is licensed under the MIT License.

---

## Author

Kaushav Kumar
