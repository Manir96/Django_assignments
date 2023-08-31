from django.shortcuts import render

# Create your views here.
def panel(request):
    return render(request,'base_code/index.html', {"courses":5})


def variable(request):
    java = 'Java Variables: Declaration, Scope, and Naming Conventions'
    python = 'Python Data Types'
    php = 'Php Programming Examples With Output'
    c_langoage = 'c Programming Examples With Output'
    ch = 'Kotlin Variables and Data Types'
    ther = 'ther are six seson'
    course_ditails = {'j':java, 'p':python, 'ph':php, 'c':c_langoage, 'a':ch, 't':ther,}
    return render(request,'common_code/common.html', course_ditails,)

def variable_data(request):

    data_ditails = {'data':['java','python','php','c_langoage','ch','ther',]}
    return render(request,'common_code/common.html', data_ditails,)


def common_code(request):
    return render(request,'common_code/common_code.html',)