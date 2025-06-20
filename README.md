![Ask Omar](./images/omar_banner.png)

Omar is your AI-powered spiritual companion. A serene guide who listens deeply and connects you to the most relevant wisdom through specialized agents.
Whether you seek biblical understanding, philosophical musings, or gentle moral reflection,
Preacher channels the right voice for your soul's question.

## ✨ Who is Omar?

Omar is a multi-agent AI assistant built using [Google ADK](https://google.github.io/adk-docs/).
At its core is a "root" agent (Omar) who delegates questions to domain-specific subagents:

- `christian_agent`: for Christian scripture and theology
- `muslim_agent`: for Islamic teachings and interpretations
- `philosopher_agent`: for global philosophical traditions
- `general_agent`: for universal or ambiguous spiritual queries

Each subagent is designed with care, clarity, and empathy to ensure thoughtful, nuanced responses.

## 🧠 How It Works

When a user submits a question, Omar:

1. Analyzes the intent and context
2. Selects the most appropriate subagent
3. Transfers the question to the subagent
4. Returns the subagent's answer (seamlessly)

The user sees only one trusted voice, even though a community of agents is working behind the scenes.

## 💻 Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) 3.10+
- [uv](https://github.com/astral-sh/uv) (optional, for dependency management)
- [Openai API key](https://platform.openai.com/api-keys)

### Setup

#### Development 👷🏽

> Clone the repository and enter the project folder

```bash
git clone https://github.com/clovisphere/preacher.git
cd preacher
```

> Install project dependencies:

```bash
uv sync --frozen           # Update the project's environment
source .venv/bin/activate  # Activate the virtual environment
```

> Run the Chat

```bash
make
```

#####  🛠️ Developer Commands

```bash
make         # Start the interactive CLI
make hooks   # Run pre-commit hooks
make clear   # Clean .pyc, __pycache__, etc.
```

## ✍️ License

This project is licensed under the terms of the **MIT License**. See [MIT License](./LICENSE) for more details.

## 🤍 Contributing

We welcome thoughtful contributors! Add new agents, refine prompts, or improve the CLI experience. All voices are welcome in this house of code.

## 🙏 A Final Word

> Ask, and it will be given to you; seek, and you will find.

Happy seeking, friend.
