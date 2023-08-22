from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'flourish_facet'
    verbose_name = 'Flourish Facet'
    admin_site_name = 'flourish_facet_admin'
