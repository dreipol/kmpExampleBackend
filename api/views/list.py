from typing import List

from ninja import Router, ModelSchema

from api.models import Content

router = Router(tags=["List"])


class ContentSchema(ModelSchema):
    class Config:
        model = Content
        model_fields = ("content",)


@router.get("", response=List[ContentSchema])
def list_all(request):
    return Content.objects.all()


@router.post("", response={201: ContentSchema})
def create(request):
    new_object = Content(content=request.body.decode("utf-8"))
    new_object.save()
    return 201, new_object
