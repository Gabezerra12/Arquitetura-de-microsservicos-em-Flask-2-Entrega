from database import db
class Reserva(db.Model):
    __tablename__ = 'reserva'
    id = db.Column(db.Integer, primary_key=True)
    num_sala = db.Column(db.String(50))
    lab = db.Column(db.Boolean, default=False)
    data = db.Column(db.String(50))
    turma_id = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {"id":self.id,"num_sala":self.num_sala,"lab":self.lab,"data":self.data,"turma_id":self.turma_id}
