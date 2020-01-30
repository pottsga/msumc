from pyramid.security import Allow, Everyone, Authenticated

class Root(object):
    __acl__ = [
        # Ex: ( Allow, Everyone, 'view'),
        (Allow, 'group:admins', 'administrate'),
    ]

    def __init__(self, request):
        self.request = request
