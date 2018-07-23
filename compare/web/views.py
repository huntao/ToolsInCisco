from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from web.form import UploadFileForm
import re
from bs4 import BeautifulSoup
# Create your views here.

x1 = ''
x2 = ''
x3 = ''
x4 = ''
def handle_uploaded_file(f, k):
    #f = UploadFileFormt(request.POST, request.FILES)
    with open('upload/%s.html' % k, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.__dir__())
        if form.is_valid():
            #for a in request.FILES:

            handle_uploaded_file(request.FILES['file1'], request.POST['title1'])
            handle_uploaded_file(request.FILES['file2'], request.POST['title2'])
            handle_uploaded_file(request.FILES['file3'], request.POST['title3'])
            handle_uploaded_file(request.FILES['file4'], request.POST['title4'])
            global x1,x2,x3,x4
            x1 = request.POST['title1']
            x2 = request.POST['title2']
            x3 = request.POST['title3']
            x4 = request.POST['title4']
            return redirect('/result/')
    else:
        form = UploadFileForm()
    return render_to_response('init.html', {'form': form})


def error_flag(self):
    if error_flag is True:
        print('there is an error')


def create_table(soup):
    result = []
    table = []
    case = soup.find_all(text=re.compile('test_cases'))
    v = soup.select('a')
    for i in range(0, len(v)):
        x = str(v[i]).split('>')
        result.append(x[1])
    for i in range(0, len(v)):
        if len(case) != len(v):
            error_flag(True)
        else:
            table.append([case[i],result[i]])
    return table


def list_to_dict(table):
    dic = {}
    for i in range(0, len(table)):
        dic[table[i][0]]= table[i][1]
    return dic


def compare_dict(result_1, result_2):
    differences = {}
    for key in result_2.keys():
        if key in result_1.keys():
            if result_2[key] != '*.Pass</a':
                differences[key]=[result_1[key], result_2[key]]
    return differences


def compare(request):
    global x1, x2, x3, x4
    file1 = 'upload/%s.html' % x1
    file2 = 'upload/%s.html' % x2
    file3 = 'upload/%s.html' % x3
    file4 = 'upload/%s.html' % x4
    soup_1 = BeautifulSoup(open(file1), 'lxml')
    soup_2 = BeautifulSoup(open(file2), 'lxml')
    soup_3 = BeautifulSoup(open(file3), 'lxml')
    soup_4 = BeautifulSoup(open(file4), 'lxml')
    table_1 = create_table(soup_1)
    table_2 = create_table(soup_2)
    table_3 = create_table(soup_3)
    table_4 = create_table(soup_4)
    table_a = table_1 + table_2
    table_b = table_3 + table_4
    dict_1 = list_to_dict(table_a)
    dict_2 = list_to_dict(table_b)
    dict_content = compare_dict(dict_1, dict_2)
    print(dict_content)
    return render_to_response('result.html', {'data': dict_content})
