from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Flourish Facet'
    site_header = 'Flourish Facet'
    index_title = 'Flourish Facet'
    site_url = '/administration/'
    enable_nav_sidebar = False


flourish_facet_admin = AdminSite(name='flourish_facet_admin')
