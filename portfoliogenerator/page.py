from portfoliogenerator.sections import make_sections
from portfoliogenerator.paragraph import make_paragraph


def make_page(page):
    return {
        'title': page['title'],
        'header': page['header'],
        'icon': page['icon'],
        'subheader': make_paragraph(page['subheader']),
        'sections': make_sections(page['sections']),
    }
