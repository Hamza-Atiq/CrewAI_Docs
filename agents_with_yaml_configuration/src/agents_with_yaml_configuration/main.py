import sys
import warnings

from datetime import datetime

from agents_with_yaml_configuration.crew import AgentsWithYamlConfiguration

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs AgenticAI',
        'current_year': str(datetime.now().year)
    }
    
    try:
        AgentsWithYamlConfiguration().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def kickoff():
    """
    Kickoff the crew.
    """
    run()
