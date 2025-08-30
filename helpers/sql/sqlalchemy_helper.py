from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base


# Base class for all models
Base = declarative_base()
DATABASE_URL = "sqlite:///data/smart-closet.db"
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))


def get_session():
    """Return a new database session."""
    return SessionLocal()


def init_db():
    """Create all tables (if not already created)."""
    Base.metadata.create_all(bind=engine)


def add_instance(instance):
    """Add a new instance (row) to the database."""
    session = get_session()
    try:
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance
    except Exception as error:
        session.rollback()
        raise error
    finally:
        session.close()


def get_all(model):
    """Get all rows from a table (model)."""
    session = get_session()
    try:
        return session.query(model).all()
    finally:
        session.close()


def get_unique(model):
    """Get all rows from a table (model)."""
    session = get_session()
    try:
        return session.query(model.name).distinct().all()
    finally:
        session.close()


def get_by_id(model, obj_id, id_field="id"):
    """Get a row by its ID."""
    session = get_session()
    try:
        return session.query(model).filter(getattr(model, id_field) == obj_id).first()
    finally:
        session.close()


def get_quantity_by_name(model, product_name):
    # Query for a specific product (e.g., by name or barcode)
    session = get_session()
    product = session.query(model.product_qty).filter(model.name == product_name).all()

    total = 0
    for elem in product:
        total += elem[0]
    if product:
        return total
    return None


def delete_instance(instance):
    """Delete a row from the database."""
    session = get_session()
    try:
        session.delete(instance)
        session.commit()
    except Exception as error:
        session.rollback()
        raise error
    finally:
        session.close()
