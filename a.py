import asyncio
import aiofiles
from random import choice

a = [x for x in range(1000)]

async def run_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()

async def run():
    async with aiofiles.open("a.txt", "w") as f:
        await f.write(str(choice(a)))
    await run_cmd("git add --all && git commit -m 'a'")

async def main():
    i = 0
    for _ in range(100000000000):
        for __ in range(1000):
            i += 1
            await run()
            print(i)
        await run_cmd("git push")

asyncio.run(main())
