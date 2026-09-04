from django.shortcuts import render
from django.http import HttpResponse

def newmessage(request):
    return HttpResponse("This is my first program")

def program(request):
    name = "Basit"
    Spec = "Btech CSE"
    return HttpResponse(f"The name is {name} and the program name is {Spec}")

# Question 1: Create a view(Function) named performance that accepts five variables as course1, course2,course3,course4,course5 and assign the values to these  variables, then calculate the percentage of the student and print the same as an HttpResponse on the browser by creating a path as "result/" in urls.py. Also, print the percentage in bold and in greem color.

# Example: The percentage of the student is 89.7%

def performance(request):
    course1, course2, course3, course4, course5 = 89,56,71,45,98
    percentage = ((course1+course2+course3+course4+course5)/500)*100
    return HttpResponse(f"<p>The Percentage of the student is <b style='color:green; border:2px solid blue'>{percentage}%<b></p>")

def simplehtml(request):
    return HttpResponse("""<h1>This is a heading</h1>
                        <h2>This is a heading2</h2> 
                        <h3>This is a heading3</h3>""")
# Question 2: Print Grades Grade A green Grade B Blue Grade C Orange Grade D Red Color with If condition
def grade(request):
    marks = 60
    if marks >= 80 and marks <= 100:
        return HttpResponse("<p style='color:green;'>The Grade is A</p>")
    elif marks >= 60 and marks < 80:
        return HttpResponse("<p style='color:blue;'>The Grade is B</p>")
    elif marks >= 40 and marks < 60:
        return HttpResponse("<p style='color:orange;'>The Grade is C</p>")
    elif marks >= 0 and marks < 40:
        return HttpResponse("<p style='color:red;'>The Grade is D</p>")
    else:
        return HttpResponse("<p style='color:black;'>Invalid marks</p>")

# Question 3: Table
def table(request):
    number = 51
    content = f"<h1>Table of {number}</h1>"
    for i in range(1,11):
        content+=f"{number} x {i} = {number*i}<br>"
    return HttpResponse(content)

# Lists Used []
def products(request):
    prods=["Chair", "Table", "Cupboard", "Bed"]
    content = "<h1>The products are:</h1>"
    for prod in prods:
        content+= f"<li>{prod}</li>"
    return HttpResponse(content)

# Dictionary used: {}
def prodinfo(request):
    prod={
        "name":"Bed",
        "type":"single",
        "material":"wood",
        "price":2300
    }
    content=""
    for key, value in prod.items():
        content+=f"<p>The {key} is {value}</p>"
    return HttpResponse(content)

# tuple used ()

def prodsinfo(request):
    prods=[
        {"name":"Chair", "type":"double","material":"steel","price":1200},
        {"name":"Table", "type":"single", "material":"wood", "price":3300},
        {"name":"Cupboard", "type":"double", "material":"iron", "price":7000},
        {"name":"Bed", "type":"single", "material":"wood", "price":6700},
    ]
    content="""
    <table>
    <tr>
    <th>Name</th>
    <th>Material</th>
    <th>Price</th>
    </tr>
    """
    for i in prods:
        content += f"""
        <tr>
            <td>{i["name"]}</td>
            <td>{i["material"]}</td>
            <td>{i["price"]}</td>
        </tr>
        """
    content += "</table>"
    return HttpResponse(content)


# Dynamic URL
def greetings(request, name):
    return HttpResponse(f"Welcome,{name}")


def foodlist(request, foodvalue):
    fooditems = {
        "ice cream": "Size is small, price is 100",
        "milk shake": "Size is large,price is 80",
        "browine": "Size is medium, price is 70",
    }
    if foodvalue in fooditems:
        return HttpResponse(
            f"You have selected {foodvalue}. {fooditems[foodvalue]}"
        )
    else:
        return HttpResponse(
            f"Sorry, {foodvalue} is not available."
        )

    # -------------Dynamic URLs(Query parameter)------
def searchquery(request):
        querysubject = request.GET.get('q')
        return HttpResponse(f"You searched for {querysubject}")

#----------------------Regex--------------------------
def customer_profile(request, customername):
    return HttpResponse(f'Customer Profile: {customername}')

def customer_profile1(request, customername):
    return HttpResponse(f'Customer Profile: {customername}')