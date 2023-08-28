"""flourish_facet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .admin_site import flourish_facet_admin
from django.urls import path
from edc_dashboard import UrlConfig
from django.views.generic.base import RedirectView
from .views import FacetConsentListboardView
from .patterns import subject_identifier, screening_identifier, study_maternal_identifier


app_name = 'flourish_facet'

urlpatterns = [
    path('admin/', flourish_facet_admin.urls),
    # path('', RedirectView.as_view(url='admin/'), name='home_url'),
]

flourish_facet_consent_listboard_url_config = UrlConfig(
    url_name='flourish_facet_consent_listboard_url',
    view_class=FacetConsentListboardView,
    label='flourish_facet_consent_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)


urlpatterns += flourish_facet_consent_listboard_url_config.listboard_urls