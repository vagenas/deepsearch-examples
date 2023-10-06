from typing import Optional
from pydantic import BaseSettings, validator
from dotenv import find_dotenv

class NotebookSettings(BaseSettings):
    class Config:
        env_prefix = "DS_BK_"
        env_file = find_dotenv()
        env_file_encoding = "utf-8"

    profile: Optional[str] = None


class ProjectNotebookSettings(NotebookSettings):
    proj_key: str = ""
    cleanup: bool = True

    @validator("proj_key")
    def set_proj_key(cls, v):
        return v or input("Project key: ")


class KGProjectNotebookSettings(ProjectNotebookSettings):
    kg_key: str = ""

    @validator("kg_key")
    def set_kg_key(cls, v):
        return v or input("Knowledge graph key: ")