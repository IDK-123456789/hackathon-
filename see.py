import cv2
import os

# Set the folder where you want to save images
save_folder = os.path.join(os.getcwd(), "captured")
os.makedirs(save_folder, exist_ok=True)

# Open the default camera (0) (used AI to generate the code)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

ret, frame = cap.read()
if ret:
    img_path = os.path.join(save_folder, "captured_image.jpg")
    cv2.imwrite(img_path, frame)
    print(f"Image saved at {img_path}")
else:
    print("Failed to capture image")

cap.release()

# Display the captured image
cv2.imshow("Captured Image", frame)
cv2.waitKey(3000)  # Display for 5 seconds

cv2.destroyAllWindows()