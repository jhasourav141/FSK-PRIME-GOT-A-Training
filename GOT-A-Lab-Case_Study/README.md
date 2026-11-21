# Jan-Samadhan: Smart Citizen Grievance Redressal & Policy Assistant

**Capstone Case Study | GOT-A Programme (Government Officer Training – Advanced in AI), NIELIT Delhi Centre**
**Submitted by:** Sourav Kumar Jha, NIC
**Submission deadline:** 24 November 2026, 9:00 PM

## Overview

Government departments receive thousands of citizen grievances every day on CPGRAMS. Officers read, categorise, prioritise and reply to each one by hand, which creates backlogs and delays.

**Jan-Samadhan** is a proof-of-concept pipeline built as an NIC AI Taskforce member. It:

1. explores and cleans historical grievance data,
2. uses Machine Learning to route each complaint to the right department and estimate its urgency,
3. uses Generative AI with Retrieval-Augmented Generation (RAG) to help officers draft accurate, empathetic and policy-compliant replies, and
4. adds privacy and security safeguards (PII masking and a prompt-injection risk assessment).

## Repository Contents

| File | Description |
|------|-------------|
| `CaseStudy_JanSamadhan_SouravKumarJha.ipynb` | Main notebook containing all four phases, code, outputs and written explanations |
| `jan_samadhan_grievances.csv` | 500-row sample dataset used in the notebook |
| `generate_dataset.py` | Script that created the sample dataset (reproducible, fixed random seed) |
| `insight1_top5_departments.png` | Chart: top 5 departments by complaints |
| `insight2_monthly_trend.png` | Chart: monthly volume and average resolution time |
| `confusion_matrix.png` | Confusion matrix of the routing model |

## Dataset

A self-created, AI-assisted **500-row sample** of CPGRAMS-style grievances, as permitted in the case study brief. It has structured fields (`Complaint_ID`, `Date`, `State`, `Department`, `Urgency`, `Status`, `Resolution_Days`) and one unstructured field (`Complaint_Text`). It deliberately includes missing values, messy text, and fake PII (phone numbers, Aadhaar-like numbers, emails, addresses). **All data is fictional**; no real citizen information is used.

## Work Done, Phase by Phase

### Phase 1: Data Exploration & Visualization
- Loaded the data with Pandas and classified columns as structured or unstructured.
- Filled missing states with "Unknown", dropped rows with no complaint text (10 rows, leaving 490), and cleaned the text (lowercase, special characters, digits and extra spaces removed).
- Produced two visual insights: top 5 departments by complaint count, and monthly complaint volume with average resolution time.

### Phase 2: Predictive ML Modeling
- Built a **TF-IDF + Logistic Regression** text classifier to route complaints to a department.
- Evaluation on a held-out 20% test set:

| Model | Accuracy |
|-------|----------|
| Logistic Regression (department routing) | **94.9%** |
| Random Forest (comparison) | 92.9% |
| Logistic Regression (urgency: High / Medium / Low) | 92.9% |

- Included a classification report and confusion matrix, and tested the model on new complaints.
- **Why not a deep neural network or BERT?** The dataset is small, deep models need far more data and GPUs, Logistic Regression trains in seconds and is explainable to officers. Details are in the notebook.

### Phase 3: GenAI & RAG-Based Officer Co-Pilot
- **Prompt engineering (C.R.O.S.S framework):** a structured system prompt that makes an LLM read an angry complaint and return a neutral 2-sentence summary, a High/Medium/Low urgency rating with a reason, and a polite draft acknowledgment letter. The prompt treats complaint text as untrusted data.
- **Mini-RAG (optional task):** a fictional pension SOP is split into clauses, the relevant clauses are retrieved with TF-IDF similarity, and the LLM is instructed to answer **only** from them or say the information is not available. This reduces hallucination.
- LLM tool used for testing: *(add tool name, for example ChatGPT / Gemini / Claude)*

### Phase 4: Governance, Ethics & Security Audit
- **PII masking:** a regex-based function masks Aadhaar numbers, phone numbers, emails, PAN and simple addresses before text goes to any external AI API. It passed its unit tests and masked PII in 158 of 490 complaints.
- **Risk assessment:** identified **prompt injection inside a complaint** as the main adversarial risk and proposed a layered NIC mitigation strategy (untrusted-data prompting, input screening, least privilege, human-in-the-loop review, output validation, red-teaming). Regional-language bias is noted as a secondary risk.

## How to Run

**Requirements:** Python 3.12 and Jupyter Notebook.

```bash
py -3.12 -m pip install notebook pandas numpy matplotlib seaborn scikit-learn
py -3.12 -m notebook
```

Open `CaseStudy_JanSamadhan_SouravKumarJha.ipynb` and choose **Kernel > Restart Kernel and Run All Cells**. Keep the CSV and `generate_dataset.py` in the same folder as the notebook. If the CSV is missing, the notebook regenerates it automatically.

On Linux or macOS, use `python3` instead of `py -3.12`.

## Limitations and Next Steps
- The sample is small and synthetic, so results on real CPGRAMS data would need retraining and fresh evaluation.
- Regex PII masking misses names and free-form addresses; production use should add a Named Entity Recognition model and run masking on NIC servers.
- The LLM outputs in Phase 3 are generated outside the notebook by pasting the prompts into an AI tool.
- Future work: multilingual models for Hindi and regional languages, per-language accuracy reporting, and integration with a real SOP document store.

## Acknowledgements
Case study prescribed by the NIELIT Delhi Centre, Ministry of Electronics and Information Technology (MeitY), Government of India.
