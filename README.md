# capture_tube

YouTubeから動画を引っ張ってきて文字認識を行なう。

## modules

- cv2
- pafy
- youtube_dl
- pyocr
- PIL

## tools

- Tesseract OCR

### install

各モジュールをインストール

```
pip install cv2 pafy youtube_dl pyocr
```

OCRツールをインストール

```
brew install tesseract
```

多言語の解析ができるようにデータをインストール

```
brew install tesseract-lang
# 使用言語確認
tesseract --list-langs
```
