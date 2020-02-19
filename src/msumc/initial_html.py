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
    <h2>Pastor &mdash; Brian Arant</h2>
    <p>Cell phone: <a href="tel:8648040603">(864) 804-0603</a></p>
    <p>E-mail: <a href="mailto:bjarant@umcsc.org">bjarant@umcsc.org</a></p>
    <h2>Church Office</h2>
    <p>Office Hours: Monday - Thursday, 8:00AM - 12:00PM.</p>
    <p>Address: <a href="https://www.google.com/maps/place/300+N+Main+St,+Abbeville,+SC+29620/@34.179594,-82.3826759,17z/data=!3m1!4b1!4m5!3m4!1s0x88f7fb56e27ced83:0xd8cb226ccab72018!8m2!3d34.179594!4d-82.3804872">300 N. Main St., Abbeville, SC 29620</a></p>
    <p>P.O. Box <a href="#">P.O. Box 656 Abbeville, SC 29620</a></p>
    <p>Telephone: <a href="tel:8643662367">(864) 366-2367</a></p>
    <p>Fax:  <a href="fax:8643662328">(864) 366-2328</a></p>
    <p>E-mail: <a href="mailto:abbvmsumc@wctel.net">abbvmsumc@wctel.net</a> or <a href="mailto:mainstreetumcabbeville@gmail.com">mainstreetumcabbeville@gmail.com</a></p>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='our_staff',
        title='Our Staff',
        body=f'''
    <h1>Our Staff</h1>
    <h2>Pastor</h2>
    <p>Brian J. Arant</p>

    <h2>Secretary</h2> 
    <p>Betty Bowen</p>

    <h2>Choir Director</h2> 
    <p>Kerri Hall</p>

    <h2>Organist</h2>    
    <p>Kerri Hall</p>

    <h2>Youth Director</h2>
    <p>VACANT</p>

    <h2>Custodian</h2> 
    <p>Mike Wilson</p>
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
    Page(
        path='links',
        title='Links',
        body=f'''
    <h1>Links</h1>
    <ul>
      <li>South Carolina Conference <a href="https://www.umcsc.org/">https://www.umcsc.org/</a></li>
      <li>Advocate Newsletter <a href="https://www.advocatesc.org/">https://www.advocatesc.org/</a></li>
      <li>Anderson District Office <a href="http://andersondistrictumc.org/">http://andersondistrictumc.org/</a></li>
      <li>Find a Church <a href="https://www.umc.org/find-a-church/search">https://www.umc.org/find-a-church/search</a></li>
      <li>Epworth Children's Home <a href="https://www.epworthchildrenshome.org/">https://www.epworthchildrenshome.org/</a></li>
      <li>UCMAC <a href="http://ucmac.net/">http://ucmac.net/</a></li>
      <li>Faith Home <a href="https://faithhomegwd.net/">https://faithhomegwd.net/</a></li>
      <li>Reciprical Ministries International <a href="https://www.rmibridge.org/">https://www.rmibridge.org/</a></li>
    </ul>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='newsletters',
        title='Newsletters',
        body=f'''
    <h1>Newsletters</h1>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='sermons',
        title='Sermons',
        body='''
    <h1>Sermons</h1>
    <p>
        Our most recent three videos are linked below. Please visit our YouTube page for more!
        <a target="_blank" href="https://www.youtube.com/channel/UCNeW4jmKZsGiwes300WSSiw">View our YouTube page.</a>
    </p>
    <div class="my-2">
        <div class="row">
          <div class="col-12">
            <iframe 
                class="latestVideoEmbed" 
                vnum='0' 
                cid="UCNeW4jmKZsGiwes300WSSiw" 
                width="100%" 
                height="340" 
                frameborder="0" 
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen></iframe>
          </div>
          <div class="col-12">
            <iframe 
                class="latestVideoEmbed" 
                vnum='1' 
                cid="UCNeW4jmKZsGiwes300WSSiw" 
                width="100%" 
                height="340" 
                frameborder="0" 
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen></iframe>
          </div>
          <div class="col-12">
            <iframe 
                class="latestVideoEmbed" 
                vnum='2' 
                cid="UCNeW4jmKZsGiwes300WSSiw" 
                width="100%" 
                height="340" 
                frameborder="0" 
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen></iframe>
          </div>
        </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>

    <script>
    var reqURL = "https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent("https://www.youtube.com/feeds/videos.xml?channel_id=");
    function loadVideo(iframe){
        $.getJSON( reqURL + iframe.getAttribute('cid'),
          function(data) {
             var videoNumber = (iframe.getAttribute('vnum')?Number(iframe.getAttribute('vnum')):0);
            console.log(videoNumber);
             var link = data.items[videoNumber].link;
             id = link.substr(link.indexOf("=") + 1);
             iframe.setAttribute("src","https://youtube.com/embed/"+id + "?controls=0&autoplay=1");
          }
       );
    }
    var iframes = document.getElementsByClassName('latestVideoEmbed');
    for (var i = 0, len = iframes.length; i < len; i++){
           loadVideo(iframes[i]);
    }
    </script>

        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='our_ministries',
        title='Our Ministries',
        body=f'''
    <h1>Our Ministries</h1>
    <h2>A</h2>
    <h3>A Place For Us Ministries</h3>
    <p>The UMW and the UMM supports this program.</p>
    <h3>Adoption of World Vision Child</h3>
    <p>the Wesley Sunday School class makes a monthly donation to the World Vision program.</p>
    <h3>Agnes Closet School Box Fund</h3>
    <p>The Agnes Rogers circle sponsors the Agnes Closet project that provides school supplies, activities assistance and clothes to needy children.  Each year two upscale used clothing sales are held to raise money for the project.</p>
    <h3>Angel Tree</h3>
    <p>The Ann Moore Circle and the Agnes Rogers Circle spearhead a project that provides Christmas presents for over 600 needy children.  This project has grown to include Church wide and community wide participation.  The UMW, UMM,  Outreach and Wesley Sunday School classes made donations.  Many church members and youth help wrap presents.</p>
    <h2>B</h2>
    <h3>Bible School</h3>
    <p>Each year our Church sponsors Vacation Bible School.  About 70 to 80 children from our Church and the community participate.</p>
    <h3>Boy Scouts</h3>
    <p>Our Church sponsors a Boy Scout troop, and our youth building is used for Boy Scout meetings.  In 2011 two young men received their Eagle Scout awards at Main Street and in 2012 one young man received his Eagle Scout award.</p>
    <h2>C</h2>
    <h3>Collect Campbell Soup Labels</h3>
    <p>These labels are given to a local school to help buy equipment.</p>
    <h3>Council on Aging Gift project</h3>
    <p>Lovely Lane Circle provides Christmas and Easter favors for the Council on Aging participants.</p>
    <h2>F</h2>
    <h3>Faith Home</h3>
    <p>Loose change collection benefited the Faith Home.  The UMW supports this home. </p>
    <h3>Food for Needy and Food Pantry</h3>
    <p>Church members and groups, participant in food drives throughout the year for the United Christian Ministries food pantry which is located in the basement of Main Street.</p>
    <h2>H</h2>
    <h3>Habitats for Humanity</h3>
    <p>the Methodist Men contribute their time and talents to building homes.  A member of our Church serves on the Board of Directors. </p>
    <h3>Healing Hands Health Ministry</h3>
    <p>our Lunch and Learn series sponsors programs such as The Healing Power of Art, Laughter is the Best Medicine, Medicare and You, Understanding Alzheimer and Help for the Caregiver, The Healing Power of Art II, Laughter is the Best Medicine II, Music Sooths the Soul and other interesting topics</p>
    <h3>Helping Hands</h3>
    <p>helps our members with small task around the house.  This Helping Hands ministry is a joint effort between Healing Hands, United Methodist Men and the Youth</p>
    <h2>K</h2>
    <h3>Kairos Prison Ministry</h3>
    <p>All the Circles participate in the cookie ministry for prisoners. </p>
    <h2>L</h2>
    <h3>Lent Card</h3>
    <p>the first Sunday of Lent, cards were given out, and then returned Easter Sunday.  One half of this offering goes to the Tracy Jackson Summer Food Program.  The remaining half goes to the United Christian Ministries of Abbeville County.</p>
    <h3>Loose Change Sunday</h3>
    <p>The 4th Sunday of each month buckets are held at each Sanctuary door to collect money for various local mission projects.  The projects helped this year are Faith Home, Salkehatchie, Haven of Rest Ministries, UCMAC Food Pantry, School Box Fund, and Henderson Settlement.</p>
    <h2>M</h2>
    <h3>Meals for Bereaved Families</h3>
    <p>the Church has three committees that prepare and serve meals to bereaved families of deceased Church members.  The Wesley Class serves a meal when a class member or family member dies.</p>
    <h3>Meals for JV Football</h3>
    <p>The UMM provided a meal for the JV football team.</p>
    <h3>Meals on Wheels</h3>
    <p>The UMW, the Youth Sunday School class donated to the local Meals on Wheels.</p>
    <h3>Minister to our own members</h3>
    <p>A Christmas cantata and Christmas party is held each year.  Youth week is held during the summer. Family activities such as a valentine dinner, lake outing, kite sunday, fall hayride and cookout, and movie night are held during the year.</p>
    <h2>R</h2>
    <h3>Relay for Life</h3>
    <p>For several years our Church members have helped fight Cancer by purchasing lumanaries.  Many of our Church members are very active in the organization.</p>
    <h2>S</h2>
    <h3>Salkehatchie</h3>
    <p>Each year our church sends several youths and adults to attend the weeklong Salkehatchie program, helping repair homes for needy people of South Carolina.  The loose change collection and the UMW, Outreach class and Methodist Men made additional gifts.  </p>
    <h3>Special Attention to Shut In and Others</h3>
    <p>The UMW has a project that sends greeting cards to shut ins and sick people each month.  Lovely Lane Circle provided Sunshine Baskets for Shut ins.  Susanna Wesley Circle provises prayer shawls for sick or shut in people.  The Ann Moore Circle sends out birthday cards each month to members of our congregation.</p>
    <h3>Support Missionaries</h3>
    <p>Main Street supports Tim Crawford (GBGM missionary) at the Red Bird Mission.  The Church sends a monthly check.  The UMW have made additional gifts. </p>
    <h2>T</h2>
    <h3>Thanksgiving and Christmas Dinner</h3>
    <p>a group of individuals from several churches, including Main Street, with the help of Haven of Rest Ministries, provide a free Thanksgiving and Christmas dinner to needy or elderly people.  This is served in our church’s Greene Center.  Many of our church members, including the youth groups, volunteer to help with the meals and provide desserts.  We served over 500 Thanksgiving meals and 550 Christmas meals in 2019</p>
    <h3>Tracy Jackson Food Program of G.I.F.T.</h3>
    <p>Our Church makes a monthly donation and the loose change collection supports the Food Program.  The UMW, UMYF and UMM took the responsibility of providing sandwich makers for each day during the summer program.  The Susanna Wesley Circle collected arts and crafts supplies.  Also, several groups made monetary contributions.</p>
    <h2>U</h2>
    <h3>United Christian Ministries of Abbeville County (UCMAC)</h3>
    <p>Main Street was instrumental in forming a united ministry for Abbeville County with 24 other Churches in 2008. This ministy provides financial help, and food to families in Abbeville County that have had a crisis. In 2011 UCMAC opened a Free Medical Clinic.  Several Main Street members are on the Board of Directors.  Many Main Street members are volunteering their time as intake workers, receptionist, clerical workers, as well as part of the executive staff. </p>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='our_history',
        title='Our History',
        body=f'''
