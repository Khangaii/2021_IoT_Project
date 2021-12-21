import cv2

# image 파일 읽기
img = cv2.imread('markiplier.jpg')
img2 = cv2.resize(img, (700, 620))

# imshow(윈도우이름, 출력할 영상데이터)
cv2.imshow('Markiplier', img2)

# Edge선 추출하기
edge = cv2.Canny(img, 50, 100)

cv2.imshow('edge', edge)

# 키보드 입력을 기다림 (millisecond)
# 기본값 0, 0인 경우 키보드 입력이 있을 때까지 계속 기다림
# waitkey()를 호출해야 화면에 영상이 나타남
cv2.waitKey(0)

# 열려있는 모든 창 닫기
cv2.destroyAllWindows()
