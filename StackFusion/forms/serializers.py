from rest_framework import serializers
from forms.models import FormModel
# from forms import views


class FormModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormModel
        fields = ['name', 'dateOfBirth', 'email', 'contact']
