# Keyword-based study assistant using a small local learning dataset
import re

materials = [
    {"Topic": "Programming", "Concept": "Functions",
     "Explanation": "Functions are reusable blocks of code that perform a task.",
     "Keywords": "python parameters return", "Quiz_Question": "What does a function help you reuse?",
     "Difficulty": "Easy", "Answer": "A block of code"},
    {"Topic": "Programming", "Concept": "Lists",
     "Explanation": "A list stores an ordered, changeable collection of values.",
     "Keywords": "python sequence items", "Quiz_Question": "Are lists ordered?",
     "Difficulty": "Easy", "Answer": "Yes"},
    {"Topic": "Artificial Intelligence", "Concept": "Machine Learning",
     "Explanation": "Machine learning uses data to learn patterns and make predictions.",
     "Keywords": "models training data", "Quiz_Question": "What do models learn from?",
     "Difficulty": "Medium", "Answer": "Data"},
    {"Topic": "Artificial Intelligence", "Concept": "Neural Networks",
     "Explanation": "A neural network is a computational model inspired by connected neurons. It contains layers of nodes that learn patterns through training.",
     "Keywords": "nodes layers training", "Quiz_Question": "What are the basic units in a neural network commonly called?",
     "Difficulty": "Medium", "Answer": "Nodes or neurons"},
    {"Topic": "Data Science", "Concept": "Data Cleaning",
     "Explanation": "Data cleaning corrects missing, duplicated, or inconsistent records.",
     "Keywords": "missing duplicate quality", "Quiz_Question": "Name one issue data cleaning addresses.",
     "Difficulty": "Easy", "Answer": "Missing or duplicated data"},
    {"Topic": "Data Science", "Concept": "Data Visualization",
     "Explanation": "Data visualization communicates data patterns with charts and plots.",
     "Keywords": "charts graphs plots", "Quiz_Question": "What can a chart help reveal?",
     "Difficulty": "Easy", "Answer": "Patterns in data"},
]

def tokenize(text):
    return set(re.findall(r"[a-zA-Z]+", str(text).lower()))

def retrieve(query):
    words = tokenize(query)
    scored = []
    for row in materials:
        searchable = " ".join(str(row[key]) for key in ("Topic", "Concept", "Explanation", "Keywords"))
        score = len(words & tokenize(searchable)) / max(len(words), 1)
        scored.append(score)
    best = max(range(len(scored)), key=scored.__getitem__)
    return (materials[best], scored[best]) if scored[best] > 0 else (None, 0)

print("Available concepts:", ", ".join(row["Concept"] for row in materials))
query = input("\nEnter a topic or concept to study: ")
material, score = retrieve(query)
if material is None:
    print("No matching material found. Try another concept.")
else:
    print("\n----- PERSONALIZED STUDY NOTES -----")
    print("Topic       :", material["Topic"])
    print("Concept     :", material["Concept"])
    print("Explanation :", material["Explanation"])
    print("Match score :", round(score * 100, 2), "%")
    print("\n----- QUICK QUIZ -----")
    print("Question    :", material["Quiz_Question"])
    print("Difficulty  :", material["Difficulty"])
    print("Answer      :", material["Answer"])
print("\nStudy assistant session completed.")
print("Note: Matching is based on keyword overlap, not a live Generative AI model.")
