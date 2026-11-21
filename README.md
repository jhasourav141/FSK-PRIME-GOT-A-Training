# GOT-A Training Submissions

**Program:** Government Officer Training – Advanced in Artificial Intelligence (GOT-A)
**Institute:** National Institute of Electronics and Information Technology (NIELIT), Delhi Centre – East Campus (Karkardooma), MeitY, Government of India
**Course Instructor:** Anita Mahajan

**Submitted by:** Sourav Kumar Jha, DIA-Garhwa_District_Centre-Jharkhand, National Informatics Centre (NIC)

This repository holds my two submissions for the GOT-A programme. Each project is in its own folder.

| Project | Folder | Deadline | What it covers |
|---------|--------|----------|----------------|
| **Lab Exercises** | [`GOT-A-Lab-Exercises`](./GOT-A-Lab-Exercises) | 23 Nov 2026, 9:00 PM | Five hands-on exercises: Pandas and Excel reporting, OpenCV image blending, AI video prompt engineering, Flipkart review analytics with a word cloud, and a Gradio chatbot |
| **Capstone Case Study** | [`GOT-A-Lab-Case_Study`](./GOT-A-Lab-Case_Study) | 24 Nov 2026, 9:00 PM | "Jan-Samadhan", a citizen grievance assistant: data analysis, ML routing (about 95% accuracy), GenAI with RAG, PII masking and a security risk assessment |

## Quick Start

```bash
py -3.12 -m pip install notebook pandas numpy matplotlib seaborn scikit-learn openpyxl opencv-python wordcloud kagglehub gradio
py -3.12 -m notebook
```

Open any `.ipynb` file inside a project folder and choose **Kernel > Restart Kernel and Run All Cells**. Use Python 3.12, because Python 3.15 is too new for some libraries on Windows.

---

