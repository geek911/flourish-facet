from edc_visit_schedule import FormsCollection, Crf

mother_crfs = FormsCollection(
    Crf(show_order=1, model='flourish_facet.householdhungerscale'),
    Crf(show_order=2, model='flourish_facet.intimatepartnerviolence'),
    Crf(show_order=3, model='flourish_facet.maternalhivart'),

    name='facet_enrollment')
