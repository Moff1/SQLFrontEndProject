from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.db.models import Q
import mysql.connector
import pandas as pd

def IDChecker():
    mydbstarter = mysql.connector.connect(host="localhost", user = "root", passwd="Moff-19192023$", database = "shoppingdata")

    #print(mydbstarter)

    TypedQuery = "select * from finalrecommendation order by customer_id asc"
    mycursor = mydbstarter.cursor()
    mycursor.execute(TypedQuery)

    myresultstarter = mycursor.fetchall()

    df = pd.DataFrame (myresultstarter, columns = ['customer_id','product_id','quantity','total_price'])
    #print (df)
    listid = df['customer_id'].array
    desired_array = [str(i) for i in listid]

    for i in desired_array:
        if i == '1':
            return True

#The above code is a way to see if a customer_ID is in the ResultSet or not

#This function acts the opening screen for the entire site, not just our application
def index(request):
    return HttpResponse("Greetings in the URL please type 127.0.0.1:8000/TesterSQLQuery to get to our application!")

#These are just tester functions commented out because we no longer had use for them.
#def hello(request):
    #data = request.POST.get('name')
    #print(data)
    #holder(data)
    #return render(request,'TesterFile.html',{'data':data})


#def holder(data):
    #print('This is the second iteration',data)

# This function returns the ResultSet in a more user-friendly manner (easier to read an intepret.
def dictfetchall(cursor):
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

#This function gets the request from the front-end HTML, which is the inputed Query, and returns it to the HTML file
def TesterSQLQuery(request):
    TypedQuery = request.POST.get('name',default = "64")
    TypedQueryToRun = "select * from finalrecommendation where customer_id = "+str(TypedQuery)
    NumberofCustomer = str(TypedQuery)
    print(TypedQueryToRun)
    print(TypedQuery)
    #myresult = SQLRunner(TypedQuery)
    myrealresult = SQLRunner(TypedQueryToRun)
    if IDChecker() == True:
        return render(request,'SQLQuery.html',{'myresult':myrealresult})
    else:
        return render(request,'SQLQuery.html',{'NothingHere':NumberofCustomer})


# This function actually connects the front-end to the backend and runs the query.
def SQLRunner(TypedQuery):
    mydb = mysql.connector.connect(host="127.0.0.1", port="3306", user = "root", passwd="Moff-19192023$", database = "shoppingdata")
    print(mydb)

    if(mydb):
        print("Connection Successful")
    else:
        print("Connection unsuccessful")

    mycursor = mydb.cursor()
    mycursor.execute(TypedQuery)
    myresult = dictfetchall(mycursor)

    print(myresult)
    print(connection.queries)

    for row in myresult:
        print(row)

    print(connection.queries)
    return myresult
