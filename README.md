# Yuuz12-Api
> 文档地址: https://doc.yuuz12.top/web/#/5/
> 
> PYPI 地址: https://pypi.org/project/yuuz12-sdk
> 
> GitHub 仓库: https://github.com/NumberSir/yuuz12-sdk

## 简介
全异步编写，可调用 Yuuz12-Api。需要 Python 3.11+

安装：
```pip install yuuz12-sdk```

## 使用说明
1. 在项目根目录下新建 `.env` 文件，并在其中填写环境变量：
```env
API_VERSION=2            # API 版本，可不填，默认为 2
API_KEY_V1=your_api_key  # v1 API 密钥
API_KEY_V2=your_api_key  # v2 API 密钥
```
2. 请使用 `httpx` 库进行 API 异步调用，使用 `python-dotenv` 库读取环境变量
3. 传入初始化 client 实例化 API 类，并调用对应的 API：
```python
import asyncio
import httpx
import os
from dotenv import load_dotenv
from yuuz12_sdk.apis import User

load_dotenv()

async def main():
    async with httpx.AsyncClient() as client:
        """实例化 API 类"""
        user = User(client)
        # 若 API 版本为 v1:
        # user = User(client, version=1)
        
        """调用 API 方法，需显示传入关键字参数"""
        await user.get_user_info(qq=1234567)
        
        """获取 API 响应体"""
        user.response: httpx.Response
        
        """获取 API 二进制返回信息，如返回图片的 API 可通过此属性获取图片二进制内容"""
        user.raw: bytes
        
        """获取 API 响应是否出错，仅能判断对 API 的调用是否出错，不能判断网络请求本身是否出错"""
        user.error: bool
        
        """以下值仅在该 API 有 json 格式返回信息时才有意义，否则均为 None 或空字典"""
        """获取 API json 格式返回信息，默认为空字典"""
        user.raw_data: dict
        
        """获取 API json 格式返回信息中的具体数据，如 get_user_info 返回数据中的 'user' 键对应值，默认为空字典"""
        user.data: dict | list
        
        """获取 API json 格式返回信息中的响应代码，默认为 None"""
        user.raw_code: int
        
        """获取 API json 格式返回信息中的响应信息，默认为 None"""
        user.raw_msg: str

if __name__ == "__main__":
    asyncio.run(main())
```
4. 使用示例:

```python
"""调用随机选择回声洞中回声信息"""
import asyncio
import httpx
from yuuz12_sdk.apis import Cave


async def main():
    async with httpx.AsyncClient() as client:
        cave = Cave(client)
        await cave.get_cave()
        
    data: dict = cave.data
    qq: int = data["qq"]
    string: str = data["string"]
    time: str = data["time"]

if __name__ == '__main__':
    asyncio.run(main())
```

```python
"""获取签到图片"""
import asyncio
import httpx
from yuuz12_sdk.apis import UserCheck
from yuuz12_sdk.models import UserModel

async def main():
    async with httpx.AsyncClient() as client:
        check = UserCheck(client)
        await check.get(qq=1234567, favorability=1, coin=5)
    
    image_binary: bytes = check.raw

if __name__ == '__main__':
    asyncio.run(main())
```