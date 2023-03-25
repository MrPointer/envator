from pathlib import Path
import subprocess
from envator.errors.handlingfailed import HandlingFailedError

from envator.handlers.handler import Handler
from envator.model.container import ContainerConfig
from envator.model.env import EnvatorEnvConfig


class RunContainerHandler(Handler):
    def __init__(self, config: EnvatorEnvConfig):
        self._config = config

    def handle(self, *args, **kwargs):
        run_result = subprocess.run(self._construct_run_command(), capture_output=True)
        if run_result.returncode != 0:
            raise HandlingFailedError(run_result.stderr)

        for cmd in self._config.custom_commands.post_start:
            subprocess.run(self._construct_post_start_command(cmd))

    def _construct_run_command(self) -> list[str]:
        container_config: ContainerConfig = self._config.backend_config
        command = [container_config.provider, "run", "-d", "--name", self._config.name]
        for port_mapping in self._get_mapped_ports(container_config.native_options):
            command += ["-p", f"{port_mapping}"]
        for volume_mapping in self._get_mapped_volumes(container_config.native_options):
            command += ["-v", f"{volume_mapping}"]
        if self._interactive_mode_enabled(container_config.native_options):
            command.append("-it")

        # Specifying the image is the most important part
        command.append(container_config.image)

        return command

    def _construct_post_start_command(self, post_start_command: str) -> list[str]:
        container_config: ContainerConfig = self._config.backend_config
        command = [container_config.provider, "exec", self._config.name]
        substituted_cmd = post_start_command.replace('"', '\\\"')
        command += ["bash", "-c", f"{substituted_cmd}"]

        return command

    def _get_mapped_ports(self, container_options: dict) -> list[str]:
        if "ports" not in container_options:
            return []

        return container_options["ports"]

    def _get_mapped_volumes(self, container_options: dict) -> list[str]:
        if "volumes" not in container_options:
            return []

        result_map = []
        volume_map: str
        for volume_map in container_options["volumes"]:
            split_paths = volume_map.split(":")
            host_path = split_paths[0]
            if "$HOME" in host_path:
                host_path = host_path.replace("$HOME", str(Path.home()))
            result_map.append(f"{host_path}:{split_paths[1]}")

        return result_map

    def _interactive_mode_enabled(self, container_options: dict) -> bool:
        if "interactive" not in container_options:
            return False
        return container_options["interactive"]
