from pathlib import Path
from vyper import v

from envator.model.container import ContainerConfig
from envator.model.env import BackendConfig, EnvatorEnvConfig
from envator.config.configdict import EnvatorConfigDict
from envator.util.namingcase import NamingCase


class ConfigReader:
    def read_config(self, config_source: Path) -> EnvatorEnvConfig:
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
            backend_config = ContainerConfig(share_uid=share_uid, native_options=docker_options)

        custom_commands = EnvatorConfigDict(v.get("env.customCommands")).with_keys_case(NamingCase.SNAKE)

        return EnvatorEnvConfig(name=env_name, backend_config=backend_config, custom_commands=custom_commands)
