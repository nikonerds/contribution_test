import asyncio
import aiofiles

async def run(i):
    async with aiofiles.open("a.txt", "a") as f:
        await f.write("a")
    proc = await asyncio.create_subprocess_shell(
        "git add --all && git commit -m 'a'",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    await proc.communicate()
    print(i)

async def main():
    for i in range(100000000000000000000000000):
        await run(i)
asyncio.run(main())
