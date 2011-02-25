from models import RequestStore

class RequestStoreWare:
  def process_response(self, request):
    host = request.get_host()
    path = request.get_full_path()
    method = request.method
    if request.user.is_authenticated: user = request.user
    r_s = RequestStore(host = host, path=path, method=method, user=user)
    r_s.save()
    