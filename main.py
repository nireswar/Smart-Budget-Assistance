import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import json
import firebase_admin
from firebase_admin import credentials

GEMINI_API_KEY = "cccccccccccccccccccccccccccccccU"   #your gemini api key here
genai.configure(api_key=GEMINI_API_KEY)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/planner")
def planner():
    return render_template("planner.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/insights")
def insights():
    return render_template("insights.html")

@app.route("/api/analyze", methods=['POST'])
def analyze_expense_api():
    try:
        data = request.get_json()
        description = data.get('description')
        amount = data.get('amount')
        if not description or not amount:
            return jsonify({"error": "Missing description or amount"}), 400
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        system_prompt = f"""You are a financial analyst for an Indian user. Your task is to analyze a single transaction. 
        First, classify the transaction as either 'Need' or 'Want'. 'Needs' are essential (groceries, bills, rent). 'Wants' are non-essential (entertainment, dining out, luxury shopping).
        Second, provide a single, short, actionable tip on how to save money on this specific type of expense in the future.
        You must respond with only a valid JSON object in the following format and nothing else: {{"classification": "Need or Want", "tip": "Your short tip here..."}}
        If no specific tip is relevant, provide a general encouragement.
        Transaction to analyze:
        - Description: "{description}"
        - Amount: ₹{amount}"""
        response = model.generate_content(system_prompt)
        raw_text = response.text.strip().replace("```json", "").replace("```", "")
        parsed_json = json.loads(raw_text)
        return jsonify(parsed_json)
    except Exception as e:
        print(f"An error occurred in /api/analyze: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

@app.route("/api/insights", methods=['POST'])
def insights_chat_api():
    try:
        data = request.get_json()
        question = data.get('question')
        context = data.get('context')
        if not question:
            return jsonify({"error": "Missing question"}), 400
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        system_prompt = f"""You are an expert financial assistant for an Indian user of the PocketMind app. Your name is 'PocketMind Assistant'. Your primary goal is to provide helpful, actionable, and concise advice on a wide range of money-related topics. Analyze the user's provided financial data to make your advice personal and specific.
        Your capabilities include:
        - Creating budget-friendly trip itineraries within India.
        - Suggesting saving strategies for specific goals.
        - Providing shopping advice, like when to look for sales.
        - Explaining financial concepts clearly (e.g., "what is a mutual fund?").
        Your rules are:
        1. You MUST only answer questions related to personal finance.
        2. If asked a non-financial question, you MUST politely decline by responding with: "I can only answer money-related questions."
        3. Keep answers relevant to an Indian context.
        4. Do not claim to have live internet access.
        USER'S FINANCIAL DATA:
        {context}
        """
        response = model.generate_content(system_prompt + f"\nUser Question: {question}")
        return jsonify({"answer": response.text})
    except Exception as e:
        print(f"An error occurred in /api/insights: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

if __name__ == "__main__":
    app.run(debug=True)
