import sys
sys.path.append('C:\\Users\\User\\Desktop\\Projests Practicing for self\\Image Processing\\Face Recognition Attendence System\\Face Mesh')
import cv2
import medoapipe_face_mesh



def registerStudent():
    studentDetails = getStudentDetails()
    startCamera(studentDetails["camNumber"])


# This function get student details such as UIN, Name, webcam Number from keyboard 
def getStudentDetails():
    UIN = input("Enter your UIN\n")
    name = input("Enter your name\n")
    # we will use this in future for to take video from a mp4 file instead of a webcam
    camNumber = input("Enter Camera Number as zero '0'\n")
    if camNumber != "0":
        print("!!!!!!!!!!!!! Please follow the instruction correctly !!!!!!!!!!!!\n")
        print("!!!!!!!!!!!! You were told to put camera number as zero'0' !!!!!!!!!!!!\n")
        camNumber = "0"
    return {"UIN":UIN,"name":name,"camNumber":camNumber}
    
# start camera to detect face
def startCamera(camNumber):
    localMP = medoapipe_face_mesh.FaceMesh()
    cap = cv2.VideoCapture(int(camNumber))
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





# def switch(case):
#     print(case)
#     # switchCase = {"isRegistration":registerStudent()
#     # }
#     if case = 
#     # return switchCase.get(case, print("Please select a valid input")) 

isRegistration = input("Are you here to register as a student (Y / N)\n")
if isRegistration == "Y" or isRegistration == "y":
    # print(isRegistration)
    registerStudent()




