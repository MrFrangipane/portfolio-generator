from portfoliogenerator.sections import make_sections
from portfoliogenerator.paragraph import make_paragraph


def make_index_data(index):
    return {
        'title': index['title'],
        'main_button': index['main_button'],
        'welcome_phrase': make_paragraph(index['welcome_phrase']),
        'header': index['header'],
        'sections': make_sections(index['sections']),
        'footer': index['footer']
    }
