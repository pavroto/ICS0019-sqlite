import sqlite3 as sq3
from os import getcwd
from os.path import join

DATABASE_NAME = "DINERS.db"

SCRIPT_DIRECTORY = join(getcwd(), "sql-scripts")
CREATE_TABLE_CANTEEN = "create-table-CANTEEN.sql"
CREATE_TABLE_PROVIDER = "create-table-PROVIDER.sql"


def create_database():
    f = open(DATABASE_NAME, "w")
    f.close()

    connection = sq3.connect(DATABASE_NAME)

    cur = connection.cursor()

    # Creating tables #
    for i in [CREATE_TABLE_PROVIDER, CREATE_TABLE_CANTEEN]:
        try:
            script = return_script(i)
            cur.execute(script)
        except FileNotFoundError as e:
            cur.close()
            connection.close()

            print(e)
            return

    connection.commit()

    cur.close()
    connection.close()


def return_script(name):
    try:
        script = open(join(SCRIPT_DIRECTORY, name), "r")
        return script.read()

    except FileNotFoundError as e:
        raise e


if __name__ == "__main__":
    create_database()
