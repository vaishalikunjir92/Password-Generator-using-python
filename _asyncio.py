import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1) # pause for 1 second
    print("World")

asyncio.run(greet())