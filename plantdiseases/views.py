from django.shortcuts import render


class PDObj:
    def __init__(self, na, de, sy, ca, cao, mo, org, cr, pl, pa, ge, pr, co ):
        self.id = '4g5h2'
        self.name = na
        self.description = de
        self.symptom = sy
        self.causativeAgent = ca
        self.causativeOrganism = cao
        self.modeOfSpread = mo
        self.organAffected = org
        self.cropAffected = cr
        self.plantTypesAffected = pl
        self.pathogenGeneration = pa
        self.geographicDistribution = ge
        self.prevention = pr
        self.control = co


ctx = {
    'plant_diseases':  [
        PDObj(
            'cassava mosaic disease', 
            'viral disease recognised for ...',
            [],
            'virus',
            'begomo virus',
            [],
            ['leaves'],
            ['cassava'],
            [], '', '',
            ['removal of crop residues', 'uproot weeds', 'crop rotation with cereals', 'spray preventative fungicide'],
            ['prune and burn diseased leaves', 'spray cyproconazole', 'spray copper oxychloride products', 'spray sulphur based products']
        ),
        PDObj(
            'powdery mildew',
            'fungal disease recognised for its powdery loose white substance on leaves',
            ['powdery white substance on leaves, in early stages', 'black leaf surface'],
            'fungus',
            'podosphaera xanthii',
            ['airborne'],
            ['leaves'],
            ['okra', 'pumpkin'],
            ['vegetables'],
            '', '',
            ['removal of crop residues', 'uproot weeds', 'crop rotation with cereals', 'spray preventative fungicide'],
            ['prune and burn diseased leaves', 'spray cyproconazole', 'spray copper oxychloride products', 'spray sulphur based products']
        ),
        PDObj(
            'early leaf spot', 
            'fungal disease recognised for ...',
            [],
            'fungus',
            'passalora arachidicola',
            [],
            ['leaves'],
            ['groundnuts'],
            ['legumes'],
            '', '',
            ['removal of crop residues', 'uproot weeds', 'crop rotation with cereals', 'spray preventative fungicide'],
            ['prune and burn diseased leaves', 'spray cyproconazole', 'spray copper oxychloride products', 'spray sulphur based products']
        )
    ]
}


def app(request):
    return render(request, 'src/index.html', ctx)


def dynamic(request):
    return render(request, 'src/slug.html', ctx)