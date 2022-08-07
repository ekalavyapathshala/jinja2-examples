##############################################################################################
# Author: Ekalavya
# Description: This code demonstrates how looping can be done in a JINJA template
# this code can be enhanced further to develop a metadata driven ingestion framework
# or automate SQL conversions from one database to another
##############################################################################################
import jinja2

# the below lists are hard-coded, but this can also be populated from a metadata store
# the objective of this example is to show how to use looping using JINJA
# the following lists are zipped and the zipped value is used in the jinja template
# "insert_as_select.tmplt"
columns = ['column1', 'column2', 'coulmn3']
alias = ['col1', 'col2', 'col3']
column_position = [1, 2, 3]
total_size = [3, 3, 3]

zipped_col_info = list(zip(columns, alias, column_position, total_size))


def load_template(tmplt_name):
    tmplt_loader = jinja2.FileSystemLoader(searchpath='../templates')
    tmplt_env = jinja2.Environment(loader=tmplt_loader)
    tmplt = tmplt_env.get_template(tmplt_name)

    return tmplt  # Return the select.tmplt template object


def main():
    template = load_template('insert_as_select.tmplt')
    out_sql = template.render(zipped_col_info_var=zipped_col_info)  # Finally, render the SQL output

    print(out_sql)


if __name__ == "__main__":
    main()
