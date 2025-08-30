import asyncio
from collections.abc import AsyncGenerator

from acp_sdk.models import Message
from acp_sdk.server import Context, RunYield, RunYieldResume, Server

server = Server()


@server.agent()
async def echo(
    input: list[Message], context: Context
) -> AsyncGenerator[RunYield, RunYieldResume]:
    """Echoes everything"""
    for message in input:
        await asyncio.sleep(0.5)
        yield {"thought": "I should echo everything"}
        await asyncio.sleep(0.5)
        yield message

        # TODO: Implement the reverse echo functionality here
        # Hint: You'll need to:
        # 1. Extract the content from the message
        # 2. Reverse it
        # 3. Create a new message with the reversed content
        # 4. Yield the new message


server.run()
