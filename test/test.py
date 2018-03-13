import random,string,pymysql
#定义科目，不可为空
subject='随机字符'



#mysql
def insert1(subject,question):
    db=pymysql.connect('192.168.1.98','test','Lxq_204389','Examination_system',port=3306,charset='utf8')
    dbc=db.cursor()
    print(11111111)
    sql="insert into Questions(subject,question,answer1,answer2,answer3,answer4,Right_Answer) values('%s','%s','','','',''  ,'')" %(subject,question)
    print(22222222)
    dbc.execute(sql)
    db.commit()
    db.close()

def insert2(question,ziduan,bianliang):
    db = pymysql.connect('192.168.1.98', 'test', 'Lxq_204389', 'Examination_system', port=3306, charset='utf8')
    dbc = db.cursor()
    print(33333333)
    sql="update Questions set %s='%s' where question='%s'" %(ziduan,bianliang,question)
    print(44444444)
    dbc.execute(sql)
    db.commit()
    db.close()

def insert3(question,bianliang):
    db = pymysql.connect('192.168.1.98', 'test', 'Lxq_204389', 'Examination_system', port=3306, charset='utf8')
    dbc = db.cursor()
    sql="update Questions set Right_Answer='%s' where question='%s'" %(bianliang,question)
    dbc.execute(sql)
    db.commit()
    db.close()

num = random.randint(5,20)
#问题
question=''
for i in range(num):
    question+=random.choice(string.ascii_letters)
insert1(subject,question)
print('插入题目')
ccc=random.randint(1,4)
for a in range(1,5):
    num = random.randint(5, 10)
    answer='answer'+str(a)
    bbb=''
    for b in range(num):
        bbb+=random.choice(string.ascii_letters)
    if a == ccc:
        insert3(question,bbb)
    print(bbb)
    insert2(question, answer, bbb)
    print(answer+':'+bbb)

