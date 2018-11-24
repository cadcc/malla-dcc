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
            for semester in iter(r.data.get('semestres')):
                self.render_semester(semester, doc)
        return doc.getvalue()

    def render_semester(self, semester, doc):
        with doc.tag('td', klass='rotate'):
            doc.text('Semestre ' + semester.get('numero'))
        for ramo in iter(semester['ramos']):
            self.render_ramo(ramo, doc)

    def render_ramo(self, ramo, doc):
        pass


if __name__ == '__main__':
    r = Renderer('../malla.json')
    r.render_program()