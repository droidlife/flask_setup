def log_data(request):
    print(request.method, request.endpoint, request.data)
