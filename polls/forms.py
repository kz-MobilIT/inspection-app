from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(
        label="点検内容",
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "例: 12か月点検、車検、オイル交換 など"
        }),
        error_messages={"required": "点検内容は必須です。"},
    )

    car_model = forms.CharField(
        label="車種",
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "例: プリウス"
        }),
    )

    mileage = forms.IntegerField(
        label="走行距離(km)",
        required=False,
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={
            "placeholder": "例: 45000"
        }),
        error_messages={
            "min_value": "走行距離は0以上で入力してください。",
            "invalid": "数字を入力してください。",
        },
    )

    class Meta:
        model = Question
        fields = ["question_text", "car_model", "mileage"]

        error_messages = {
            "question_text":{
                "required": "点検内容は必須です。",
            },
            "mileage": {
                "min_value": "走行距離は０以上で入力してください。",
            },
        }