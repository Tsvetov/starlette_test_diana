from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def test(request):
    return JSONResponse({'diana': 123123123123123})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/diana/', test),
])
