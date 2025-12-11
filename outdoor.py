def outdoor_function(self):

    import cv2
    import pyttsx3

    engine=pyttsx3.init()
    thres = 0.95
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    cap.set(10,70)

    classNames= []
    classFile = 'coco.data'
    with open(classFile,'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'
    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/ 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    while True:
        success,img = cap.read()
        classIds, confs, bbox = net.detect(img,confThreshold=0.45)
        if len(classIds) != 0:
            for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                object_name=(classNames[classId-1])
                object_id=[classId-1]
                print(object_id)


                if object_id ==[2]:
                     print(" car ")
                     # ser1.write(b'A')
                     cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                     cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30),cv2.FONT_HERSHEY_COMPLEX, 1, (255,192, 203), 2)
                     cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),cv2.FONT_HERSHEY_COMPLEX, 1, (255,192, 203), 2)
                     # print(" bicycle detect")
                     pyttsx3.speak("car detected")
                     cv2.rectangle(img, box, color=(255,192, 203), thickness=2)

                if object_id == [3]:
                    print("motorcycle")
                    # ser1.write(b'A')
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (255,192, 203), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255,192, 203), 2)
                    # print(" bicycle detect")
                    pyttsx3.speak("motorcycle detected")
                    cv2.rectangle(img, box, color=(255,192, 203), thickness=2)

                if object_id == [5]:
                    print("bus")
                    # ser1.write(b'A')
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1], (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (255,192, 203), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255,192, 203), 2)
                    # print(" bicycle detect")
                    pyttsx3.speak("bus detected")
                    cv2.rectangle(img, box, color=(255,192, 203), thickness=2)


        cv2.imshow("Output",img)
        cv2.waitKey(1)


