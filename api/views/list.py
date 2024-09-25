from ninja import Router

router = Router(tags=["List"])


@router.get("", response=str)
def list_all(request):
    return "Hello World"
