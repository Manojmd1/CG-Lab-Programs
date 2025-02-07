import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Read the input image (replace 'your_image.jpg' with the actual image path)
image_path = 'test2.png'
image = cv2.imread("test2.png")

# Check if the image was loaded successfully
if image is None:
    raise ValueError(f"Image not found or unable to load: {image_path}")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Save or display the result
cv2.imwrite('detected_faces.png', image)  # Save the result
cv2.imshow('Detected Faces', image)  # Display the result
cv2.waitKey(0)
cv2.destroyAllWindows()
