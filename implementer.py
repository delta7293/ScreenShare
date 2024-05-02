import asyncio      # importing asyncio library #
import websockets   # importing websocket library #
import pyautogui    # importing pyautogui library #
# Asynchronous function receive the message from client #
async def handler(websocket, path):
    async for message in websocket:
        try:
            pointer = message.split(',')
            pyautogui.moveTo(int(pointer[0]), int(pointer[1]))
            print('X : ', pointer[0])
            print('Y : ', pointer[1])
        except:
            pass
# Iinitating the server #
start_server = websockets.serve(handler, "localhost", 5000)
# Run's the server continuously #
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()