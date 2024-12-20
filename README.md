# Face-Detection
Rectangles drawn around the detected faces.

CODE EXPLANATION:


This code uses OpenCV, a popular computer vision library, to detect faces in an image using the Haar Cascade Classifier method. Let me explain it step by step:

1. Import OpenCV library:
   ======================

   import cv2

   #This imports the OpenCV library, which is used for computer vision tasks like image processing, object detection, and more.


2. Load the Haar Cascade Classifier:
   ================================

   face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

   #cv2.CascadeClassifier is used to load a pre-trained Haar Cascade Classifier for face detection.
   #cv2.data.haarcascades is the path to the directory where OpenCV stores the pre-trained cascade files.
   #"haarcascade_frontalface_default.xml" is a classifier file specifically trained to detect frontal faces.


3. Read the Image:
   ===============

   imp = cv2.imread("A:\\imgpros\\TomHolland.jpg")

   #cv2.imread() reads an image from the given path.
   #"A:\\imgpros\\TomHolland.jpg" is the path to the input image.
   #imp holds the image data in the form of a NumPy array.

4. Convert the Image to Grayscale:
   ==============================

   gim = cv2.cvtColor(imp, cv2.COLOR_BGR2GRAY)

   #cv2.cvtColor() converts the image from BGR (Blue-Green-Red) color space to grayscale.
   #The Haar Cascade Classifier requires grayscale images for processing as it works on pixel intensity, not color.

5. Detect Faces in the Image:
   ==========================

   face = face_classifier.detectMultiScale(gim, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

   #detectMultiScale() is the function used to detect objects (faces in this case).
   Parameters:
   ----------
   #gim: The grayscale image.
   #scaleFactor=1.1: Specifies how much the image size is reduced at each scale. Smaller values increase accuracy but slow down processing.
   #minNeighbors=5: Minimum number of rectangles (detections) a candidate region needs to be considered a face.
   #minSize=(20,20): The minimum size of a face to be detected.
   The function returns a list of detected faces. Each face is represented as a rectangle (x, y, w, h),
   where:
     (x, y) is the top-left corner of the rectangle.
     w and h are the width and height of the rectangle.

6. Draw Rectangles Around Detected Faces:
   =====================================

   for (x, y, w, h) in face:
    cv2.rectangle(imp, (x, y), (x + w, y + h), (2, 22, 222), 4)

   #for loop iterates through all the detected face rectangles.
   #cv2.rectangle() draws rectangles around the detected faces.
   #imp: The original image.
   #(x, y) and (x + w, y + h): Coordinates of the top-left and bottom-right corners of the rectangle.
   #(2, 22, 222): The color of the rectangle in BGR format (a shade of blue).
   #4: The thickness of the rectangle lines.

7. Display the Image with Detected Faces:
   =====================================

   cv2.imshow("pic", imp)

   #cv2.imshow() displays the processed image in a window titled "pic".

8. Wait for a Key Press
   ====================

   cv2.waitKey()

   #cv2.waitKey() waits indefinitely for any key press. Once a key is pressed, the program closes the display window.




   STEPS TO RUN THE CODE:
   


   1. Set Up the Environment:
      =======================

      Make sure you have Python and OpenCV installed on your system.

      Install Python (if not already installed):

      Download and install Python from https://www.python.org/.
      During installation, make sure to check the option "Add Python to PATH".

      Install OpenCV: Run the following command in your terminal or command prompt:
      pip install opencv-python

      This will install the OpenCV library required for the code.

   2. Prepare the Input Image:
      ========================

      Place an image (e.g., TomHolland.jpg) in the path you specify in the code. Update the path in this line:

      imp = cv2.imread("A:\\imgpros\\TomHolland.jpg")

   3. Save the Code to a File:
      =======================
      
      Create a new Python file, for example, face_dect.py.
      Copy and paste the code into the file.
      
   4. Run the Code:
      =============
      
      Open a terminal (Command Prompt or any IDE terminal like VS Code or PyCharm).
      Navigate to the directory where you saved the Python file.

      Run the script using the following command:
      python face_detection.py



      OUTPUT:
      ======
      ![Screenshot 2024-12-20 234021](https://github.com/user-attachments/assets/f330e409-6dcd-4f9d-a093-840023854f46)








   

   


   


   


   
   
   
