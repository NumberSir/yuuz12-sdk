class Invitation:
    """邀请码相关"""
    def __init__(self, client): ...
    """获取邀请码"""
    async def obtain_invitation_codes(self, qq: int): ...
    """查询邀请码"""
    async def query_invitation_codes(self, qq: int): ...

    @property
    def data(self) -> dict: ...
    @property
    def raw_code(self) -> int: ...
    @property
    def error(self) -> bool: ...