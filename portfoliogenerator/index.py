from portfoliogenerator.sections import make_sections


def make_index_data(index):
    if isinstance(index['welcome_phrase'], list):
        welcome_phrase = '&nbsp;<br/>'.join(index['welcome_phrase'])
    else:
        welcome_phrase = index['welcome_phrase']

    return {
        'title': index['title'],
        'main_button': index['main_button'],
        'welcome_phrase': welcome_phrase,
        'header': index['header'],
        'sections': make_sections(index['sections']),
        'footer': index['footer']
    }
