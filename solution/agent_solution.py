import asyncio
from collections.abc import AsyncGenerator

from acp_sdk.models import Message, MessagePart
from acp_sdk.server import Context, RunYield, RunYieldResume, Server

server = Server()


@server.agent()
async def echo(
    input: list[Message], context: Context
) -> AsyncGenerator[RunYield, RunYieldResume]:
    """Echoes everything and returns a reversed version"""
    for message in input:
        await asyncio.sleep(0.5)
        yield {"thought": "I should echo everything and then reverse it"}
        
        # Echo the original message
        await asyncio.sleep(0.5)
        yield message
        
        # Create and return the reversed message
        for part in message.parts:
            if part.content_type == "text/plain":
                reversed_content = part.content[::-1]
                
                # Create a new message with the reversed content
                reversed_message = Message(
                    role="assistant",
                    parts=[MessagePart(content=f"Reversed: {reversed_content}", content_type="text/plain")]
                )
                
                await asyncio.sleep(0.5)
                yield reversed_message


server.run()
