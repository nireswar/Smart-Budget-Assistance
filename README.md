Take control of your finances with AI-driven insights, smart classification, and automated planning.

PocketMind is a comprehensive financial management web application designed for the Indian context. It goes beyond simple tracking by leveraging the Google Gemini 1.5 Flash model to analyze spending habits, provide actionable saving tips, and act as a personal financial consultant.

✨ Key Features
📊 Interactive Dashboard: Visualize your financial health with real-time income vs. expense tracking and category-wise spending breakdowns using Chart.js.

🧠 AI Expense Analyzer: Input a transaction (e.g., "Dinner with friends - ₹1200") and let Gemini classify it as a "Need" or "Want" while providing a personalized saving tip.

💡 AI Financial Insights: A built-in chatbot that provides expert advice on Indian personal finance, from planning budget trips to explaining mutual funds.

📅 Payment Reminders: Never miss a bill again. Add upcoming payments and receive visual alerts for urgent or upcoming due dates.

🔐 Secure Authentication: Full user lifecycle management (Signup/Login/Signout) powered by Firebase Auth.

🌓 Dynamic UI: A modern, responsive design featuring a Dark/Light Mode toggle and sleek "Inter" typography.

☁️ Cloud Sync: All transactions, income data, and reminders are stored securely in Google Firestore.

🛠️ Tech Stack
Backend: Python, Flask

AI Engine: Google Gemini Pro (Generative AI SDK)

Frontend: HTML5, CSS3 (Custom CSS Variables), JavaScript (Vanilla ES6)

Database: Google Firebase Firestore

Authentication: Firebase Authentication

Visualization: Chart.js

📂 Project Structure
Plaintext
PocketMind/
│
├── main.py                 # Flask Server, API Routes & AI Logic
├── project.py              # Gemini API testing script
├── serviceAccountKey.json  # Firebase Admin SDK Credentials (Required)
├── templates/              # UI Components
│   ├── home.html           # Landing Page & Auth Modals
│   ├── dashboard.html      # Stats & Transaction Management
│   ├── analysis.html       # AI Expense Classification Tool
│   ├── insights.html       # AI Chatbot Interface
│   └── planner.html        # Bill Reminders & CRUD operations
└── static/                 # (Optional) CSS/JS/Image files
⚙️ Setup & Installation
1. Prerequisites
Python 3.8+

A Google Cloud Project with the Generative Language API enabled.

A Firebase Project.

2. Install Dependencies
Bash
pip install flask google-generativeai firebase-admin
3. API Configuration
Gemini: Open main.py and replace GEMINI_API_KEY with your actual key from Google AI Studio.

Firebase Admin: Download your serviceAccountKey.json from the Firebase Console (Project Settings > Service Accounts) and place it in the root directory.

Firebase Web SDK: Update the firebaseConfig object in the <script> section of all HTML templates with your project's web credentials.

4. Run the App
Bash
python main.py
Visit http://127.0.0.1:5000 to start managing your money!

🤖 AI Logic Overview
PocketMind uses specialized system prompts to ensure the AI remains focused:

Classification: Uses a strict JSON response format to identify "Needs" vs "Wants".

Insights: Constrained to "Personal Finance" topics only. If asked about non-financial topics, the assistant politely declines to maintain professional utility.
