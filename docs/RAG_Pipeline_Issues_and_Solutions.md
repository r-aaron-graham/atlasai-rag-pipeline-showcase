# 🧠 RAG Pipeline Issues & Solutions

This document outlines core challenges and strategic improvements to Retrieval-Augmented Generation (RAG) pipelines at scale. It addresses both architectural bottlenecks and infrastructure constraints, offering actionable revisions for AtlasAI-style production systems.

---

## ⚠️ Identified Issues

### 1. Trimming Step Bottleneck

The trimming step exists to reduce input size before hitting the LLM, but:

- It uses a **per-page partitioning** strategy, often creating oversized chunks (~1700+ tokens).
- `.docx` files don’t contain reliable page boundaries — chunking by page is fundamentally flawed.
- Mini models (e.g., `o3-mini`) struggle to trim meaningfully in large chunks.
- Inconsistent trimming leads to missing references (e.g., referencing X at start/mid/end but returning only 2/3).

> ⚡ **Impact**: Reduces retrieval precision, slows throughput, and overburdens infra.

---

## 🔥 Infra Constraints

### Infrastructure Throughput Limits

- GPT-4o supports ~60x more tokens than o3-mini.
- Because **trimming happens on o3-mini**, that becomes the **actual throughput ceiling**.
- Current token quota distribution prevents full use of higher-capacity models.
- EA quotas and subscription load-balancing could help — but the trimming step is still the bottleneck.

---

## ✅ Proposed Pipeline Solutions

### 1. Replace Trimming with Smarter Chunking

#### 📏 Chunk Size

- Target **~250 tokens per chunk** for optimal balance.
- Avoid going above 1024 tokens (Top-K retrieval degrades, citations break).

#### 🔁 Rehydration Strategy

- Retrieve **adjacent chunks** along with top hits.
- Optional: Select based on retrieval score.

#### 🧠 Context-Aware Chunking

- Chunk using semantic divisions:
  - Use `.docx` metadata and paragraph tags.
  - Avoid cutting off mid-thought.
- Very small paragraphs should be merged to hit minimum thresholds.
- Very large paragraphs should be split **at sentence boundaries** using lightweight LLMs or rule-based splitting.

#### 🔤 Format-Aware Grouping

- Use Word metadata or OCR where possible to distinguish visual blocks.
- Avoid naïve line-based chunking (e.g., splitting “V.” from its content in legal docs).

---

## 🧩 Citations Format Fix

- Current syntax: `!@{ 'id': '1' }@!` is too complex.
- Recommend switching to simpler LLM-friendly tag:  
  Example: `<AtlasSource id=1>`

---

## 🏗 Infra Strategy Recommendations

- Offload trimming entirely by improving chunking quality upstream.
- Use EA capacity for GPT-4o as main retrieval and response engine.
- Minimize token usage by reducing average chunk payload.
- Consider **load balancing** across model subscriptions if scale requires.

---

## ✅ Summary Recommendations

| Challenge         | Fix |
|------------------|-----|
| Trimming overload | Replace with 250-token chunks |
| Mid-thought splits | Context-aware semantic chunking |
| Mini model limits | Offload to GPT-4o and chunk rehydration |
| Overhead citation syntax | Switch to `<AtlasSource id=X>` |
| PDF/Docx splitting | Use paragraph detection & metadata |
