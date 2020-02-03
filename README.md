# capture_tube

YouTubeから動画を引っ張ってきて文字認識を行なう。

## modules

- cv2
- pafy
- youtube_dl

## tools

- Tesseract OCR

### install

各モジュールをインストール

```
pip install cv2 pafy youtube_dl
```

OCRツールをインストール

```
brew install tesseract
```

日本語の解析ができるようにデータをインストール

```
brew install tesseract-lang
```
