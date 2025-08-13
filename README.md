# Assessment Recommendation Engine

## Project Overview
An NLP-powered recommendation system that suggests relevant assessments based on user-provided text. Designed for education and training platforms to personalize content delivery.

## Problem Statement
In large learning platforms, users are often overwhelmed by the number of available assessments. Recommending the most relevant ones improves user engagement and learning efficiency.

## Objectives
- Build an NLP pipeline to process user input and identify relevant assessments.
- Serve recommendations through both a backend API and a user-friendly interface.

## Dataset & Input
- Input: User-provided text describing learning goals or topics.
- Dataset: Collection of assessment descriptions with associated metadata.
- Output: Top N recommended assessments ranked by similarity score.

## Methodology
1. Preprocessed text data (tokenization, stopword removal, lemmatization).
2. Converted text to numerical vectors using TF-IDF.
3. Computed cosine similarity to rank assessments.
4. Built a FastAPI backend for real-time recommendation requests.
5. Developed a Streamlit front-end for interactive use.

## Results
- Deployed for 150+ active users with positive feedback.
- Delivered recommendations in under 500ms on average.
- Architecture supports easy scaling and integration with other systems.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, FastAPI, Streamlit, TF-IDF, Cosine Similarity

## Future Enhancements
- Integrate with user profile history for personalized recommendations.
- Use transformer-based models (BERT) for better semantic matching.
- Deploy on cloud with CI/CD pipelines for continuous updates.
