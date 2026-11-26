# Prompting styles with local demonstration rules (no live LLM call)
examples = [
    {"id": "T101", "technique": "Zero-Shot", "role": "Sentiment analyst",
     "task": "Classify review sentiment", "text": "The delivery was quick and the product works perfectly."},
    {"id": "T102", "technique": "One-Shot", "role": "Customer feedback analyst",
     "task": "Classify review sentiment", "text": "The battery stopped working after one day.",
     "example": "The service was excellent and helpful.", "label": "Positive"},
    {"id": "T103", "technique": "Few-Shot", "role": "Product review analyst",
     "task": "Classify review sentiment", "text": "The camera quality is poor and the screen is dull."},
    {"id": "T104", "technique": "Role-Based", "role": "Academic writing tutor",
     "task": "Rewrite the sentence professionally", "text": "hey, send me the project file now"},
    {"id": "T105", "technique": "Few-Shot", "role": "Support analyst",
     "task": "Classify ticket priority", "text": "The application is unavailable for every user."},
]
positive = {"quick", "perfectly", "excellent", "helpful", "love", "early", "great"}
negative = {"poor", "dull", "stopped", "broken", "slow", "unavailable"}

def sentiment(text):
    words = set(text.lower().replace(".", "").replace(",", "").split())
    score = len(words & positive) - len(words & negative)
    return "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"

def construct_prompt(row):
    technique = row["technique"]
    if technique == "Zero-Shot":
        return f"You are a {row['role']}. {row['task']}: {row['text']}"
    if technique == "One-Shot":
        return f"You are a {row['role']}. {row['task']}. Example: {row['example']} -> {row['label']}. New input: {row['text']}"
    if technique == "Few-Shot":
        return f"You are a {row['role']}. {row['task']}. Examples: Excellent service -> Positive; Poor quality -> Negative. New input: {row['text']}"
    return f"Act as a {row['role']}. {row['task']}: {row['text']}"

print("----- ROLE-BASED AND EXAMPLE-BASED PROMPTING -----")
for row in examples:
    prompt = construct_prompt(row)
    if "sentiment" in row["task"].lower():
        response = sentiment(row["text"])
    elif "priority" in row["task"].lower():
        response = "High" if "unavailable" in row["text"].lower() else "Low"
    else:
        response = "Suggested rewrite: Please share the project file at your earliest convenience."
    print(f"\nID: {row['id']} | Technique: {row['technique']}")
    print("Constructed prompt:", prompt)
    print("Python demonstration response:", response)
print("\nResponses use predefined Python rules, not a live LLM.")
