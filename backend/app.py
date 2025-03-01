from flask import Flask, render_template, Response
import cv2
import numpy as np
from recognize import loadModel, findHand, predict

app = Flask(__name__, template_folder="templates")

# Load model
MODEL_PATH = "hand_sign_keras.h5"
model = loadModel(MODEL_PATH)

cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (100, 100), (300, 300), (20, 34, 255), 2)
        hand = findHand(frame)

        try:
            digit = predict(hand, model)[0]
            cv2.putText(frame, str(digit), (350, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 200, 25), 3, cv2.LINE_AA)
        except:
            pass  # Ignore prediction errors

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
