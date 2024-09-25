from typing import Optional, Any

from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI
from .views.list import router as list_router


api = NinjaAPI(title="KMP Test API",
               docs_decorator=staff_member_required
               )
api.add_router("/list/", list_router)
