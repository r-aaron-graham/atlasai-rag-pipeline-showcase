# 🧠 AtlasAI RAG Pipeline Showcase

A modular and advanced suite of Jupyter Notebooks demonstrating real-world Retrieval-Augmented Generation (RAG) strategies — from optimization and deployment to hybrid retrieval and CI/CD integration.

> 📌 Prepared for AtlasAI Interview  
> 👤 Author: **Robert Graham**  
> 📨 [GitHub](https://github.com/r-aaron-graham) | [LinkedIn](https://linkedin.com/in/r-aaron-graham) | [HuggingFace](https://huggingface.co/raarongraham)

---

## 🔍 Overview

This repository provides a comprehensive exploration of:

- ✅ **Chunking strategies** to eliminate trimming and reduce latency  
- ✅ **Hybrid search integration** using FAISS, BM25, and LlamaIndex  
- ✅ **LangChain pipelines** for modular orchestration  
- ✅ **Azure & Docker deployment** including AKS + Helm  
- ✅ **Frontend integration** with .NET Blazor  
- ✅ **CI/CD with Azure DevOps** for reproducible infra  
- ✅ **Infra-aware design** targeting GPT-4o, o3-mini, and throughput constraints

---

## 📘 Notebook Showcase

### 📂 Index Notebook
- [Notebook Index](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/notebooks/00_index.ipynb)

### 🔧 Optimization
- [RAG Pipeline Optimization](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/optimization/RAG_Pipeline_Optimization.ipynb)
- [Creative RAG Optimization](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/optimization/Creative_RAG_Optimization.ipynb)
- [Advanced RAG Strategies](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/optimization/Advanced_RAG_Strategies.ipynb)

### 🔌 Integration
- [LangChain + LlamaIndex]([https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/integration/LangChain_LlamaIndex_RAG_Integration.ipynb](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/notebooks/integration/LangChain_LlamaIndex_RAG_Integration.ipynb))
- [Hybrid BM25 + Vector](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/integration/Hybrid_BM25_Vector_RAG_Integration.ipynb)
- [FAISS Vector Search](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/integration/FAISS_VectorDB_RAG_Integration.ipynb)

### 🚀 Deployment
- [Docker Deployment](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/deployment/Docker_RAG_Deployment_Notebook.ipynb)
- [Helm / AKS Deployment](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/deployment/Helm_AKS_RAG_Deployment_Notebook.ipynb)

### 💻 Frontend
- [.NET Blazor Frontend](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/frontend/RAG_Blazor_Frontend_Notebook.ipynb)

### 🔁 CI / CD
- [Azure DevOps Pipeline](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/cicd/AzureDevOps_RAG_CICD_Notebook.ipynb)

### 🧬 .NET Hybrid
- [Hybrid RAG (.NET + OpenAI)](https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/dotnet/Hybrid_RAG_DotNet_OpenAI.ipynb)

---

## 🛠️ Environment Setup

To install all dependencies:

```bash
conda env create -f environment.yml
conda activate atlasai-rag-env
jupyter lab
```

---

## ⚠️ Troubleshooting Notebook Links

If you encounter 404 errors when accessing notebooks, ensure you are using the correct paths:

- **Notebooks are located in top-level folders**, not under `notebooks/` except for the index.
- All links above use the correct case and directory structure.
- Check that you are on the `main` branch or adjust links if using a different branch.

**Example of a correct URL:**

```
https://github.com/r-aaron-graham/atlasai-rag-pipeline-showcase/blob/main/optimization/RAG_Pipeline_Optimization.ipynb
```

If you continue to experience issues, please verify that the files exist in the remote repository and that your local changes have been committed and pushed.
