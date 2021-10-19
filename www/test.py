# test.py

import asyncio
import orm
from models import User


async def test(loop):
    await orm.create_pool(user='root', password='passw0rd', db='awesome', loop=loop)
    u = User(name='Michael', email='1486749400@qq.com', passwd='slfe0sdjfds', image='abut:blank')
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
