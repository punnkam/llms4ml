import __main__
import modal.object

class _ProxyHandle(modal.object._Handle):
    ...

class _Proxy(modal.object._Provider[_ProxyHandle]):
    ...

class ProxyHandle(modal.object.Handle):
    def __init__(self):
        ...


class Proxy(modal.object.Provider[ProxyHandle]):
    def __init__(self):
        ...
