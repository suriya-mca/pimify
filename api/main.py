import orjson
from ninja import NinjaAPI
from ninja.parser import Parser
from ninja.renderers import BaseRenderer

from .public_routers import router as public_router


class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)  
 
        
app = NinjaAPI(parser=ORJSONParser(), renderer=ORJSONRenderer())
app.add_router("public/", public_router)