# Self-Healing ETL Pipeline

## Overview

This project shows a self-healing ETL pipeline that uses agentic AI powered by LLMs. The pipeline is designed to autonomously detect, diagnose, and fix runtime errors—such as broken SQL queries and schema mismatches—by analyzing error logs and rewriting code dynamically.

The goal is to reduce manual debugging and improve the reliability of data workflows using automation.

---

## Features

- Executes a simple ETL job with intentionally introduced errors to simulate failure scenarios.
- Captures and logs runtime errors during ETL execution.
- Uses an LLM-based agent to analyze error logs and generate fixes.
- Automatically updates the ETL script and retries execution.
- Demonstrates the potential of agentic automation in data engineering pipelines.

---

## Project Structure

- `main.py`: Orchestrates ETL execution, error handling, and AI-driven remediation loop.  
- `etl_job.py`: Contains the ETL logic with a sample faulty SQL query.  
- `agent.py`: Interfaces with OpenAI’s GPT-4 API to analyze logs and generate code fixes.  
- `utils.py`: Provides helper functions for error logging.  
- `log.txt`: Stores error logs generated during pipeline runs.  

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- OpenAI API key (https://platform.openai.com/signup)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/self-healing-etl.git
    cd self-healing-etl
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY="your_api_key_here"  # On Windows: set OPENAI_API_KEY=your_api_key_here
    ```

### Running the Pipeline

Run the pipeline with:
```bash
python main.py
