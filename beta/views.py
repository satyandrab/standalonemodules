
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import BetaRegistration
from binascii import hexlify
from beta.forms import EmailForm
import os

def index(request):
    if request.POST:
        form = EmailForm(request.POST)
        if form.is_valid():
            if request.is_ajax():
                message = "got the ajax request."
                email_id = request.POST['email']
                print email_id
                email_in_beta = BetaRegistration.objects.get(email = email_id)
                if email_in_beta:
                    print 'in if'
                    pass
                else:
                    print 'in else'
                    new_entry_obj = BetaRegistration(email = email_id,
                                                     url_hash = createId(),
                                                     invite_hash = createId()
                                                     )
                    new_entry_obj.save()
                    print 'Saved'
                return render_to_response('index.html',
                                          {'form':form,
                                           'message':message},
                                          context_instance=RequestContext(request))
            else:
                return render_to_response('index.html',
                                          {'form':form},
                                          context_instance=RequestContext(request))

    else:
        form = EmailForm()

    return render_to_response('index.html', {'form':form},
                              context_instance=RequestContext(request))
    
def createId():
    """
    """
    return hexlify(os.urandom(16))
