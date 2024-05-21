import glob
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
        yaml_site = yaml.safe_load(file)

    site = {
        'title': yaml_site['title'],
        'menus': '\n'.join(make_menus(yaml_site['menu'])),
        'footer': yaml_site['footer'],
        'homepage': yaml_site['homepage']
    }

    env = Environment(loader=FileSystemLoader('./resources/html5up-twenty'))
    for yaml_source in glob.glob(os.path.join(source_directory, '*.yml')):
        page_data = {
            'site': site
        }

        if yaml_source == site_yaml_filepath:
            continue

        with open(yaml_source, 'r') as file:
            yaml_page = yaml.safe_load(file)

        if yaml_page['template'] == 'index':
            page_data['page'] = make_index_data(yaml_page)

        elif yaml_page['template'] == 'no-sidebar':
            page_data['page'] = make_page(yaml_page)

        template = env.get_template(yaml_page['template'] + '.html.j2')
        page_filepath = os.path.join(target_directory, os.path.splitext(os.path.basename(yaml_source))[0] + '.html')

        with open(page_filepath, 'wb+') as file:
            file.write(template.render(page_data).encode('utf-8'))

main(
    source_directory='E:/PROJECTS_2024/portfolios/frangitron/source',
    target_directory='E:/PROJECTS_2024/portfolios/frangitron/output'
)
