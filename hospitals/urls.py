from django.urls.conf import path
from hospitals.views import NurseView, AddNoteView, NoteDetails

app_name = "hospitals"

urlpatterns = [
    path("nurse/", NurseView.as_view(), name="nurse-index"),
    path("add-note/<int:patient_id>/", AddNoteView.as_view(), name="add-note"),
    path("note-details/<int:pk>/", NoteDetails.as_view(), name="note-details")
]
