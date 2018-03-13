from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import datetime
def time(request):
    now = datetime.datetime.now()
    print(now)
    delta = datetime.timedelta(minutes=30, seconds=5)
    print(delta)
    now += delta
    TIME=now.strftime('%Y/%m/%d %H:%M:%S')
    return render(request,'jishi.html',{'DATETIME':TIME,'NOW':now})