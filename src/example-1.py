##############################################################################################
# Author: Ekalavya
# Description: This code shows how a jinja template engine works. It takes input data and
# a template as inouts and then renders the final output
##############################################################################################
from configparser import ConfigParser

import jinja2


def load_template(tmplt_name):
    tmplt_loader = jinja2.FileSystemLoader(searchpath='../templates')
    tmplt_env = jinja2.Environment(loader=tmplt_loader)

    tmplt = tmplt_env.get_template(tmplt_name)
    return tmplt                                    # Return the select.tmplt template object


def main(env):
    config_parser = ConfigParser()
    config_parser.read('../conf/env.ini')
    DB = config_parser.get(env, 'DB')               # Get the input data from .ini
    SCHEMA = config_parser.get(env, 'SCHEMA')       # Get the input data from .ini
    template = load_template('select.tmplt')
    out_sql = template.render(DB=DB,
                              SCHEMA=SCHEMA)        # Finally, render the SQL output

    print(out_sql)


if __name__ == "__main__":
    main('DEV')
    main('PROD')
    main('STAGE')
