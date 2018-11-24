import json
from yattag import Doc


class Renderer:

    def __init__(self, file):
        json_file = open(file, encoding='utf8')
        contents = json_file.read()
        self.data = json.loads(contents)

    def render_program(self):
        doc = Doc()
        with doc.tag('tr'):
            for semester in iter(r.data['semestres']):
                self.render_semester(semester)

    def render_semester(self, semester):
        pass


if __name__ == '__main__':
    r = Renderer('../malla.json')
    r.render_program()