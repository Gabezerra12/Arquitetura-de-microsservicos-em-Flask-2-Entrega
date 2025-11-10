from database import db
class Atividade(db.Model):
    __tablename__ = 'atividade'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    descricao = db.Column(db.String(500))
    peso_porcento = db.Column(db.Integer)
    data_entrega = db.Column(db.String(50))
    turma_id = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {"id":self.id,"titulo":self.titulo,"descricao":self.descricao,"peso_porcento":self.peso_porcento,"data_entrega":self.data_entrega,"turma_id":self.turma_id,"professor_id":self.professor_id}

class Nota(db.Model):
    __tablename__ = 'nota'
    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.Float)
    aluno_id = db.Column(db.Integer, nullable=False)
    atividade_id = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {"id":self.id,"nota":self.nota,"aluno_id":self.aluno_id,"atividade_id":self.atividade_id}
