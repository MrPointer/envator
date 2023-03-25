from enum import Enum
from pathlib import Path

from pydantic import BaseModel

from envator.model.env import BackendConfig


class ContainerProvider(str, Enum):
    DOCKER = "docker"
    PODMAN = "podman"


class ContainerPortMapping(BaseModel):
    host: int
    container: int


class ContainerVolumeMapping(BaseModel):
    source: Path
    target: Path
    readonly: bool = False


class ContainerConfig(BackendConfig):
    image: str
    provider: ContainerProvider = ContainerProvider.DOCKER
    share_uid: bool = False
    native_options: dict = None
