# Sign_Speak

# SignSpeak - Sign Language Digit Recognizer

SignSpeak is a real-time sign digit recognition system that uses deep learning to interpret hand gestures representing numbers (0-9). This project aims to break communication barriers and will be extended to assist individuals with hearing impairments by recognizing full sign language.

## 🚀 Features
- 📹 Real-time sign digit recognition via webcam
- 🤖 Deep learning-based hand gesture classification
- 🎨 Interactive and visually appealing UI
- 🔄 Future expansion for full sign language interpretation

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS (to be replaced with React in the future)
- **Backend:** Flask (to handle video streaming and model inference)
- **Model Architecture:** Conv->MaxPool->Conv->MaxPool->Flatten->Dense(512)->Dense(128)->Output(10)
- **Database (Future Scope):** MongoDB/PostgreSQL

## 📷 How It Works
1. The user shows a digit sign using their hand in front of the webcam.
2. The backend processes the frame and passes it through the trained deep-learning model.
3. The recognized digit is displayed on the UI in real-time.

## 🏗️ Installation & Setup
```sh
# Clone the repository
git clone https://github.com/suhani1503/SignSpeak.git
cd SignSpeak

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask backend
python backend/app.py
```
Then open `http://127.0.0.1:5000/` in your browser.

## 🔮 Future Enhancements
- 🖐️ Full sign language recognition
- 🗣️ Text-to-speech conversion for seamless communication
- 🌍 Multi-language support
- 📱 Mobile application development

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue or suggest new features.

---
Made with ❤️ by Suhani Ghosh

