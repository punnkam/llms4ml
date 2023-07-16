import __main__
import modal._resolver
import modal.functions
import modal.gpu
import modal.mount
import modal.network_file_system
import modal.object
import modal.secret
import modal_proto.api_pb2
import os
import pathlib
import typing

def _validate_python_version(version: str) -> None:
    ...


def _dockerhub_python_version(python_version=None):
    ...


def _get_client_requirements_path():
    ...


def _flatten_str_args(function_name: str, arg_name: str, args: typing.Tuple[typing.Union[str, typing.List[str]], ...]) -> typing.List[str]:
    ...


class _ImageHandle(modal.object._Handle):
    def _is_inside(self) -> bool:
        ...


class _ImageRegistryConfig:
    def __init__(self, registry_type: int = 0, secret: typing.Union[modal.secret._Secret, None] = None):
        ...

    async def resolve(self, resolver: modal._resolver.Resolver) -> modal_proto.api_pb2.ImageRegistryConfig:
        ...


class _Image(modal.object._Provider[_ImageHandle]):
    force_build: bool

    @staticmethod
    def _from_args(base_images={}, context_files={}, dockerfile_commands: typing.Union[typing.List[str], typing.Callable[[], typing.List[str]]] = [], secrets: typing.Sequence[modal.secret._Secret] = [], ref=None, gpu_config: typing.Union[modal_proto.api_pb2.GPUConfig, None] = None, build_function: modal.functions._Function = None, context_mount: typing.Union[modal.mount._Mount, None] = None, image_registry_config: typing.Union[_ImageRegistryConfig, None] = None, force_build: bool = False, _namespace: int = 1):
        ...

    def extend(self, *, context_files={}, dockerfile_commands: typing.Union[typing.List[str], typing.Callable[[], typing.List[str]]] = [], secrets: typing.Sequence[modal.secret._Secret] = [], ref=None, gpu_config: typing.Union[modal_proto.api_pb2.GPUConfig, None] = None, build_function: modal.functions._Function = None, context_mount: typing.Union[modal.mount._Mount, None] = None, image_registry_config: typing.Union[_ImageRegistryConfig, None] = None, force_build: bool = False, _namespace: int = 1) -> _Image:
        ...

    def copy_mount(self, mount: modal.mount._Mount, remote_path: typing.Union[str, pathlib.Path] = '.') -> _Image:
        ...

    def copy(self, mount: modal.mount._Mount, remote_path: typing.Union[str, pathlib.Path] = '.') -> _Image:
        ...

    def copy_local_file(self, local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.Path] = './') -> _Image:
        ...

    def copy_local_dir(self, local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.Path] = '.') -> _Image:
        ...

    def pip_install(self, *packages: typing.Union[str, typing.List[str]], find_links: typing.Union[str, None] = None, index_url: typing.Union[str, None] = None, extra_index_url: typing.Union[str, None] = None, pre: bool = False, force_build: bool = False, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    def pip_install_private_repos(self, *repositories: str, git_user: str, gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, secrets: typing.Sequence[modal.secret._Secret] = [], force_build: bool = False) -> _Image:
        ...

    def pip_install_from_requirements(self, requirements_txt: str, find_links: typing.Union[str, None] = None, force_build: bool = False, *, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    def pip_install_from_pyproject(self, pyproject_toml: str, optional_dependencies: typing.List[str] = [], force_build: bool = False, *, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    def poetry_install_from_file(self, poetry_pyproject_toml: str, poetry_lockfile: typing.Union[str, None] = None, ignore_lockfile: bool = False, old_installer: bool = False, force_build: bool = False, with_: typing.List[str] = [], without: typing.List[str] = [], only: typing.List[str] = [], *, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    def dockerfile_commands(self, dockerfile_commands: typing.Union[str, typing.List[str]], context_files: typing.Dict[str, str] = {}, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, context_mount: typing.Union[modal.mount._Mount, None] = None, force_build: bool = False) -> _Image:
        ...

    def run_commands(self, *commands: typing.Union[str, typing.List[str]], secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, force_build: bool = False) -> _Image:
        ...

    @staticmethod
    def conda(python_version: str = '3.9', force_build: bool = False) -> _Image:
        ...

    def conda_install(self, *packages: typing.Union[str, typing.List[str]], channels: typing.List[str] = [], force_build: bool = False, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    def conda_update_from_environment(self, environment_yml: str, force_build: bool = False, *, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    @staticmethod
    def micromamba(python_version: str = '3.9', force_build: bool = False) -> _Image:
        ...

    def micromamba_install(self, *packages: typing.Union[str, typing.List[str]], channels: typing.List[str] = [], force_build: bool = False, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    @staticmethod
    def _registry_setup_commands(tag: str, setup_dockerfile_commands: typing.List[str]) -> typing.List[str]:
        ...

    @staticmethod
    def from_dockerhub(tag: str, setup_dockerfile_commands: typing.List[str] = [], force_build: bool = False, **kwargs) -> _Image:
        ...

    @staticmethod
    def from_gcp_artifact_registry(tag: str, secret: typing.Union[modal.secret._Secret, None] = None, setup_dockerfile_commands: typing.List[str] = [], force_build: bool = False, **kwargs) -> _Image:
        ...

    @staticmethod
    def from_aws_ecr(tag: str, secret: typing.Union[modal.secret._Secret, None] = None, setup_dockerfile_commands: typing.List[str] = [], force_build: bool = False, **kwargs) -> _Image:
        ...

    @staticmethod
    def from_dockerfile(path: typing.Union[str, pathlib.Path], context_mount: typing.Union[modal.mount._Mount, None] = None, force_build: bool = False, *, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    @staticmethod
    def debian_slim(python_version: typing.Union[str, None] = None, force_build: bool = False) -> _Image:
        ...

    def apt_install(self, *packages: typing.Union[str, typing.List[str]], force_build: bool = False, secrets: typing.Sequence[modal.secret._Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> _Image:
        ...

    def run_function(self, raw_f: typing.Callable[[], typing.Any], *, secret: typing.Union[modal.secret._Secret, None] = None, secrets: typing.Sequence[modal.secret._Secret] = (), gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, mounts: typing.Sequence[modal.mount._Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system._NetworkFileSystem] = {}, network_file_systems: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system._NetworkFileSystem] = {}, cpu: typing.Union[float, None] = None, memory: typing.Union[int, None] = None, timeout: typing.Union[int, None] = 86400, cloud: typing.Union[str, None] = None, force_build: bool = False) -> _Image:
        ...

    def env(self, vars: typing.Dict[str, str]) -> _Image:
        ...


class ImageHandle(modal.object.Handle):
    def __init__(self):
        ...

    def _is_inside(self) -> bool:
        ...


class Image(modal.object.Provider[ImageHandle]):
    force_build: bool

    def __init__(self):
        ...

    @staticmethod
    def _from_args(base_images={}, context_files={}, dockerfile_commands: typing.Union[typing.List[str], typing.Callable[[], typing.List[str]]] = [], secrets: typing.Sequence[modal.secret.Secret] = [], ref=None, gpu_config: typing.Union[modal_proto.api_pb2.GPUConfig, None] = None, build_function: modal.functions.Function = None, context_mount: typing.Union[modal.mount.Mount, None] = None, image_registry_config: typing.Union[_ImageRegistryConfig, None] = None, force_build: bool = False, _namespace: int = 1):
        ...

    def extend(self, **kwargs) -> Image:
        ...

    def copy_mount(self, mount: modal.mount.Mount, remote_path: typing.Union[str, pathlib.Path] = '.') -> Image:
        ...

    def copy(self, mount: modal.mount.Mount, remote_path: typing.Union[str, pathlib.Path] = '.') -> Image:
        ...

    def copy_local_file(self, local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.Path] = './') -> Image:
        ...

    def copy_local_dir(self, local_path: typing.Union[str, pathlib.Path], remote_path: typing.Union[str, pathlib.Path] = '.') -> Image:
        ...

    def pip_install(self, *packages: typing.Union[str, typing.List[str]], find_links: typing.Union[str, None] = None, index_url: typing.Union[str, None] = None, extra_index_url: typing.Union[str, None] = None, pre: bool = False, force_build: bool = False, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    def pip_install_private_repos(self, *repositories: str, git_user: str, gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, secrets: typing.Sequence[modal.secret.Secret] = [], force_build: bool = False) -> Image:
        ...

    def pip_install_from_requirements(self, requirements_txt: str, find_links: typing.Union[str, None] = None, force_build: bool = False, *, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    def pip_install_from_pyproject(self, pyproject_toml: str, optional_dependencies: typing.List[str] = [], force_build: bool = False, *, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    def poetry_install_from_file(self, poetry_pyproject_toml: str, poetry_lockfile: typing.Union[str, None] = None, ignore_lockfile: bool = False, old_installer: bool = False, force_build: bool = False, with_: typing.List[str] = [], without: typing.List[str] = [], only: typing.List[str] = [], *, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    def dockerfile_commands(self, dockerfile_commands: typing.Union[str, typing.List[str]], context_files: typing.Dict[str, str] = {}, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, context_mount: typing.Union[modal.mount.Mount, None] = None, force_build: bool = False) -> Image:
        ...

    def run_commands(self, *commands: typing.Union[str, typing.List[str]], secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, force_build: bool = False) -> Image:
        ...

    @staticmethod
    def conda(python_version: str = '3.9', force_build: bool = False) -> Image:
        ...

    def conda_install(self, *packages: typing.Union[str, typing.List[str]], channels: typing.List[str] = [], force_build: bool = False, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    def conda_update_from_environment(self, environment_yml: str, force_build: bool = False, *, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    @staticmethod
    def micromamba(python_version: str = '3.9', force_build: bool = False) -> Image:
        ...

    def micromamba_install(self, *packages: typing.Union[str, typing.List[str]], channels: typing.List[str] = [], force_build: bool = False, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    @staticmethod
    def _registry_setup_commands(tag: str, setup_dockerfile_commands: typing.List[str]) -> typing.List[str]:
        ...

    @staticmethod
    def from_dockerhub(tag: str, setup_dockerfile_commands: typing.List[str] = [], force_build: bool = False, **kwargs) -> Image:
        ...

    @staticmethod
    def from_gcp_artifact_registry(tag: str, secret: typing.Union[modal.secret.Secret, None] = None, setup_dockerfile_commands: typing.List[str] = [], force_build: bool = False, **kwargs) -> Image:
        ...

    @staticmethod
    def from_aws_ecr(tag: str, secret: typing.Union[modal.secret.Secret, None] = None, setup_dockerfile_commands: typing.List[str] = [], force_build: bool = False, **kwargs) -> Image:
        ...

    @staticmethod
    def from_dockerfile(path: typing.Union[str, pathlib.Path], context_mount: typing.Union[modal.mount.Mount, None] = None, force_build: bool = False, *, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    @staticmethod
    def debian_slim(python_version: typing.Union[str, None] = None, force_build: bool = False) -> Image:
        ...

    def apt_install(self, *packages: typing.Union[str, typing.List[str]], force_build: bool = False, secrets: typing.Sequence[modal.secret.Secret] = [], gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None) -> Image:
        ...

    def run_function(self, raw_f: typing.Callable[[], typing.Any], *, secret: typing.Union[modal.secret.Secret, None] = None, secrets: typing.Sequence[modal.secret.Secret] = (), gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, mounts: typing.Sequence[modal.mount.Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system.NetworkFileSystem] = {}, network_file_systems: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system.NetworkFileSystem] = {}, cpu: typing.Union[float, None] = None, memory: typing.Union[int, None] = None, timeout: typing.Union[int, None] = 86400, cloud: typing.Union[str, None] = None, force_build: bool = False) -> Image:
        ...

    def env(self, vars: typing.Dict[str, str]) -> Image:
        ...
