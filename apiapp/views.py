from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination, User1, Register
import json
from .ReadJSONData import myjsonfile

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token





# Create your views here.


dest1 = User1()
#dest1.name='Mumbai'
#dest1.desc='How are you??'



dest2 = Register()
#dest2.desc="Have a nice day!"


def DisplayData1():
   
   import sqlite3

   conn = sqlite3.connect('database.db')

   c = conn.cursor()

   UPasswordData = c.execute("SELECT Uname, Uemail FROM userdata102")
   
   result1 = UPasswordData.fetchall()

   result2 = dict(result1)

   myresult = json.dumps(result2)

   return myresult

   conn.commit()

   conn.close()


def DisplayData2():
   
   import sqlite3

   conn = sqlite3.connect('database.db')

   c = conn.cursor()

   UPasswordData = c.execute("SELECT * FROM userdata102")
   
   result = UPasswordData.fetchall()

   myresult = json.dumps(result)

   return myresult

   conn.commit()

   conn.close()


def DisplayData3():

   import json

   myjsonfile = open('apiapp\JSON_Data\JSON_Data_1.json', 'r')
   jsondata = myjsonfile.read()


   obj = json.loads(jsondata)

   #print(str(obj['comments']))
   #print(str(obj['total']))
   #print(str(obj['skip']))
   #print(str(obj['limit']))

   list = obj['comments']
   return list

   #print(len(list))

   
   #for i in range(len(list)):
      #print("..........................")
      #print("Address of",i,"is :")
      #print("..........................")
      #print("Id:",list[i].get("id"))
      #print("body:",list[i].get("body"))
      #print("postId:",list[i].get("postId"))
      #print("user:",list[i].get("user"))
      #print()
      
   #return list
  
    #("Id:",list[i].get("id"), "body:",list[i].get("body"),"postId:",list[i].get("postId"),"user:",list[i].get("user"))
  
def rhome2(request):
    return render(request, "rhome2.html",{'DisplayData3':DisplayData3()})
    #return render(request, "DisplayData3()")



def LoginDetails1():

   import sqlite3

   conn = sqlite3.connect('database.db')

   c = conn.cursor()


   UPasswordData = c.execute("SELECT UPassword FROM userdata103")

   myresult = UPasswordData.fetchall()

   return myresult

   conn.commit()

   conn.close()




def LoginDetails2():

   import sqlite3

   conn = sqlite3.connect('database.db')

   c = conn.cursor()

   UemailData = c.execute("SELECT Uemail FROM userdata103")

   for item in UemailData:
      return item


   conn.commit()

   conn.close()


# Create your views here.

def home(request): 
     return render(request, 'home.html')

def Aboutus(request):
     
     return render(request, "Aboutus.html",{'dest1':dest1})


def Home(request):
    return render(request, "home.html")


def contactus(request):
    
    return render(request, "contactus.html")



def login(request):
   #These are input values we entered:
   
   import sqlite3

   conn = sqlite3.connect('database.db')

   c = conn.cursor()
   
   Uname = request.POST.get('Uname', None)
   Uemail = request.POST.get('Uemail', None)
   Umobile = request.POST.get('Umobile', None)
   Upassword = request.POST.get('Upassword', None)

   email = request.POST.get('email', None)
   mobile = request.POST.get('mobile', None)
   password = request.POST.get('password',None)
   
   #conn.commit()

   #conn.close()

   #return render(request, "login.html")

   

   def PasswordVerify():
   
      StoredPassword = str(LoginDetails1())
      InputPassword = request.POST.get('password',None)
      #InputPassword = str(password)

      import sqlite3

      conn = sqlite3.connect('database.db')

      c = conn.cursor()

      c.execute("SELECT * FROM userdata103")

      results = c.fetchall()
      lists = list(results)
      
      n = len(lists)

      i=0
      while(i<n):
         
          #print(lists[i][3])
          
          if(str(lists[i][3])==str(InputPassword)):
            return True
          i +=1



   def EmailIdVerify():

      StoredEmail = str(LoginDetails2())
      InputEmail = request.POST.get('email',None)
      #InputPassword = str(password)

      import sqlite3

      conn = sqlite3.connect('database.db')

      c = conn.cursor()

      c.execute("SELECT * FROM userdata103")

      results = c.fetchall()
      lists = list(results)
      
      n = len(lists)

      i=0
      while(i<n):
         #print(i)
         #print(str(InputPassword+"IP"))
         #print(str(lists[i][3])+"LP")
         #print(lists[i][1])
          
          if(str(lists[i][1])==str(InputEmail)):
            return True
          i +=1


   InputName = request.POST.get('name',None)

   #StoredPassword = str(LoginDetails1()[0])

   #InputEmail = str(email)

   #StoredEmail = str(LoginDetails2()[0])

   #n = len(StoredPassword)
   #for i in range(n):
   #   pass
   #'InputPassword':InputPassword, 'StoredPassword':StoredPassword, 'InputEmail':InputEmail, 'StoredEmail':StoredEmail
   #'InputPassword':InputPassword, 'StoredPassword':StoredPassword, 'InputEmail':InputEmail, 'StoredEmail':StoredEmail, 'PasswordVerify':PasswordVerify()

   if(PasswordVerify()):
      if(EmailIdVerify()):
        name = 'name'
        return render(request, "login.html",{'dest1':dest1, 'dest2':dest2, 'InputName':InputName, 'DisplayData1':DisplayData1(), 'DisplayData2':DisplayData2(), 'DisplayData3':DisplayData3(), 'out1':DisplayData3()})
      else:
        res = 'Email_Id'
        return render(request, "loginfailed.html", {'result':res})
   else:
     res='Password'
     return render(request, "loginfailed.html", {'result':res})

  
   conn.commit()

   conn.close()


   return render(request, "login.html")  # May be remove, not require




