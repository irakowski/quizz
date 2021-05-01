from django.core.management.base import BaseCommand
from ._questions import zrodla_questions, analiza_podatkowa, podstawy_miedzynarodowe, \
    prawo_materialne, zobowiazania_podatkowe, tajemnica_skarbowa, vat, pit, cit, \
        tonaz, akcyza, kopaliny, instytucje_finansowe, nieruchomosci, gry, transport, \
            kpa, pos_pod, kont_pod, kont_cel, zaswiadczenia, sady, id_pod, \
            rolne, ccc, spadki, oplaty, egzek, celne, dewizy, \
                kks, organiz, rachunk, ewidencja, etyka 
from ._quizdata import *

class Command(BaseCommand):
    help = 'Prepopulates categories with questions and answers'
    def handle(self, *args, **options):
        create_category(categories)
        self.stdout.write(self.style.SUCCESS("Successfully created Categories"))
        create_questions("I. ŹRÓDŁA PRAWA I WYKŁADNIA PRAWA",zrodla_questions)
        create_questions("II. ANALIZA PODATKOWA", analiza_podatkowa)
        create_questions("III. PODSTAWY MIĘDZYNARODOWEGO ORAZ WSPÓLNOTOWEGO PRAWA PODATKOWEGO", podstawy_miedzynarodowe)
        create_questions("IV. MATERIALNE PRAWO PODATKOWE ZAGADNIENIA WSPÓLNE", prawo_materialne)
        create_questions("Zobowiązania podatkowe", zobowiazania_podatkowe)
        create_questions("Tajemnica skarbowa", tajemnica_skarbowa)
        create_questions("Podatek od towarów i usług", vat)
        create_questions("Podatek dochodowy od osób fizycznych", pit)
        self.stdout.write(self.style.SUCCESS("Still creating questions! Be Patient!"))
        create_questions("Podatek dochodowy od osób prawnych", cit)
        create_questions("Podatek tonażowy", tonaz)
        create_questions("Podatek akcyzowy", akcyza)
        create_questions("Podatek od wydobycia niektórych kopalin", kopaliny)
        create_questions("Podatek od gier", gry)
        create_questions("Podatek od niektórych instytucji finansowych", instytucje_finansowe)
        create_questions("Podatki i opłaty samorządowe. Podatek od nieruchomości", nieruchomosci)
        create_questions("Podatki i opłaty samorządowe. Podatek od środków transportowych", transport)
        create_questions("Podatki i opłaty samorządowe. Podatek rolny i podatek leśny", rolne)
        create_questions("Podatki i opłaty samorządowe. Podatek od czynności cywilnoprawnych", ccc)
        create_questions("Podatki i opłaty samorządowe. Podatek od spadków i darowizn", spadki)
        create_questions("Opłata skarbowa i inne opłaty samorządowe", oplaty)
        create_questions("Postępowanie egzekucyjne w administracji", egzek)
        self.stdout.write(self.style.SUCCESS("Category 5"))
        create_questions("V. POSTĘPOWANIE PRZED ORGANAMI ADMINISTRACJI PUBLICZNEJ I SĄDAMI ADMINISTRACYJNYMI. KPA", kpa)
        create_questions("Postępowanie podatkowe", pos_pod)
        create_questions("Czynności sprawdzające i kontrola podatkowa", kont_pod)
        create_questions("Kontrola celno-skarbowa", kont_cel)
        create_questions("Wydawanie zaświadczeń przez organy podatkowe", zaswiadczenia)
        create_questions("Prawo o postępowaniu przed sądami administracyjnymi", sady)
        create_questions("Ustawa o zasadach ewidencji i identyfikacji podatników i płatników", id_pod)
        create_questions("VI. MIĘDZYNARODOWE, WSPÓLNOTOWE I KRAJOWE PRAWO CELNE", celne)
        create_questions("VII. PRAWO DEWIZOWE", dewizy)
        create_questions("VIII. PRAWO KARNE SKARBOWE", kks)
        create_questions("IX. ORGANIZACJA I FUNKCJONOWANIE KRAJOWEJ ADMINISTRACJI SKARBOWEJ", organiz)
        create_questions("X. RACHUNKOWOŚĆ", rachunk)
        self.stdout.write(self.style.SUCCESS("Category 10"))
        create_questions("XI. EWIDENCJA PODATKOWA I ZASADY PROWADZENIA KSIĄG RACHUNKOWYCH", ewidencja)
        create_questions("XII. PRZEPISY O DORADZTWIE PODATKOWYM I ETYKA ZAWODOWA", etyka)



        self.stdout.write(self.style.SUCCESS("Successfully populated categories with questions!"))