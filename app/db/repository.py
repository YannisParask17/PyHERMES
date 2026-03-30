import sqlite3
from typing import Dict
from app.models.normalized_model import NormalizedJob



class JobRepository:
    """
    Write and retrieve fetched jobs. Knows SQL (for now in-memory repo)  
    """
    def __init__(self):
        self._jobs: dict[int, dict] = {}
        self._next_id : int = 1
        

    def write(self, job: NormalizedJob) -> int:
        """ An in-memory repo is implemented for simplicity. Needs to be changed to an SQL version later. 

        Parameters
        ----------
        job : NormalizedJob
            _description_

        Returns
        -------
        int
            _description_
        """

        job_id = self._next_id

        self._jobs[job_id] = {'title': job.title,
                              'company': job.company}

        self._next_id += 1
        return job_id
    
    def get_jobs(self) -> dict[int, dict]:
        return self._jobs.copy()
    


if __name__ == '__main__':

    from app.models.normalized_model import NormalizedJob
    from datetime import datetime


    # Dummy job
    job = NormalizedJob(external_id='1',
                        title='Senior Development engineer',
                        company='My Company A/S',
                        location='Compenhagen',
                        country=None,
                        url='www.sample.spl',
                        description='An exciting job sample',
                        work_mode='onsite',
                        commitment='full-time',
                        employment_type = 'permanent',
                        posted_at = None,
                        fetched_at=datetime(2026,2, 17))

    repo = JobRepository()
    print(f'Writing job: {job.title}')
    repo.write(job=job)
    # Check that repo is okay
    print(f'{job.title} has been succesfully written to repo!')
    print(repo.get_jobs())