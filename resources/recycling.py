class Recycling_Centers(db.Model):
    center_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(120), unique=True, nullable=False)
    contact_info = db.Column(db.String(120), unique=True, nullable=False)
    operating_hours = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"Recycling_Centers('{self.center_id}', '{self.location}')"

class Recycled_Materials(db.Model):
    material_id = db.Column(db.Integer, primary_key=True)
    material_name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    recycling_transactions = db.relationship('Recycling_Transactions', backref='material', lazy=True)
    
    def __repr__(self):
        return f"Recycled_Materials('{self.material_id}', '{self.material_name}')"

class Recycling_Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    material_id = db.Column(db.Integer, db.ForeignKey('recycled_materials.material_id'), nullable=False)
    quantity = db.Column(db.String(120), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    note = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"Recycling_Transactions('{self.transaction_id}', '{self.user_id}', '{self.transaction_date}')"
