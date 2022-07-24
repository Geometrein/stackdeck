from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from methods.util import (
    check_query_results,
    search_single_framework
)


views = APIRouter()
templates = Jinja2Templates(directory="templates")


@views.get("/", include_in_schema=False, status_code=200)
async def homepage(request: Request):
    """
    Home Page.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@views.get("/search/{framework}", response_class=HTMLResponse, include_in_schema=False, status_code=200)
async def get_item_by_path_param(request: Request, framework: str or list) -> Jinja2Templates.TemplateResponse:
    """
    Search cards by path parameters.
    """
    search_results = search_single_framework(framework)
    if check_query_results(search_results):
        return templates.TemplateResponse("stack-search.html", {"request": request, "search_results": search_results})
    else:
        return templates.TemplateResponse("not-found.html", {"request": request})


@views.get("/search/", response_class=HTMLResponse, include_in_schema=False, status_code=200)
async def get_item_by_query_param(request: Request, query: str = 'python') -> Jinja2Templates.TemplateResponse:
    """
    Search cards by query parameters.
    """
    search_results = search_single_framework(query)
    if check_query_results(search_results):
        return templates.TemplateResponse("stack-search.html", {"request": request, "search_results": search_results})
    else:
        return templates.TemplateResponse("not-found.html", {"request": request})


@views.get("/404", response_class=HTMLResponse, include_in_schema=False, status_code=404)
async def page_not_found(request: Request) -> Jinja2Templates.TemplateResponse:
    """
    404 page
    """
    return templates.TemplateResponse("404.html", {"request": request})
