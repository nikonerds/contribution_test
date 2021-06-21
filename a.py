import asyncio
import aiofiles

async def run():
    async with aiofiles.open("a.txt", "a") as f:
        await f.write("a")
    proc = await asyncio.create_subprocess_shell(
        "git add --all && git commit -m 'a'",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    await proc.communicate()

async def main():
    for i in range(1000):
        tasks = [run() for _ in range(100)]
        await asyncio.gather(*tasks)

asyncio.run(run())
