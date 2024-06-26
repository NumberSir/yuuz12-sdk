class MinecraftPing:
    """服务器查询"""
    def __init__(self, client): ...
    """查询服务器数据"""
    async def ping(self, ip: str, port: int = None): ...

    @property
    def data(self) -> dict: ...
    @property
    def raw_data(self) -> dict: ...
    @property
    def raw_code(self) -> int: ...
    @property
    def error(self) -> bool: ...


class MinecraftServer:
    """服务器查询"""
    def __init__(self, client): ...
    """按名称查询服务器"""
    async def select_name(self, name: str): ...
    """按QQ群查询服务器"""
    async def select_qq_group(self, qq_group: int): ...

    @property
    def data(self) -> dict: ...
    @property
    def raw_code(self) -> int: ...
    @property
    def error(self) -> bool: ...


class MinecraftBlacklist:
    """服务器黑名单"""
    def __init__(self, client): ...
    """查询是否在黑名单"""
    async def get_user_info(self, qq: int): ...
    """添加封禁"""
    async def insert_user(self, qq: int, email: str, online_id: str, normal_id: str, reason: str): ...
    """删除封禁"""
    async def delete_user(self, qq: int, id: int): ...

    @property
    def data(self) -> dict: ...
    @property
    def raw_code(self) -> int: ...
    @property
    def error(self) -> bool: ...