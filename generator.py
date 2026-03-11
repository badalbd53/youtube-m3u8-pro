import json
import subprocess

with open("channels.json") as f:
    channels = json.load(f)

playlist = "#EXTM3U\n"

for ch in channels:
    try:
        stream = subprocess.check_output(
            ["yt-dlp","-f","best","-g",ch["url"]],
            stderr=subprocess.DEVNULL
        ).decode().splitlines()[0]

        playlist += f'#EXTINF:-1 tvg-logo="{ch["logo"]}",{ch["name"]}\n'
        playlist += stream + "\n"

    except Exception as e:
        print("Error:", ch["name"], e)

with open("playlist.m3u8","w") as f:
    f.write(playlist)
