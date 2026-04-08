```json
{
    "agents/agent_definition.py": {
        "content": "
import logging
from typing import Dict, List
from langfuse import StateGraph
from agentops.ai import AgentLifecycle
from wandb import Weave

class AdaptiveAgent:
    """
    Adaptive agent for Montessori Adaptive Curriculum Engine.
    
    Attributes:
    non_stationary_drift_index (float): Index of non-stationary drift in the agent's environment.
    stochastic_regime_switch (bool): Flag indicating whether the agent is in a stochastic regime switch.
    """

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initializes the adaptive agent.
        
        Args:
        non_stationary_drift_index (float): Index of non-stationary drift in the agent's environment.
        stochastic_regime_switch (bool): Flag indicating whether the agent is in a stochastic regime switch.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.logger = logging.getLogger(__name__)

    def update_state(self, state_graph: StateGraph) -> None:
        """
        Updates the agent's state using the provided state graph.
        
        Args:
        state_graph (StateGraph): State graph representing the agent's environment.
        
        Raises:
        Exception: If an error occurs during state update.
        """
        try:
            self.logger.info('Updating agent state')
            state_graph.update_state()
        except Exception as e:
            self.logger.error(f'Error updating agent state: {e}')

    def evaluate_performance(self, weave: Weave) -> Dict[str, float]:
        """
        Evaluates the agent's performance using the provided Weave instance.
        
        Args:
        weave (Weave): Weave instance representing the agent's performance metrics.
        
        Returns:
        Dict[str, float]: Dictionary containing the agent's performance metrics.
        
        Raises:
        Exception: If an error occurs during performance evaluation.
        """
        try:
            self.logger.info('Evaluating agent performance')
            return weave.evaluate_performance()
        except Exception as e:
            self.logger.error(f'Error evaluating agent performance: {e}')

    def manage_memory(self, agent_lifecycle: AgentLifecycle) -> None:
        """
        Manages the agent's memory using the provided AgentLifecycle instance.
        
        Args:
        agent_lifecycle (AgentLifecycle): AgentLifecycle instance representing the agent's memory management.
        
        Raises:
        Exception: If an error occurs during memory management.
        """
        try:
            self.logger.info('Managing agent memory')
            agent_lifecycle.manage_memory()
        except Exception as e:
            self.logger.error(f'Error managing agent memory: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    non_stationary_drift_index = 0.5
    stochastic_regime_switch = True
    agent = AdaptiveAgent(non_stationary_drift_index, stochastic_regime_switch)
    
    state_graph = StateGraph()
    agent.update_state(state_graph)
    
    weave = Weave()
    performance_metrics = agent.evaluate_performance(weave)
    print(performance_metrics)
    
    agent_lifecycle = AgentLifecycle()
    agent.manage_memory(agent_lifecycle)
",
        "commit_message": "feat: implement specialized agent_definition logic"
    }
}
```