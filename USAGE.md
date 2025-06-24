# 🚀 Usage Guide: Running the RAG Showcase

This guide will walk you through setting up, exploring, and extending the Retrieval-Augmented Generation (RAG) notebooks provided in this repository.

---

## 🧰 Prerequisites

- Python 3.10+
- Conda (recommended)
- JupyterLab or VSCode
- OpenAI API Key (stored as `OPENAI_API_KEY` in env)

---

## 1️⃣ Setup Instructions

### 🔹 Clone the Repository

```bash
git clone https://github.com/your-username/atlasai-rag-pipeline-showcase.git
cd atlasai-rag-pipeline-showcase

conda env create -f environment.yml
conda activate atlasai-rag-env

OPENAI_API_KEY=your-key-here

jupyter lab

notebooks/00_index.ipynb



