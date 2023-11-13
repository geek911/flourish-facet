from edc_list_data import PreloadData
from edc_constants.constants import OTHER, NONE, NOT_APPLICABLE, UNKNOWN

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
        (OTHER, 'Other, Specify'),
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
    ],
    'flourish_facet.chronicconditions': [
        ('chist_asthma', 'Asthma'),
        ('chist_headache', 'Headache (includes migraines, tension headaches)'),
        ('chist_anemia', 'Anemia'),
        ('chist_murmur', 'Cardiac murmur'),
        ('chist_seizure', 'Seizure disorder or other epilepsy'),
        ('chist_diab', 'Diabetes'),
        ('chist_hbp', 'High Blood Pressure'),
        ('chist_cholest', 'High Cholesterol'),
        ('chist_depress', 'Depression'),
        ('chist_lupus', 'Systemic Lupus'),
        ('chist_arthrit ', 'Juvenile rheumatoid arthritis'),
        ('chist_nephrotic ', 'Nephrotic syndrome'),
        ('chist_renal', 'Renal insufficiency'),
        ('chist_nephrol', 'Nephrolithiasis (kidney stones)'),
        ('chist_canc_tumor', 'Cancer (Solid tumor)'),
        ('chist_canc_leuk', 'Cancer (Leukemia, lymphoma related) '),
        ('chist_arrhyt ', 'Cardiac arrhythmia'),
        ('chist_thyroid ', 'Thyroid disorder'),
        ('chist_ibs', 'Inflammatory bowel disease (Crohn’s, ulcerative colitis)'),
        ('chist_other', 'Other, Specify'),
        ('chist_na', 'Not Applicable')
    ],

    'flourish_facet.medications': [
        ('inhaler', 'Inhaler/Albuterol'),
        ('antibiotics', 'Antibiotics'),
        ('anti_anxiety_drugs', 'Anti-anxiety drugs'),
        ('anti_asthmatic_drugs', 'Anti-asthmatic drugs'),
        ('antidepressant_drugs', 'Antidepressant drugs'),
        ('cholesterol_medications', 'Cholesterol medications'),
        ('diabetic_medications', 'Diabetic medications'),
        ('heart_disease_medications', 'Heart disease medications'),
        ('hypertensive_medications', 'Hypertensive medications'),
        ('pain_killers', 'Pain killers'),
        ('tb_treatment', 'TB Treatment'),
        ('tpt', 'TPT (TB preventive therapy)'),
        ('traditional_medications', 'Traditional medications'),
        ('vitamin_d_supplement', 'Vitamin D supplement'),
        (UNKNOWN, 'Unknown'),
        (OTHER, 'Other'),
    ],
    'flourish_facet.generalsymptoms': [
        ('cough', 'Cough'),
        ('fever', 'Fever'),
        ('headache', 'Headache'),
        ('vomiting', 'Vomiting'),
        ('diarrhea', 'Diarrhea'),
        ('fatigue', 'Fatigue'),
        ('congestion', 'Congestion'),
        ('enlarged_lymph_nodes', 'Enlarged Lymph nodes'),
        (OTHER, 'Other'),
    ]
}

preload_data = PreloadData(
    list_data=list_data)
