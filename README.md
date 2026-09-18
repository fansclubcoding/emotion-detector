# Emotion Detector

A Flask web application that detects emotions in text using the Watson NLP
EmotionPredict API. The user submits a statement in the browser, and the app
returns the detected scores for anger, disgust, fear, joy and sadness, along
with the dominant emotion.

## Project structure

```
EmotionDetection/
    __init__.py
    emotion_detection.py
static/
    mywebscript.js
templates/
    index.html
server.py
test_emotion_detection.py
requirements.txt
```

## How to run

```bash
pip install -r requirements.txt
python server.py
```

Then open http://localhost:5000 in a browser, enter a statement and click
"Run Sentiment Analysis".

## Running unit tests

```bash
python -m unittest test_emotion_detection.py -v
```

## Static code analysis

```bash
pylint server.py EmotionDetection/emotion_detection.py EmotionDetection/__init__.py test_emotion_detection.py
```

The codebase is written to score 10.00/10 with default pylint settings.
