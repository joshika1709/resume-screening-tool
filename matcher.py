SKILLS = ["python", "sql", "excel", "tableau", "power bi", "communication"]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]
