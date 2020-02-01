import datetime

from msumc.app.models.page import Page

index = Page(
    path='index',
    title='Index',
    body=f'''
<h1>Main Street United Methodist Church</h1>
<p class="text-muted">300 N Main St, Abbeville, SC 29620</p>
<h2>Welcome!</h2>
<p>Thank you for visiting our website.</p>
<p>Our Lord in His Providence has caused your path to cross ours. We invite you to worship with us. We are always happy to have guests to join us to worship, study, fellowship and to serve Christ.</p>
<p>Main Street United Methodist Church exists to glorify God by offering praise and worship, teaching and making disciples of Jesus Christ, supporting each other, serving the community, and spreading the Good News of salvation.</p>
    ''',
    created_by='pottsga',
    created_on=datetime.datetime.now(),
)

contact_us = Page(
    path='contact_us',
    title='Contact Us',
    body=f'''
<h1>Contact Us</h1>
    ''',
    created_by='pottsga',
    created_on=datetime.datetime.now(),
)

our_staff = Page(
    path='our_staff',
    title='Our Staff',
    body=f'''
<h1>Our Staff</h1>
    ''',
    created_by='pottsga',
    created_on=datetime.datetime.now(),
)

pages = [
    index,
    contact_us,
    our_staff,
]
