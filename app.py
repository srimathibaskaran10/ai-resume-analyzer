import streamlit as st
import PyPDF2

# Page Settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Analyzer")

st.markdown("""
Analyze resumes, calculate ATS scores,
detect technical skills and get job recommendations.
""")

# Sidebar
with st.sidebar:
    st.header("About Project")

    st.write("""
    AI Resume Analyzer

    Features:
    ✅ Resume Upload
    ✅ Skill Detection
    ✅ ATS Score
    ✅ Resume Suggestions
    ✅ Job Role Prediction
    ✅ Download Report
    """)

# Upload Section
st.info("Upload your resume PDF below to begin analysis.")

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text

    # Resume Content
    st.subheader("📄 Resume Content")

    st.write(text)

    # Skills Database
    skills = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Data Science",
        "Flask",
        "TensorFlow",
        "HTML",
        "CSS",
        "JavaScript"
    ]

    # Skill Detection
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("🛠 Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.success(skill)
    else:
        st.warning("No matching skills found")

    # ATS Score
    score = len(found_skills) * 10

    if score > 100:
        score = 100

    st.subheader("📊 ATS Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATS Score", f"{score}/100")

    with col2:
        st.metric("Skills Found", len(found_skills))

    if score >= 80:
        st.success("Excellent Resume!")
    elif score >= 60:
        st.info("Good Resume")
    else:
        st.warning("Add more technical skills to improve ATS score")

    # Resume Summary
    st.subheader("📋 Resume Summary")

    st.write(
        f"""
        Your resume contains {len(found_skills)} detected technical skills.

        Current ATS score is {score}/100.
        """
    )

    # Missing Skills
    st.subheader("🚀 Resume Improvement Suggestions")

    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    if missing_skills:

        st.write("Recommended skills to learn:")

        for skill in missing_skills:
            st.error(skill)

    # Personalized Suggestions
    if "SQL" in missing_skills:
        st.info("Learning SQL can improve your data-related opportunities.")

    if "Machine Learning" in missing_skills:
        st.info("Consider learning Machine Learning and adding a project.")

    if "Data Science" in missing_skills:
        st.info("Data Science skills are valuable for analytics and AI roles.")

    if "Flask" in missing_skills:
        st.info("Building Flask projects can strengthen your backend skills.")

    # Job Role Prediction
    st.subheader("💼 Recommended Job Roles")

    recommended_roles = []

    if "Python" in found_skills:
        recommended_roles.append("Python Developer")

    if "SQL" in found_skills:
        recommended_roles.append("Data Analyst")

    if "Machine Learning" in found_skills:
        recommended_roles.append("AI/ML Engineer")

    if "Data Science" in found_skills:
        recommended_roles.append("Data Scientist")

    if "Flask" in found_skills:
        recommended_roles.append("Backend Developer")

    if "TensorFlow" in found_skills:
        recommended_roles.append("Deep Learning Engineer")

    if recommended_roles:
        for role in recommended_roles:
            st.success(role)
    else:
        st.warning("No suitable role predictions available.")

    # Download Report
    st.subheader("📥 Download Analysis Report")

    report = f"""
RESUME ANALYSIS REPORT

ATS Score: {score}/100

Skills Found:
{', '.join(found_skills)}

Missing Skills:
{', '.join(missing_skills)}

Recommended Roles:
{', '.join(recommended_roles)}
"""

    st.download_button(
        label="Download Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )