from enum import Enum
from typing import List

from pydantic import BaseModel


class SupportedBackend(str, Enum):
    CONTAINER = "container"
    SSH = "ssh"


class BackendConfig(BaseModel):
    pass


class CustomCommandsConfig(BaseModel):
    init: List[str] = []
    post_create: List[str] = []
    post_start: List[str] = []
    post_stop: List[str] = []


class EnvatorEnvConfig(BaseModel):
    name: str
    type: SupportedBackend
    backend_config: BackendConfig
    custom_commands: CustomCommandsConfig = None
