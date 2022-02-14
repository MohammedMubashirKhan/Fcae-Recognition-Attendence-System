import cv2
from cv2 import destroyWindow
import medoapipe_face_mesh


localMP = medoapipe_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)
frame_width = cap.get(3)
frame_height = cap.get(4)

while(True):
    success, frame = cap.read()
    if success != True:
        print("Video has ended")
        break

    frameRGB = frame[:,:,::-1]

    # processing face mesh and storing all point in a list in pixel form
    face_meshs_custom_landmarks = localMP.faceMeshDetection(frameRGB, frame_width=frame_width, frame_height=frame_height)


    
    frame = localMP.drawFaceMeshPoints(frame, face_meshs_custom_landmarks=face_meshs_custom_landmarks)

    faceLocation = localMP.extractFace(face_meshs_custom_landmarks=face_meshs_custom_landmarks)
    
    
    
    
    
    
    
    # If face is present in an Image the this will croped face and display in other window
    # and if face is out of frame then it will destroy the croped window
    if faceLocation:
        face1 = faceLocation[0]
        cv2.imshow("Croped", frame[face1[1]:face1[3],face1[0]:face1[2]])
    else:
        try:
            cv2.destroyWindow(winname="Croped")
        except:
            pass
    
    cv2.imshow("frame", frame)
    cv2.waitKey(1)