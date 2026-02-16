# 📊 Image Analysis and Improvement Suggestion Module

An AI-inspired image analysis system that evaluates marketing creatives and provides professional improvement suggestions using computer vision, OCR, and optional local LLM integration.

---

## 🚀 Project Overview

This project analyzes marketing images (posters, ads, and digital creatives) to identify design and communication issues and provide actionable improvement suggestions based on digital marketing best practices.

The system supports **local Large Language Model (LLM) integration using Ollama** for AI-powered evaluation, with a **rule-based expert system fallback** for low-resource environments.

---

## 🧠 Key Features

- 📄 Text extraction using OCR (EasyOCR)
- 📈 Image quality analysis (brightness & contrast)
- ✅ Rule-based marketing evaluation engine
- 🤖 Optional AI-powered evaluation using Ollama (local LLM)
- ⚡ FastAPI backend for scalable API handling
- 🎨 Streamlit frontend for interactive UI
- 🆓 Fully offline & free (no paid API dependency)

---

## 🤖 AI / LLM Integration (Ollama)

This project is architected to support **local LLM inference using Ollama**, enabling AI-driven marketing analysis without relying on cloud-based APIs.

### Why Ollama?
- No API keys required
- Runs fully offline
- Ensures data privacy
- Suitable for enterprise and restricted environments
- Cost-effective (100% free)

### Supported Models
- LLaMA family (hardware dependent)
- Gemma (recommended for low-resource systems)

> ⚠️ Due to system memory constraints, the current implementation uses a **rule-based evaluation engine by default**.  
> The architecture is **LLM-ready** and can seamlessly switch to Ollama-based inference when hardware resources permit.

---

## 🏗️ System Architecture

