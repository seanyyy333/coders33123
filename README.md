git clone https://github.com/yourusername/symbolic-ai-planning.git
cd symbolic-ai-planning
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
Search successful!
Path:
Step 0: SymbolicState({'number': 0})
Step 1: SymbolicState({'number': 2})
Step 2: SymbolicState({'number': 4})
Step 3: SymbolicState({'number': 6})
Step 4: SymbolicState({'number': 8})
Step 5: SymbolicState({'number': 10})
Total Cost: 7.5
def preconditions(state: SymbolicState) -> bool:
    # Define conditions
    return True

def transformations(state: SymbolicState) -> Tuple[SymbolicState, float]:
    # Define state transformation and cost
    new_state = SymbolicState({...})
    return new_state, cost

new_task = Task("TaskName", preconditions, transformations, cost=1.0)
def custom_cost_function(from_state: SymbolicState, task: Task, to_state: SymbolicState) -> float:
    # Calculate and return the cost
    return cost

def custom_heuristic(state: SymbolicState) -> float:
    # Estimate and return the heuristic value
    return heuristic
python -m unittest discover tests