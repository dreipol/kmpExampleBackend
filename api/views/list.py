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
