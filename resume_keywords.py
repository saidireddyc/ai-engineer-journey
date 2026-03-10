resume = """
Python developer with experience in APIs, Git, FastAPI,
machine learning, and data analysis.
"""

keywords = ["python", "api", "git", "fastapi", "machine learning", "docker"]

found = []

for word in keywords:
    if word in resume.lower():
        found.append(word)

print("Skills found in resume:")
for skill in found:
    print("-", skill)