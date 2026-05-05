from fastapi import FastAPI, UploadFile, File
import shutil, os

from parser import read_resume
from matcher import extract_skills
from scorer import compute_similarity

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...), jd_text: str = ""):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = read_resume(file_path)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    similarity = compute_similarity(resume_text, jd_text)

    return {
        "similarity": similarity,
        "resume_skills": resume_skills,
        "jd_skills": jd_skills
    }
