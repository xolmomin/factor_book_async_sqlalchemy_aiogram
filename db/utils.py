import asyncio
import time
from typing import Any, List, Dict, Union
import requests
from sqlalchemy.engine import Dialect
from sqlalchemy_file import ImageField

import aiohttp


#
# async def upload_file(img_bytes):
#     url = 'https://telegra.ph/upload'
#
#     print(1243433)
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, data={'file': img_bytes}) as response:
#             if response.status == 200:
#                 data = await response.json()
#                 return "https://telegra.ph" + data[0]['src']
#             print(f"Error uploading file: {response.status}")
#     return
def upload_file(img_bytes):
    url = 'https://telegra.ph/upload'
    response = requests.post(url, files={'file': img_bytes})
    if response.status_code == 200:
        return "https://telegra.ph" + response.json()[0]['src']
    print(f"Error uploading file: {response.status_code}")
    return


class CustomImageField(ImageField):

    def process_bind_param(self, value: Any, dialect: Dialect) -> Union[None, Dict[str, Any], List[Dict[str, Any]]]:
        data = {
            'telegra_image_url': upload_file(value.file)
        }
        value.update(data)
        return super().process_bind_param(value, dialect)
