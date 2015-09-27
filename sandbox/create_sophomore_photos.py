from django.core.files import File
from charterclub.models import *

netids=[
'abalji',
'cnsong',
'jasonmk',
'maxb',
'rmarek',
'tkloehn',
'achavda',
'dgift',
'jc33',
'mcstoner',
'rrmiller',
'tlomont',
'ajbowman',
'drelkind',
'jdwright',
'mdaigger',
'rshao',
'tpbyrne',
'ajs6',
'dysun',
'jganatra',
'mghinson',
'ruchames',
'vdu',
'arfarina',
'echo',
'jhyates',
'mlchiang',
'sc27',
'vmorin',
'axie',
'egordon',
'jjliu',
'mtorre',
'sgallo',
'wbein',
'bferda',
'eoshima',
'jontang',
'obiajulu',
'skwang',
'wkr',
'chay',
'eyli',
'joseip',
'paguas',
'sleos',
'wrose',
'chua',
'ibosetti',
'joshuau',
'raguilar',
'smuleady',
'yooliml',
'clualdi',
'iingato',
'lgrundy',
'rcreyes',
'spiegel',
'yy3',
'cmytelka',
'jasongg',
'map5',
'rhxu',
'tab4',
'zacharyk']

for netid in netids:
    try:
        url = 'media/member_images/%s.jpg' % netid
        image = File(open(url))

        m_o = Member.objects.filter(netid=netid)[0]
        m_o.image.save(url, image)
        m_o.save()
    except:
        print "Could not find an image for member: %s" % (netid)