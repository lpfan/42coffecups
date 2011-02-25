from models import RequestStore

class RequestStoreWare:
  def process_request(self, request):
    r_s = RequestStore()
    r_s.host = request.get_host()
    r_s.path = request.get_full_path()
    r_s.method = request.method
    if request.user.is_authenticated():
      r_s.user = request.user
    r_s.save()
    return None
    