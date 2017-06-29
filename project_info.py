from measures import Measures


class ProjectInfo:
    def __init__(self, id: int):
        self.id = id
        self.url = None
        self.name = None
        self.ccn_per_function: Measures = None
        self.code_lines_per_function: Measures = None
        self.comment_lines_per_function: Measures = None
        self.code_lines_per_class: Measures = None
        self.comment_lines_per_class: Measures = None
        self.functions_per_class: Measures = None

    def __str__(self):
        return 'Project "{0}" ({1}):'.format(self.name, self.url)
