import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print('Showing camera feed. Click window or press any key to stop.')
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()

'''cv2.EVENT_MOUSEMOVE: This event refers to mouse movement.
cv2.EVENT_LBUTTONDOWN: This event refers to the left button going down when it is pressed.
cv2.EVENT_RBUTTONDOWN: This event refers to the right button going down when it is pressed.
cv2.EVENT_MBUTTONDOWN: This event refers to the middle button going down when it is pressed.
cv2.EVENT_LBUTTONUP: This event refers to the left button coming back up when it is released.
cv2.EVENT_RBUTTONUP: This event refers to the right button coming back up when it is released.
cv2.EVENT_MBUTTONUP: This event refers to the middle button coming back up when it is released.
cv2.EVENT_LBUTTONDBLCLK: This event refers to the left button being double-clicked.
cv2.EVENT_RBUTTONDBLCLK: This event refers to the right button being double-clicked.
cv2.EVENT_MBUTTONDBLCLK: This event refers to the middle button being double-clicked.
cv2.EVENT_MBUTTONDBLCLK: This event refers to the middle button being double-clicked.
cv2.EVENT_FLAG_LBUTTON: This event refers to the left button being pressed.
cv2.EVENT_FLAG_RBUTTON: This event refers to the right button being pressed.
cv2.EVENT_FLAG_MBUTTON: This event refers to the middle button being pressed.
cv2.EVENT_FLAG_CTRLKEY: This event refers to the Ctrl key being pressed.
cv2.EVENT_FLAG_SHIFTKEY: This event refers to the Shift key being pressed.
cv2.EVENT_FLAG_ALTKEY: This event refers to the Alt key being pressed.
'''