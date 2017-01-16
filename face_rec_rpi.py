import cv2, sys, numpy, os, pyttsx, time, picamera, io
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)

print('Training...')
# Create a list of images and a list of corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (112, 92)

# Create a Numpy array from the two lists above
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

model = cv2.createLBPHFaceRecognizer()
model.train(images, labels)

#use LBPHFace recognizer on camera frame
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = picamera.PiCamera()
webcam.resolution = (320, 240)


def getFrame():
    jpegBuffer = io.BytesIO()
    webcam.capture(jpegBuffer, format='jpeg')
    buff = numpy.fromstring(jpegBuffer.getvalue(), dtype=numpy.uint8)
    return cv2.imdecode(buff, 1)


while True:
    im = getFrame()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        #Try to recognize the face
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if prediction[1]<120:
		
	        cv2.putText(im,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
	        engine.say('Hello')
                engine.say(names[prediction[0]],prediction[1])
                engine.say('Have a good day')
                time.sleep(0.3)
		  

    	else:
		cv2.putText(im,'not recognized',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
	  	engine.say('It is an unknown face')
	  	time.sleep(0.3)
		
	engine.runAndWait()
	#cv2.imshow('OpenCV', im)
	#key = cv2.waitKey(10)
	#if key == 27:
	exit()
