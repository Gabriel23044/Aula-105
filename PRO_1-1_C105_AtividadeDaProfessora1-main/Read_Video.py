import cv2
vid = cv2.VideoCapture(2)
#vid = cv2.VideoCapture('C:/Users/Familia/Desktop/PRO_1-1_C105_AtividadeDaProfessora1-main/AnthonyShkraba.mp4')
if vid.isOpened()==False:
    print('não foi possivel ver o video :/')
    
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))    
print(height)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))    
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'),160,(width,height))

while True:
    ret,frame = vid.read()
    
    cv2.imshow('Web cam',frame)
    out.write(frame)
    if cv2.waitKey(1)==32:
        break
    
vid.release()
out.release()
cv2.destroyAllWindows()
