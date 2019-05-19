# /usr/bin/env python
# coding:utf-8
"""
    MOT多目标追踪
======================
OpenCV_version = 3.4.4
Author @ WUD
"""
import cv2


class Mot_Tracker:
    def __init__(self):
        pass

    def Tracking(self, Video_Stream):
        print('Select 3 tracking targets')

        cv2.namedWindow("tracking")
        camera = cv2.VideoCapture(Video_Stream)
        tracker = cv2.MultiTracker_create()  # 多目标追踪
        init_once = False

        ok, image = camera.read()
        if not ok:
            print('Failed to read video')
            exit()

        bbox1 = cv2.selectROI('tracking', image)
        bbox2 = cv2.selectROI('tracking', image)
        bbox3 = cv2.selectROI('tracking', image)

        while camera.isOpened():
            ok, image = camera.read()
            if not ok:
                print('no image to read')
                break

            if not init_once:
                ok = tracker.add(cv2.TrackerMIL_create(), image, bbox1)
                ok = tracker.add(cv2.TrackerMIL_create(), image, bbox2)
                ok = tracker.add(cv2.TrackerMIL_create(), image, bbox3)
                init_once = True

            ok, boxes = tracker.update(image)
            print(ok, boxes)

            for newbox in boxes:
                p1 = (int(newbox[0]), int(newbox[1]))
                p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
                cv2.rectangle(image, p1, p2, (200, 0, 0))

            cv2.imshow('Motracking', image)
            k = cv2.waitKey(1)
            if k == 27:
                break  # esc pressed


if __name__ == '__main__':
    Video_Stream = "Mot_Test_video.mp4"
    Mot_Tracker().Tracking(Video_Stream)
