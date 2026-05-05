🚀 Automated Resume Screening Tool

📌 Project Overview

This project is a **simulation of an Applicant Tracking System (ATS)** used by companies to screen resumes.

In real companies, HR teams receive **hundreds of resumes** for one job.
Manually checking all resumes is time-consuming.

👉 This tool helps **automate that process** by:

* Reading resumes
* Comparing them with job descriptions
* Identifying relevant skills
* Giving a matching score

---

🎯 Objective

The goal of this project is to build a system that:

* Extracts important information from resumes
* Matches resumes with job requirements
* Helps HR quickly shortlist candidates

---

🛠️ Technologies Used

* **Python** → Main programming language
* **FastAPI** → To create backend API
* **Scikit-learn** → For similarity calculation (TF-IDF, Cosine Similarity)
* **Basic NLP** → For skill extraction

---

⚙️ How It Works (Step-by-Step)

1. Resume Upload

User uploads a resume file (currently `.txt` format).

2. Job Description Input

User enters the job description manually.

3. Text Processing

The system reads both:

* Resume text
* Job description text

---
4. Skill Extraction

The system checks for predefined skills like:

* Python
* SQL
* Excel
* Tableau
* Communication

---

5. Similarity Calculation

The system compares resume and job description using:

* **TF-IDF Vectorization**
* **Cosine Similarity**

👉 This gives a **matching score**

---

6. Output

The system returns:

* Similarity score
* Skills found in resume
* Skills required in job

---

📊 Sample Output

Example:

* Similarity Score: **0.78**
* Resume Skills: `python, sql, excel`
* Job Skills: `python, sql, tableau`

👉 Interpretation:

* Candidate matches most requirements
* Missing skill: Tableau

---

📁 Project Structure

resume-screening-tool/
│
├── main.py          # FastAPI application
├── parser.py        # Reads resume file
├── matcher.py       # Extracts skills
├── scorer.py        # Calculates similarity
├── requirements.txt # Dependencies
├── README.md        # Project documentation
├── data/            # Sample resumes

---

▶️ How to Run the Project

Step 1: Install dependencies

pip install -r requirements.txt

Step 2: Run the server

uvicorn main:app --reload

Step 3: Open in browser

http://127.0.0.1:8000/docs

---

🧪 How to Test

* Upload a sample resume (.txt file)
* Enter a job description
* Click **Execute**

👉 You will see the result instantly

---

🔍 Key Features

✔ Simple and easy to use
✔ Fast resume screening
✔ Skill-based matching
✔ Real-world HR use case

---

⚠️ Limitations

* Works only with `.txt` files (currently)
* Uses keyword-based skill matching
* Does not fully understand context

---

🔮 Future Improvements

* Add PDF and DOCX support
* Build frontend dashboard
* Improve NLP using machine learning
* Add candidate ranking system

---

💼 Real-World Relevance

This project is useful for:

* HR professionals
* Recruiters
* Companies handling bulk hiring

---

🎤 Interview Explanation (How to Explain)

You can say:

"I built an Automated Resume Screening Tool using FastAPI and NLP techniques.
It extracts skills from resumes, compares them with job descriptions using TF-IDF and cosine similarity, and provides a matching score to help in candidate shortlisting."

---

🙌 Conclusion

This project demonstrates:

* Backend development
* Basic NLP concepts
* Real-world HR application

It is a strong **proof-of-work project** for roles like:

* Data Analyst
* Business Analyst
* HR Analyst

---

