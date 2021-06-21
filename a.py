import asyncio
import aiofiles
from random import randint

async def run():
    async with aiofiles.open("a.txt", "a") as f:
        await f.write("a")
    proc = await asyncio.create_subprocess_shell(
        "git add --all && git commit -m 'a'",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    await proc.communicate()
    print(randint(10, 100))

async def main():
    for i in range(100):
        await run()
asyncio.run(main())
