from edc_visit_schedule import FormsCollection, Crf

child_crfs = FormsCollection(
    Crf(show_order=1, model='flourish_facet.childhivtesting'),
    Crf(show_order=2, model='flourish_facet.childanthropometry'),
    name='facet_enrollment')