import cv2
mode = True
def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if mode:
            cv2.circle(img,(x,y),100,(255,0,0),5)
        else:
            cv2.rectangle(img,(x,y),(x+100,y+100),(0,255,0),5)
img = cv2.imread("./1.jpg")     
cv2.namedWindow('1')
cv2.setMouseCallback('1',draw)
while(True):
    cv2.imshow('1',img)
    if cv2.waitKey(20) == ord('m'):
        mode = not mode
    elif cv2.waitKey(20) == 27:
        break
cv2.destroyAllWindows()