# test_solver.py
from backend.solver import can_schedule_weeks

def test_small_case():
    result = can_schedule_weeks(8, 4, 2, "Depth-First Search (DFS)")
    assert result is not None
