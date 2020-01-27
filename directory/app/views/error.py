import logging
logger = logging.getLogger(__name__)

from pyramid.view import (
    view_config, 
    notfound_view_config, 
    forbidden_view_config, 
    exception_view_config,
)

class ErrorViews:

    def __init__(self, request):
        self.request = request

    @notfound_view_config(renderer='../templates/error/404.jinja2')
    def notfound(self):
        request = self.request

        return {
        }

    @forbidden_view_config(renderer='../templates/error/403.jinja2')
    def forbidden(self):
        request = self.request

        return {
        }

    @exception_view_config(ValueError, renderer='../templates/error/500.jinja2')
    def exception(self):
        request = self.request

        logger.error(request.exception) 

        return {
        }
