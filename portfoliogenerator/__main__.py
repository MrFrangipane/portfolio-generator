import yaml
from jinja2 import Environment, FileSystemLoader


def make_menus(menu: list[dict], html_lines: list[str] = None):
    if html_lines is None:
        html_lines = list()

    for item in menu:
        if item['type'] == 'menu':
            html_lines.append(f'<li class="submenu">')
            html_lines.append(f'<a href="#">{item['title']}</a>')
            html_lines.append(f'<ul>')

            make_menus(item['value'], html_lines)

            html_lines.append(f'</ul>')
            html_lines.append(f'</li>')

        elif item['type'] == 'link':
            html_lines.append(f'<li><a href="{item['value']}">{item['title']}</a></li>')

    return html_lines


def make_index_article_featured_icons(article):
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


def make_index_article_images_text_4cols(article):
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


def make_index_articles(articles):
    articles_html = list()
    for article in articles:
        if article['type'] == 'featured-icons':
            articles_html.append(make_index_article_featured_icons(article))
        elif article['type'] == 'images-text-4cols':
            articles_html.append(make_index_article_images_text_4cols(article))

    return articles_html


def make_index_data(index):
    if isinstance(index['welcome_phrase'], list):
        welcome_phrase = '<br/>'.join(index['welcome_phrase'])
    else:
        welcome_phrase = index['welcome_phrase']

    return {
        'title': index['title'],
        'main_button': index['main_button'],
        'welcome_phrase': welcome_phrase,
        'header': index['header'],
        'articles': make_index_articles(index['articles'])
    }


def main(in_filepath: str, out_filepath: str):
    with open(in_filepath, 'r') as file:
        yaml_data = yaml.safe_load(file)

    to_inject = {
        'title': yaml_data['title'],
        'index': make_index_data(yaml_data['index']),
        'menus': '\n'.join(make_menus(yaml_data['menu']))
    }

    env = Environment(loader=FileSystemLoader('./resources/html5up-twenty'))
    template = env.get_template('index.html.j2')

    with open(out_filepath, 'wb') as file:
        file.write(template.render(to_inject).encode('utf-8'))


main('../../input/tests.yml', '../../output/index.html')
