"""
agent_framework — Production-grade async agentic framework for Vertex AI (Gemini).

A minimal-wiring, resilient framework for building agentic workflows with circuit breaking,
retry policies, observability, and tool orchestration.

Supported Python: 3.9+
Required: google-cloud-vertex-ai >= 1.40.0

Example:
    >>> from agent_framework import AgentLoop, VertexClient, ToolRegistry, AgentConfig
    >>> client = VertexClient(project="my-gcp-project", location="us-central1")
    >>> agent = AgentLoop(client=client, registry=ToolRegistry(), config=AgentConfig())
    >>> turn = await agent.run("What is the capital of France?")
    >>> print(turn.final_response)
"""

from typing import TYPE_CHECKING

__version__ = "0.1.0"
__author__ = "Your Team"
__license__ = "Apache-2.0"

# Core API
from .agent import AgentConfig, AgentError, AgentLoop, Turn
from .circuit_breaker import AsyncCircuitBreaker, CircuitBreakerError, CircuitState
from .observability import AgentMetrics, LatencyRecord
from .retry import RetryPolicy
from .tools import ToolDefinition, ToolRegistry, ToolResult
from .vertex_client import VertexClient

# Type stubs (optional, heavy imports only for type checkers)
if TYPE_CHECKING:
    from google.cloud.aiplatform import aiplatform

__all__ = [
    "__version__",
    "AgentConfig",
    "AgentError",
    "AgentLoop",
    "AgentMetrics",
    "AsyncCircuitBreaker",
    "CircuitBreakerError",
    "CircuitState",
    "LatencyRecord",
    "RetryPolicy",
    "ToolDefinition",
    "ToolRegistry",
    "ToolResult",
    "Turn",
    "VertexClient",
]


def _check_dependencies() -> None:
    """Validate required dependencies at import time."""
    try:
        import google.cloud.aiplatform  # noqa: F401
    except ImportError as e:
        raise ImportError(
            "agent_framework requires google-cloud-vertex-ai. "
            "Install with: pip install agent_framework[vertex]"
        ) from e


_check_dependencies()
