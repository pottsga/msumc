def includeme(config):
    config.add_static_view(name='/static', path='directory:app/static')

    # Index
    config.add_route('index.index', '/')

    # Contact
    config.add_route('contact.index', '/contact')

    # Contact
    config.add_route('ministry.view_all', '/ministries') # to view on the main website
    config.add_route('ministry.index', '/ministry')
    config.add_route('ministry.add', '/ministry/add')
    config.add_route('ministry.view', '/ministry/{ministry_id}/view')
    config.add_route('ministry.update', '/ministry/update')
    config.add_route('ministry.delete', '/ministry/delete')

    # Family
    config.add_route('family.index', '/family')
    config.add_route('family.add', '/family/add')
    config.add_route('family.view', '/family/{family_id}/view')
    config.add_route('family.update', '/family/{family_id}/update')
    config.add_route('family.delete', '/family/{family_id}/delete')

    # Person
    config.add_route('person.index', '/person')
    config.add_route('person.add', '/person/add')
    config.add_route('person.view', '/person/{person_id}/view')
    config.add_route('person.update', '/person/{person_id}/update')
    config.add_route('person.delete', '/person/{person_id}/delete')

    # Admin
    config.add_route('admin.index', '/admin')

    # Auth
    config.add_route('auth.login', '/auth/login')
    config.add_route('auth.logout', '/auth/logout')
