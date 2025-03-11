from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import Dict, Tuple, Union, Any

@CrewBase
class TaskGuardrails():
	"""TaskGuardrails crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def validate_blog_content(self, result : str) -> Tuple[bool, Any]:
		"""Validates the blog content meets requirements"""

		try:
			blog = result.raw if hasattr(result, "raw") else result
			word_count = len(blog.split())
			if word_count < 200:
				return (False, f"Blog content is too short: only {word_count} words")
			elif word_count > 500:
				return (False, f"Blog content is too long: {word_count} words")
			else:
				return (True, blog.strip())
		except Exception as e:
				return (False, f"Unexpected error during validation: {e}")

	@agent
	def blog_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['blog_writer'],
			verbose=True
		)

	@task
	def blogger_task(self) -> Task:
		return Task(
			config=self.tasks_config['blogger_task'],
			agent = self.blog_writer(),
			verbose=True,
			guardrail=self.validate_blog_content,
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TaskGuardrails crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
