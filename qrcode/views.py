from django.shortcuts import render , HttpResponse ,HttpResponseRedirect, redirect ,reverse
from participant.models import Participant,Evaluation
from django.shortcuts import get_object_or_404
# Create your views here.


def home(request):
    return render(request,'qrcode/qr.html')

def qr_plain(request, qrid):
    user=request.user
    if user.is_authenticated:
        p=Participant.objects.filter(pk=qrid)
        if not p.exists():
            return HttpResponseRedirect(reverse('qrcode:scan'))
        cat=user.judge.category
        if cat :
            eval=Evaluation.objects.filter(participant__pk=qrid,category=cat)
            if eval.exists() :
                return redirect('admin:category_evaluation_change',eval[0].pk)
            return HttpResponseRedirect(
                reverse('admin:category_evaluation_add') + f'?participant={qrid}&category={cat.pk}')
        return HttpResponse('This user is not linked to any category please contact admin')

    return HttpResponseRedirect(f"{reverse('admin:login')}?next=/{qrid}")
