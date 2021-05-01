from quiz.models import Category, Question, Answer

categories = [
    ("I. ŹRÓDŁA PRAWA I WYKŁADNIA PRAWA"),
    ("II. ANALIZA PODATKOWA"),
    ("III. PODSTAWY MIĘDZYNARODOWEGO ORAZ WSPÓLNOTOWEGO PRAWA PODATKOWEGO"),
    ("IV. MATERIALNE PRAWO PODATKOWE ZAGADNIENIA WSPÓLNE"),
    ("Zobowiązania podatkowe"),
    ("Tajemnica skarbowa"),
    ("Podatek od towarów i usług"),
    ("Podatek dochodowy od osób fizycznych"),
    ("Podatek dochodowy od osób prawnych"),
    ("Podatek tonażowy"),
    ("Podatek akcyzowy"),
    ("Podatek od wydobycia niektórych kopalin"),
    ("Podatek od gier"),
    ("Podatek od niektórych instytucji finansowych"),
    ("Podatki i opłaty samorządowe. Podatek od nieruchomości"),
    ("Podatki i opłaty samorządowe. Podatek od środków transportowych"),
    ("Podatki i opłaty samorządowe. Podatek rolny i podatek leśny"),
    ("Podatki i opłaty samorządowe. Podatek od czynności cywilnoprawnych"),
    ("Podatki i opłaty samorządowe. Podatek od spadków i darowizn"),
    ("Opłata skarbowa i inne opłaty samorządowe"),
    ("Postępowanie egzekucyjne w administracji"),
    ("V. POSTĘPOWANIE PRZED ORGANAMI ADMINISTRACJI PUBLICZNEJ I SĄDAMI ADMINISTRACYJNYMI. KPA"),
    ("Postępowanie podatkowe"),
    ("Czynności sprawdzające i kontrola podatkowa"),
    ("Kontrola celno-skarbowa"),
    ("Wydawanie zaświadczeń przez organy podatkowe"),
    ("Prawo o postępowaniu przed sądami administracyjnymi"),
    ("Ustawa o zasadach ewidencji i identyfikacji podatników i płatników"),
    ("VI. MIĘDZYNARODOWE, WSPÓLNOTOWE I KRAJOWE PRAWO CELNE"),
    ("VII. PRAWO DEWIZOWE"),
    ("VIII. PRAWO KARNE SKARBOWE"),
    ("IX. ORGANIZACJA I FUNKCJONOWANIE KRAJOWEJ ADMINISTRACJI SKARBOWEJ"),
    ("X. RACHUNKOWOŚĆ"),
    ("XI. EWIDENCJA PODATKOWA I ZASADY PROWADZENIA KSIĄG RACHUNKOWYCH"),
    ("XII. PRZEPISY O DORADZTWIE PODATKOWYM I ETYKA ZAWODOWA")
]

def create_category(categories):
    for name in categories:
        Category.objects.create(name=name)

def create_questions(name, questions):
    category = Category.objects.get(name=name)
    for i in range(len(questions)):
        question = Question.objects.create(text=questions[i]['text'], category=category)
        answers = questions[i]['answers']
        for answer, flag in answers:
            Answer.objects.create(text=answer, is_correct=flag, question=question)