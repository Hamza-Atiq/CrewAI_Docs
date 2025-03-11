#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from tasks_with_direct_configuration.crew import crew, reporting_task

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Cyber Security',
        'current_year': str(datetime.now().year)
    }
    
    try:
        crew.kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def kickoff():

    run()
    task_output = reporting_task.output
    print(f"Task Description: {task_output.description}")
    print(f"Task Summary: {task_output.summary}")
    print(f"Raw Output: {task_output.raw}")
    if task_output.json_dict:
        print(f"JSON Output: {json.dumps(task_output.json_dict, indent=2)}")
    if task_output.pydantic:
        print(f"Pydantic Output: {task_output.pydantic}")