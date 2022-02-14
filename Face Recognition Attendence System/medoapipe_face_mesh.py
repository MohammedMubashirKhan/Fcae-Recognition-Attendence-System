import cv2
from matplotlib.pyplot import draw
import mediapipe as mp


class FaceMesh:
    def __init__(self) -> None:
        self.mp_face_mesh = mp.solutions.mediapipe.python.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh()
            
    # It takes a frame of an image and return list of face meshs
    # This function return a list of all face mesh
    def faceMeshDetection (self, image, frame_width,frame_height):
        face_mesh_result = self.face_mesh.process(image)

        face_meshs_custom_landmarks=[]

        if face_mesh_result.multi_face_landmarks:
            for face_landmarks in face_mesh_result.multi_face_landmarks:
                
                face_mesh_custom_landmark = []
                for landmark in face_landmarks.landmark:
                    x = landmark.x * frame_width
                    x = int (x)
                    y = landmark.y * frame_height
                    y = int(y)
                    z = landmark.z 
                    face_mesh_custom_landmark.append((x, y, z))
                face_meshs_custom_landmarks.append(face_mesh_custom_landmark)
                # print((face_meshs_custom_landmarks[0][0][0]))
        return face_meshs_custom_landmarks
    

    # Drawing all point on a face in an image provided to function
    def drawFaceMeshPoints(self, image, face_meshs_custom_landmarks):
  
        for face in face_meshs_custom_landmarks:
            for origin in face:
                x, y, z = origin
                cv2.circle(image, (x, y), 1, color=(0,0,255), thickness=-1)        
        return image

    # Return face location in a list (xmin, ymin, xmax, ymax)
    def extractFace(self, face_meshs_custom_landmarks):
        xmin = 0
        xmax = 0
        ymin = 0
        ymax = 0
        faecLocation = []
        for face in face_meshs_custom_landmarks:
            for origin in face:
                x, y, z = origin
                if(xmin == 0 and xmax == 0):
                    xmin = x
                    xmax = x
                    ymin = y
                    ymax = y

                if xmin > x :
                    xmin = x
                if ymin > y :
                    ymin = y
                if xmax < x :
                    xmax = x
                if ymax < y :
                    ymax = y
            faecLocation.append((xmin,ymin,xmax,ymax))
        return faecLocation
                
                    


        
        
