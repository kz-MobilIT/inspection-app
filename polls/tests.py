import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Question


def create_question(question_text, days):
    """
    days がマイナス → 過去
    days がプラス → 未来
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "質問がありません。")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        create_question("過去の質問", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            ["<Question: 過去の質問>"],
            transform=repr
        )

    def test_future_question(self):
        create_question("未来の質問", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "質問がありません。")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_and_past_question(self):
        create_question("過去の質問", days=-30)
        create_question("未来の質問", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            ["<Question: 過去の質問>"],
            transform=repr,
        )

    def test_two_past_questions(self):
        create_question("過去の質問1", days=-30)
        create_question("過去の質問2", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            ["<Question: 過去の質問2>", "<Question: 過去の質問1>"],
            transform=repr,
        )
