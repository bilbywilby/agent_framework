# agent_framework

Production-grade async agentic framework for **Vertex AI (Gemini)**.

## Installation

```bash
pip install agent_framework
# or with dev dependencies
pip install agent_framework[dev]
```

## Minimal Example

```python
import asyncio
from agent_framework import AgentLoop, VertexClient, ToolRegistry, AgentConfig

async def main():
    client = VertexClient(
        project="my-gcp-project",
        location="us-central1",
        model_name="gemini-1.5-pro",
    )
    agent = AgentLoop(
        client=client,
        registry=ToolRegistry(),
        config=AgentConfig(system_prompt="You are a helpful assistant."),
    )
    turn = await agent.run("What is the capital of France?")
    print(turn.final_response)

asyncio.run(main())
```

## Supported Python Versions

- Python 3.9+
- Requires `google-cloud-vertex-ai >= 1.40.0`

## Features

- **Circuit Breaking & Retries**: Protect your quota and handle transient failures
- **Parallel Tool Execution**: Run multiple tool calls simultaneously
- **Observability**: In-process metrics for latency and error tracking
- **Type Safety**: Full type hints with mypy support
- **Production Ready**: Comprehensive error handling and logging

See [examples/](examples/) for more patterns.
