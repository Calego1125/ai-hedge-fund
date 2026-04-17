"""
Alpha Generator Agent
Generates trading signals based on quantitative factors.
"""
import pandas as pd
import numpy as np
from src.agents.base import BaseAgent

class AlphaGenerator(BaseAgent):
    """Generates alpha signals from market data."""
    
    def __init__(self, config=None):
        super().__init__("AlphaGenerator", config)
        self.factors = self.config.get("factors", ["momentum", "volatility"])
        
    def run(self, data: pd.DataFrame) -> Dict[str, Any]:
        """
        Generate signals from OHLCV data.
        
        Args:
            data: DataFrame with columns [timestamp, open, high, low, close, volume]
            
        Returns:
            Dict with signals and metadata
        """
        signals = {}
        
        if "momentum" in self.factors:
            signals["momentum"] = self._calc_momentum(data)
        if "volatility" in self.factors:
            signals["volatility"] = self._calc_volatility(data)
            
        return {
            "signals": signals,
            "timestamp": pd.Timestamp.now(),
            "agent": self.name
        }
    
    def _calc_momentum(self, data: pd.DataFrame) -> float:
        """Simple momentum calculation (Return over last N days)."""
        if len(data) < 2:
            return 0.0
        return (data['close'].iloc[-1] / data['close'].iloc[0]) - 1
    
    def _calc_volatility(self, data: pd.DataFrame) -> float:
        """Calculate realized volatility."""
        if len(data) < 2:
            return 0.0
        returns = data['close'].pct_change().dropna()
        return returns.std() * np.sqrt(252)
