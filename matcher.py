from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import streamlit as st


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def calculate_match(resume_text, job_description):
    model = load_model()

    resume_embedding = model.encode(resume_text)
    job_embedding = model.encode(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )

    match_percentage = similarity[0][0] * 100

    return round(match_percentage, 2)


def compare_skills(resume_text, job_description):
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
        "GitHub",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "NLP",
        "Data Analysis"
    ]

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matching_skills = []
    missing_skills = []

    for skill in skills_list:
        if skill.lower() in job_description:
            if skill.lower() in resume_text:
                matching_skills.append(skill)
            else:
                missing_skills.append(skill)

    return matching_skills, missing_skills