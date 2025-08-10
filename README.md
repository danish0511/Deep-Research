# Deep-Research

**Deep-Research** is an advanced, AI-powered research automation tool designed to streamline the process of gathering, analyzing, and delivering high-quality insights.  
It leverages the power of **OpenAI’s API** along with SDK traces to orchestrate a sequence of intelligent agents—each specialized for a part of the research workflow.

The system operates like a virtual research assistant:  
- It **understands your query**,  
- **Plans a strategy** for retrieving relevant information,  
- **Searches and analyzes** data from multiple sources,  
- **Synthesizes findings** into a well-structured, human-readable report, and  
- **Delivers the results straight to your inbox** via SMTP email.  

The entire application is wrapped in an **interactive Gradio interface**, making it accessible even to non-technical users.  
Whether you need quick background research for a project, competitive analysis, or technical deep-dives—Deep-Research automates the heavy lifting so you can focus on decision-making.

---


## Features

- Fully autonomous AI-driven research pipeline  
- Modular architecture with specialized agents for planning, searching, and writing  
- Real-time interaction through a Gradio web UI  
- SMTP email integration for direct delivery of research results  
- Built on top of OpenAI’s API for high-quality, context-aware content generation  
- Easily extensible to support more agents or custom workflows  

---

## Architecture & Agents

| Component              | Responsibility                                                                 |
|------------------------|--------------------------------------------------------------------------------|
| `deep_research.py`     | Main orchestrator that initializes and runs all agents                        |
| `search_agent.py`      | Handles information gathering from online sources or search APIs              |
| `planner_agent.py`     | Plans and structures the research workflow                                    |
| `writer_agent.py`      | Crafts research outputs using AI-generated insights                            |
| `research_manager.py`  | Manages overall research flow, data storage, and agent coordination            |
| `email_agent.py`       | Sends research deliverables via SMTP to designated recipients                  |

---

## Installation

```
git clone https://github.com/danish0511/Deep-Research.git
cd Deep-Research
uv init
uv pip install -r requirements.txt
uv run deep_research.py
```

Environment Variables:
```
OPENAI_API_KEY="your_openai_api_key"
GMAIL_APP_PASSWORD="your_email_app_password"
```
