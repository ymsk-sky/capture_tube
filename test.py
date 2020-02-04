# -*- utf-8 -*-

import cv2
import pafy
import youtube_dl

def main():
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

        # グレイスケール→二値化
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

        cv2.imshow('tube', binary)

        key = cv2.waitKey(fps) & 0xFF
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