def loginfailed(request):

   return render(request, "loginfailed.html")


def Output(request):
    #user = dest1.objects.all()
    #print("MyOutput", user)
    return render(request, "Output.html")



def Register(request):

   import sqlite3

   conn = sqlite3.connect('database.db')

   c = conn.cursor()
   
   Uname = request.POST.get('Uname', None)
   Uemail = request.POST.get('Uemail', None)
   Umobile = request.POST.get('Umobile', None)
   Upassword = request.POST.get('Upassword',None)
   
   #c.execute("INSERT INTO userdata102 VALUES('Uname2','Uemail2','Umobile2','Upassword2')")
   
   c.execute("""
    CREATE TABLE IF NOT EXISTS userdata103(
    Uname TEXT NOT NULL UNIQUE,
    Uemail TEXT NOT NULL UNIQUE,
    Umobile INT,
    Upassword CHAR(15) NOT NULL UNIQUE
    )
    
   """)


   records = (Uname, Uemail, Umobile,Upassword)
   
   c.execute("INSERT INTO userdata103 VALUES(?,?,?,?)", (Uname, Uemail, Umobile, Upassword))
   
   # Command to delete all the records from table (Empty the table)
   #c.execute("DELETE FROM userdata103")

   conn.commit()

   conn.close()

   #Uname = request.POST.get('Uname',None) , {'Uname':Uname}
   return render(request, "Register1.html")



def Register1(request):
    return render(request, "Register1.html")



def my_redirect1(request):
   return redirect("https://github.com/")



#.....................................................................................................


@api_view(['GET'])
#def home(request):
def Out1(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)

    return Response({'status' : 200, 'payload' : serializer.data})




from rest_framework_simplejwt.tokens import RefreshToken



class RegisterUser(APIView):

    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status':403, 'message':'Something went wrong'})
    
        serializer.save()

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status': 200, 
        'payload': serializer.data, 
        'refresh': str(refresh),
        'access': str(refresh.access_token), 
        'message': 'you sent'})



from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication





# http://127.0.0.1:8000/student/
# path('student/', StudentAPI.as_view()),

class StudentAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        print(request.user)
        return Response({'status': 200, 'payload': serializer.data,'message': 'data loaded'})


    def post(self, request):
            data = request.data
            serializer = StudentSerializer(data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'message':'Something went wrong here'})
    
            serializer.save()

            return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})



    def patch(self, request):
        try:
            student_obj = Student.objects.get(id= request.data['id'])
    
            serializer = StudentSerializer(student_obj, data = request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'message':'Something went wrong'})
    
            serializer.save()

            return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})

        except Exception as e:
            return Response({ 'status':403, 'message':'you have entered wrong id'})



    def put(self, request):
        pass

    def delete(self, request):
        try:

            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({'status':200, 'message':'deleted'})
    
        except Exception as e:
            print(e)
            return Response({'status':403, 'message':'invalid id'})








"""
#.................................................................................................
# Create your views here.

#def home(request):
#    return render(request, 'home.html')


# API of GET request

@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)

    return Response({'status' : 200, 'payload' : serializer.data})


# API of POST request

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403, 'message':'Something went wrong'})
    
    serializer.save()

    return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})



# API of PUT request

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
    
        serializer = StudentSerializer(student_obj, data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'message':'Something went wrong'})
    
        serializer.save()

        return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})

    except Exception as e:
        return Response({ 'status':403, 'message':'you have entered wrong id'})



# API of DELETE request

@api_view(['DELETE'])
def delete_student(request, id):
    try:

        student_obj = Student.objects.get(id=id)
        student_obj.delete()
        return Response({'status':200, 'message':'deleted'})
    
    except Exception as e:
        print(e)
        return Response({'status':403, 'message':'invalid id'})




@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    return Response({'status':200, 'payload':serializer.data})


#...................................................................................
"""


















