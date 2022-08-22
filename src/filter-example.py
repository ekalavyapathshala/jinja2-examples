import jinja2

col_list = ['col1','col2','col3','col4']



def load_template(tmplt_name):
    tmplt_loader = jinja2.FileSystemLoader(searchpath='../templates')
    tmplt_env = jinja2.Environment(loader=tmplt_loader)
    tmplt = tmplt_env.get_template(tmplt_name)

    return tmplt  # Return the select.tmplt template object


def main():
    template = load_template('select_from_table.tmplt')
    table_name = "test_table"
    out_sql = template.render(col_list=col_list,
                              table_name=table_name)  # Finally, render the SQL output

    print(out_sql)


if __name__ == "__main__":
    # for i in range(len(col_list)):
    #     print(col_list[i])
    main()