

def make_paragraph(content):
    if isinstance(content, list):
        return '&nbsp;<br/>'.join(content)

    if isinstance(content, dict):
        lines = content.get('lines', None)
        if lines is not None:
            return '&nbsp;<br/>'.join(lines)

        text = content.get('text', None)
        if text is not None:
            return make_paragraph(text)

    return content
