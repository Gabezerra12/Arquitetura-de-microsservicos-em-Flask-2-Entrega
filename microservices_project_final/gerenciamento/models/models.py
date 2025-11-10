from database import db
class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(120))
    turmas = db.relationship('Turma', backref='professor', lazy=True)
    def to_dict(self):
        return {"id":self.id, "nome":self.nome, "idade":self.idade, "materia":self.materia}

class Turma(db.Model):
    __tablename__ = 'turma'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(120))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=True)
    ativo = db.Column(db.Boolean, default=True)
    alunos = db.relationship('Aluno', backref='turma', lazy=True)
    def to_dict(self):
        return {"id":self.id, "descricao":self.descricao, "professor_id":self.professor_id, "ativo":self.ativo}

class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=True)
    def to_dict(self):
        return {"id":self.id, "nome":self.nome, "idade":self.idade, "turma_id":self.turma_id}
