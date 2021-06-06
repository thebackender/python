import asyncio

async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    print("continue")
    await task
    print("finish")

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())