from pathlib import Path

from pydantic import BaseModel

from envator.config.model.env import BackendConfig


class ContainerPortMapping(BaseModel):
    host: int
    container: int


class ContainerVolumeMapping(BaseModel):
    source: Path
    target: Path
    readonly: bool = False


class DockerConfig(BackendConfig):
    share_uid: bool = False
    native_options: dict
