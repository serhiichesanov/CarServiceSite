def get_last_entry(session, objclass):
    return session.query(objclass).order_by(objclass.id.desc()).first()
