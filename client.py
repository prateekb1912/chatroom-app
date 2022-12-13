import asyncio
import websockets

async def echo(websocket):
    async for msg in websocket:
        await websocket.send(msg)

async def main():
    async with websockets.serve(echo, "localhost", 8080):
        await asyncio.Future()

asyncio.run(main())