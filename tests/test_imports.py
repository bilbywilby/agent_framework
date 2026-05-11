"""Smoke test: verify package imports and exports."""
import pytest


def test_package_imports():
    """All public symbols should import without errors."""
    from agent_framework import (
        AgentConfig,
        AgentError,
        AgentLoop,
        AgentMetrics,
        AsyncCircuitBreaker,
        CircuitBreakerError,
        CircuitState,
        LatencyRecord,
        RetryPolicy,
        ToolDefinition,
        ToolRegistry,
        ToolResult,
        Turn,
        VertexClient,
    )
    
    assert AgentConfig is not None
    assert AgentLoop is not None
    assert VertexClient is not None
    assert AgentMetrics is not None


def test_version_export():
    """__version__ should be accessible."""
    from agent_framework import __version__
    
    assert isinstance(__version__, str)
    assert len(__version__.split(".")) >= 2  # semantic versioning


def test_all_exports():
    """__all__ should match actual exports."""
    import agent_framework
    
    for name in agent_framework.__all__:
        assert hasattr(agent_framework, name), f"Missing export: {name}"
