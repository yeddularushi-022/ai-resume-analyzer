from pypdf import PdfReader


def extract_resume_text(pdf_file):
    reader = PdfReader(pdf_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    return resume_text


def extract_skills(resume_text):
    skills_list = [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Machine Learning",
        "Scikit-learn",
        "Streamlit",
        "Git",
        "GitHub"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    return found_skills


def extract_education(resume_text):
    education_keywords = [
        "B.Tech",
        "Bachelor",
        "M.Tech",
        "Master",
        "B.E.",
        "B.Sc",
        "M.Sc",
        "Ph.D"
    ]

    found_education = []

    for keyword in education_keywords:
        if keyword.lower() in resume_text.lower():
            found_education.append(keyword)

    return found_education


def extract_experience(resume_text):
    experience_keywords = [
        "Internship",
        "Intern",
        "Work Experience",
        "Professional Experience",
        "Employment",
        "Years of Experience"
    ]

    found_experience = []

    for keyword in experience_keywords:
        if keyword.lower() in resume_text.lower():
            found_experience.append(keyword)

    return found_experience