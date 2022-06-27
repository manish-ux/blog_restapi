import base64
import uuid
from rest_framework.fields import Field
from django.core.files.base import ContentFile
from rest_framework import serializers

class Base64ContentField(Field):
    def to_internal_value(self, data):
        try:
            format,datastr = data.split(';base64,')
            ext = format.split('/')[-1]
            file = ContentFile(base64.b64decode(datastr), name=str(uuid.uuid4())+'.'+ext)

        except Exception as ex:
            print(ex)
            raise serializers.ValidationError("Error in decoding base 64 data")
        return file

    def to_representation(self, value):
        if not value:
            return None
        return value.url

