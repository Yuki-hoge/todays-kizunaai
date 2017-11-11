# Today's KizunaAI
## What's this?
今日アップロードされたキズナアイさんの動画を検索し，再生します．
## What do these files do?
- todays-kizunaai.sh
  - 再生開始
- goodbye-kizunaai.sh
  - 再生終了，プロセス消去
- movemouse.py
  - マウスを動かすためのコマンドです．ディスプレイを復帰させるのに使います，現在の音声のみ再生の仕様では使いません
- myenv.py.sample
  - YouTubeのapiを叩くようのapiキーを設定するファイルのサンプルです．中の値を適切なapiキー(自作して下さい)で設定したらmyenv.pyにリネームして下さい．
- playlist.txt
  - 検索してヒットした動画のリストが格納されます．
- search.py
  - youtubeのapiを叩いてキズナアイさんが今日上げた動画を検索し，playlist.txtに格納します．検索の際に一件以上ヒットした場合playlist.txtを書き換えますが，まだ今日動画が上がってない場合は書き換えず，前の検索結果を維持する仕様になっています．
## How to use?
### Requirements
- mpv(動画再生に使います)
- python
  - (pyautogui)(現在の仕様では必要ありません，将来的に使います)
### Play Tpday's KizunaAI
./todays-kizunaai.sh
### Stop and quit for playing
./goodbye-kizunaai.sh
