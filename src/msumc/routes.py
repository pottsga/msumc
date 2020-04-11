def includeme(config):
    config.add_static_view(name='/static', path='msumc:app/static')

    # Index
    config.add_route('index.index', '')

    # Household
    config.add_route('household.index', '/household')
    config.add_route('household.add', '/household/add')
    config.add_route('household.view', '/household/{household_id}/view')
    config.add_route('household.update', '/household/{household_id}/update')
    config.add_route('household.delete', '/household/{household_id}/delete')

    # Person
    config.add_route('person.index', '/person')
    config.add_route('person.add', '/person/add')
    config.add_route('person.view', '/person/{person_id}/view')
    config.add_route('person.update', '/person/{person_id}/update')
    config.add_route('person.delete', '/person/{person_id}/delete')

    # Email
    config.add_route('email.index', '/email')

    # Upload
    config.add_route('upload.index', '/upload')
    config.add_route('upload.add', '/upload/add')
    config.add_route('upload.view', '/upload/{upload_id}/view')
    config.add_route('upload.delete', '/upload/{upload_id}/delete')

    # Directory
    config.add_route('directory.index', '/directory')
    config.add_route('directory.pdf', '/directory.pdf')

    # Admin
    config.add_route('admin.index', '/admin')

    # User
    config.add_route('user.index', '/user')
    config.add_route('user.add', '/user/add')
    config.add_route('user.view', '/user/{user_id}/view')
    config.add_route('user.delete', '/user/{user_id}/delete')

    # Auth
    config.add_route('auth.login', '/auth/login')
    config.add_route('auth.logout', '/auth/logout')
    config.add_route('auth.register', '/auth/register')
    config.add_route('auth.verify', '/auth/verify/{verification_id}')
    config.add_route('auth.forgot_password', '/auth/forgot_password')
    config.add_route('auth.reset_password', '/auth/{verification_id}/reset_password')

    # Page
    config.add_route('page.index', '/page')
    config.add_route('page.add', '/page/add')
    config.add_route('page.view', '/page/{page_id}/view')
    config.add_route('page.update', '/page/{page_id}/update')
    config.add_route('page.delete', '/page/{page_id}/delete')
    config.add_route('page.view_page', '/{path:.*}')
