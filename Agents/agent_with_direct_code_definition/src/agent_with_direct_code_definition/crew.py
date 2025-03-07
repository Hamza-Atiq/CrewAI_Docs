from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class AgentWithDirectCodeDefinition():
	"""AgentWithDirectCodeDefinition crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			role = "{topic} Senior Data Researcher",
			goal = "Uncover cutting-edge developments in {topic}",
			backstory = """
			You're a seasoned researcher with a knack for uncovering the latest
			developments in {topic}. Known for your ability to find the most relevant
			information and present it in a clear and concise manner.""",
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			role = "{topic} Reporting Analyst",
			goal = "Create detailed reports based on {topic} data analysis and research findings",
			backstory = """
			ou're a meticulous analyst with a keen eye for detail. You're known for
			your ability to turn complex data into clear and concise reports, making
			it easy for others to understand and act on the information you provide.""",
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			description = """
			Conduct a thorough research about {topic}
			Make sure you find any interesting and relevant information given
			the current year is {current_year}.""",
			expected_output = "A list with 10 bullet points of the most relevant information about {topic}",
			agent = self.researcher()
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			description = """
			Review the context you got and expand each topic into a full section for a report
			Make sure the report is detailed and contains any and all relevant information.""",
			expected_output = """
			A fully fledged report with the main topics, each with a full section of information.
			Formatted as markdown without '```' """,
			agent = self.reporting_analyst(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AgentWithDirectCodeDefinition crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
