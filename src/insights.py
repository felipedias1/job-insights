from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    job_type = []
    for job in jobs:
        if job["job_type"] not in job_type:
            job_type.append(job["job_type"])
    return job_type


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    data = read(path)
    industry_type = []
    for industry in data:
        if industry["industry"] and industry["industry"] not in industry_type:
            industry_type.append(industry["industry"])
    return industry_type


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    max_salary = []
    for row in data:
        try:
            max_salary.append(int(row["max_salary"]))
        except ValueError:
            pass

    return max(max_salary)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    # Refactoring Function with help of Carlos Mello(Instructor) on monitoring
    data = read(path)
    min_salary = []
    for row in data:
        try:
            min_salary.append(int(row["min_salary"]))
        except ValueError:
            pass

    # Original Function
    """ min_salary = [
        int(job["min_salary"])
        for job in data
        if job["min_salary"] != "" #and job["min_salary"] != "invalid"
    ] """

    return min(min_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif type(job['min_salary']) != int or type(job['max_salary']) != int:
        raise ValueError
    elif type(salary) != int:
        raise ValueError
    elif job['min_salary'] > job['max_salary']:
        raise ValueError
    else:
        return job['min_salary'] <= salary <= job['max_salary']
    """ try:
        job['min_salary'] <= salary <= job['max_salary']
    except (KeyError, ValueError, TypeError):
        raise ValueError """


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_in_salary_range = []
    try:
        for job in jobs:
            if job["min_salary"] <= salary <= job["max_salary"]:
                jobs_in_salary_range.append(job)
    except (ValueError, TypeError):
        pass

    return jobs_in_salary_range
