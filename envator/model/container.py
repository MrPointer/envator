from pathlib import Path

from pydantic import BaseModel

from envator.model.env import BackendConfig


class ContainerPortMapping(BaseModel):
    host: int
    container: int


class ContainerVolumeMapping(BaseModel):
    source: Path
    target: Path
    readonly: bool = False


class ContainerConfig(BackendConfig):
    share_uid: bool = False
    native_options: dict
