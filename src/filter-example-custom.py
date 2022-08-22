import jinja2


def get_table_view_mapping(table_name):
    tbl_col_map = {"test_table": "test_view",
                   "test_table_1": "test_view_1"}

    col_list = tbl_col_map.get(table_name)

    return col_list


def get_table_col_mapping(table_name):
    tbl_col_map = {"test_table": ['col1', 'col2', 'col3', 'col4'],
                   "test_table_1": ['col5', 'col6', 'col7', 'col8']}

    col_list = tbl_col_map.get(table_name)

    return col_list


def get_column_properties(col_name, properties):
    aliases = {"col1": "column_1",
               "col2": "column_2",
               "col3": "column_3",
               "col4": "column_4"}

    alias = aliases.get(col_name)
    return alias


def load_template(tmplt_name):
    tmplt_loader = jinja2.FileSystemLoader(searchpath='../templates')
    tmplt_env = jinja2.Environment(loader=tmplt_loader)
    tmplt_env.filters["get_property"] = get_column_properties
    tmplt_env.filters["tbl_col_map"] = get_table_col_mapping
    tmplt_env.filters["get_view"] = get_table_view_mapping
    tmplt = tmplt_env.get_template(tmplt_name)

    return tmplt  # Return the select.tmplt template object


def main():
    template = load_template('select_from_table_custom.tmplt')
    table_name = "test_table"
    out_sql = template.render(table_name=table_name)  # Finally, render the SQL output

    print(out_sql)


if __name__ == "__main__":
    # for i in range(len(col_list)):
    #     print(col_list[i])
    main()
