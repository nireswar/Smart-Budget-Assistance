import google.generativeai as genai

genai.configure(api_key="AIzaSyAaaqNRCuO0KbuOZ5zPaXFp9_3-VFINh5U")  # use your actual Gemini API key here

model = genai.GenerativeModel('gemini-1.5-flash-latest')

prompt = """You are a helpful assistant. User asks: Plan a trip to Tamil Nadu with a budget of ₹5000."""

response = model.generate_content(prompt)

print("RAW RESPONSE:\n", response)
print("\nTEXT:\n", response.text)
