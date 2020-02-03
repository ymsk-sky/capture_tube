# -*- utf-8 -*-

import cv2
import pafy
import youtube_dl

def main():
    url = 'https://www.youtube.com/watch?v=bojIHQKjCwo'
    v_pafy = pafy.new(url)
    play = v_pafy.getbest(preftype="webm")

    video = cv2.VideoCapture(play.url)

    if not video.isOpened():
        return

    fps = int(video.get(cv2.CAP_PROP_FPS))

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        cv2.imshow('tube', frame)

        key = cv2.waitKey(fps) & 0xFF
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
