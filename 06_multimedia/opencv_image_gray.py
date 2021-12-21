import cv2

# image 파일 읽기
img = cv2.imread('markiplier.jpg')
img2 = cv2.resize(img, (700, 620))

# 색상 변환하기
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# image 파일 일기
cv2.imshow('Markiplier_original', img)
cv2.imshow('Markiplier_resize', img2)
cv2.imshow('Markiplier_gray', gray)

# 키보드 입력을 기다림 (millisecond)
# 기본값 0, 0인 경우 키보드 입력이 있을 때까지 계속 기다림
# ENTER: 13, ESC: 27
while True:
  if cv2.waitKey(0) == 13:
    break

# 파일 저장하기
cv2.imwrite('Markiplier_GRAY.jpg', gray)

# 열려있는 모든 창 닫기
cv2.destroyAllWindows()