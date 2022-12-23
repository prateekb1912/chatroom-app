import asyncio
import websockets

# handler for each connection
async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data received as {data}"
    await websocket.send(reply)

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()