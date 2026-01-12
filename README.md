 
https://github.com/user-attachments/assets/57fbd88f-6a85-43d8-84db-8171e28a516a


Your Research Companion
AI-Based Research Paper Summarization & Interactive Assistant

Your Research Companion is an AI-powered web application designed to help students and researchers understand research papers more efficiently.
It enables users to upload academic papers in PDF format and automatically generates concise summaries, extracts important metadata, and provides an interactive assistant for paper-specific queries.

The system follows a hybrid AI architecture, combining LLM-based summarization with rule-based Natural Language Processing techniques. This approach ensures better explainability, reduced dependency on external APIs, and suitability for academic environments.

Features

Upload research papers in PDF format
Automatic AI-based literature review generation 
Extraction of contributors (authors) 
Keyword identification using NLP heuristics  
Paper statistics including page count and word count 
Context-aware chatbot for paper-specific questions  

Example: What is UAV? 
Responses are generated strictly from the uploaded document 
Dark and light theme support 
Download generated summaries as PDF 
Persistent chat history
Smooth, SPA-like user experience without page reloads

Project Type

Hybrid AI-Based Research Assistance System
Utilizes pretrained language models for summarization
Applies rule-based NLP methods for keyword and contributor extraction
Executes entirely locally without requiring paid APIs or API keys

Technology Stack
Frontend
HTML5
CSS3
Vanilla JavaScript

Backend
Python 3
Flask
AI and NLP
Hugging Face Transformers
PyTorch
Rule-based NLP using heuristics and frequency analysis
Document Processing
PyMuPDF for PDF text extraction
ReportLab for PDF summary generation
 
  
PROJECT STRUCTURE

 project-root/
│
├── backend/
│   ├── app.py
│   ├── summarizer.py
│   ├── chatbot.py
│   ├── nlp_utils.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── uploads/
│   └── sample_papers/
│
├── outputs/
│   └── generated_summaries/
│
└── README.md
