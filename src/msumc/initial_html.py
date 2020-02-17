import datetime

from msumc.app.models.page import Page

pages = [
    Page(
        path='index',
        title='Index',
        body=f'''
    <h1>Main Street United Methodist Church</h1>
    <p class="text-muted">300 N Main St, Abbeville, SC 29620</p>
    <h2>Welcome!</h2>
    <p>Thank you for visiting our website.</p>
    <p>Our Lord in His Providence has caused your path to cross ours. We invite you to worship with us. We are always happy to have guests to join us to worship, study, fellowship and to serve Christ.</p>
    <p>Main Street United Methodist Church exists to glorify God by offering praise and worship, teaching and making disciples of Jesus Christ, supporting each other, serving the community, and spreading the Good News of salvation.</p>
    <video autoplay loop muted playsinline style="width: 100%;">
        <source src="/static/video/ChurchVideo.mp4" type="video/mp4">
    </video>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='contact_us',
        title='Contact Us',
        body=f'''
    <h1>Contact Us</h1>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='our_staff',
        title='Our Staff',
        body=f'''
    <h1>Our Staff</h1>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='calendar',
        title='Calendar',
        body=f'''
    <h1>Calendar</h1>
    <iframe src="https://www.google.com/calendar/embed?showTitle=0&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=mainstreetumcabbeville%40gmail.com&amp;color=%23691426&amp;src=en.usa%23holiday%40group.v.calendar.google.com&amp;color=%23182C57&amp;ctz=America%2FNew_York" style=" border-width:0 " scrolling="no" width="700" height="600" frameborder="0"></iframe>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
]
