import __main__
import asyncio.locks
import modal.object
import typing
import typing_extensions

class _VolumeHandle(modal.object._Handle):
    _lock: asyncio.locks.Lock

    def _initialize_from_empty(self):
        ...

    async def commit(self):
        ...

    async def reload(self):
        ...

    async def _do_reload(self, lock=True):
        ...


class VolumeHandle(modal.object.Handle):
    _lock: asyncio.locks.Lock

    def __init__(self):
        ...

    def _initialize_from_empty(self):
        ...

    class __commit_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    commit: __commit_spec

    class __reload_spec(typing_extensions.Protocol):
        def __call__(self):
            ...

        async def aio(self, *args, **kwargs):
            ...

    reload: __reload_spec

    class ___do_reload_spec(typing_extensions.Protocol):
        def __call__(self, lock=True):
            ...

        async def aio(self, *args, **kwargs):
            ...

    _do_reload: ___do_reload_spec


class _Volume(modal.object._Provider[_VolumeHandle]):
    @staticmethod
    def new() -> _Volume:
        ...

    @staticmethod
    def persisted(label: str, namespace=1, environment_name: typing.Union[str, None] = None) -> _Volume:
        ...


class Volume(modal.object.Provider[VolumeHandle]):
    def __init__(self):
        ...

    @staticmethod
    def new() -> Volume:
        ...

    @staticmethod
    def persisted(label: str, namespace=1, environment_name: typing.Union[str, None] = None) -> Volume:
        ...
