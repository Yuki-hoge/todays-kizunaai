# search
python search.py >/dev/null 2>&1

# wake up display
tvservice -p
fbset -depth 32
xrefresh -d :0.0
python movemouse.py

# play
mpv --fs --playlist=./playlist.txt
