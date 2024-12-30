from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, courses, sections

app = FastAPI(
    title="Fast API Learning Management System",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Behrouz",
        "email": "Behrouzsharifidev@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)


app.include_router(users.router)

app.include_router(courses.router)

app.include_router(sections.router)

