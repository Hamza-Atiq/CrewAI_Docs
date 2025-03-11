from crewai import Agent, Crew, Process, Task
	
researcher_agent = Agent(
	role = "{topic} Senior Data Researcher",
	goal = "Uncover cutting-edge developments in {topic}",
	backstory = """
	You're a seasoned researcher with a knack for uncovering the latest
	developments in {topic}. Known for your ability to find the most relevant
	information and present it in a clear and concise manner.""",
	verbose=True
)

reporting_analyst_agent = Agent(
	role = "{topic} Reporting Analyst",
	goal = "Create detailed reports based on {topic} data analysis and research findings",
	backstory = """
	ou're a meticulous analyst with a keen eye for detail. You're known for
	your ability to turn complex data into clear and concise reports, making
	it easy for others to understand and act on the information you provide.""",
	verbose=True
)

research_task = Task(
	description = """
	Conduct a thorough research about {topic}
	Make sure you find any interesting and relevant information given
	the current year is {current_year}.""",
	expected_output = "A list with 2 bullet points of the most relevant information about {topic}",
	agent = researcher_agent
)

reporting_task = Task(
	description = """
	Review the context you got and expand each topic into a full section for a report
	Make sure the report is detailed and contains any and all relevant information.""",
	expected_output = """
	A fully fledged report with the main topics, each with a full section of information.
	Formatted as markdown without '```' """,
	agent = reporting_analyst_agent,
	context = [research_task],  # This task will wait for research_task to complete
	output_file='report.md'
)

crew = Crew(
	agents=[
		researcher_agent,
		reporting_analyst_agent
	], 
	tasks=[
		research_task,
		reporting_task
	],
	process=Process.sequential,
	verbose=True,
			
)
