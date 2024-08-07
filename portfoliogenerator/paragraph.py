

def make_paragraph(content):
    if isinstance(content, list):
        return '&nbsp;<br/>'.join([item if item is not None else "" for item in content])

    if isinstance(content, dict):
        lines = content.get('lines', None)
        if lines is not None:
            return '&nbsp;<br/>'.join([item if item is not None else "" for item in lines])

        text = content.get('text', None)
        if text is not None:
            return make_paragraph(text)

    return content
