from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


no_url_namespace = True if settings.APP_NAME == 'flourish_facet' else False

flourish_facet = Navbar(name='flourish_facet')

flourish_facet.append_item(
    NavbarItem(
        name='facet_mother_listboard',
        title='facet_mother_listboard',
        label='FACET Mother Listboard',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES[
            'facet_mother_listboard_url'],
        no_url_namespace=no_url_namespace))


flourish_facet.append_item(
    NavbarItem(
        name='facet_child_listboard',
        title='facet_child_listboard',
        label='FACET Child Listboard',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES[
            'facet_child_listboard_url'],
        no_url_namespace=no_url_namespace))


site_navbars.register(flourish_facet)
