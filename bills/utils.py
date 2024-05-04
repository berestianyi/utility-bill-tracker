import re
from decimal import Decimal
from PyPDF2 import PdfReader


def pdf_reader(file) -> str:
    reader = PdfReader(file)
    page = reader.pages[0]
    return page.extract_text()


def is_heat_bill(pdf_text: str) -> bool:
    pattern = re.compile(r'Постачання теплової енергії')
    return bool(pattern.search(pdf_text))


def heat_total_price(pdf_text: str) -> str:
    total_str = re.search(r'ПДВ:(.*?)\nВсього до', pdf_text).group(1)
    return ''.join(total_str.split(' ')).replace(",", ".")


def general_bill_info(pdf_text: str) -> dict:
    months = {
        "СІЧЕНЬ": "01-01", "ЛЮТИЙ": "02-01",
        "БЕРЕЗЕНЬ": "03-01", "КВІТЕНЬ": "04-01",
        "ТРАВЕНЬ": "05-01", "ЧЕРВЕНЬ": "06-01",
        "ЛИПЕНЬ": "07-01", "СЕРПЕНЬ": "08-01",
        "ВЕРЕСЕНЬ": "09-01", "ЖОВТЕНЬ": "10-01",
        "ЛИСТОПАД": "11-01", "ГРУДЕНЬ": "12-01"
    }

    gen_info_dict = {'year': r'(\w{4}) Р.',
                     'house_number': r'КВАРТИРА/ПРИМІЩЕННЯ № (.*?)\s',
                     'month': r'ЗА (.*?) 20[0-9][0-9] Р\.'}
    for name in gen_info_dict.keys():
        maintenance_str = re.search(gen_info_dict.get(name), pdf_text).group(1)
        gen_info_dict[name] = ''.join(maintenance_str.split(" "))

    for month in months.keys():
        if month == gen_info_dict['month']:
            gen_info_dict['month_paid'] = gen_info_dict.get("year") + "-" + months.get(month)

    gen_info_dict["file_name"] = gen_info_dict['month_paid'] + "-" + gen_info_dict['house_number'] + ".pdf"
    return gen_info_dict


def communal_services_extract(pdf_text: str) -> dict:
    gen_names = {'maintenance_of_the_building': r'(\s[1-9]\s\w+,\w+|\w+,\w+|\w+)\nВнесок на утримання охорони',
                 'security': r'(\s[1-9]\s\w+,\w+|\w+,\w+|\w+)\nЗагальні показники лічильників',
                 'water_supply': r'(\s[1-9]\s\w+,\w+|\w+,\w+|\w+)\nСпоживання електричної енергії',
                 'electricity': r'(\s[1-9]\s\w+,\w+|\w+,\w+)\nБорг станом',
                 'gen_total_price': r'Всього нараховано за місяць: (.*?)\nПеня:'}
    for name in gen_names.keys():
        maintenance_str = re.search(gen_names.get(name), pdf_text).group(1)
        gen_names[name] = ''.join(maintenance_str.split(" ")).replace(',', '.')

    return gen_names