## Table of Contents
1. [Repository Structure](#1-repository-structure)
2. [Project 1: Lab Exercises](#2-project-1-lab-exercises)
3. [Project 2: Capstone Case Study "Jan-Samadhan"](#3-project-2-capstone-case-study-jan-samadhan)
4. [Setup and How to Run](#4-setup-and-how-to-run)
5. [Skills Demonstrated](#5-skills-demonstrated)
6. [Limitations](#6-limitations)
7. [Acknowledgements](#7-acknowledgements)

---

## 1. Repository Structure

```
.
├── README.md                      This document
│
├── GOT-A-Lab-Exercises/           Project 1 (due 23 Nov 2026, 9:00 PM IST)
│   ├── Exercise1_SouravKumarJha.ipynb
│   ├── Exercise2_SouravKumarJha.ipynb
│   ├── Exercise3_SouravKumarJha.ipynb
│   ├── Exercise4_SouravKumarJha.ipynb
│   ├── Exercise5_SouravKumarJha.ipynb
│   ├── Exercise1_output.xlsx
│   ├── image1.jpg, image2.jpg, blended.jpg, comparison.png
│   ├── Exercise3_video.mp4, Exercise3_screenshot.png
│   └── Exercise5_screenshot.png
│
└── GOT-A-Lab-Case_Study/          Project 2 (due 24 Nov 2026, 9:00 PM IST)
    ├── CaseStudy_JanSamadhan_SouravKumarJha.ipynb
    ├── jan_samadhan_grievances.csv
    ├── generate_dataset.py
    ├── insight1_top5_departments.png
    ├── insight2_monthly_trend.png
    ├── confusion_matrix.png
    └── Phase3_RAG_Q1_screenshot.png, Phase3_RAG_Q2_screenshot.png
```

---

## 2. Project 1: Lab Exercises

Five practical laboratory exercises for the final evaluation. Each is a Jupyter Notebook with Markdown notes and comments explaining logic, inputs and outputs.

| # | Exercise | What was done | Output files |
|---|----------|---------------|--------------|
| 1 | **EDA & Automated Reporting (Pandas)** | Created a DataFrame with columns `f1` to `f4` of random values, plotted a scatter plot of `f2` vs `f3`, computed the row-wise mean into `f5`, and exported all five columns to Excel | `Exercise1_output.xlsx` |
| 2 | **Image Blending (OpenCV)** | Loaded two images, resized them to matching dimensions, blended them with `cv2.addWeighted`, and displayed and saved the originals and the result | `blended.jpg`, `comparison.png` |
| 3 | **Prompt Engineering for Video Synthesis** | Chose an AI video tool, wrote a structured prompt for a 3-second video using the three images, and documented the tool, exact prompt, camera and transition instructions in a single Markdown cell | `Exercise3_video.mp4`, `Exercise3_screenshot.png` |
| 4 | **E-Commerce Text & Quantitative Analytics** | Loaded the Flipkart reviews dataset (Kaggle), cleaned the rating and price fields, grouped by product to build the `items` DataFrame (mean rating and mean price), and generated a word cloud from the `Summary` column | Notebook outputs |
| 5 | **Interactive AI Prototyping (Gradio)** | Built and launched a `gr.ChatInterface` chatbot with a title, a welcome description and three sample prompts | `Exercise5_screenshot.png` |

**Dataset note (Exercise 4):** `Dataset-SA.csv` comes from Kaggle (*Flipkart Product Customer Reviews Dataset*) and is not included in the repository because of its size.
**AI video tool used (Exercise 3):** *(add the tool name, for example Google Veo)*

---

## 3. Project 2: Capstone Case Study "Jan-Samadhan"

### Problem
Departments receive thousands of grievances daily on CPGRAMS. Officers manually read, categorise, prioritise and reply to each, causing backlogs. The goal was a proof-of-concept pipeline that combines Machine Learning and Generative AI with RAG to help officers.

### Dataset
A self-created, AI-assisted **500-row sample** (permitted by the brief), generated by `generate_dataset.py` with a fixed random seed. It has structured fields (`Complaint_ID`, `Date`, `State`, `Department`, `Urgency`, `Status`, `Resolution_Days`) and unstructured `Complaint_Text`. It deliberately includes missing values, messy text and fake PII. **All data is fictional.**

### Phase summary

| Phase | Tasks | What was done |
|-------|-------|---------------|
| **1. Data Exploration** | 1.1 to 1.3 | Classified structured vs unstructured columns, filled missing states, dropped rows without text (490 remain), cleaned text, and charted the top 5 departments plus monthly volume with average resolution time |
| **2. Predictive ML** | 2.1 to 2.3 | TF-IDF + Logistic Regression routing model, evaluated with accuracy, classification report and confusion matrix; compared with Random Forest; added an urgency model; explained why a lightweight model suits this prototype |
| **3. GenAI & RAG** | 3.1, 3.2 | C.R.O.S.S system prompt (summary, urgency, polite draft letter); mini-RAG over a fictional pension SOP, tested on Google Gemini |
| **4. Governance & Security** | 4.1, 4.2 | Regex PII masking function (Aadhaar, phone, email, PAN, address) and a risk assessment of prompt injection with a layered mitigation plan |

### Key results

| Model | Accuracy |
|-------|----------|
| Logistic Regression: department routing | **94.9%** |
| Random Forest: department routing (comparison) | 92.9% |
| Logistic Regression: urgency (High / Medium / Low) | 92.9% |

- **PII masking:** the function passed its unit tests and masked PII in 158 of 490 complaints.
- **RAG test (Google Gemini):** the model answered the SOP-covered question correctly (21 working days, Clause 5) and refused the question the SOP does not cover, with the exact fallback sentence instead of inventing a rule.

### Design decisions
- **Logistic Regression over BERT or a deep network:** the sample is small, deep models need far more data and GPUs, and Logistic Regression is fast and explainable, which suits accountability in governance.
- **Complaint text treated as untrusted data** in the prompt, to reduce prompt-injection risk.
- **Human in the loop:** officers review every AI-generated summary, urgency and letter before anything reaches a citizen.

---

## 4. Setup and How to Run

**Requirements:** Python 3.12 and Jupyter Notebook.

```bash
py -3.12 -m pip install notebook pandas numpy matplotlib seaborn scikit-learn openpyxl opencv-python wordcloud kagglehub gradio
py -3.12 -m notebook
```

On Linux or macOS use `python3` in place of `py -3.12`.

1. Open the notebook you want inside its project folder.
2. Choose **Kernel > Restart Kernel and Run All Cells**.
3. Keep data files in the same folder as the notebook.

**Extra notes**
- **Exercise 2:** keep `image1.jpg` and `image2.jpg` beside the notebook.
- **Exercise 4:** download `Dataset-SA.csv` from Kaggle and place it beside the notebook.
- **Exercise 5:** after running the last cell, open the local link it prints (for example `http://127.0.0.1:7860`).
- **Case study:** if the CSV is missing, the notebook regenerates it using `generate_dataset.py`. The Phase 3 AI replies come from pasting the printed prompts into an AI tool.

---

## 5. Skills Demonstrated
- Data analysis and visualisation with Pandas, NumPy, Matplotlib and Seaborn
- Computer vision basics with OpenCV
- Supervised text classification with scikit-learn (TF-IDF, Logistic Regression, Random Forest) and model evaluation
- Prompt engineering (C.R.O.S.S framework) and Retrieval-Augmented Generation
- Building a web interface with Gradio
- AI governance: PII masking, prompt-injection risk assessment and human-in-the-loop design

---

## 6. Limitations
- The case study dataset is small and synthetic; real CPGRAMS data would need retraining and fresh evaluation.
- Regex PII masking misses names and free-form addresses; production use should add Named Entity Recognition and run masking on NIC servers.
- The Gradio chatbot in Exercise 5 is rule-based and meant as a prototype interface.
- Phase 3 LLM outputs were generated outside the notebook and pasted in.
- Future work: multilingual models for Hindi and regional languages, per-language accuracy reporting, and integration with a real SOP document store.

---

## 7. Acknowledgements
Sincere thanks to **Anita Mahajan Madam**, Course Instructor, for her guidance throughout the GOT-A programme.

Exercises and case study prescribed by NIELIT Delhi Centre, Ministry of Electronics and Information Technology (MeitY), Government of India.
