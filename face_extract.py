import cv2
import os
import pickle

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter Name

try:
    #os.mkdir("dataset")
    names=pickle.load(open("names.dat","rb"))
    id_list=pickle.load(open("id_list.dat","rb"))
except FileNotFoundError:
    names=['None']
    id_list=[]
    print ("Name file is not present, skipping the reading process...")	
except :
    print("folder exists")
face_name = input('\n enter name  and press <return> ==>  ')

if id_list==[]:
    face_id = 1
else:
    face_id = int(id_list[len(id_list)-1]+1)

names.append(face_name)
id_list.append(face_id)
pickle.dump(names,open("names.dat","wb"))
pickle.dump(id_list,open("id_list.dat","wb"))

print("\n INFO---> Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        #cv2.imwrite("dataset/"+str(face_name)+'.' + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imwrite("/home/samyak/Desktop/Face_Recognition-master/dataset/"+str(face_name)+'.' + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        #cv2.imwrite("sam.jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 25: # Take  face sample and stop video
         break

# Do a bit of cleanup
print("\n INFO---> Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


    
