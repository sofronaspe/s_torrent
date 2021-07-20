# S_Torrent is a python based torrent application
# By Peter Sofronas

# The goal of this program is to download the iso listed in test/

import asyncio
from random import randint
import modules.Interpreter as Interpreter

async def connect(ip, port):
    print(f"Connecting to {ip}")
    reader, writer = await asyncio.open_connection(ip, port)

    print(f"Connection established with {ip}")
    await asyncio.sleep(randint(0, 5))

    writer.close()
    print(f"Connection with {ip} closed")

if __name__ == '__main__':
    # # basically the core of all async apps
    # loop = asyncio.get_event_loop()
    #
    # # Run each function. When you hit await, run the next function until the previous await gets returned
    # work = [
    #     asyncio.ensure_future(connect('1.1.1.1', '53')),
    #     asyncio.ensure_future(connect('1.0.0.1', '53')),
    # ]
    #
    # loop.run_until_complete(asyncio.gather(*work))
    interpreter = Interpreter.Interpreter()
    # assert(interpreter.decode(b'i42e') == [42])
    # assert(interpreter.decode(b'i-42e') == [-42])
    assert(interpreter.decode(b'i32ei41e') == [32,41])