import cv2 as cv
import logging
import os
import random
import string 
#print (cv.__version__)

video_path='C:/Users/Administrator/Desktop/python course/Video/videos/vacas.mp4'
save_path='C:/Users/Administrator/Desktop/python course/Video/fotos'
def rand_string(length):
    rand_str=(''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for i in range(length)))
    print (length)       
    return rand_str

def length_of_video ( video_path ) :
    cap = cv.VideoCapture(video_path)
    length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    return length
    print(length)
def extracting_frames (video_path, save_path, skip_frames = 30):

    print("******Entering extracting phase******")
file_name=os.path.split(video_path)

file_name_without_ext=os.path.splitext("test.mp4")[0]

length=length_of_video(video_path)
print(length)

if length==0:
    print('length=0, exit')

    #return 0
cap=cv.VideoCapture(video_path)
count=0
random_string=rand_string(5)

ret,frame=cap.read()
test_file_path=os.path.join(
    save_path,
    file_name_without_ext[:6]+\
        '{}_{}.jpg'.format(random_string,count))
cv.imwrite(test_file_path,frame)
if os.path.isfile(test_file_path):
    print("saving test sucefully and continue extracting")
    count=1
    skip_frames=1
    while ret:
        ret,frame=cap.read()
        if ret and count % skip_frames==0:
            cv.imwrite(os.path.join(save_path,
            file_name_without_ext[:6]+
        '{}_{}.jpg'.format(random_string,count)),frame)
        else:
            count+=1
        print(count)
else:
    print('Problem with save the file')
   # return 0
cap.release()
print('*******FINALIZANDO EXTRAÇÂO******')

if __name__=='__main__':
    public_movies=["vacas.mp4"]
    save_path='C:Users/Administrator/Desktop/python course/Video/fotos'
    for movie in public_movies:
        print(movie)
        extracting_frames(movie,save_path, skip_frames=30)

