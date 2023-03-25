from pathlib import Path

from vyper import v

from envator.config.configdict import EnvatorConfigDict
from envator.errors.notsupported import NotSupportedError
from envator.model.container import ContainerConfig
from envator.model.env import EnvatorEnvConfig, SupportedBackend
from envator.util.namingcase import NamingCase


class ConfigReader:
    def read_config(self, config_source: Path) -> EnvatorEnvConfig:
        v.set_config_name(config_source.stem)
        v.add_config_path(config_source.parent)
        v.read_in_config()

        env_name = v.get_string("env.name")

        backend_type = v.get_string("env.backend.type")
        if backend_type is None:
            raise ValueError("Environment's backend must be explicitly specified")

        if backend_type == SupportedBackend.CONTAINER:
            container_image = v.get_string("env.backend.image")
            container_provider = v.get_string("env.backend.provider")
            container_options = v.get("env.options")
            share_uid = container_options.pop("shareUid")
            concrete_backend_config = ContainerConfig(
                image=container_image,
                provider=container_provider,
                share_uid=share_uid,
                native_options=container_options,
            )
        else:
            raise NotSupportedError(f"{backend_type} backend is not fully supported yet")

        custom_commands = EnvatorConfigDict(v.get("env.customCommands")).with_keys_case(NamingCase.SNAKE)

        return EnvatorEnvConfig(
            name=env_name,
            type=backend_type,
            backend_config=concrete_backend_config,
            custom_commands=custom_commands,
        )
