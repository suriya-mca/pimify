from ninja import Router

from .schemas import Message


router = Router()


@router.get("/health", response={200: Message, 204: None})
async def home(request):

    return 200, {'message': 'success'}

