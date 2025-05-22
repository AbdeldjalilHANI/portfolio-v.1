from app import create_app, db
from app.models import Project, Message

def initialize_database():
    # Create the Flask application
    app = create_app()
    
    # Establish the application context
    with app.app_context():
        # Create all database tables
        print("Creating database tables...")
        db.create_all()
        
        # Check if projects already exist to avoid duplicates
        if not Project.query.first():
            # Add sample projects
            projects = [
                Project(
                    title="E-commerce Website",
                    description="Built with Flask and Stripe integration for payments.",
                    image_url="https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a",
                    project_url="#"
                ),
                Project(
                    title="Task Manager API",
                    description="RESTful API with JWT authentication for task management.",
                    image_url="https://images.unsplash.com/photo-1586281380117-5a60ae2050cc",
                    project_url="#"
                ),
                Project(
                    title="Portfolio Website",
                    description="A responsive portfolio built with Flask and Bootstrap.",
                    image_url="https://images.unsplash.com/photo-1498050108023-c5249f4df085",
                    project_url="#"
                )
            ]
            
            # Add projects to the database session
            for project in projects:
                db.session.add(project)
            
            # Commit the changes
            db.session.commit()
            print("✅ Added 3 sample projects!")
        else:
            print("⚠️ Database already contains projects. Skipping seeding.")
        
        print("Database initialization complete!")

if __name__ == "__main__":
    initialize_database()