<h1>Our History</h1>
<p>The present sanctuary of Main Street United Methodist Church was dedicated in 1888 by the bishop.  The architect and builder was James D. McCullough.  Not long after, in 1890, the bell now in the bell tower was purchased.  That church was the first church on this lot (1840), but it was Abbeville’s second Methodist church; the first one was built in 1827 on Washington Street and was the first church in the village—then known as Abbeville Court House.</p>

<p>The founder of Methodism in Abbeville was a woman, Ann Fisher Moore.  She came to Abbeville as a young wife and wanted very much to have a church in the town where she would raise her children.  Born in England and raised in Charleston, she was Roman Catholic, but after reading a Charles Wesley hymn, she converted to Methodism.  Her husband, James Moore, became the church’s first “local” preacher—he married, baptized, and buried people, and preached when the circuit rider was not present.</p>

<p>The nave of the present sanctuary originally faced the northeast wall.  The front door was where the Good Shepherd window is, and the window on the northeast wall was over the front door.  When the railroad came through Abbeville, and the railroad shops were built on the outskirts of town, the population increased by 1,000.  The Methodists invited the newcomers to join, and, as a result, the nave had to be enlarged.  It was re-oriented and what then became the back wall was moved.  The bishop dedicated the remodeled church in 1895.  The architects were Bruce and Morgan of Atlanta, also the architects for the exuberant Queen Anne Harris House at 200 South Main and Tillman Hall at Clemson.</p>

