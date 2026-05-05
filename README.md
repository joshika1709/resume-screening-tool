# 🚀 Automated Resume Screening Tool

---

## 📌 Project Overview

The **Automated Resume Screening Tool** is a Python-based application that simulates how companies filter and shortlist resumes using technology.

In real-world hiring, recruiters receive a large number of applications. This tool helps automate the initial screening process by:

* Reading resumes
* Extracting skills
* Comparing them with job requirements
* Generating a match score

It acts as a **mini Applicant Tracking System (ATS)** built using Python and basic NLP techniques.

---

## ❗ Problem Statement

Recruiters often face challenges such as:

* Too many resumes to review manually
* Time-consuming shortlisting process
* Human bias and inconsistency
* Missing qualified candidates due to manual errors

👉 This project solves these problems by:

* Automating resume screening
* Providing objective scoring
* Highlighting relevant skills quickly

---

## 🌍 Industry Relevance

This project is highly relevant in industries like:

* Human Resource Management (HRM)
* Recruitment & Talent Acquisition
* HR Tech and SaaS platforms

Real companies use similar systems (ATS) to:

* Filter resumes automatically
* Rank candidates
* Improve hiring efficiency

👉 This project demonstrates how technology supports **data-driven hiring decisions**.

---

## ✨ Features

* 📄 Resume parsing (TXT format)
* 🧠 Skill extraction using keyword matching
* 📊 Resume vs Job Description comparison
* 📈 Similarity scoring using NLP techniques
* ⚡ FastAPI backend for real-time analysis
* 🔍 Clear output showing skills and match score

---

## 🛠️ Tech Stack

* **Python** → Core programming language
* **FastAPI** → Backend API development
* **Scikit-learn** → TF-IDF & Cosine Similarity
* **Basic NLP** → Skill extraction
* **Uvicorn** → Server

---

## 📁 Folder Structure

```
resume-screening-tool/
│
├── main.py              # FastAPI application
├── parser.py            # Resume reader
├── matcher.py           # Skill extraction logic
├── scorer.py            # Similarity calculation
├── requirements.txt     # Dependencies
├── README.md            # Documentation
│
├── data/
│   └── resumes/
│       ├── resume1.txt
│       └── resume2.txt
│
├── uploads/             # Temporary uploaded files
```

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```
git clone https://github.com/your-username/resume-screening-tool.git
cd resume-screening-tool
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run the server

```
uvicorn main:app --reload
```

### Step 4: Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Sample Input

### Resume (resume1.txt)

```
Data analyst skilled in Python, SQL, Excel and Power BI.
```

### Job Description

```
Looking for a data analyst with Python, SQL, Tableau and communication skills.
```

---

## 📊 Sample Output

```
Similarity Score: 0.78

Resume Skills:
['python', 'sql', 'excel', 'power bi']

Job Description Skills:
['python', 'sql', 'tableau', 'communication']
```

👉 Interpretation:

* Candidate matches most required skills
* Missing skills: Tableau, Communication

---

## 📸 Screenshots

*(Add these after running your project)*

1. FastAPI Swagger UI (`/docs`)
2. Resume upload screen
3. Output response with similarity score
4. Project folder structure

👉 Tip: Take screenshots using your system and upload them to your GitHub repo.

---

## 🎓 Learning Outcomes

Through this project, I learned:

* ✅ How to build REST APIs using FastAPI
* ✅ Basics of Natural Language Processing (NLP)
* ✅ How TF-IDF and Cosine Similarity work
* ✅ How to structure a real-world project
* ✅ GitHub project management and documentation
* ✅ Understanding of HR tech and ATS systems

---

## 🔮 Future Improvements

* Support for PDF and DOCX resumes
* Advanced NLP models for better accuracy
* Candidate ranking system
* Frontend dashboard (React / Next.js)
* Database integration

---

## 🎤 Interview Explanation

“I developed an Automated Resume Screening Tool that uses NLP techniques like TF-IDF and cosine similarity to compare resumes with job descriptions. It extracts skills, calculates a matching score, and helps in efficient candidate shortlisting.”

---

## 🙌 Conclusion

This project demonstrates a **real-world application of Python, NLP, and HR analytics**.

It serves as a strong **proof-of-work project** for roles such as:

* Data Analyst
* Business Analyst
* HR Analyst

---

