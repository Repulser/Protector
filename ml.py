from typing import Tuple, Optional

import aiohttp

import utils

session = aiohttp.ClientSession()
config = utils.load_config()


async def predict(content: str) -> Optional[Tuple[str, float]]:
    """
    Prediction API Wrapper.
    :param content: Content of message
    :return:
    """
    base_url = config['api_base']
    async with session.get(f'{base_url}/predict?content={content}') as response:
        if response.status != 200:
            print(await response.text())
            return None
        prediction = await response.json()
    return prediction["classification"], prediction["score"]
