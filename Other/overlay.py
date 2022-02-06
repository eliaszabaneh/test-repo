import cv2
from datetime import datetime
from datetime import timedelta


# import numpy as np


def showthis_frame(f, t):
    if f is not None:
        timestr = "frame at " + str(t)
        cv2.imshow(timestr, f)
    else:
        print("No frame")


def main():
    cam = cv2.VideoCapture(0)
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
    starttime = datetime.now()
    count_idx = 3
    images = []
    # FramesArray = np.array(images)
    while True:
        ret, frame = cam.read()
        if ret:
            #            print("Start time: ", starttime)
            frame = cv2.flip(frame, 1)
            cv2.putText(frame, datetime.strftime(datetime.now(), "%S:%f"), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)
            if (datetime.now() - starttime > timedelta(seconds=3)) and (count_idx > 0):
                print("3 seconds have lapsed: ", datetime.now())
                images.append(frame)
                showthis_frame(frame, datetime.now())
                starttime = datetime.now()
                count_idx -= 1
            else:
                if count_idx == 0:
                    print(len(images))
                    print(str(count_idx))
                    for i in range(len(images) - 1):
                        newoutput = cv2.addWeighted(images[i], 0.8, images[i + 1], 0.2, 0)
                        # subimg = cv2.subtract(images[i], images[i + 1])
                        # cv2.imshow("subtraction", subimg)
                        # diffimg = cv2.absdiff(images[i], images[i + 1])
                        # cv2.imshow("difference", diffimg)
                        # add1 = images[i] + images[i + 1]
                        # cv2.imshow("addition", add1)
                        cv2.imshow("Overlay", newoutput)
                    count_idx = -1
            cv2.imshow("test", frame)
            out.write(frame)
            key = cv2.waitKey(10)
            if key == 27:
                break
        else:
            break
    out.release()
    cam.release()
    cv2.destroyAllWindows()

    # img = cv2.imread("images/test1.jpg")
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    # canny = cv2.Canny(img, 50, 150)
    # cv2.imshow("canny", canny)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
