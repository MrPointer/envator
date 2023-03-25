from typing import List

from pydantic import BaseModel


class BackendConfig(BaseModel):
    pass


class CustomCommandsConfig(BaseModel):
    post_create: List[str] = []
    post_start: List[str] = []
    post_stop: List[str] = []


class EnvatorEnvConfig(BaseModel):
    name: str
    backend_config: BackendConfig
    custom_commands: CustomCommandsConfig
