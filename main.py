import language_output
from config import Config

from project_info import ProjectInfo
import psycopg2
import db_helpers as db
import project_output


def main():
    conn = None
    try:
        conn_params = Config.get_postgresql_conn_parameters()
        conn = psycopg2.connect(**conn_params)


        language_output.print_cpp_info(conn)
        language_output.print_java_info(conn)
        language_output.print_cs_info(conn)



    finally:
        if conn is not None:
            conn.close()
        print("connection_closed")

    exit(0)


if __name__ == "__main__":
    main()