<p>Of the art nouveau Good Shepherd window that was installed in 1895, The Southern Christian Advocate said it was “a beautiful work of art not surpassed…in the South.” The “ruby cut-through clear glass” over the door between the narthex and nave also dates from 1895.  The other windows in the nave, the windows in the DuPré Chapel, and the glass over the other doors are thought to have been installed in 1888.</p>

<p>In 2018, Keep the Music Flowing - A Campaign to Replace and Restore the Organ resulted in a new 649 pipe organ custom built for us by Kegg Pipe Organ Company.  The façade pipes of the 1900 Felgemaker pipe organ were restored and the console and other pipes were replaced.  The new and restored pipe organ was installed and dedicated during the February 17, 2019 worship service; District Superintendent Rev. Steve Patterson led the congregation in a pipe organ dedication Litany.</p>

<p><em>“We dedicate the pipe organ for the worship, honor, praise and glory of God. May this organ encourage our praise and lift our singing. May the music it produces bring our prayers to you in times of joy and times of sorrow.”</em></p>

<p>In 1925, to celebrate the 100th Anniversary and to “care for the young…of the church,” the congregation built the Education Building and remodeled the exterior of the sanctuary to be architecturally compatible with the new building.  James C. Hemphill was the architect.  The bishop dedicated it in 1944.  In 1993, Jane Greene and her children gave the congregation the Greene Center to honor her parents Nora and Leman Greene.  More recently, through the 21st Century Capital Campaign, the church raised the money needed to re-decorate and repair all church buildings, including the parsonage on Florence Street, for ministry in the new millennium.  The bishop preached the sermon to celebrate the church’s 175th Anniversary in 2002.</p>

