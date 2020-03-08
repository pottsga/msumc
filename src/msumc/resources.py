from pyramid.security import Allow, Everyone, Authenticated

class Root(object):
    __acl__ = [
        (
            Allow, 
            'group:admins', 
            (
                'administrate',
                'view_directory',
            ),
        ),
        (Allow, 'group:members', 'view_directory'),
    ]

    def __init__(self, request):
        self.request = request
