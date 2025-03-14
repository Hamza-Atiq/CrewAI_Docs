# TasksWithDirectConfiguration Crew

Welcome to the TasksWithDirectConfiguration Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
or
```bash
uv add crewai
```
### Customizing

**Add your `OPENAI_API_KEY` or `GEMINI_API_KEY` or any other with `MODEL` into the `.env` file**

- Modify `src/agents_with_yaml_configuration/crew.py` to add your own logic, tools, define your agents and tasks and specific args
- Modify `src/agents_with_yaml_configuration/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
uv run run_crew
```

This command initializes the Agents_with_yaml_configuration Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.
