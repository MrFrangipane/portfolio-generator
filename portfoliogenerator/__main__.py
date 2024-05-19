import os.path
import shutil

import yaml
from jinja2 import Environment, FileSystemLoader

from portfoliogenerator.index import make_index_data
from portfoliogenerator.menus import make_menus
from portfoliogenerator.page import make_page


def main(source_directory: str, target_directory: str):
    here = os.path.dirname(__file__)
    template_directory = os.path.join(here, 'resources', 'html5up-twenty')

    site_yaml_filepath = os.path.join(source_directory, "site.yml")
    if not os.path.isfile(site_yaml_filepath):
        raise FileNotFoundError(f"Site description file is missing '{site_yaml_filepath}")

    if os.path.exists(target_directory):
        if not os.path.isdir(target_directory):
            raise NotADirectoryError(f"Output must be a directory '{target_directory}'")
        else:
            print("Deleting everything in output directory")
            shutil.rmtree(target_directory)
    else:
        print("Creating output directory")
        os.mkdir(target_directory)

    shutil.copytree(os.path.join(template_directory, "assets"), os.path.join(target_directory, 'assets'))

    shutil.copytree(source_directory, target_directory, dirs_exist_ok=True)

    with open(site_yaml_filepath, 'r') as file:
        yaml_data = yaml.safe_load(file)

    to_render = {
        'title': yaml_data['title'],
        'index': make_index_data(yaml_data['index']),
        'menus': '\n'.join(make_menus(yaml_data['menu'])),
        'footer': yaml_data['footer']
    }

    env = Environment(loader=FileSystemLoader('./resources/html5up-twenty'))
    template = env.get_template('index.html.j2')

    index_filepath = os.path.join(target_directory, 'index.html')
    with open(index_filepath, 'wb+') as file:
        file.write(template.render(to_render).encode('utf-8'))

    for page in yaml_data['pages']:
        page_filepath = os.path.join(target_directory, page['filename']) + '.html'
        template = env.get_template('no-sidebar.html.j2')
        to_render['page'] = make_page(page)
        with open(page_filepath, 'wb+') as file:
            file.write(template.render(to_render).encode('utf-8'))


main(
    source_directory='../../input',
    target_directory='../../output'
)
