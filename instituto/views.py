from django.http import JsonResponse

def estudiantes(request):
    if request.method == 'GET':
        estudiante ={
            'id':'1',
            'nombre':'Guilherme'
        }
        return JsonResponse(estudiante)


