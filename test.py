# -*- coding: utf-8 -*-

import cv2
import pafy
import youtube_dl

def main():
    src = 'test.mp4'
    video = cv2.VideoCapture(src)
    if not video.isOpened():
        return
    # fpsを取得
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # 分類器を作成
    cascade_file = 'lbpcascade_animeface.xml'
    clf = cv2.CascadeClassifier(cascade_file)

    # 1フレームごとに処理を行なう
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        # グレイスケール→二値化
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 検出
        faces = clf.detectMultiScale(gray)
        # 描画
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0 ,255), 2)

        cv2.imshow('tube', frame)

        key = cv2.waitKey(fps) & 0xFF
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def dl(url):
    ydl = youtube_dl.YoutubeDL({'outtmple': '%(id)s%(ext)s', 'format': '137'})

    with ydl:
        result = ydl.extract_info(url, download=True)


if __name__ == '__main__':
    main()
