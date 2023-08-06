from sanic import Sanic
from sanic import response
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY

app = Sanic("MusicApp")

@app.get('/')
async def toggle_music(_):
    win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
    return response.json({}, status=200)