"""
Base Agent Class for AI Hedge Fund
"""
import logging
from typing import Dict, Any, List

class BaseAgent:
    """Abstract base class for all agents in the system."""
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}
        self.logger = logging.getLogger(f"agent.{name}")
        self.state: Dict[str, Any] = {}

    def run(self, data: Any) -> Dict[str, Any]:
        """Execute agent logic. Must be implemented by subclasses."""
        raise NotImplementedError

    def save_state(self):
        """Persist agent state."""
        self.logger.info(f"Saving state for {self.name}")

    def load_state(self):
        """Restore agent state."""
        self.logger.info(f"Loading state for {self.name}")
