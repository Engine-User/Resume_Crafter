import streamlit as st

# --- Custom CSS for enhanced UI ---
def get_custom_css():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Orbitron:wght@400;500;600;700&family=VT323&display=swap');
    
    :root {
        --primary-color: #0A0A0A;
        --secondary-color: #1A1A1A;
        --accent-red: #E74C3C;
        --accent-blue: #3498DB;
        --text-color: #ECF0F1;
        --highlight-color: #F39C12;
        --metallic-light: linear-gradient(145deg, #333333, #111111);
        --metallic-dark: linear-gradient(145deg, #222222, #000000);
        --button-hover-bg: #2C3E50;
        --button-active-bg: #1C2833;
    }
    
    /* Global Styles */
    .stApp {
        background-color: var(--primary-color);
        color: var(--text-color);
        font-family: 'Montserrat', sans-serif;
        padding: 2rem;
    }
    
    /* Main Title Styling */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        background: linear-gradient(90deg, var(--accent-blue), var(--accent-red));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        margin-bottom: 1.5rem;
        text-align: center;
        text-shadow: 0 0 20px rgba(52, 152, 219, 0.7), 0 0 30px rgba(231, 76, 60, 0.7);
        letter-spacing: 3px;
        padding: 15px;
        position: relative;
    }
    
    .main-title::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 25%;
        width: 50%;
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--accent-blue), var(--accent-red), transparent);
    }
    
    /* Subtitle Styling */
    .subtitle {
        font-family: 'Montserrat', sans-serif;
        font-weight: 300;
        color: var(--text-color);
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    /* Input Box Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stNumberInput > div > div > input {
        background-color: var(--secondary-color) !important;
        color: var(--text-color) !important;
        font-family: 'Montserrat', monospace !important;
        font-size: 1.1rem !important;
        border: 2px solid var(--accent-blue) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3), inset 0 1px 2px rgba(52, 152, 219, 0.2) !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stNumberInput > div > div > input:focus {
        border-color: var(--accent-red) !important;
        box-shadow: 0 4px 12px rgba(231, 76, 60, 0.3), inset 0 1px 2px rgba(231, 76, 60, 0.2) !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: var(--metallic-light) !important;
        color: var(--text-color) !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 1rem 2rem !important;
        margin: 1rem 0 !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: 500 !important;
        letter-spacing: 2px !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
    }
    
    .stButton > button:hover {
        background: var(--button-hover-bg) !important;
        box-shadow: 0 6px 12px rgba(52, 152, 219, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button:active {
        background: var(--button-active-bg) !important;
        transform: translateY(1px) !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3) !important;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: var(--secondary-color);
        border-radius: 10px;
        padding: 8px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: var(--secondary-color);
        color: var(--text-color);
        font-family: 'Orbitron', sans-serif;
        border-radius: 8px;
        margin: 0 8px;
        padding: 0.8rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(145deg, var(--accent-blue), var(--accent-red));
        color: var(--text-color);
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    /* Subheader Styling */
    h2, .st-emotion-cache-10trblm e1nzilvr1 {
        font-family: 'Orbitron', sans-serif;
        color: var(--accent-blue);
        text-align: center;
        margin: 2rem 0;
        letter-spacing: 2px;
        text-transform: uppercase;
        position: relative;
        display: inline-block;
        width: 100%;
    }

    h2::after {
        content: "";
        position: absolute;
        bottom: -10px;
        left: 30%;
        width: 40%;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--accent-red), transparent);
    }

    /* Download Button Specific Styling */
    .stDownloadButton > button {
        background: linear-gradient(145deg, var(--accent-blue), var(--accent-red)) !important;
        margin: 1rem !important;
        min-width: 200px !important;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(145deg, var(--accent-red), var(--accent-blue)) !important;
        transform: translateY(-2px) !important;
    }
    
    """
from resume_agent import ResumeGenerator
from utils import create_docx

def main():
    st.markdown(f"<style>{get_custom_css()}</style>", unsafe_allow_html=True)
    st.markdown('<p class="main-title">Resume Crafter</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Generate a draft resume to help you apply for jobs faster</p>', unsafe_allow_html=True)

    # Create tabs for different sections
    tab1, tab2 = st.tabs(["Generate Resume", "Settings"])
    
    with tab1:
        st.markdown('<h2>Enter Your Details</h2>', unsafe_allow_html=True)
        # st.subheader("Enter Your Details") # Replaced with styled markdown

        # Contact information
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            email = st.text_input("Email Address:")
        with col2:
            full_name = st.text_input("Full Name:")
        with col3:
            website = st.text_input("Personal Website URL:")
        with col4:
            linkedin = st.text_input("LinkedIn Profile URL:")

        
        # Basic Information
        col1, col2 = st.columns(2)
        with col1:
            job_title = st.text_input("Desired Job Title:")
        with col2:
            years_exp = st.number_input("Years of Experience:", min_value=0, max_value=50)
            
        # Detailed Information
        experience = st.text_area("Professional Experience (List all your roles and achievements):")
        education = st.text_area("Education Background:", height=100)
        skills = st.text_area("Technical Skills:", height=100)

        # Other details
        st.markdown('<h2>Additional Information</h2>', unsafe_allow_html=True)
        # st.subheader("Additional Information") # Replaced with styled markdown
        col1, col2 = st.columns(2)
        with col1:
            certifications = st.text_area("Certifications (if any):", height=100)
        with col2:
            projects = st.text_area("Projects (if any):", height=100)
      
    
        
        if st.button("Generate Resume"):
            if job_title and experience:
                with st.spinner('Generating your professional resume...'):
                    generator = ResumeGenerator()
                    resume_draft = generator.generate_resume(
                        job_title=job_title,
                        experience=experience,
                        education=education,
                        skills=skills,
                        email=email,
                        linkedin=linkedin,
                        website=website,
                        full_name=full_name,
                        certifications=certifications,
                        projects=projects
                    )
                    
                    st.success("Resume Generated!")
                    st.markdown(resume_draft)
                    
                    # Download buttons
                    st.markdown('<h2>Download Options</h2>', unsafe_allow_html=True)
                    # st.subheader("Download Options") # Replaced with styled markdown
                    download_col1, download_col2 = st.columns(2)
                    
                    with download_col1:
                        st.download_button(
                            label="📄 Download as TXT",
                            data=resume_draft,
                            file_name=f"{job_title.lower().replace(' ', '_')}_resume.txt",
                            mime="text/plain",
                            help="Download your resume as a plain text file"
                        )
                    
                    with download_col2:
                        docx_data = create_docx(resume_draft)
                        st.download_button(
                            label="📑 Download as DOCX",
                            data=docx_data,
                            file_name=f"{job_title.lower().replace(' ', '_')}_resume.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                            help="Download your resume as a Word document"
                        )
            else:
                st.error("Please provide at least the job title and experience.")

    with tab2:
        st.markdown('<h2>Resume Settings</h2>', unsafe_allow_html=True)
        # st.subheader("Resume Settings") # Replaced with styled markdown
        st.slider("AI Creativity Level", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

if __name__ == "__main__":
    main()