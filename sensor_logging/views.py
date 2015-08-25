from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# def my_render_callback(response):
    # Do content-sensitive processing
    # do_post_processing()

def main_view(request):
    # Create a response
    response = TemplateResponse(request, 'base.html', {})
    # Register the callback
    # response.add_post_render_callback(my_render_callback)
    # Return the response
    return response