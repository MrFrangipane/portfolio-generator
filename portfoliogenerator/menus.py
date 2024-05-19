

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
