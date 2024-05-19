

def make_paragraph(content):
    if isinstance(content, list):
        return '&nbsp;<br/>'.join(content)

    return content
