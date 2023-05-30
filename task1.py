from keras.models import load_model
import cv2
import numpy as np 


class Task1:
    def __init__(self, index):
        self.index = index
        self.stopped = False 
        self.is_activated = False
        print("Init task 1", index)

        np.set_printoptions(suppress=True)
        # Disable scientific notation for clarity

        # Load the model
        self.model = load_model("keras_model.h5", compile=False)

        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        self.camera = cv2.VideoCapture(index)

        # Add a variable to track the number of consecutive failed attemps
        self.failed_attempts = 0 
        self.max_failed_attempts = 3 

        return

    def Task1_Run(self):
        if not self.is_activated:
            print("2 camera task, camera", self.index, "is activated")
        self.is_activated = True

        while not self.stopped:
            # Grab the webcamera's image.
            ret, image = self.camera.read()
       
            if not ret:
                self.failed_attempts += 1
                print("Failed to capture image from camera", self.index)
                if self.failed_attempts >= self.max_failed_attempts:
                    print("Maximum number of consecutive failed attempts reached. Please try to connect cameras again")
                    self.stopped = True
                continue
            
            #Reset failed attempts counter
            self.failed_attempts = 0 
            
            # Resize the raw image into (224-height,224-width) pixels
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

            # Show the image in a window
            cv2.imshow("Webcam Image", image)

            # Make the image a numpy array and reshape it to the models input shape.
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

            # Normalize the image array
            image = (image / 127.5) - 1

            # Predicts the model
            prediction = self.model.predict(image)
            index = np.argmax(prediction)
            class_name = self.class_names[index]
            confidence_score = prediction[0][index]

            # Print prediction and confidence score
            print("Class:", class_name[2:], end="")
            print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
            cv2.waitKey(1)

task1 = Task1(1) 
task1.Task1_Run()