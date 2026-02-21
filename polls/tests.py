from django.test import TestCase
from polls.forms import QuestionForm


class QuestionFormTest(TestCase):
    def test_mileage_must_be_zero_or_more(self):
        form = QuestionForm(data={
            "question_text": "テスト点検",
            "mileage": -1,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("mileage", form.errors)

    def test_required_fields(self):
        form = QuestionForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("question_text", form.errors)