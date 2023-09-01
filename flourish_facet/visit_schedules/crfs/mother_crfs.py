from edc_visit_schedule import FormsCollection, Crf

mother_crfs = FormsCollection(
    Crf(show_order=1, model='flourish_facet.householdhungerscale'),
    Crf(show_order=2, model='flourish_facet.intimatepartnerviolence'),
    Crf(show_order=3, model='flourish_facet.maternalhivart'),
    # Crf(show_order=4, model='flourish_caregiver.sociodemographicdata'),
    # Crf(show_order=5, model='flourish_caregiver.caregiverphqdeprscreening'),
    # Crf(show_order=6, model='flourish_caregiver.relationshipfatherinvolvement'),
    name='facet_enrollment')
