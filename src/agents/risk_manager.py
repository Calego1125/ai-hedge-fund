"""
Risk Management Agent
Controls portfolio exposure and position sizing.
"""
from src.agents.base import BaseAgent

class RiskManager(BaseAgent):
    """Manages risk and position sizing."""
    
    def __init__(self, config=None):
        super().__init__("RiskManager", config)
        self.max_exposure = self.config.get("max_exposure", 1.0)
        self.stop_loss = self.config.get("stop_loss", 0.05)
        
    def run(self, signals: dict) -> dict:
        """
        Apply risk constraints to signals.
        """
        self.logger.info("Applying risk constraints...")
        return {"allocations": {}, "risk_metrics": {}}
