class BaiduCensor:
    """百度相关"""
    def __init__(self, client): ...
    """图片色情内容审核"""
    async def censor(self, imgurl: str): ...

    @property
    def data(self) -> dict: ...
    @property
    def raw_code(self) -> int: ...
    @property
    def error(self) -> bool: ...