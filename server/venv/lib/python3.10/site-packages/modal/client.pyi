import grpclib.exceptions
import typing
import typing_extensions

def _get_metadata(client_type: int, credentials: typing.Union[typing.Tuple[str, str], None], version: str) -> typing.Dict[str, str]:
    ...


async def _http_check(url: str, timeout: float) -> str:
    ...


async def _grpc_exc_string(exc: grpclib.exceptions.GRPCError, method_name: str, server_url: str, timeout: float) -> str:
    ...


class _Client:
    def __init__(self, server_url, client_type, credentials, version='0.50.2632', *, no_verify=False):
        ...

    @property
    def stub(self):
        ...

    async def _open(self):
        ...

    async def _close(self):
        ...

    def set_pre_stop(self, pre_stop: typing.Callable[[], typing.Awaitable[None]]):
        ...

    async def _verify(self):
        ...

    async def __aenter__(self):
        ...

    async def __aexit__(self, exc_type, exc, tb):
        ...

    @classmethod
    async def verify(cls, server_url, credentials):
        ...

    @classmethod
    async def unauthenticated_client(cls, server_url: str):
        ...

    async def start_token_flow(self, utm_source: typing.Union[str, None] = None) -> typing.Tuple[str, str]:
        ...

    async def finish_token_flow(self, token_flow_id) -> typing.Tuple[str, str]:
        ...

    @classmethod
    async def from_env(cls, _override_config=None) -> _Client:
        ...

    @classmethod
    def set_env_client(cls, client):
        ...


class Client:
    def __init__(self, server_url, client_type, credentials, version='0.50.2632', *, no_verify=False):
        ...

    @property
    def stub(self):
        ...

    class ___open_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _open: ___open_spec

    class ___close_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _close: ___close_spec

    class __set_pre_stop_spec(typing_extensions.Protocol):
        def __call__(self, pre_stop: typing.Callable[[], None]):
            ...

        def aio(self, pre_stop: typing.Callable[[], typing.Awaitable[None]]):
            ...

    set_pre_stop: __set_pre_stop_spec

    class ___verify_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _verify: ___verify_spec

    def __enter__(self):
        ...

    async def __aenter__(self, *args, **kwargs):
        ...

    def __exit__(self, exc_type, exc, tb):
        ...

    async def __aexit__(self, *args, **kwargs):
        ...

    @classmethod
    def verify(cls, server_url, credentials):
        ...

    @classmethod
    def unauthenticated_client(cls, server_url: str):
        ...

    class __start_token_flow_spec(typing_extensions.Protocol):
        def __call__(self, utm_source: typing.Union[str, None] = None) -> typing.Tuple[str, str]:
            ...

        async def aio(self, *args, **kwargs) -> typing.Tuple[str, str]:
            ...

    start_token_flow: __start_token_flow_spec

    class __finish_token_flow_spec(typing_extensions.Protocol):
        def __call__(self, token_flow_id) -> typing.Tuple[str, str]:
            ...

        async def aio(self, *args, **kwargs) -> typing.Tuple[str, str]:
            ...

    finish_token_flow: __finish_token_flow_spec

    @classmethod
    def from_env(cls, _override_config=None) -> Client:
        ...

    @classmethod
    def set_env_client(cls, client):
        ...


HEARTBEAT_INTERVAL: float

HEARTBEAT_TIMEOUT: float

CLIENT_CREATE_ATTEMPT_TIMEOUT: float

CLIENT_CREATE_TOTAL_TIMEOUT: float