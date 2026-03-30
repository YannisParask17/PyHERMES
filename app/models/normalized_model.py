from pydantic import BaseModel
from datetime import datetime
from typing import Literal
from enum import Enum



class Commitment(Enum):
    """ Defining job commitment names """

    FULL_TIME = 'full-time'
    PART_TIME = 'part-time'

class WorkMode(Enum):
    """ Defining work type """

    ONSITE = 'onsite'
    HYBRID = 'hybrid'
    REMOTE = 'remote'

class EmploymentType(Enum):
    """ Defining employment type """

    PERMANENT = 'permanent'
    TEMPORARY = 'temporary'

class NormalizedJob(BaseModel):
    """ Pydantic model. Normalized job for internal processing

    Parameters
    ----------
    BaseModel : _type_
        
    """

    external_id: str

    title: str
    company: str
    
    location: str
    country: Literal['DK'] | None
    
    description: str
    url: str
    commitment : Commitment | None = None       # Full-time / part-time
    employment_type: EmploymentType | None = None    # permanent / temporary 
    work_mode : WorkMode | None = None          # remote / hybrid / onsite
    
    posted_at : datetime | None
    fetched_at: datetime
    
