# AI_DEV_AGENT
AI-powered Python development agent that generates project structures, files, and code using Gemini AI with structured execution and safer automation workflows.

# AI Development Agent

An AI-powered Python development agent that takes user project requirements, generates development steps using Gemini AI, and automatically creates project files and folders.

---

## Features

- AI-generated project structure
- Dynamic file and folder creation
- Gemini AI integration
- JSON-based structured actions
- Cross-platform support
- Safer architecture than shell-only execution
- Interactive terminal execution flow

---

## Tech Stack

- Python
- Gemini API
- JSON-based AI planning
- File system automation

---

## Project Structure

```bash
ai_dev_agent/
│
├── main.py
├── agent.py
├── file_manager.py
├── prompts.py
├── validator.py
├── executor.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd ai_dev_agent
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv myenv
source myenv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Get API key from:

https://aistudio.google.com

---

## Run Project

```bash
python main.py
```

---

## Example Input

```text
Create a portfolio website using HTML CSS and JavaScript
```

---

## Example Flow

```text
User Input
   ↓
Gemini AI Generates Steps
   ↓
Python Executes Structured Actions
   ↓
Files & Folders Created
```

---

## Future Improvements

- AI debugging
- Code editing
- Docker sandboxing
- GitHub integration
- Automatic dependency installation
- Multi-agent architecture
- Project templates
- Error recovery system

---

## Security Notes

This project includes:
- basic validation
- safer structured actions
- controlled file generation

Avoid running unrestricted shell commands directly from AI output.

---

## Author

Yogesh Kumbhakarn

Backend Developer | Python Developer | Django & DRF Developer