import asyncio
import websockets

async def echo(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"Echo: {message}")
            print(f"Sent: Echo: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def main():
    server = await websockets.serve(echo, "127.0.0.1", 8765)  # You can change 8765 to any port you prefer
    print("Server started at ws://127.0.0.1:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
