import os
import subprocess
import sys
import pathlib
from datetime import datetime

# Config - LANGSUNG KE FILE MANAGER
DOWNLOAD_DIR = "/storage/emulated/0/Download/TDown"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Colors
P = "\033[95m"; C = "\033[96m"; G = "\033[92m"; Y = "\033[93m"
R = "\033[91m"; W = "\033[97m"; D = "\033[90m"; B = "\033[1m"; RESET = "\033[0m"

def clear():
    os.system("clear")

def banner():
    print(f"{P}{B}")
    print("  ████████╗██████╗ ██████╗ ██╗    ██╗███╗   ██╗")
    print("  ╚══██╔══╝██╔══██╗██╔══██╗██║    ██║████╗  ██║")
    print("     ██║   ██║  ██║██║  ██║██║ █╗ ██║██╔██╗ ██║")
    print("     ██║   ██║  ██║██║  ██║██║███╗██║██║╚██╗██║")
    print("     ██║   ██████╔╝██████╔╝╚███╔███╔╝██║ ╚████║")
    print(f"     ╚═╝   ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝{RESET}")
    print(f"{C}  ─────────────────────────────────────────────{RESET}")
    print(f"  {W}T-Down Pro v2.5  •  Anti-429 Bypass  •  Android Client{RESET}")
    print(f"  {D}Save to: {DOWNLOAD_DIR}{RESET}")
    print(f"{C}  ─────────────────────────────────────────────{RESET}")
    print(f"  {D}© 2026 Created by {W}{B}BC-Mrt{D} | All Rights Reserved{RESET}")
    print(f"{C}  ─────────────────────────────────────────────{RESET}\n")

def download(url, quality):
    if not url.strip(): return
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"\n{P}┌─ [{timestamp}] START DOWNLOAD ─────────────────┐{RESET}")
    print(f"{P}│{RESET} {D}Mode:{RESET} {C}{quality}{RESET}")
    print(f"{P}└──────────────────────────────────────────────┘{RESET}\n")

    base_args = [
        "yt-dlp",
        "--extractor-args", "youtube:player_client=android",
        "--js-runtimes", "node",
        "--no-warnings",
        "--progress",
        "--concurrent-fragments", "4",
    ]

    if quality == "mp3":
        cmd = base_args + ["-x","--audio-format","mp3","--audio-quality","0","-o",f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",url]
    elif quality == "1080p":
        cmd = base_args + ["-f","bv*[height<=1080]+ba/best[height<=1080]/best","-o",f"{DOWNLOAD_DIR}/%(title)s.%(ext)s","--no-playlist",url]
    elif quality == "720p":
        cmd = base_args + ["-f","bv*[height<=720]+ba/best[height<=720]/best","-o",f"{DOWNLOAD_DIR}/%(title)s.%(ext)s","--no-playlist",url]
    else:
        cmd = base_args + ["-f","bv*+ba/best","-o",f"{DOWNLOAD_DIR}/%(title)s.%(ext)s","--no-playlist",url]

    result = subprocess.run(cmd)
    if result.returncode == 0:
        print(f"\n{G}{B}  ✅ BERHASIL BOS! Cek di File Manager > Download > TDown{RESET}")
    else:
        print(f"\n{R}  ❌ GAGAL. Coba link lain bos{RESET}")

def main():
    clear(); banner()
    print(f"{W}Pilih Kualitas:{RESET}")
    print(f"  {P}[1]{RESET} Best Quality {G}← Recommended{RESET}")
    print(f"  {P}[2]{RESET} 1080p Full HD")
    print(f"  {P}[3]{RESET} 720p Hemat Kuota")
    print(f"  {P}[4]{RESET} MP3 Audio Only")
    print(f"  {P}[0]{RESET} Keluar\n")
    q_map = {"1":"best","2":"1080p","3":"720p","4":"mp3"}
    pilih = input(f"{C}Pilih [1-4] > {RESET}").strip()
    if pilih=="0": sys.exit()
    quality = q_map.get(pilih,"best")
    print(f"\n{Y}Paste link, ketik 'q' buat keluar.{RESET}\n")
    while True:
        try:
            url = input(f"{P}┌─[ {G}T-Down {P}]─[ {W}{quality} {P}]\n{P}└──> {W}").strip()
        except KeyboardInterrupt:
            break
        if url.lower() in ["q","quit","exit"]: break
        if url: download(url, quality); print(f"\n{D}──────────────────────────────────────{RESET}\n")

if __name__ == "__main__":
    main()
