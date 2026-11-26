# Rule-based prompt-quality checklist; does not call a live LLM
import pandas as pd

examples = [
    ("P101", "Explain photosynthesis",
     "You are a biology teacher helping a student. Explain photosynthesis in under 150 words and include an example in a table."),
    ("P102", "Write a formal email",
     "Act as a communications manager at a college. Draft a formal email in under 150 words and include a subject line."),
    ("P103", "Python debugging",
     "You are a Python tutor. Review this project code in under five words and suggest three fixes."),
    ("P104", "Summarize a report",
     "You are an editor for a student report. Summarize the report in under 100 words and present bullet points in a table."),
    ("P105", "Compare algorithms",
     "Act as an algorithms instructor. Compare sorting methods and include an example in a table."),
]
criteria = {
    "Role": ("act as", "you are"),
    "Context": ("student", "manager", "college", "project", "report"),
    "Clear task": ("explain", "draft", "review", "summarize", "compare"),
    "Constraints": ("words", "bullet", "under", "three", "five"),
    "Output format": ("table", "subject", "bullet points", "example"),
}
weak_prompts = ["Explain photosynthesis", "Write email", "Fix code", "Summarize this", "Algorithms"]

def evaluate(prompt):
    text = prompt.lower()
    matched = {label: any(term in text for term in terms)
               for label, terms in criteria.items()}
    return sum(matched.values()), matched

rows = []
print("----- PROMPT DESIGN AND EVALUATION -----")
for (prompt_id, task, improved), weak in zip(examples, weak_prompts):
    weak_score, _ = evaluate(weak)
    improved_score, features = evaluate(improved)
    rows.append((weak_score, improved_score))
    print(f"\nPrompt ID: {prompt_id} | Task: {task}")
    print(f"Weak prompt score     : {weak_score}/5")
    print(f"Improved prompt score : {improved_score}/5")
    print("Satisfied features    :", ", ".join(k for k, v in features.items() if v))
    print("Evaluation            :", "Improved" if improved_score > weak_score else "Needs review")

df = pd.DataFrame(rows, columns=["Weak_Score", "Improved_Score"])
print("\n----- OVERALL SUMMARY -----")
print("Average weak prompt score    :", round(df["Weak_Score"].mean(), 2))
print("Average improved prompt score:", round(df["Improved_Score"].mean(), 2))
print("\nEvaluation is a rule-based checklist, not an LLM evaluation.")
