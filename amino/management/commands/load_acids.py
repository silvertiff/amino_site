from django.core.management.base import BaseCommand
from amino.models import AminoAcid


ACIDS = [
    {'name': 'Аланин', 'three_letter_code': 'Ala', 'one_letter_code': 'A', 'structure_image' : 'Alanine.png', 'description': ''},
    {'name': 'Аргинин', 'three_letter_code': 'Arg', 'one_letter_code': 'R', 'structure_image': 'Arginine.png', 'description': ''},
    {'name': 'Аспарагин', 'three_letter_code': 'Asn', 'one_letter_code': 'N', 'structure_image': 'Asparagine.png', 'description': ''},
    {'name': 'Аспарагиновая кислота', 'three_letter_code': 'Asp', 'one_letter_code': 'D', 'structure_image': 'Aspartic_acid.png', 'description': ''},
    {'name': 'Цистеин', 'three_letter_code': 'Cys', 'one_letter_code': 'C', 'structure_image': 'Cysteine.png', 'description': ''},
    {'name': 'Глутаминовая кислота', 'three_letter_code': 'Glu', 'one_letter_code': 'E', 'structure_image': 'Glutamic_acid.png', 'description': ''},
    {'name': 'Глутамин', 'three_letter_code': 'Gln', 'one_letter_code': 'Q', 'structure_image': 'Glutamin.png', 'description': ''},
    {'name': 'Глицин', 'three_letter_code': 'Gly', 'one_letter_code': 'G', 'structure_image': 'Glycine.png', 'description': ''},
    {'name': 'Гистидин', 'three_letter_code': 'His', 'one_letter_code': 'H', 'structure_image': 'Histidine.png', 'description': ''},
    {'name': 'Изолейцин', 'three_letter_code': 'Ile', 'one_letter_code': 'I', 'structure_image': 'Isoleucine.png', 'description': ''},
    {'name': 'Лейцин', 'three_letter_code': 'Leu', 'one_letter_code': 'L', 'structure_image': 'Leucine.png', 'description': ''},
    {'name': 'Лизин', 'three_letter_code': 'Lys', 'one_letter_code': 'K', 'structure_image': 'Lysine.png', 'description': ''},
    {'name': 'Метионин', 'three_letter_code': 'Met', 'one_letter_code': 'M', 'structure_image': 'Methionine.png', 'description': ''},
    {'name': 'Фенилаланин', 'three_letter_code': 'Phe', 'one_letter_code': 'F', 'structure_image': 'Phenylalanine.png', 'description': ''},
    {'name': 'Пролин', 'three_letter_code': 'Pro', 'one_letter_code': 'P', 'structure_image': 'Proline.png', 'description': ''},
    {'name': 'Серин', 'three_letter_code': 'Ser', 'one_letter_code': 'S', 'structure_image': 'Serine.png', 'description': ''},
    {'name': 'Треонин', 'three_letter_code': 'Thr', 'one_letter_code': 'T', 'structure_image': 'Threonine.png', 'description': ''},
    {'name': 'Триптофан', 'three_letter_code': 'Trp', 'one_letter_code': 'W', 'structure_image': 'Tryptophan.png', 'description': ''},
    {'name': 'Тирозин', 'three_letter_code': 'Tyr', 'one_letter_code': 'Y', 'structure_image': 'Tyrosin.png', 'description': ''},
    {'name': 'Валин', 'three_letter_code': 'Val', 'one_letter_code': 'V', 'structure_image': 'Valine.png', 'description': ''},
]


class Command(BaseCommand):
    help = 'Load 20 amino acids'

    def handle(self, *args, **kwargs):
        for acid in ACIDS:
            AminoAcid.objects.get_or_create(
                name=acid['name'],
                three_letter_code=acid['three_letter_code'],
                one_letter_code=acid['one_letter_code'],
                structure_image=acid['structure_image'],
                description=acid['description']
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded amino acids'))
