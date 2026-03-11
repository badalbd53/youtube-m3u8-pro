import json
import subprocess

playlist = "#EXTM3U\n"

try:
    with open("channels.json") as f:
        channels = json.load(f)
except:
    channels = []

for ch in channels:
    try:
        result = subprocess.check_output(
            ["yt-dlp", "-f", "best", "-g", ch["url"]],
            stderr=subprocess.DEVNULL
        ).decode().splitlines()

        if len(result) > 0:
            stream = result[0]

            playlist += f'#EXTINF:-1 tvg-logo="{ch["logo"]}",{ch["name"]}\n'
            playlist += stream + "\n"

    except Exception as e:
        print("Skip:", ch["name"])

with open("playlist.m3u8", "w") as f:
    f.write(playlist)
