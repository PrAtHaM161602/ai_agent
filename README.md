

# AI Agent CLI – Automate Your Daily Tasks with Intelligence

**AI Agent CLI** is a powerful command-line tool that acts as your personal assistant. It automates various daily tasks using intelligent agents powered by AI and integrates multiple utilities such as web scraping, searching, voice interaction, task execution, and more — all from your terminal.



## ✨ Features

* ✅ **Natural Language Interface** – Just type what you want it to do
* 🔍 **Web Search & Summarization** – Get concise answers from the web
* 🔗 **Tool Integration** – Connects with tools like `requests`, `BeautifulSoup`, `subprocess`, `OpenAI`, and more
* 🖥️ **Pure CLI** – Lightweight and fast, no GUI overhead

---

### 🧰 Supported Pentesting Features:

* 🔎 **Port Scanning** – Scans target IPs using your favorite tools (e.g., Nmap wrapper or custom scanner)
* 🕷️ **Directory Bruteforcing** – Automatically runs directory enumeration (e.g., via `dirb` or `gobuster`)

### 🧠 Example Commands

```bash
> scan ports on 192.168.1.1
> enumerate directories on http://example.com
> find vulnerabilities in Apache 2.4.49
> passive recon on domain.com
> generate pentest report
```

> ⚠️ **Disclaimer**: This tool is for educational and authorized security testing only. Always obtain permission before scanning any network or domain.

---

## 📦 Requirements

* Python 3.10+
* `pip` packages from `requirements.txt`:

  ```txt
  openai
  langchain
  python-dotenv
  requests
  beautifulsoup4
  pyttsx3
  SpeechRecognition
  pyaudio
  colorama
  ```

You’ll also need some CLI tools installed (optional but enhances functionality):

* `nmap`
* `whois`
* `dig`
* `curl`
* `dirb`, `ffuf`, or `gobuster` (for directory bruteforcing)

---

## 🚀 Installation

```bash
git clone https://github.com/PrAtHaM161602/ai_agent.git
cd ai-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file for your GEMINI API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 🧠 How It Works

This agent uses a combination of:

* **LangChain** to manage agent logic
* **Gemini** for natural language processing
---

## 🛠️ Usage

Run the tool:

```bash
python ai_agent.py
```

Then enter your task, for example:

```bash
> search latest news
> scan ports on example.com
> lookup today's weather
> execute "ls -la"
> say 'Hello, world'
```

---

## 📁 Project Structure

```
ai-agent/
├── agent.py         # Main CLI interface
├── requirements.txt
├── examples
└── .env                # API keys (not included in repo)
```

---


