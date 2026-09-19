"""Root-level module exposing the packaged emotion detector.

Allows running `from emotion_detection import emotion_detector` directly
from the project root folder when testing the application. The canonical
implementation lives in the EmotionDetection package.
"""
from EmotionDetection.emotion_detection import emotion_detector

__all__ = ['emotion_detector']
