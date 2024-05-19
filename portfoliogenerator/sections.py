

def make_section_featured_icons(article):
    html_lines = [
        '<section class="wrapper style2 container special-alt">',
        '<div class="row gtr-50">',
        '<div class="col-8 col-12-narrower">',
        '<header>',
        f"<h2>{article['title']}</h2>",
        '</header>',
        f'<p>{article['text']}</p>'
    ]

    if article.get('button', None) is not None:
        html_lines += [
            '<footer>',
            '<ul class="buttons">',
            f'<li><a href="#" class="button">{article['button']}</a></li>',
            '</ul>',
            '</footer>'
        ]

    html_lines += [
        '</div>',
        '<div class="col-4 col-12-narrower imp-narrower">',
        '<ul class="featured-icons">'
    ]
    for icon in article['icons']:
        html_lines.append(f'<li><span class="icon solid fa-{icon}"><span class="label">{icon}</span></span></li>')

    html_lines += [
        '</ul>',
        '</div>',
        '</div>',
        '</section>'
    ]
    return '\n'.join(html_lines)


def make_section_images_text_4cols(article):
    col = 0

    html_lines = [
        '<section class="wrapper style3 container special">',
        '<header class="major">',
        f"<h2>{article['title']}</h2>",
        '</header>',
    ]
    for section in article['sections']:
        if col == 0:
            html_lines.append('<div class="row">')

        html_lines += [
            '<div class="col-6 col-12-narrower">',
            '<section>',
            f'<a href="{section['link']}" class="image featured"><img src="{section['image']}" alt="" /></a>',
            '<header>',
            f'<h3>{section['title']}</h3>',
            '</header>',
            f'<p>{section['text']}</p>',
            '</section>',
            '</div>'
        ]

        col += 1
        if col == 2:
            html_lines.append('</div>')
            col = 0

    if col == 1:
        html_lines.append('</div>')

    if article.get('button', None) is not None:
        html_lines += [
            '<footer class="major">',
            '<ul class="buttons">',
            f'<li><a href="{article['link']}" class="button">{article['button']}</a></li>',
            '</ul>',
            '</footer>',
        ]

    html_lines.append('</section>')

    return '\n'.join(html_lines)


def make_section_columns3(section):
    def _section(sub_section):
        _html_lines = [
            '<div class="col-4 col-12-narrower">',
            '<section>'
        ]

        if sub_section.get('icon', None) is not None:
            _html_lines.append(f'<span class="icon solid featured fa-{sub_section['icon']}"></span>')

        _html_lines += [
            '<header>',
            f'<h3>{sub_section['title']}</h3>',
            '</header>',
            f'<p>{sub_section['text']}</p>'
        ]

        if sub_section.get('button', None) is not None:
            _html_lines += [
                '<footer>',
                '<ul class="buttons">',
                f'<li><a href="{sub_section['link']}" class="button small">{sub_section['button']}</a></li>',
                '</ul>',
                '</footer>'
            ]

        _html_lines += [
            '</section>',
            '</div>',
        ]

        return _html_lines

    html_lines = [
        '<section class="wrapper style1 container special">',
        '<div class="row">'
    ]

    html_lines += _section(section['left'])
    html_lines += _section(section['middle'])
    html_lines += _section(section['right'])
    html_lines += [
        '</div>',
        '</section>'
    ]
    return '\n'.join(html_lines)


def make_section_article(section):
    html_lines = [
        '<section class="wrapper style4 container">',
        '<div class="content">',
        '<section>'
    ]
    if section.get('image', None) is not None:
        html_lines.append(f'<a href="#" class="image featured"><img src="images/{section['image']}" alt="" /></a>')

    html_lines += [
        '<header>',
        f'<h3>{section['title']}</h3>',
        '</header>'
    ]
    for paragraph in section['paragraphs']:
        html_lines.append(f'<p>{paragraph}</p>')

    html_lines += [
        '</section>',
        '</div>',
        '</section>'
    ]

    return '\n'.join(html_lines)


def make_sections(sections):
    sections_html = list()
    for section in sections:
        if section['type'] == 'featured-icons':
            sections_html.append(make_section_featured_icons(section))

        elif section['type'] == 'images-text-4cols':
            sections_html.append(make_section_images_text_4cols(section))

        elif section['type'] == 'columns3':
            sections_html.append(make_section_columns3(section))

        elif section['type'] == 'article':
            sections_html.append(make_section_article(section))

    return sections_html
