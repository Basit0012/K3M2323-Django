from django.http import HttpResponse
def handler404(request, exception):
    return HttpResponse("<h1 style=color:red>Dear user, the content you are looking for do not exist</h1>",status=404)