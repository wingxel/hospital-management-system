from django.urls.conf import path
from hospitals.views import NurseView

app_name = "hospitals"

urlpatterns = [
    path("nurse/", NurseView.as_view(), name="nurse-index")
]
