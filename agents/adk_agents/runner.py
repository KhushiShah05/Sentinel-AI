from google.adk.runners import Runner

from agents.adk_agents.root_agent import root_agent


class ADKRunner:

    def __init__(self):

        self.runner = Runner(
            agent=root_agent
        )

    async def run(self, message):

        response = await self.runner.run(
            user_input=message
        )

        return response