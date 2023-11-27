from django.urls.conf import path
from hospitals.views import NurseView, AddNoteView

app_name = "hospitals"

urlpatterns = [
    path("nurse/", NurseView.as_view(), name="nurse-index"),
    path("add-note/", AddNoteView.as_view(), name="add-note")
]
