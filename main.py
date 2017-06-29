from typing import List

from config import Config
from measures import Measures
from project_info import ProjectInfo
import psycopg2
import db_helpers as db
import project_output




def main():

    conn = None
    try:
        conn_params = Config.get_postgresql_conn_parameters()
        conn = psycopg2.connect(**conn_params)

        project_info = ProjectInfo(1)
        db.fill_basic_project_info(conn, project_info)
        print(project_info)
        project_output.print_java_info(conn, project_info)
        project_output.print_cpp_info(conn, project_info)
        project_output.print_cs_info(conn, project_info)



    finally:
        if conn is not None:
            conn.close()
        print("connection_closed")





    exit(0)


if __name__ == "__main__":
    main()
