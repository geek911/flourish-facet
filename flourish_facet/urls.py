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
from .views import FacetMotherConsentListboardView
from .views import FlourishConsentListboardView
from .views import FacetChildConsentListboardView
from .views import FacetMotherDashboardView
from .views import FacetChildDashboardView
from .patterns import subject_identifier, child_subject_identifier


app_name = 'flourish_facet'

urlpatterns = [
    path('admin/', flourish_facet_admin.urls),
    # path('', RedirectView.as_view(url='admin/'), name='home_url'),
]

facet_mother_listboard_url_config = UrlConfig(
    url_name='facet_mother_listboard_url',
    view_class=FacetMotherConsentListboardView,
    label='facet_mother_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)

flourish_consent_listboard_url_config = UrlConfig(
    url_name='facet_flourish_consent_listboard_url',
    view_class=FlourishConsentListboardView,
    label='flourish_consent_listboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)


facet_mother_dashboard_url_config = UrlConfig(
    url_name='facet_mother_dashboard_url',
    view_class=FacetMotherDashboardView,
    label='facet_mother_dashboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)


facet_child_listboard_url_config = UrlConfig(
    url_name='facet_child_listboard_url',
    view_class=FacetChildConsentListboardView,
    label='facet_child_listboard',)


facet_child_dashboard_url_config = UrlConfig(
    url_name='facet_child_dashboard_url',
    view_class=FacetChildDashboardView,
    label='facet_child_dashboard',
    identifier_label='subject_identifier',
    identifier_pattern=subject_identifier)


urlpatterns += facet_mother_listboard_url_config.listboard_urls
urlpatterns += flourish_consent_listboard_url_config.listboard_urls
urlpatterns += facet_mother_dashboard_url_config.dashboard_urls
urlpatterns += facet_child_listboard_url_config.listboard_urls
urlpatterns += facet_child_dashboard_url_config.dashboard_urls
