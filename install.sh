#!/data/data/com.termux/files/usr/bin/bash
echo "--- Installer T-Down Pro v2.5 by BC-Mrt ---"
pkg install python ffmpeg yt-dlp nodejs -y
cp tdown.py $HOME/
echo '#!/data/data/com.termux/files/usr/bin/bash
cd $HOME
python tdown.py' > $PREFIX/bin/tdown
chmod +x $PREFIX/bin/tdown
chmod +x $HOME/tdown.py
mkdir -p /storage/emulated/0/Download/TDown
echo "✅ BERHASIL! Ketik tdown - © BC-Mrt"
