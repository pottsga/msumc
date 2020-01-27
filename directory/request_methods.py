def parameters(request):
    parameters = { 
        param: 
            None if request.params.get(param) == '' 
            else request.params.get(param) 
        for param in request.params
    }

    return parameters
