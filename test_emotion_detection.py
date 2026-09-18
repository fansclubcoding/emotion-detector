"""Unit tests for the EmotionDetection.emotion_detection module."""
import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Verify dominant emotions detected for polar sample statements."""

    def check_dominant_emotion(self, statement, expected):
        """Assert the expected dominant emotion and positive float scores."""
        result = emotion_detector(statement)
        self.assertEqual(result["dominant_emotion"], expected)
        for emotion in ("anger", "disgust", "fear", "joy", "sadness"):
            self.assertIsInstance(result[emotion], float)
            self.assertGreater(result[emotion], 0.0)

    def test_joy(self):
        """A happy statement is dominated by joy."""
        self.check_dominant_emotion("I am so happy I am doing this", "joy")

    def test_anger(self):
        """An angry statement is dominated by anger."""
        self.check_dominant_emotion("I am so angry I could scream", "anger")

    def test_disgust(self):
        """A disgusted statement is dominated by disgust."""
        self.check_dominant_emotion("I feel disgusted seeing this", "disgust")

    def test_fear(self):
        """A terrified statement is dominated by fear."""
        self.check_dominant_emotion("I am terrified of spiders", "fear")

    def test_sadness(self):
        """A sad statement is dominated by sadness."""
        self.check_dominant_emotion("I am so sad about this news", "sadness")

if __name__ == "__main__":
    unittest.main()
