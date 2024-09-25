import json
from typing import List

from ninja import Router, ModelSchema
from ninja.errors import HttpError

from api.models import Content

router = Router(tags=["Chat"])


class ContentSchema(ModelSchema):
    class Config:
        model = Content
        model_fields = ("content", "user", "date_added",)


@router.get("", response=List[ContentSchema])
def list_all(request):
    return Content.objects.all()


@router.post("", response={201: ContentSchema})
def create(request):
    message_json = json.loads(request.body)
    content = message_json.get("content")
    user = message_json.get("user")
    if content is None or user is None:
        raise HttpError(400, "Content or user name not provided!")

    new_object = Content(content=content, user=user)
    new_object.save()
    return 201, new_object
