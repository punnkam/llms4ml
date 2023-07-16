import modal._function_utils
import modal._output
import modal.app
import modal.client
import modal.functions
import modal.gpu
import modal.image
import modal.mount
import modal.network_file_system
import modal.object
import modal.proxy
import modal.retries
import modal.schedule
import modal.secret
import modal.volume
import os
import synchronicity.combined_types
import typing
import typing_extensions

class LocalEntrypoint:
    raw_f: typing.Callable[..., typing.Any]
    _stub: _Stub

    def __init__(self, raw_f, stub):
        ...

    def __call__(self, *args, **kwargs):
        ...


def check_sequence(items: typing.Sequence[typing.Any], item_type: typing.Type[typing.Any], error_msg: str):
    ...


CLS_T = typing.TypeVar("CLS_T", bound="typing.Type")

class _Stub:
    _name: typing.Union[str, None]
    _description: str
    _app_id: str
    _blueprint: typing.Dict[str, modal.object._Provider]
    _function_mounts: typing.Dict[str, modal.mount._Mount]
    _mounts: typing.Sequence[modal.mount._Mount]
    _secrets: typing.Sequence[modal.secret._Secret]
    _function_handles: typing.Dict[str, modal.functions._FunctionHandle]
    _web_endpoints: typing.List[str]
    _local_entrypoints: typing.Dict[str, LocalEntrypoint]
    _app: typing.Union[modal.app._App, None]
    _all_stubs: typing.ClassVar[typing.Dict[str, typing.List[_Stub]]]

    def __init__(self, name: typing.Union[str, None] = None, *, image: typing.Union[modal.image._Image, None] = None, mounts: typing.Sequence[modal.mount._Mount] = [], secrets: typing.Sequence[modal.secret._Secret] = [], **blueprint: modal.object._Provider) -> None:
        ...

    @property
    def name(self) -> typing.Union[str, None]:
        ...

    @property
    def app(self) -> typing.Union[modal.app._App, None]:
        ...

    @property
    def description(self) -> str:
        ...

    def _validate_blueprint_value(self, key: str, value: typing.Any):
        ...

    def _infer_app_desc(self):
        ...

    def __getitem__(self, tag: str):
        ...

    def __setitem__(self, tag: str, obj: modal.object._Provider):
        ...

    def __getattr__(self, tag: str) -> modal.object._Provider:
        ...

    def __setattr__(self, tag: str, obj: modal.object._Provider):
        ...

    def is_inside(self, image: typing.Union[modal.image._Image, None] = None) -> bool:
        ...

    def _set_app(self, app: modal.app._App) -> typing.AsyncContextManager[None]:
        ...

    def run(self, client: typing.Union[modal.client._Client, None] = None, stdout=None, show_progress: bool = True, detach: bool = False, output_mgr: typing.Union[modal._output.OutputManager, None] = None) -> typing.AsyncContextManager[modal.app._App]:
        ...

    async def deploy(self, name: typing.Union[str, None] = None, namespace=1, client=None, stdout=None, show_progress=True, object_entity: str = 'ap') -> modal.app._App:
        ...

    def _get_default_image(self):
        ...

    @property
    def _pty_input_stream(self):
        ...

    def _get_watch_mounts(self):
        ...

    def _get_function_handle(self, info: modal._function_utils.FunctionInfo) -> modal.functions._FunctionHandle:
        ...

    def _add_function(self, function: modal.functions._Function):
        ...

    @property
    def registered_functions(self) -> typing.Dict[str, modal.functions._FunctionHandle]:
        ...

    @property
    def registered_entrypoints(self) -> typing.Dict[str, LocalEntrypoint]:
        ...

    @property
    def registered_web_endpoints(self) -> typing.List[str]:
        ...

    def local_entrypoint(self, name: typing.Union[str, None] = None) -> typing.Callable[[typing.Callable[..., typing.Any]], None]:
        ...

    def function(self, image: typing.Union[modal.image._Image, None] = None, schedule: typing.Union[modal.schedule.Schedule, None] = None, secret: typing.Union[modal.secret._Secret, None] = None, secrets: typing.Sequence[modal.secret._Secret] = (), gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, serialized: bool = False, mounts: typing.Sequence[modal.mount._Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system._NetworkFileSystem] = {}, network_file_systems: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system._NetworkFileSystem] = {}, allow_cross_region_volumes: bool = False, volumes: typing.Dict[typing.Union[str, os.PathLike], modal.volume._Volume] = {}, cpu: typing.Union[float, None] = None, memory: typing.Union[int, None] = None, proxy: typing.Union[modal.proxy._Proxy, None] = None, retries: typing.Union[int, modal.retries.Retries, None] = None, concurrency_limit: typing.Union[int, None] = None, container_idle_timeout: typing.Union[int, None] = None, timeout: typing.Union[int, None] = None, interactive: bool = False, keep_warm: typing.Union[int, None] = None, name: typing.Union[str, None] = None, is_generator: typing.Union[bool, None] = None, cloud: typing.Union[str, None] = None, _cls: typing.Union[type, None] = None) -> typing.Callable[[typing.Union[modal.functions._PartialFunction, typing.Callable[..., typing.Any]]], modal.functions._FunctionHandle]:
        ...

    def web_endpoint(self, method: str = 'GET', label: typing.Union[str, None] = None, wait_for_response: bool = True):
        ...

    def asgi_app(self, label: typing.Union[str, None] = None, wait_for_response: bool = True):
        ...

    def wsgi_app(self, label: typing.Union[str, None] = None, wait_for_response: bool = True):
        ...

    async def interactive_shell(self, cmd=None, image=None, **kwargs):
        ...

    def cls(self, image: typing.Union[modal.image._Image, None] = None, secret: typing.Union[modal.secret._Secret, None] = None, secrets: typing.Sequence[modal.secret._Secret] = (), gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, serialized: bool = False, mounts: typing.Sequence[modal.mount._Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system._NetworkFileSystem] = {}, network_file_systems: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system._NetworkFileSystem] = {}, allow_cross_region_volumes: bool = False, volumes: typing.Dict[typing.Union[str, os.PathLike], modal.volume._Volume] = {}, cpu: typing.Union[float, None] = None, memory: typing.Union[int, None] = None, proxy: typing.Union[modal.proxy._Proxy, None] = None, retries: typing.Union[int, modal.retries.Retries, None] = None, concurrency_limit: typing.Union[int, None] = None, container_idle_timeout: typing.Union[int, None] = None, timeout: typing.Union[int, None] = None, interactive: bool = False, keep_warm: typing.Union[int, None] = None, cloud: typing.Union[str, None] = None) -> typing.Callable[[CLS_T], CLS_T]:
        ...

    def _hydrate_function_handles(self, client: modal.client._Client, container_app: modal.app._App):
        ...

    def _get_deduplicated_function_mounts(self, mounts: typing.Dict[str, modal.mount._Mount]):
        ...


