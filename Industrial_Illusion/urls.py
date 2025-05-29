from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", include("home_page.urls")),
    path("reservation/", include("reservation.urls")),
    path("rooms/", include("rooms.urls")),
    path("contact/", include("contact.urls")),
)
