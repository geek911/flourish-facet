from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


no_url_namespace = True if settings.APP_NAME == 'flourish_facet' else False

flourish_facet = Navbar(name='flourish_facet')

flourish_facet.append_item(
    NavbarItem(
        name='flourish_facet_consent_listboard',
        title='FACET Consents',
        label='FACET Listboard',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES[
            'flourish_facet_consent_listboard_url'],
        no_url_namespace=no_url_namespace))


site_navbars.register(flourish_facet)
