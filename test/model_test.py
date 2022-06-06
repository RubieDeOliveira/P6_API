import unittest

from app.model import Model


class MyTestCase(unittest.TestCase):
    def test_model(self):
        data = "How to use python dict ?"
        model = Model()

        prediction = model.predict_tags(data)
        self.assertTrue("python" in prediction)
