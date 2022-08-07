import sqlparse


def parse_sql(script_location):
    with open(script_location) as f:
        source_sql = f.read()

    return source_sql

def get_from_table_name(script_location):
    source_sql = parse_sql(script_location)
    statements = sqlparse.parse(source_sql)[0]
    st_tokens = statements.tokens
    from_found = False
    for token in st_tokens:
        if isinstance(token,sqlparse.sql.IdentifierList):
            print (token.get_identifiers())
            for identifier in token.get_identifiers():
                print(identifier)
        if str(token).upper() == 'FROM':
            from_found = True
        elif from_found and token.ttype is None:
            print(token)



def get_column_identifier_from_select(script_location):
    source_sql = parse_sql(script_location)
    statements = sqlparse.parse(source_sql)[0]
    st_tokens = statements.tokens
    column_identifier_object = []
    select_found = False

    for token in st_tokens:
        #print(token.get_identifiers())
        if isinstance(token,sqlparse.sql.IdentifierList):
            print(token)
        if isinstance(token, sqlparse.sql.Comment):
            # Do nothing
            continue
        if str(token).upper() == 'SELECT':
            select_found = True
        elif select_found and token.ttype is None:
            for identifier in token.get_identifiers():
                column_identifier_object.append(identifier)
            break
    print(column_identifier_object)
    return column_identifier_object


def get_columns_in_select(script_location):
    column_identifier_object = get_column_identifier_from_select(script_location)
    columns_in_select = []
    alias = []
    column_pos = []
    for column_identifier in column_identifier_object:
        columns_in_select.append(column_identifier.get_real_name())
        alias.append(column_identifier.get_name())

    print(alias)
    return columns_in_select


if __name__ == "__main__":
    get_from_table_name('../sql/teradata_insert_as_sql.sql')
    #columns = get_columns_in_select('../sql/teradata_insert_as_sql.sql')
    #print(columns)
