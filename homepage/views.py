from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from io import BytesIO
from . import yanzheng
from mysql import qurty as mysql
import datetime,random
# Create your views here.

def login(request):
    login_dict={}
    login_dict['USERNAME']='姓　名：'
    login_dict['PASSWORD']='密　码：'
    login_dict['STUDENT_ID']='学　号：'
    return render(request,'login.html',login_dict)


def verification(request):
    # GET方法返回表单
    if request.method == 'GET':
        return render(request, '/')
    # POST方法用来验证提交的验证码是否正确
    else:
        code = request.POST.get('code', '')
    if code == request.session.get('check_code', 'error'):
        if request.method == 'POST':
            username = request.POST['''username''']
            if yanzheng.username_judge(username) == False:
                return HttpResponse('''<script language="javascript"> 
    				alert("请输入正确的姓名"); 
    				window.history.back('/'); 
    				</script>''')
            password = request.POST['''password''']
            student_id = request.POST['student_id']
            print(username)
            print(student_id)
            password=yanzheng.md5_encryption(password)
            if username == '' or password == '' or student_id == '':
                return HttpResponse('''<script language="javascript"> 
    				alert("账号/密码/学号不能为空"); 
    				window.history.back('/'); 
    				</script>''')
            else:
                returninfo = mysql.verification(username,student_id)
                if returninfo == '账号不存在':
                    return HttpResponse('''<script language="javascript"> 
    					alert("此用户名不存在"); 
    					window.history.back('/'); 
    					</script>''')
                else:
                    userID,Password,Class = returninfo
                    if password != Password:
                        return HttpResponse('''<script language="javascript"> 
    						alert("密码不正确"); 
    						window.history.back('/'); 
    						</script>''')
                    else:
                        request.session['userID'] = str(userID)
                        request.session['username'] = username
                        request.session['class']=Class
                        return HttpResponseRedirect('/index.html')
    else:
        # session=request.session.get('session')
        return HttpResponse('''<script language="javascript"> 
    		alert("验证码错误"); 
    		window.history.back('/'); 
    	    </script>''')

def create_code_img(request):
    #在内存中开辟空间用以生成临时的图片
    f=BytesIO()
    img,code = yanzheng.create_code()
    request.session['check_code']=code
    img.save(f,'PNG')
    return HttpResponse(f.getvalue())

def indexpage(request):
    userID=request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    Class=request.session.get('class')
    student_dict={}
    student_dict['USERNAME']=username
    student_dict['CLASS']=Class
    return render(request,'index.html',student_dict)

def exit_login(request):
    userID=request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    del request.session['userID']
    del request.session['username']
    return HttpResponseRedirect('/')

def curriculum(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    Class = request.session.get('class')
    data=mysql.select_subjects(Class)
    data=data[0].split(',')
    return render(request,'subjects.html',{'SUBJECTS':data,'USERNAME':username,'CLASS':Class})

def subject(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    subject_dict={}
    subject_dict['USERNAME']=username
    Class = request.session.get('class')
    subject_dict['CLASS']=Class
    subject=request.GET.get('subject')
    data=mysql.questions1(subject)
    print(data)
    subject_dict['DATA']=data
    return render(request,'Single.html',subject_dict)


def examination(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    Class = request.session.get('class')
    data=mysql.select_subjects(Class)
    data=data[0].split(',')
    return render(request,'examination.html',{'SUBJECTS':data,'USERNAME':username,'CLASS':Class})

def Examination(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    subject_dict={}
    subject_dict['USERNAME']=username
    Class = request.session.get('class')
    subject_dict['CLASS']=Class
    subject=request.GET.get('subject')
    request.session['subject']=subject
    DATA=mysql.questions(subject)
    num_list=[i for i in range(len(DATA))]
    que_num=random.sample(num_list,20)
    data=[]
    num=1
    for i in que_num:
        data_list=list(DATA[i])
        data_list.append(num)
        data.append(data_list)
        num+=1
    subject_dict['DATA']=data
    now=datetime.datetime.now()
    delta = datetime.timedelta(minutes=0, seconds=30)
    now += delta
    TIME = now.strftime('%Y/%m/%d %H:%M:%S')
    subject_dict['DATETIME']=TIME
    #取出正确答案，放进session
    Right_Answe=[]
    for i in data:
        Right_Answe.append(i[5])
    request.session['RIGHT_AUSWE']=Right_Answe
    print('正确答案：'+str(Right_Answe))
    return render(request,'testing.html',subject_dict)

def Judge(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    subject = request.session.get('subject')
    Right_Auswe=request.session.get('RIGHT_AUSWE')
    answers=[]
    for num in range(1,21):   #range(1,21):   #20道题
        answer=request.POST.get('question'+str(num))
        answers.append(answer)
    #分数
    Error=0
    for i in range(20): #range(20)
        if Right_Auswe[i] != answers[i]:
            Error+=1
    achievement=str(100-Error*5)
    print(achievement)
    now = datetime.datetime.now()
    #插入考试记录
    mysql.insert_achievement(userID,achievement,now,subject)
    del request.session['RIGHT_AUSWE']
    del request.session['subject']
    return HttpResponseRedirect('/achievement/finish')

def last_achievement(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    Class = request.session.get('class')
    #最后一次成绩
    Last=mysql.show_last_achievement(userID)
    Last=Last[0]
    last_dict={}
    last_dict['USERNAME']=username
    last_dict['CLASS']=Class
    last_dict['LAST']=Last
    return render(request,'last.html',last_dict)

def show_historical_achievement(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    Class = request.session.get('class')
    data=mysql.select_istorical_achievement(userID)
    show_dict={}
    show_dict['USERNAME']=username
    show_dict['CLASS']=Class
    show_dict['DATA']=data
    return render(request,'historical.html',show_dict)

def PersonalInformation(request):
    userID = request.session.get('userID')
    if userID == None:
        return HttpResponseRedirect('/')
    username = request.session.get('username')
    Class = request.session.get('class')
    data=mysql.PersonalInformation(userID)
    person_dict={}
    person_dict['USERNAME']=username
    person_dict['CLASS']=Class
    person_dict['TIME']=data
    return render(request,'PersonalInformation.html',person_dict)