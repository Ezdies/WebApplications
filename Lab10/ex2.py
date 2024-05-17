import asyncio
import websockets

async def hello():
    async with websockets.connect("wss://echo.websocket.org") as websocket:
        print("Connection established")
        
        message = "Hello"
        await websocket.send(message)
        print(f"Sent: {message}")
        
        response = await websocket.recv()
        print(f"Received: {response}")
        
asyncio.run(hello())
