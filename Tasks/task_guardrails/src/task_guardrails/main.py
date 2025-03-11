#!/usr/bin/env python
import sys
import warnings

from task_guardrails.crew import TaskGuardrails

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Retrieval-based Chatbots',
        'word_count': str(300)
    }
    
    try:
        TaskGuardrails().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def kickoff():
    """
    Run the crew.
    """
    run()