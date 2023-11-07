# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "carly_taylor_example_resume.pdf" 
profile_pic = current_dir / "headshot.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Carly Taylor"
PAGE_ICON = ":wave:"
NAME = "Carly Taylor"
DESCRIPTION = """
DATA LEADER
"""
EMAIL = "carlytaylor@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/carly-taylor-data/",
    "GitHub": "https://github.com/carlytaylor0017",
    "Website": "https://rebeldatascience.com",
}
PROJECTS = {
    "🏆 Selected Projects": "https://carlytaylor0017.github.io/",
}
CODE = {
    "🏆 Build your Own Interactive CV": "https://github.com/carlytaylor0017/health-universe-interactive-cv",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- Data scientist, technical strategist, and video game enthusiast with an M.S. in computational chemistry
and 5+ years of experience in tech. I thrive in a position of balancing hands-on development while
collaborating with executive leadership to align on strategic visions.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Technologies: Kafka, Docker, Kubernetes, Apache Spark, Amazon Web Services (AWS), Google Cloud Platform (GCP)
- 📊 Tools & Libraries: Keras, Numpy, Pandas, Scikit-Learn, TensorFlowPowerBi, MS Excel, Plotly
- 📚 Modeling: Clustering, Regression, Classification, Deep Learning, Anomaly Detection, Supervised Learning, Operational Efficiency, Unsupervised Learning, Natural Language ProcessingLogistic regression, linear regression, decition trees
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Director - Franchise Security Strategy | Activision**")
st.write("Oct 2023 - Present")
st.write(
    """
- ► Promoted to Director of Franchise Security Strategy
- ► Develop security strategy roadmap and internal communication strategy with Activision executive leadership about disruptive behavior in Call of Duty®
- ► Ownership of end-to-end security strategy from client-side protections to server-side technologies that protect our players from disruptive behavior
"""
)

# --- JOB 2
st.write("🚧", "**Senior Manager - Machine Learning Security Strategy | Activision**")
st.write("Mar 2022 - Oct 2023")
st.write(
    """
- ► Reduced player churn by 15% by deploying scalable machine learning models to detect disruptive behavior
- ► Authored strategic roadmap for machine learning approach to disruptive behavior as well as best practices in machine learning to key development areas (in-game AI, automated QA, compression)
- ► Built a team of machine learning and game engineers focused on strengthening the technology that delivers low-latency concurrent experiences to millions of players
- ► Developed security technologies that leverage our fleet of game servers to take action to protect our players
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Lead Data Scientist | Activision**")
st.write("Jan 2022 - Mar 2022")
st.write(
    """
- ► Managed a team of data scientists developing distributed machine learning models
- ► Built, refined, and executed a roadmap for the Machine Learning team’s approach to disruptive behavior
- ► Collaborated with executive leadership, game studios, live-ops, and marketing to align on project roadmaps and execute internal and external communication strategies
- ► Utilized Kafka and Spark Structured Streaming to develop real-time machine learning models for ingame anomaly detection
- ► Outlined team best-practices including library packaging, versioning, containerization, CI/CD and task-scheduling
- ► Triaged and shaped incoming requests and supervise team deliverables
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Senior Data Scientist | Activision**")
st.write("Aug 2020 - Jan 2022")
st.write(
    """
- ► Built scalable machine learning models to detect disruptive behavior
- ► Designed and maintained efficient, production-quality detection tools to inform operations and measure performance
- ► Translated requirements from cross-disciplinary teams in Game Operations, Marketing, CRM, and Business Planning into data solutions
- ► Surfaced and communicated results to technical and non-technical colleagues by generating quarterly presentations and online dashboards
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- Build your Own ---
st.write('\n')
st.subheader("Build your Own Interactive CV")
st.write("---")
for code, link in CODE.items():
    st.write(f"[{code}]({link})")
