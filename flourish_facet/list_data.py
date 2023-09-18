from edc_list_data import PreloadData
from edc_constants.constants import OTHER, NONE, NOT_APPLICABLE

list_data = {
    'flourish_facet.artchallenges': [
        ('travel_out_of_town', 'Travel out of town'),
        ('someone_may_find_out_the_mothers_hiv_status',
         'Someone may find out the mothers HIV status'),
        ('remembering_to_take_the_medicine', 'Remembering to take the medicine'),
        ('side_effects', 'Side Effects'),
        ('believe_that_medication_may_not_be_effective',
         'Believe that medication may not be effective'),
        ('lost_medication', 'Lost medication'),
        ('medication_stock_outs', 'Medication stocks outs'),
        ('other_specify', 'Other, Specify'),
    ],

    'flourish_facet.partnerreaction': [
        ('confused', 'Confused'),
        ('angry', 'Angry'),
        ('scared', 'Scared'),
        ('neutral', 'Neutral'),
        ('dont_know', 'Dont know'),
        (NOT_APPLICABLE, 'Not applicable')
    ],
    'flourish_facet.expensecontributors': [
        ('partner', 'Partner/husband'), ('mother', 'Mother'),
        ('father', 'Father'),
        ('sister', 'Sister'), ('brother', 'Brother'), ('aunt', 'Aunt'),
        ('uncle', 'Uncle'),
        ('grandmother', 'Grandmother'), ('grandfather', 'Grandfather'),
        ('mother_in_law', 'Mother-in-law or Father-in-law'),
        ('friend', 'Friend'),
        ('unsure', 'Unsure'), (OTHER, 'Other, specify')
    ]
}

preload_data = PreloadData(
    list_data=list_data)
