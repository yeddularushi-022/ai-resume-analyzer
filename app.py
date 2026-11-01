import streamlit as st

from resume_parser import (
    extract_resume_text,
    extract_skills,
    extract_education,
    extract_experience
)

from matcher import calculate_match, compare_skills


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI-Powered Resume Analyzer")
st.caption("Analyze your resume and discover how well it matches a job description.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Resume")

    uploaded_resume = st.file_uploader(
        "Upload your resume in PDF format",
        type=["pdf"]
    )

with col2:
    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=200,
        placeholder="Paste the job description..."
    )

st.divider()

if st.button("🔍 Analyze Resume", type="primary", use_container_width=True):

    if uploaded_resume is None:
        st.warning("Please upload your resume PDF.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        with st.spinner("Analyzing your resume..."):

            resume_text = extract_resume_text(uploaded_resume)

            skills = extract_skills(resume_text)
            education = extract_education(resume_text)
            experience = extract_experience(resume_text)

            match_percentage = calculate_match(
                resume_text,
                job_description
            )

            matching_skills, missing_skills = compare_skills(
                resume_text,
                job_description
            )

        st.success("Resume analysis completed!")

        st.header("📊 Analysis Results")

        st.metric(
            label="Resume–Job Description Match",
            value=f"{match_percentage}%"
        )

        st.progress(int(match_percentage))

        st.write(
            f"Your resume has a **{match_percentage}% semantic similarity** "
            "with the job description."
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matching Skills")

            if matching_skills:
                for skill in matching_skills:
                    st.write(f"✓ {skill}")
            else:
                st.write("No matching skills found.")

        with col2:
            st.subheader("📌 Skills to Improve")

            if missing_skills:
                for skill in missing_skills:
                    st.write(f"• {skill}")
            else:
                st.write("No missing skills found.")

        st.divider()

        with st.expander("🧠 Skills Found in Resume"):
            st.write(", ".join(skills) if skills else "No skills found.")

        with st.expander("🎓 Education Found"):
            st.write(", ".join(education) if education else "No education found.")

        with st.expander("💼 Experience Keywords Found"):
            st.write(
                ", ".join(experience)
                if experience
                else "No experience keywords found."
            )

        report = f"""
AI-POWERED RESUME ANALYZER REPORT

Resume–Job Description Match: {match_percentage}%

MATCHING SKILLS:
{", ".join(matching_skills) if matching_skills else "None"}

SKILLS TO IMPROVE:
{", ".join(missing_skills) if missing_skills else "None"}

SKILLS FOUND IN RESUME:
{", ".join(skills) if skills else "None"}

EDUCATION FOUND:
{", ".join(education) if education else "None"}

EXPERIENCE KEYWORDS FOUND:
{", ".join(experience) if experience else "None"}
"""

        st.download_button(
            label="📥 Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain",
            use_container_width=True
        )

st.divider()

st.caption("Built with Python, Streamlit, and Sentence Transformers")