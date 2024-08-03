import cv2
import cv2.aruco as aruco

def findArucoMarkers(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_APRILTAG_36H11')
    arucoDict = aruco.getPredefinedDictionary(key)
    arucoParam = aruco.DetectorParameters()
    bboxs, id, rejected = aruco.detectMarkers(imgGray,arucoDict, parameters=arucoParam)

    if True:
        aruco.drawDetectedMarkers(img, bboxs)
    return [bboxs, id]

def coordinates(bbox, id, img):

    topleftx, toplefty = bbox[0][0][0], bbox [0][0][1]
    toprightx, toprighty = bbox[0][1][0], bbox [0][1][1]
    bottomrightx, bottomrighty = bbox[0][2][0], bbox [0][2][1]
    bottomleftx, bottomlefty = bbox[0][3][0], bbox [0][3][1]

    centery = (toplefty + bottomrighty) / 2
    centerx = (topleftx + bottomrightx) / 2

    for detectedID in id:
        print(str(detectedID) + " ID AprilTag's center coordinates are " + "x: " + str(centerx) + " " + "y: " + str(centery))

    if 275 < centerx < 320:
        print("CENTER!!")
    return img

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    while True:
        success, img = cap.read()
        arucoFound = findArucoMarkers(img)

        if len(arucoFound[0])!=0:
            for bbox, id in zip(arucoFound[0], arucoFound[1]):
                img = coordinates(bbox, id, img)

        cv2.imshow("Image", img)
        cv2.waitKey(10)

main()
