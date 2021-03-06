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

    try:
        if int(job['min_salary']) > int(job['max_salary']):
            raise ValueError
        return int(job['min_salary']) <= salary <= int(job['max_salary'])
    except (KeyError, ValueError, TypeError):
        raise ValueError


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
