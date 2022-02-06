import cv2
from tracker import *

def main():
    cap = cv2.VideoCapture(0)
    # Object detection from Stable camera
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
    # Create tracker object
    tracker = EuclideanDistTracker()
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.flip(frame,1,frame)
            height, width, _ = frame.shape
            # print("Frame size: {}x{}".format(width, height))

            # Extract Region of interest
            roi = frame[10: 720, 10: 800]

            #mask = object_detector.apply(frame)
            mask = object_detector.apply(roi)
            _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                # Calculate area and remove small elements
                area = cv2.contourArea(cnt)
                if area > 100:
                    # Show image
                    # cv2.imshow("area",area)
                    cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.imshow('roi', roi)
                    # detections.append([x, y, w, h])
                    # # 2. Object Tracking
                    # boxes_ids = tracker.update(detections)
                    # for box_id in boxes_ids:
                    #     x, y, w, h, id = box_id
                    #     cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
                    #     cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imshow('mask', mask)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print('Error: Cannot read frame')


if __name__ == "__main__":
    main()
