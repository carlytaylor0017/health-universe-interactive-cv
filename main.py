import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to display a section in the app
def display_section(title, content):
    st.subheader(title)
    st.write(content)

# Skills Chart
def plot_skills(skills, levels):
    fig, ax = plt.subplots()
    ax.barh(skills, levels, color='skyblue')
    ax.set_xlabel('Proficiency Level')
    for i, v in enumerate(levels):
        ax.text(v + 0.1, i, str(v), color='blue', fontweight='bold')
    return fig

# Main app layout
st.title("Interactive Bioinformatics CV")

# Personal Information
personal_info = {
    "Name": "Your Name",
    "Role": "Bioinformatics Engineer",
    "Location": "Your City, Country",
    "Summary": "Brief summary about yourself."
}
for key, value in personal_info.items():
    st.sidebar.write(f"**{key}:** {value}")

# Skills
skills = ["Python", "R", "Data Analysis", "Machine Learning", "Genomics"]
levels = [90, 85, 80, 75, 70]  # Your proficiency levels from 0 to 100
display_section("Skills", plot_skills(skills, levels))

# Experience
experience = """
- **Company 1** (Year - Year): Role and key accomplishments.
- **Company 2** (Year - Year): Role and key accomplishments.
"""
display_section("Experience", experience)

# Education
education = """
- **University Name** (Year - Year): Degree, Field of Study.
- **Other Institute** (Year - Year): Degree, Field of Study.
"""
display_section("Education", education)

# Projects
projects = {
    "Project 1": "Description of Project 1. [Link to project](#)",
    "Project 2": "Description of Project 2. [Link to project](#)"
}
for project, description in projects.items():
    if st.button(project):
        st.write(description)
        progress = st.slider(f"Project Completion - {project}", 0, 100, 50)
        st.progress(progress)

# Publications/Research
research = {
    "Paper Title 1": "[Read More](#)",
    "Paper Title 2": "[Read More](#)"
}
display_section("Publications/Research", "\n".join([f"- **{k}**: {v}" for k, v in research.items()]))

# Contact
contact = "Reach out to me at [your.email@example.com](mailto:your.email@example.com)."
display_section("Contact", contact)
