import json
import subprocess

with open("channels.json") as f:
    channels = json.load(f)

playlist = "#EXTM3U\n"

for ch in channels:
    try:
        stream = subprocess.check_output(
            ["yt-dlp","-g",ch["url"]],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        playlist += f'#EXTINF:-1 tvg-logo="{ch["logo"]}",{ch["name"]}\n'
        playlist += stream + "\n"

    except:
        print("Offline:", ch["name"])

with open("playlist.m3u8","w") as f:
    f.write(playlist)
