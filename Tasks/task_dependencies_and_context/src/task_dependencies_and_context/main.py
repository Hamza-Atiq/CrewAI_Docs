#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from task_dependencies_and_context.crew import crew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Bit Coin',
        'current_year': str(datetime.now().year)
    }
    
    try:
        crew.kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def kickoff():  

    run()