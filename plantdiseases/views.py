from django.shortcuts import render



ctx = {
    'data':[
        {
            'id':'45hg-56is',   
            'title':[
                'peter butao',
                'peterethanbuao',
                '0991894703'
            ]
        },
]}


def app(request):
    return render(request, 'src/index.html', ctx)