class Stub:
    _name: typing.Union[str, None]
    _description: str
    _app_id: str
    _blueprint: typing.Dict[str, modal.object.Provider]
    _function_mounts: typing.Dict[str, modal.mount.Mount]
    _mounts: typing.Sequence[modal.mount.Mount]
    _secrets: typing.Sequence[modal.secret.Secret]
    _function_handles: typing.Dict[str, modal.functions.FunctionHandle]
    _web_endpoints: typing.List[str]
    _local_entrypoints: typing.Dict[str, LocalEntrypoint]
    _app: typing.Union[modal.app.App, None]
    _all_stubs: typing.ClassVar[typing.Dict[str, typing.List[Stub]]]

    def __init__(self, name: typing.Union[str, None] = None, *, image: typing.Union[modal.image.Image, None] = None, mounts: typing.Sequence[modal.mount.Mount] = [], secrets: typing.Sequence[modal.secret.Secret] = [], **blueprint: modal.object.Provider) -> None:
        ...

    @property
    def name(self) -> typing.Union[str, None]:
        ...

    @property
    def app(self) -> typing.Union[modal.app.App, None]:
        ...

    @property
    def description(self) -> str:
        ...

    def _validate_blueprint_value(self, key: str, value: typing.Any):
        ...

    def _infer_app_desc(self):
        ...

    def __getitem__(self, tag: str):
        ...

    def __setitem__(self, tag: str, obj: modal.object.Provider):
        ...

    def __getattr__(self, tag: str) -> modal.object.Provider:
        ...

    def __setattr__(self, tag: str, obj: modal.object.Provider):
        ...

    def is_inside(self, image: typing.Union[modal.image.Image, None] = None) -> bool:
        ...

    class ___set_app_spec(typing_extensions.Protocol):
        def __call__(self, app: modal.app.App) -> synchronicity.combined_types.AsyncAndBlockingContextManager[None]:
            ...

        def aio(self, app: modal.app.App) -> typing.AsyncContextManager[None]:
            ...

    _set_app: ___set_app_spec

    class __run_spec(typing_extensions.Protocol):
        def __call__(self, client: typing.Union[modal.client.Client, None] = None, stdout=None, show_progress: bool = True, detach: bool = False, output_mgr: typing.Union[modal._output.OutputManager, None] = None) -> synchronicity.combined_types.AsyncAndBlockingContextManager[modal.app.App]:
            ...

        def aio(self, client: typing.Union[modal.client.Client, None] = None, stdout=None, show_progress: bool = True, detach: bool = False, output_mgr: typing.Union[modal._output.OutputManager, None] = None) -> typing.AsyncContextManager[modal.app.App]:
            ...

    run: __run_spec

    class __deploy_spec(typing_extensions.Protocol):
        def __call__(self, name: typing.Union[str, None] = None, namespace=1, client=None, stdout=None, show_progress=True, object_entity: str = 'ap') -> modal.app.App:
            ...

        async def aio(self, *args, **kwargs) -> modal.app.App:
            ...

    deploy: __deploy_spec

    def _get_default_image(self):
        ...

    @property
    def _pty_input_stream(self):
        ...

    def _get_watch_mounts(self):
        ...

    def _get_function_handle(self, info: modal._function_utils.FunctionInfo) -> modal.functions.FunctionHandle:
        ...

    def _add_function(self, function: modal.functions.Function):
        ...

    @property
    def registered_functions(self) -> typing.Dict[str, modal.functions.FunctionHandle]:
        ...

    @property
    def registered_entrypoints(self) -> typing.Dict[str, LocalEntrypoint]:
        ...

    @property
    def registered_web_endpoints(self) -> typing.List[str]:
        ...

    def local_entrypoint(self, name: typing.Union[str, None] = None) -> typing.Callable[[typing.Callable[..., typing.Any]], None]:
        ...

    def function(self, image: typing.Union[modal.image.Image, None] = None, schedule: typing.Union[modal.schedule.Schedule, None] = None, secret: typing.Union[modal.secret.Secret, None] = None, secrets: typing.Sequence[modal.secret.Secret] = (), gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, serialized: bool = False, mounts: typing.Sequence[modal.mount.Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system.NetworkFileSystem] = {}, network_file_systems: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system.NetworkFileSystem] = {}, allow_cross_region_volumes: bool = False, volumes: typing.Dict[typing.Union[str, os.PathLike], modal.volume.Volume] = {}, cpu: typing.Union[float, None] = None, memory: typing.Union[int, None] = None, proxy: typing.Union[modal.proxy.Proxy, None] = None, retries: typing.Union[int, modal.retries.Retries, None] = None, concurrency_limit: typing.Union[int, None] = None, container_idle_timeout: typing.Union[int, None] = None, timeout: typing.Union[int, None] = None, interactive: bool = False, keep_warm: typing.Union[int, None] = None, name: typing.Union[str, None] = None, is_generator: typing.Union[bool, None] = None, cloud: typing.Union[str, None] = None, _cls: typing.Union[type, None] = None) -> typing.Callable[[typing.Union[modal.functions.PartialFunction, typing.Callable[..., typing.Any]]], modal.functions.FunctionHandle]:
        ...

    def web_endpoint(self, method: str = 'GET', label: typing.Union[str, None] = None, wait_for_response: bool = True):
        ...

    def asgi_app(self, label: typing.Union[str, None] = None, wait_for_response: bool = True):
        ...

    def wsgi_app(self, label: typing.Union[str, None] = None, wait_for_response: bool = True):
        ...

    class __interactive_shell_spec(typing_extensions.Protocol):
        def __call__(self, cmd=None, image=None, **kwargs):
            ...

        async def aio(self, *args, **kwargs):
            ...

    interactive_shell: __interactive_shell_spec

    def cls(self, image: typing.Union[modal.image.Image, None] = None, secret: typing.Union[modal.secret.Secret, None] = None, secrets: typing.Sequence[modal.secret.Secret] = (), gpu: typing.Union[None, bool, str, modal.gpu._GPUConfig] = None, serialized: bool = False, mounts: typing.Sequence[modal.mount.Mount] = (), shared_volumes: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system.NetworkFileSystem] = {}, network_file_systems: typing.Dict[typing.Union[str, os.PathLike], modal.network_file_system.NetworkFileSystem] = {}, allow_cross_region_volumes: bool = False, volumes: typing.Dict[typing.Union[str, os.PathLike], modal.volume.Volume] = {}, cpu: typing.Union[float, None] = None, memory: typing.Union[int, None] = None, proxy: typing.Union[modal.proxy.Proxy, None] = None, retries: typing.Union[int, modal.retries.Retries, None] = None, concurrency_limit: typing.Union[int, None] = None, container_idle_timeout: typing.Union[int, None] = None, timeout: typing.Union[int, None] = None, interactive: bool = False, keep_warm: typing.Union[int, None] = None, cloud: typing.Union[str, None] = None) -> typing.Callable[[CLS_T], CLS_T]:
        ...

    def _hydrate_function_handles(self, client: modal.client.Client, container_app: modal.app.App):
        ...

    def _get_deduplicated_function_mounts(self, mounts: typing.Dict[str, modal.mount.Mount]):
        ...


_default_image: modal.image._Image