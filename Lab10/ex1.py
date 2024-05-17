import asyncio
import websockets

async def hello():
    async with websockets.connect("wss://echo.websocket.org") as websocket:
        print("Connection established")

asyncio.run(hello())
