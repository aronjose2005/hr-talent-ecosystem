import pytest
from src.talent_matching import match_candidate

def test_match_candidate():
    job_data = {"experience": 5.0, "skills": 8.0}
    candidate_data = {"experience": 4.5, "skills": 7.5}
    score = match_candidate(job_data, candidate_data)
    assert 0 <= score <= 100
