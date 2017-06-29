from measures import Measures
import db_helpers as db


def print_java_info(conn):
    print("Overall Java:")
    print("\tCyclomatic complexity per method:")
    print("\t" + str(Measures.from_data(db.get_all_functions_ccn(conn, "Java"))))

    print("\tCode lines per method:")
    print("\t" + str(Measures.from_data(db.get_all_functions_code_lines(conn, "Java"))))

    print("\tComment lines per method:")
    print("\t" + str(Measures.from_data(db.get_all_functions_comment_lines(conn, "Java"))))

    print("\tCode lines per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_code_lines(conn, "Java"))))

    print("\tComment lines per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_comment_lines(conn, "Java"))))

    print("\tMethods per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_n_methods(conn, "Java"))))
    print()


def print_cpp_info(conn):
    print("Overall C++:")
    print("\tCyclomatic complexity per function:")
    print("\t" + str(Measures.from_data(db.get_all_functions_ccn(conn, "C++")
                                        + db.get_all_functions_ccn(conn, "C/C++ Header"))))

    print("\tCode lines per function:")
    print("\t" + str(Measures.from_data(db.get_all_functions_code_lines(conn, "C++")
                                        + db.get_all_functions_code_lines(conn, "C/C++ Header"))))

    print("\tComment lines per function:")
    print("\t" + str(Measures.from_data(db.get_all_functions_comment_lines(conn, "C++")
                                        + db.get_all_functions_comment_lines(conn, "C/C++ Header"))))

    print("\tCode lines per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_code_lines(conn, "C++")
                                        + db.get_all_classes_code_lines(conn, "C/C++ Header"))))

    print("\tComment lines per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_comment_lines(conn, "C++")
                                        + db.get_all_classes_comment_lines(conn, "C/C++ Header"))))

    print("\tMethods per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_n_methods(conn, "C++")
                                        + db.get_all_classes_n_methods(conn, "C/C++ Header"))))
    print()


def print_cs_info(conn):
    print("Overall C#:")
    print("\tCyclomatic complexity per method:")
    print("\t" + str(Measures.from_data(db.get_all_functions_ccn(conn, "C#"))))

    print("\tCode lines per method:")
    print("\t" + str(Measures.from_data(db.get_all_functions_code_lines(conn, "C#"))))

    print("\tComment lines per method:")
    print("\t" + str(Measures.from_data(db.get_all_functions_comment_lines(conn, "C#"))))

    print("\tCode lines per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_code_lines(conn, "C#"))))

    print("\tComment lines per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_comment_lines(conn, "C#"))))

    print("\tMethods per class:")
    print("\t" + str(Measures.from_data(db.get_all_classes_n_methods(conn, "C#"))))
    print()
