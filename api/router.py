from typing import Optional, Any

from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI
from .views.chat import router as chat_router


api = NinjaAPI(title="KMP Test API",
               docs_decorator=staff_member_required
               )
api.add_router("/chat/", chat_router)
