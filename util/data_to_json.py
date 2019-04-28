
def row2dict(row):
    """Convert SQL row to text"""
    return {c.name: str(getattr(row, c.name)) for c in row.__table__.columns}


