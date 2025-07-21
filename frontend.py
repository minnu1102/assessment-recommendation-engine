import streamlit as st
import requests

st.set_page_config(page_title="Assessment Recommender", layout="wide")
st.title("AI-Powered Assessment Recommendation Engine")

st.markdown("Paste a job description or your career goal, and we'll suggest the most relevant online assessments!")

query = st.text_area("Enter Job Description or Goal", height=200)

if st.button("Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a description or goal.")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post("http://127.0.0.1:8000/recommend", json={"query": query})
            data = response.json()

            st.success("Top Recommendations:")
            for i, rec in enumerate(data["recommendations"], 1):
                st.markdown(f"### {i}. {rec['Exam Name']}")
                st.write(f"**Platform**: {rec['Platform']}")
                st.write(f"**Tags**: `{rec['Tags']}`")
                st.markdown("---")
