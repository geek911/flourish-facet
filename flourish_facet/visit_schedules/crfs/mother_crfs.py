from edc_visit_schedule import FormsCollection, Crf

mother_crfs = FormsCollection(
    Crf(show_order=0, model='flourish_facet.householdhungerscale'),
    Crf(show_order=1, model='flourish_facet.intimatepartnerviolence'),
    Crf(show_order=2, model='flourish_facet.maternalhivart'),
    Crf(show_order=3, model='flourish_facet.facetsociodemographicdata'),
    Crf(show_order=4, model='flourish_facet.depressionscreeningphq9'),
    Crf(show_order=5, model='flourish_facet.depressionscreeningedinburgh'),
    Crf(show_order=6, model='flourish_facet.anxietyscreeninggad7'),
    Crf(show_order=7, model='flourish_facet.facetcaregiveredinburghpostreferral'),
    Crf(show_order=8, model='flourish_facet.facetcaregiveredinburghreferral'),
    Crf(show_order=9, model='flourish_facet.facetcaregiveredinburghreferralfu'),
    Crf(show_order=10, model='flourish_facet.facetcaregivergadpostreferral'),
    Crf(show_order=11, model='flourish_facet.facetcaregivergadreferral'),
    Crf(show_order=12, model='flourish_facet.facetcaregivergadreferralfu'),
    Crf(show_order=13, model='flourish_facet.facetcaregiverphqpostreferral'),
    Crf(show_order=14, model='flourish_facet.facetcaregiverphqreferral'),
    Crf(show_order=15, model='flourish_facet.facetcaregiverphqreferralfu'),
    name='facet_enrollment')
