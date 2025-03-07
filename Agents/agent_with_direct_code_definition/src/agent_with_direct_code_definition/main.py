#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from agent_with_direct_code_definition.crew import AgentWithDirectCodeDefinition

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        AgentWithDirectCodeDefinition().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
def kickoff():
    """
    Run the crew.
    """
    run()


