import whisper
 
## モデル（データセット）読み込み
model = whisper.load_model("small")
 
## 音声へのパス
path ="C:\\Users\\asd-0\\Downloads\\Convert_20230407_140202.mp3"
 
## 結果を出力と同時に取得
result = model.transcribe(path, verbose=True, language='ja')