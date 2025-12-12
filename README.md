# 🛡️ FinGuard: Secure Fraud Detection RAG

**Privacy-First Financial Forensics Powered by CyborgDB**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Vector_DB-CyborgDB_Encrypted-red?logo=lock\&logoColor=white)](https://cyborgdb.ai/)
[![AI](https://img.shields.io/badge/LangChain-RAG-orange?logo=chainlink\&logoColor=white)](https://www.langchain.com/)
[![Security](https://img.shields.io/badge/Data-AES_256-green?logo=security\&logoColor=white)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **FinGuard** is a secure **Retrieval-Augmented Generation (RAG)** pipeline designed to detect anomalies and flag potential fraud in sensitive financial documents.
>
> Financial data demands absolute privacy. Unlike standard RAG implementations, FinGuard leverages **CyborgDB** to ensure that all transaction embeddings are **encrypted at rest and in transit**. We enable AI-driven insights without ever exposing raw financial vectors to plain-text vulnerabilities.

---

## 📸 Demo & Dashboard

### 📉 Fraud Analysis Dashboard

![Fraud Detection UI](./static/ui_screenshot.png)
*Real-time analysis of transaction logs with risk scoring, powered by secure RAG retrieval.*

### 🎥 Watch the System in Action

[![Watch the Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)
*Click the thumbnail above to see the Encrypted Fraud Detection pipeline flow.*

---

## 🔒 The Encrypted Architecture (ML Flow)

We utilize **CyborgDB** to maintain a "Zero-Trust" architecture for vector storage.

```mermaid
graph TD
    subgraph "Secure Ingestion"
        A[Financial Logs / PDFs] -->|Anonymize & Chunk| B(Preprocessing)
        B -->|Generate Embeddings| C[Hugging Face Transformer]
        C -->|Encrypt & Store| D[(CyborgDB Encrypted Cloud)]
    end

    subgraph "Forensic Inference"
        E[Investigator Query] -->|Embed Query| F[Hugging Face Transformer]
        F -->|Encrypted Similarity Search| D
        D -->|Retrieve Decrypted Context| G[Transaction Context]
        G -->|Combine with Risk Prompt| H[LLM Chain]
        H -->|Generate Risk Report| I[Analyst Dashboard]
    end

    style D fill:#ffcccc,stroke:#ff0000,stroke-width:2px,stroke-dasharray: 5 5
    style I fill:#bbf,stroke:#333,stroke-width:2px
```

---

## 📊 Security & Performance Benchmarks

In financial contexts, speed matters, but security is non-negotiable. We benchmarked the impact of CyborgDB's encryption on retrieval latency.  
Click here to view the full interactive `benchmark.html` report.

![Security & Performance Benchmarks](./static/benchmark.png)


---

## 🚀 Key Features

* **CyborgDB Integration**: Industry-first encrypted vector search. Even if the database is compromised, the vectors remain unreadable.
* **Context-Aware Forensics**: Queries like `"Show me transactions over $10k sent to offshore accounts"` retrieve exact matches from the encrypted index.
* **Hybrid Analysis**: Combines semantic search (RAG) with rule-based filtering for maximum fraud detection coverage.
* **Persistent Secure Indexing**: Ingest terabytes of logs once; query securely forever.

---

## 🛠️ Tech Stack

**Component — Technologies**

* Vector Database — CyborgDB (Encrypted Storage)
* Orchestration — LangChain, Python
* Embeddings — Hugging Face (all-MiniLM-L6-v2)
* Web Interface — Streamlit / Flask (adjust as per your code)
* Data Processing — Pandas, NumPy

---

## 🏗️ Deployment & Setup

### Prerequisites

* Python 3.10+
* CyborgDB API Key (Required for encrypted storage)
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/FinGuard.git
cd FinGuard
```

### 2. Set up Virtual Environment

```bash
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
.\venv\Scripts\Activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file. You must provide CyborgDB credentials to enable the encrypted layer.

```env
# CyborgDB Config (Crucial)
CYBORGDB_API_KEY=your_cyborg_api_key
CYBORGDB_URL=your_cyborg_instance_url

# AI Models
HUGGINGFACEHUB_ACCESS_TOKEN=hf_your_token_here
OPENAI_API_KEY=sk-optional-if-using-gpt
```

### 5. Run the Application

Run the Ingestion Pipeline (Index Data):

```bash
python ingestion.py
```

Launch the Dashboard:

```bash
python app.py
```

---

## 📂 Project Structure

```
FinGuard/
├── static/              # Assets & Screenshots
├── templates/           # Web Templates
├── app.py               # Main Application Logic
├── ingestion.py         # Script to encrypt & upload docs to CyborgDB
├── benchmark.py         # Latency & Accuracy Testing
├── benchmark.html       # Generated Report
├── utils/               # Helper functions for RAG
├── .env                 # Secrets (Never commit this)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 🔮 Future Scope

* [ ] Real-time Stream Processing: Hooking into Kafka for live transaction monitoring.
* [ ] Graph RAG: Using Knowledge Graphs to detect syndicate fraud rings.
* [ ] Multi-Modal Support: Scanning scanned checks and invoices (OCR).

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---
