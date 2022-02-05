import os

import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
filename = 'record-' + str(datetime.timestamp(datetime.now())) + '.mp4'
frames_per_sec = 24.0
resolution = '720p'


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


# Standard Video Dimensions Sizes
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height


VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


output_path = os.path.join('data', filename)
out = cv2.VideoWriter(output_path, get_video_type(filename), 25, get_dims(cap, resolution))


def main():
    print(filename)
    while True:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow("Recording", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
