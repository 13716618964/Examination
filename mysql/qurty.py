import pymysql
def init_connect():
    db=pymysql.connect('192.168.1.98','test','Lxq_204389','Examination_system',port=3306,charset='utf8')
    dbc=db.cursor()
    return db,dbc

def verification(username,student_id):
    db,dbc=init_connect()
    sql = "select userID,password,class from student where username='%s' and student_id='%s'" % (username,student_id)
    num = dbc.execute(sql)
    if num == 0:
        db.close()
        return '账号不存在'
    else:
        data = dbc.fetchone()
        db.close()
        print(data)
        return data

def select_subjects(CLASS):
    db, dbc = init_connect()
    sql = "select subjects from Examination_subjects where class='%s'" %CLASS
    dbc.execute(sql)
    data=dbc.fetchone()
    db.close()
    return data

def questions(subject):
    db, dbc = init_connect()
    sql="select question,answer1,answer2,answer3,answer4,Right_Answer from Questions where subject='%s'" %subject
    dbc.execute(sql)
    data=dbc.fetchall()
    db.close()
    return data

def questions1(subject):
    db, dbc = init_connect()
    sql="select a.question,a.answer1,a.answer2,a.answer3,a.answer4,a.Right_Answer,CAST(@bbb := @bbb+1 as char) from Questions a,(select @bbb:=0) b where subject='%s' ORDER BY ID DESC" %subject
    dbc.execute(sql)
    data=dbc.fetchall()
    db.close()
    return data

def insert_achievement(userID,achievement,datetime,subject):
    db,dbc=init_connect()
    sql="insert into Historical_achievement values('%s','%s','%s','%s')" %(userID,achievement,datetime,subject)
    dbc.execute(sql)
    db.commit()
    db.close()

def show_last_achievement(userID):
    db,dbc=init_connect()
    sql="select achievement from Historical_achievement where userID='%s' order by date DESC limit 0,1;" %userID
    dbc.execute(sql)
    data=dbc.fetchone()
    db.close()
    return data

def select_istorical_achievement(userID):
    db, dbc = init_connect()
    sql="select achievement,date,subject from Historical_achievement where userID='%s' order by date DESC" %userID
    dbc.execute(sql)
    data=dbc.fetchall()
    db.close()
    return data


def PersonalInformation(userID):
    db,dbc=init_connect()
    sql="select Enrollment,Graduation,student_ID from student where userID='%s'" %userID
    dbc.execute(sql)
    data=dbc.fetchone()
    return data

