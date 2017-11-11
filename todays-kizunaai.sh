# search
python search.py >/dev/null 2>&1

# wake up display
# tvservice -p
# fbset -depth 16
# fbset -depth 32
# xrefresh -d :0.0
python movemouse.py

# play
chromium-browser `cat playlisturl.txt` --window-size=1920,1080 --window-pos=0,0
