from measures import Measures
from project_info import ProjectInfo
import db_helpers as db


def print_java_info(conn, project_info: ProjectInfo):
    print("\tJava (files = {0}):".format(db.get_number_of_files(conn, "Java", project_info)))
    print("\t\tCyclomatic complexity per method:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_ccn(conn, "Java", project_info))))

    print("\t\tCode lines per method:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_code_lines(conn, "Java", project_info))))

    print("\t\tComment lines per method:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_comment_lines(conn, "Java", project_info))))

    print("\t\tCode lines per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_code_lines(conn, "Java", project_info))))

    print("\t\tComment lines per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_comment_lines(conn, "Java", project_info))))

    print("\t\tMethods per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_n_methods(conn, "Java", project_info))))
    print()


def print_cpp_info(conn, project_info: ProjectInfo):
    print("\tC++ (files = {0}):".format(db.get_number_of_files(conn, "C++", project_info)
                                        + db.get_number_of_files(conn, "C/C++ Header", project_info)))
    print("\t\tCyclomatic complexity per function:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_ccn(conn, "C++", project_info)
                                          + db.get_all_functions_ccn(conn, "C/C++ Header", project_info))))

    print("\t\tCode lines per function:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_code_lines(conn, "C++", project_info)
                                          + db.get_all_functions_code_lines(conn, "C/C++ Header", project_info))))

    print("\t\tComment lines per function:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_comment_lines(conn, "C++", project_info)
                                          + db.get_all_functions_comment_lines(conn, "C/C++ Header", project_info))))

    print("\t\tCode lines per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_code_lines(conn, "C++", project_info)
                                          + db.get_all_classes_code_lines(conn, "C/C++ Header", project_info))))

    print("\t\tComment lines per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_comment_lines(conn, "C++", project_info)
                                          + db.get_all_classes_comment_lines(conn, "C/C++ Header", project_info))))

    print("\t\tMethods per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_n_methods(conn, "C++", project_info)
                                          + db.get_all_classes_n_methods(conn, "C/C++ Header", project_info))))
    print()


def print_cs_info(conn, project_info: ProjectInfo):
    print("\tC# (files = {0}):".format(db.get_number_of_files(conn, "C#", project_info)))
    print("\t\tCyclomatic complexity per method:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_ccn(conn, "C#", project_info))))

    print("\t\tCode lines per method:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_code_lines(conn, "C#", project_info))))

    print("\t\tComment lines per method:")
    print("\t\t" + str(Measures.from_data(db.get_all_functions_comment_lines(conn, "C#", project_info))))

    print("\t\tCode lines per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_code_lines(conn, "C#", project_info))))

    print("\t\tComment lines per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_comment_lines(conn, "C#", project_info))))

    print("\t\tMethods per class:")
    print("\t\t" + str(Measures.from_data(db.get_all_classes_n_methods(conn, "C#", project_info))))
    print()
