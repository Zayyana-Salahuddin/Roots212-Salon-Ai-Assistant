# Roots212-Salon-Ai-Assistant
AI-powered Hair Salon Assistant built with Streamlit, Groq Llama 3.1, Sentence Transformers, and FAISS. Provides intelligent responses about salon services, pricing, appointments, and business information using Retrieval-Augmented Generation (RAG).

# Roots212 Salon AI Assistant

An AI-powered Hair Salon Assistant built using Streamlit, Groq Llama 3.1, Sentence Transformers, and FAISS. The assistant provides intelligent responses about salon services, pricing, appointments, treatments, and business information through Retrieval-Augmented Generation (RAG).

## Overview

Roots212 Salon AI Assistant is designed to improve customer experience by providing instant, AI-powered assistance for salon-related inquiries. The application leverages semantic search and large language models to retrieve relevant salon information and generate accurate, context-aware responses.

## Features

* AI-powered salon assistant
* Retrieval-Augmented Generation (RAG)
* Semantic search using Sentence Transformers
* FAISS vector database for fast information retrieval
* Groq Llama 3.1 integration
* Interactive Streamlit user interface
* Multi-chat session support
* Appointment and service information assistance
* Business information and customer support chatbot

## Technology Stack

* Python
* Streamlit
* Groq API
* Llama 3.1
* Sentence Transformers
* FAISS
* NumPy
* Python Dotenv

## Project Structure

```text
Roots212-Salon-AI-Assistant/
│
├── root.py
├── salon_data.json
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── roots.jpeg
```

## How It Works

1. User submits a question through the Streamlit interface.
2. The query is converted into vector embeddings using Sentence Transformers.
3. FAISS performs similarity search on the salon knowledge base.
4. Relevant salon information is retrieved.
5. Retrieved context is sent to Groq Llama 3.1.
6. The model generates an accurate response based on the salon data.
7. The answer is displayed in the chat interface.

## Architecture

```text
User Query
     │
     ▼
Sentence Transformer
     │
     ▼
Vector Embedding
     │
     ▼
FAISS Similarity Search
     │
     ▼
Relevant Salon Context
     │
     ▼
Groq Llama 3.1
     │
     ▼
AI Response
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Roots212-Salon-AI-Assistant.git
```

### Navigate to the Project Directory

```bash
cd Roots212-Salon-AI-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Run the Application

```bash
streamlit run root.py
```

## Requirements

```txt
streamlit
groq
python-dotenv
sentence-transformers
faiss-cpu
numpy
```

## Use Cases

* Salon customer support
* Appointment assistance
* Service and pricing inquiries
* Hair treatment recommendations
* Business information retrieval
* AI-powered salon knowledge base

## Future Enhancements

* Voice assistant integration
* WhatsApp integration
* Online appointment scheduling
* Customer profile management
* Analytics dashboard
* Multi-language support
* Cloud deployment support

## Security Notes

* Do not upload your `.env` file.
* Keep API keys private.
* Use `.env.example` for configuration sharing.
* Rotate API keys if they are ever exposed publicly.

## Developer

Zayyana Salahuddin

Email: [zayy.salahuddin@gmail.com](mailto:zayy.salahuddin@gmail.com)

LinkedIn: https://www.linkedin.com/in/zayyana-salahuddin-725b242b3/

Developed and maintained the Roots212 Salon AI Assistant using Streamlit, Groq Llama 3.1, Sentence Transformers, and FAISS-based Retrieval-Augmented Generation (RAG).

## License

This project is licensed under the MIT License.

## Acknowledgments

* Streamlit
* Groq
* Meta Llama
* Sentence Transformers
* FAISS

Built to enhance the digital customer experience for Roots212 Hair Salon through Artificial Intelligence and Retrieval-Augmented Generation (RAG).
