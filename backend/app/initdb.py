
from sqlalchemy.exc import SQLAlchemyError

from backend.app.db.models import User, Base
from backend.app.db.database import engine, SessionLocal


def create_tables():
    print("Creating tables...")

    Base.metadata.create_all(bind=engine)

    print("Tables created successfully!")


def seed_user():
    print("Checking test user...")

    db = SessionLocal()

    try:
        user = db.query(User).filter(
            User.username == "test"
        ).first()

        if not user:
            new_user = User(
                username="test",
                password="test123",
                role="admin"
            )

            db.add(new_user)
            db.commit()

            print("Test user created successfully!")

        else:
            print("Test user already exists.")

    except SQLAlchemyError as e:
        db.rollback()
        print("Database error:", str(e))

    finally:
        db.close()


if __name__ == "__main__":
    create_tables()
    seed_user()
