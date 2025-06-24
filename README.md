# 🧠 AtlasAI RAG Pipeline Showcase

A modular and advanced suite of Jupyter Notebooks demonstrating real-world Retrieval-Augmented Generation (RAG) strategies — from optimization and deployment to hybrid retrieval and CI/CD integration. Built to reflect robust engineering and architectural awareness for AI-driven infrastructure, this showcase addresses performance bottlenecks, model limitations, and real deployment scenarios.

> 📌 Prepared for AtlasAI Interview – by Robert Graham

---

## 🔍 Overview

This repository provides a comprehensive exploration of:

- ✅ **Chunking strategies** to eliminate trimming and reduce latency
- ✅ **Hybrid search integration** using FAISS, BM25, and LlamaIndex
- ✅ **LangChain pipelines** for modular orchestration
- ✅ **Azure & Docker deployment** including AKS + Helm
- ✅ **Frontend integration** with .NET Blazor
- ✅ **CI/CD with Azure DevOps** for reproducible infra
- ✅ Infra-aware design targeting GPT-4o, o3-mini, and throughput constraints

---

## 🔗 Notebook Showcase

### Optimization
- [RAG Pipeline Optimization](notebooks/optimization/RAG_Pipeline_Optimization.ipynb)
- [Creative RAG Optimization](notebooks/optimization/Creative_RAG_Optimization.ipynb)
- [Advanced RAG Strategies](notebooks/optimization/Advanced_RAG_Strategies.ipynb)

### Integration
- [LangChain ＋ LlamaIndex](notebooks/integration/LangChain_LlamaIndex_RAG_Integration.ipynb)
- [Hybrid BM25 ＋ Vector](notebooks/integration/Hybrid_BM25_Vector_RAG_Integration.ipynb)
- [FAISS Vector Search](notebooks/integration/FAISS_VectorDB_RAG_Integration.ipynb)

### Deployment
- [Docker Deployment](notebooks/deployment/Docker_RAG_Deployment_Notebook.ipynb)
- [Helm / AKS Deployment](notebooks/deployment/Helm_AKS_RAG_Deployment_Notebook.ipynb)

### Frontend
- [.NET Blazor Frontend](notebooks/frontend/RAG_Blazor_Frontend_Notebook.ipynb)

### CI / CD
- [Azure DevOps Pipeline](notebooks/cicd/AzureDevOps_RAG_CICD_Notebook.ipynb)

### .NET Hybrid
- [Hybrid RAG (.NET ＋ OpenAI)](notebooks/dotnet/Hybrid_RAG_DotNet_OpenAI.ipynb)

---

## 📂 Repository Structure

```bash
📦 atlasai-rag-pipeline-showcase/
├── notebooks/
│   ├── optimization/                # RAG performance tuning
│   ├── integration/                # Hybrid search and orchestration
│   ├── deployment/                 # Docker + AKS + Helm
│   ├── frontend/                   # .NET Blazor UI integration
│   ├── cicd/                       # Azure DevOps CI/CD automation
│   └── dotnet/                     # .NET-centric OpenAI integration
├── docs/                           # Design rationale and bottleneck notes
├── assets/                         # (optional) Diagrams, screenshots, visuals
├── environment.yml                 # Reproducible environment for all notebooks
└── README.md                       # You're here


GitHub: @r-aaron-graham
HuggingFace: raarongraham
LinkedIn: r-aaron-graham 
