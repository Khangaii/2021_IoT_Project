import cv2

# 카메라로부터 VideoCapture 객체 생성
cap = cv2.VideoCapture(0)

if not cap.isOpened():
  print('Camera open failed')
  exit()

# fourcc(four character code)
# DIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')    # ('D', 'I', 'V', 'X')

# 동영상 저장을 위한 VideoWriter 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))


while True:
  ret, frame = cap.read()   # 한 프레임 받아오기
  if not ret:
    break

  cv2.imshow('frame', frame)  # 현재 프레임 영상 출력
  out.write(frame)

  if cv2.waitKey(10) == 27:   # 10ms 기다린 후 다음 프레임 처리
    break

# 사용자 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()
