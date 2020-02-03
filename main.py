# -*- utf-8 -*-

import cv2
import pafy
import youtube_dl
import pyocr
from PIL import Image

def main():
    # OCRツール(Tesseractを使う)
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print('no tools')
        return
    tool = tools[0]

    # Youtubeから動画を読み込む
    url = 'https://www.youtube.com/watch?v=bojIHQKjCwo'
    v_pafy = pafy.new(url)
    play = v_pafy.getbest(preftype="webm")
    video = cv2.VideoCapture(play.url)
    if not video.isOpened():
        return
    # fpsを取得
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # 1フレームごとに処理を行なう
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('tube', gray)

        key = cv2.waitKey(fps) & 0xFF
        if key == ord('q'):
            break

    # 文字認識
    txt = tool.image_to_string(image=Image.fromarray(frame),
                               lang='jpn',
                               builder=pyocr.builders.TextBuilder(tesseract_layout=6))

    print(txt)

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
