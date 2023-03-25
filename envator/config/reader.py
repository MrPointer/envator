from pathlib import Path
from vyper import v
from envator.config.model.docker import DockerConfig

from envator.config.model.env import BackendConfig, DevatorEnvConfig


class ConfigReader:
    def read_config(self, config_source: Path) -> DevatorEnvConfig:
        v.set_config_name(config_source.stem)
        v.add_config_path(config_source.parent)
        v.read_in_config()

        env_name = v.get_string("env.name")
        backend = v.get_string("env.backend")
        if backend is None:
            raise ValueError("Environment's backend must be explicitly specified")

        backend_config: BackendConfig
        if backend == "docker":
            docker_options = v.get("env.options")
            share_uid = docker_options.pop("shareUid")

            backend_config = DockerConfig(share_uid=share_uid, native_options=docker_options)

        custom_commands = v.get("env.customCommands")

        return DevatorEnvConfig(
            name=env_name, backend_config=backend_config, custom_commands=custom_commands
        )
