from src.sorting import sort_by
import pytest


mock_jobs = [
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2021-05-01"},
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2020-05-01"}
]

mock_jobs_sorted_by_max_salary = [
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2020-05-01"},
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2021-05-01"}
]

mock_jobs_sorted_by_min_salary = [
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2021-05-01"},
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2020-05-01"}
]

mock_jobs_sorted_by_date_posted = [
    {"min_salary": "1000", "max_salary": "2000", "date_posted": "2021-05-01"},
    {"min_salary": "3000", "max_salary": "5000", "date_posted": "2020-05-01"}
]


def test_sort_by_criteria():
    sort_by(mock_jobs, "max_salary")
    assert mock_jobs == mock_jobs_sorted_by_max_salary
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == mock_jobs_sorted_by_min_salary
    sort_by(mock_jobs, "date_posted")
    assert mock_jobs == mock_jobs_sorted_by_date_posted
    with pytest.raises(ValueError):
        sort_by(mock_jobs, "invalid")
