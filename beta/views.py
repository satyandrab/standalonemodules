
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import BetaRegistration, IPLog
from binascii import hexlify
from beta.forms import EmailForm
import os

def index(request):
    message = ''
    if request.POST:
        form = EmailForm(request.POST)
        if form.is_valid():
            if request.is_ajax():
                email_id = request.POST['email']
                email_in_beta = BetaRegistration.objects.filter(email = email_id)
                if email_in_beta:
                    message = "This email id is already in our database."
                    return render_to_response('index.html',
                                          {'form':form,
                                           'message':message},
                                          context_instance=RequestContext(request))
                else:
                    new_entry_obj = BetaRegistration(email = email_id,
                                                     url_hash = createId(),
                                                     invite_hash = createId()
                                                     )
                    new_entry_obj.save()
                    url_hash = new_entry_obj.url_hash
                    message = 'Thanks, you have registered your email id successfully.'
                return render_to_response('index.html',
                                          {'form':form,
                                           'message':message,
                                           'url_hash':url_hash},
                                          context_instance=RequestContext(request))
            else:
                return render_to_response('index.html',
                                          {'form':form, 
                                           'message':message},
                                          context_instance=RequestContext(request))
    else:
        form = EmailForm()

    return render_to_response('index.html', {'message':message,
                                             'form':form},
                              context_instance=RequestContext(request))

def visiturl(request, url_hash):
    message = ''
#    print set_cookie(request, )
    url_hash_query = BetaRegistration.objects.get(url_hash = url_hash)
    if url_hash_query:
        ip_client = request.META['REMOTE_ADDR']
        try:
            ip_log_obj = IPLog(ip = ip_client)
            ip_log_obj.save()
        except:
            pass
        ip_for_click = IPLog.objects.get(ip = ip_client)
        
        #print url_hash_query.click_ips.all()
        if ip_for_click in url_hash_query.click_ips.all():
            message = 'This IP already visited this link, so counter not increased.'
        else:
            url_hash_query.click_pnts = url_hash_query.click_pnts + 1
            url_hash_query.click_ips.add(ip_for_click)
            url_hash_query.save()
            message = "Thanks for visiting URL."
    else:
        message = "URL hash not available in our database."

    return render_to_response('index.html', {'message':message},
                              context_instance=RequestContext(request))

def createId():
    """
    """
    return hexlify(os.urandom(16))

