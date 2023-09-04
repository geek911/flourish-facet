from edc_visit_schedule import FormsCollection, Crf

mother_crfs = FormsCollection(
    Crf(show_order=1, model='flourish_facet.householdhungerscale'),
    Crf(show_order=2, model='flourish_facet.intimatepartnerviolence'),
    Crf(show_order=3, model='flourish_facet.maternalhivart'),
    Crf(show_order=4, model='flourish_facet.facetsociodemographicdata'),
    Crf(show_order=5, model='flourish_facet.depressionscreeningphq9'),
    Crf(show_order=6, model='flourish_facet.depressionscreeningedinburgh'),
    name='facet_enrollment')
