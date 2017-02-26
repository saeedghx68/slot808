import csv
from django.http import StreamingHttpResponse
import cStringIO as StringIO
from django.contrib.auth import get_user_model

User = get_user_model()


def view_user_list(request, *args, **kwargs):
    def stream():
        buffer_ = StringIO.StringIO()
        writer = csv.writer(buffer_)
        writer.writerow(['id', 'username', 'first_name', 'last_name'])
        rows = User.objects.all()
        for user_obj in rows:
            writer.writerow([user_obj.id, user_obj.username, user_obj.first_name,\
                    user_obj.last_name])
            buffer_.seek(0)
            data = buffer_.read()
            buffer_.seek(0)
            buffer_.truncate()
            yield data
    response = StreamingHttpResponse(
            stream(), content_type='text/csv'
            )
    disposition = "attachment; filename=file.csv"
    response['Content-Disposition'] = disposition
    return response