from charterclub.permissions import render

def information(request):
    return render(request, "recruitment/information.html")
