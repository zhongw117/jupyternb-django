from django.shortcuts import render

def index(request):

    return render(request, 'index.html', {})
def pipeline(request):

    return render(request, 'pipeline.html', {})

def missingvalues(reqeust):

    return render(reqeust, 'missing_values.html', {})
