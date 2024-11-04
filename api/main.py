import orjson
from ninja import NinjaAPI
from ninja.parser import Parser
from ninja.renderers import BaseRenderer
from django.contrib.admin.views.decorators import staff_member_required

from .public_routers import router as public_router
from .private_routers import router as private_router


class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)  
 
        
app = NinjaAPI(parser=ORJSONParser(), 
               renderer=ORJSONRenderer(),
               docs_decorator=staff_member_required,
               title="Pimify",
               description="Pimify: Open-Source Product Information Management",
               version="v1")
app.add_router("public/", public_router)
app.add_router("private/", private_router)