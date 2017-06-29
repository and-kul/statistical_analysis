from typing import List

from project_info import ProjectInfo


def fill_basic_project_info(conn, project_info: ProjectInfo):
    select_sql = """SELECT url, name FROM projects WHERE id = %s"""
    cur = conn.cursor()
    cur.execute(select_sql, (project_info.id,))
    result = cur.fetchone()
    project_info.url = result[0]
    project_info.name = result[1]
    cur.close()


def get_all_functions_ccn(conn, language_name: str, project_info: ProjectInfo = None) -> List[int]:
    select_sql = """SELECT cyclomatic_complexity FROM functions
WHERE file_id in (SELECT id FROM files WHERE language_name = %s AND project_id = %s)"""
    select_sql_for_language = """SELECT cyclomatic_complexity FROM functions
WHERE file_id in (SELECT id FROM files WHERE language_name = %s)"""
    cur = conn.cursor()
    if project_info is not None:
        cur.execute(select_sql, (language_name, project_info.id))
    else:
        cur.execute(select_sql_for_language, (language_name,))
    result = cur.fetchall()
    cur.close()
    return list(map(lambda t: t[0], result))


def get_all_functions_code_lines(conn, language_name: str, project_info: ProjectInfo = None) -> List[int]:
    select_sql = """SELECT code_lines FROM functions
WHERE file_id in (SELECT id FROM files WHERE language_name = %s AND project_id = %s)"""
    select_sql_for_language = """SELECT code_lines FROM functions
WHERE file_id in (SELECT id FROM files WHERE language_name = %s)"""
    cur = conn.cursor()
    if project_info is not None:
        cur.execute(select_sql, (language_name, project_info.id))
    else:
        cur.execute(select_sql_for_language, (language_name,))
    result = cur.fetchall()
    cur.close()
    return list(map(lambda t: t[0], result))


def get_all_functions_comment_lines(conn, language_name: str, project_info: ProjectInfo = None) -> List[int]:
    select_sql = """SELECT comment_lines FROM functions
WHERE file_id in (SELECT id FROM files WHERE language_name = %s AND project_id = %s)"""
    select_sql_for_language = """SELECT comment_lines FROM functions
    WHERE file_id in (SELECT id FROM files WHERE language_name = %s)"""
    cur = conn.cursor()
    if project_info is not None:
        cur.execute(select_sql, (language_name, project_info.id))
    else:
        cur.execute(select_sql_for_language, (language_name,))
    result = cur.fetchall()
    cur.close()
    return list(map(lambda t: t[0], result))


def get_all_classes_code_lines(conn, language_name: str, project_info: ProjectInfo = None) -> List[int]:
    select_sql = """SELECT code_lines FROM regions
    WHERE file_id in (SELECT id FROM files WHERE language_name = %s AND project_id = %s)
    AND (region_type = 'Class' OR region_type = 'Struct')"""
    select_sql_for_language = """SELECT code_lines FROM regions
        WHERE file_id in (SELECT id FROM files WHERE language_name = %s)
        AND (region_type = 'Class' OR region_type = 'Struct')"""
    cur = conn.cursor()
    if project_info is not None:
        cur.execute(select_sql, (language_name, project_info.id))
    else:
        cur.execute(select_sql_for_language, (language_name,))
    result = cur.fetchall()
    cur.close()
    return list(map(lambda t: t[0], result))


def get_all_classes_comment_lines(conn, language_name: str, project_info: ProjectInfo = None) -> List[int]:
    select_sql = """SELECT comment_lines FROM regions
    WHERE file_id in (SELECT id FROM files WHERE language_name = %s AND project_id = %s)
    AND (region_type = 'Class' OR region_type = 'Struct')"""
    select_sql_for_language = """SELECT comment_lines FROM regions
        WHERE file_id in (SELECT id FROM files WHERE language_name = %s)
        AND (region_type = 'Class' OR region_type = 'Struct')"""
    cur = conn.cursor()
    if project_info is not None:
        cur.execute(select_sql, (language_name, project_info.id))
    else:
        cur.execute(select_sql_for_language, (language_name,))
    result = cur.fetchall()
    cur.close()
    return list(map(lambda t: t[0], result))


def get_all_classes_n_methods(conn, language_name: str, project_info: ProjectInfo = None) -> List[int]:
    select_sql = """SELECT n_functions FROM regions
    WHERE file_id in (SELECT id FROM files WHERE language_name = %s AND project_id = %s)
    AND (region_type = 'Class' OR region_type = 'Struct')"""
    select_sql_for_language = """SELECT n_functions FROM regions
        WHERE file_id in (SELECT id FROM files WHERE language_name = %s)
        AND (region_type = 'Class' OR region_type = 'Struct')"""
    cur = conn.cursor()
    if project_info is not None:
        cur.execute(select_sql, (language_name, project_info.id))
    else:
        cur.execute(select_sql_for_language, (language_name,))
    result = cur.fetchall()
    cur.close()
    return list(map(lambda t: t[0], result))