<p>As the banner on the wall of the narthex attests, Main Street considers itself a liturgical church, observing the Christian year in worship through music, drama, and sometimes dance.  Main Street United Methodist Church exists to glorify God by offering praise and worship, teaching and making disciples of Jesus Christ, supporting each other, serving the community, and spreading the Good News of salvation!</p>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='group/united-methodist-men',
        title='United Methodist Men',
        body=f'''
    <h1>United Methodist Men</h1>
    <img class="my-2" src="/static/img/united_methodist_men.jpg" alt="United Methodist Men">
    <p>The United Methodist Men meet on the first Sunday of each month for a breakfast meeting in the Greene Center at 8 am.  The men help built Habitat for Humanity Homes in the Abbeville area.  Each year the men hold a live auction to raise funds for mission projects.</p>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='group/united-methodist-women',
        title='United Methodist Women',
        body=f'''
    <h1>United Methodist Women</h1>
    <img class="my-2" src="/static/img/united_methodist_women.jpg" alt="United Methodist Women">
    <p>Main Street has an active UMW group composed of 4 Circles with over 80 members.  Our Unit received the Mission Today certification, the Five Star Unit award and the SC Projects award at the Anderson District UMW meeting this year.</p>
    <p>There are four active circles:</p>
    <ul>
      <li><strong>Lovely Lane Circle</strong> meets the 2ND Tuesday of each month at 3:30pm in the Greene Center or in a members's home.</li>
      <li><strong>Susanna Wesley Circle</strong> meets the 1st Monday of the month at 12:00pm for a lunch meeting.</li>
      <li><strong>Agnes Rogers Circle</strong> meets on the 1st Monday of the month at 6:30pm in a member's home.</li>
      <li><strong>Ann Moore Circle</strong> meets on the 1st Tuesday of the month at 6:30pm at local resturants.</li>
    </ul>
    <p>Some of the activities are:</p>
    <ul>
        <li>The Angel Tree project provides Christmas presents for over 600 individuals.  This project has grown to include community wide participation.</li>
        <li>The School Box project provides school supplies, activities assistance, and clothes to needy children. Each year two upscale used clothing sales are held to raise money for the project.</li>
        <li>A fundraiser is held each year to raise funds for local missions.  The money raised at the event was donated to the United Christian Ministries, Free Medical Clinic, Tracy Jackson Summer Food Program, School Box Fund and to help our church take a Haiti Mission Trip.</li>
        <li>The UMW  has a Special Attention project where each circle sends greeting cards to shut-ins each  month. One Circle took flowers to shut-ins.</li>
        <li>The Council on Aging Gift project provides Christmas and Easter favors for the Council on Aging participants.</li>
        <li>All the Circles participate in the Kairos Prison Ministry by making cookies for the prisoners.</li>
        <li>Prayer Shawls are given to Main Street members who are sick or shut-in.</li>
        <li>The UMW provided and served snacks during Vacation Bible School.</li>
        <li>The UMW collectsd items for gift boxes for deployed miitary personnel.</li>
    </ul>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='group/main-street-youth',
        title='Main Street Youth',
        body=f'''
    <h1>Main Street Youth</h1>
    <img class="my-2" src="/static/img/united_methodist_youth.jpg" alt="United Methodist Youth">
    <p>The youth meets at 7:00pm in the Youth Building.</p>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='group/the-goodtimers',
        title='The Goodtimers',
        body=f'''
    <h1>The Goodtimers</h1>
    <p>Main Street GOODTIMERS are our Senior Adults - we meet every second Wednesday at 12:00 for lunch.  This is followed by a devotional, a fun time and occasionally a speaker on pertinent topics for the group.  At every meeting we bring our prayer requests and our secretary sends cards accordingly.</p>
    <p>We are an ecumenical group - as well as Methodists we have Presbyterians, Baptists, an A.R. P. and Catholics.  Therefore we try to be a support group for the elderly and shut-ins of our community.  We send seasonal and all occasional cards and visit and make phone calls.</p>
    <p>Each year we make contributions to Meals on Wheels, Kairos (cookies for the prisoners), UCMAC (canned goods and staple grocery items for the needy), toilet articles for the residents at the Abbeville Nursing Home for Christmas, Angel Tree, etc.</p>
    <p>We love traveling together - we take lots of one- day trips, 2 or 3 day trips and sometimes ones lasting a week or more.  These are fun times filled with Christian fellowship and educational opportunities as well - a group having good times together.  The GOODTIMERS were formed 33 years ago and we are still very much a vital part of our Main St. congregation.</p>
    <p>Upcoming events - when warm spring weather returns we will possibly be planning a one day trip, maybe to Marietta/Kennesaw or other destinations.</p>
        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
    Page(
        path='group/healing-hands-ministry',
        title='Healing Hands Ministry',
        body=f'''
    <h1>Healing Hands Ministry</h1>
    <p>Healing the mind, body, and spirit of our community.</p>
    <div class="ml-3 my-2">
        <em>Your body is a temple of the Holy Spirit.</em><sub> 1 Corinthians 6:19</sub>
    </div>
    <p>The Healing Hands Ministry is a health ministry that emphasizes the holistic approach to healing, acknowledging the close connection between mind, body, and spirit.  God has given us a wonderful gift of life and it is our responsibility to keep ourselves well – we are stewards of our own health.</p>

    <p>Activities planned for 2015:</p>
    <ul>
        <li>Lunch and Learn - will feature programs such as "Alzhiemer Caregivers";  "Music Soothes the Soul" , and other interesting topics. These programs are held in the Greene Center and lunch is provided.</li>
        <li>Visitation of Shut-Ins - a Healing Hands committee member will visit shut-in and others with special needs.</li>
        <li>Care-Notes program - an inspirational and supportive booklet is sent to church members who may be grieving or have health challenges.</li>
        <li>Mini-Health Fairs - including blood pressure screening on Sunday mornings.</li>
        <li>Helping Hands Ministry assist members with small household chores.</li>
    </ul>

        ''',
        created_by='pottsga',
        created_on=datetime.datetime.now(),
    ),
]
