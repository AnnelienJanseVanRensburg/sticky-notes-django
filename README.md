# Sticky Notes Application

A full-featured sticky notes web application built with Django, featuring complete CRUD functionality, comprehensive test coverage, and a clean, responsive user interface.

![Django](https://img.shields.io/badge/Django-5.0+-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tests](https://img.shields.io/badge/Tests-27%20passing-brightgreen.svg)

## Features

- **Create Notes** - Add new sticky notes with titles and content
- **View Notes** - Browse all notes in an organized card layout
- **Update Notes** - Edit existing notes with pre-filled forms
- **Delete Notes** - Remove notes with confirmation prompts
- **Automatic Timestamps** - Track creation and modification times
- **Responsive Design** - Beautiful UI built with Bootstrap 5
- **Empty State Handling** - Friendly messages for new users
- **Comprehensive Testing** - 27 unit tests covering all functionality

## Project Overview

This project was developed as part of a Software Engineering bootcamp to demonstrate:
- Django MVT (Model-View-Template) architecture
- RESTful URL design
- Form validation and error handling
- Unit testing best practices
- Clean code principles
- Professional documentation

## Requirements

- Python 3.8 or higher
- Django 5.0 or higher
- A modern web browser

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sticky-notes-app.git
cd sticky-notes-app
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account for accessing the Django admin panel.

### 6. Run Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

Open your browser and navigate to:
- **Application**: http://127.0.0.1:8000/notes/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🧪 Running Tests

The project includes comprehensive unit tests covering models, views, forms, and URL routing.

```bash
# Run all tests
python manage.py test notes

# Run with verbose output
python manage.py test notes --verbosity=2

# Run a specific test class
python manage.py test notes.tests.NoteModelTest

# Run a specific test method
python manage.py test notes.tests.NoteModelTest.test_note_creation
```

### Test Coverage

- **Model Tests**: Note creation, string representation, timestamps, ordering
- **Form Tests**: Valid data acceptance, invalid data rejection, field validation
- **View Tests**: All CRUD operations, template rendering, status codes
- **Integration Tests**: Complete user workflows from creation to deletion

All 27 tests pass successfully, ensuring application reliability.

## 📁 Project Structure

```
Sticky_Notes_App/
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
├── db.sqlite3                     # SQLite database (auto-generated)
├── README.md                      # This file
│
├── sticky_notes/                  # Main project configuration
│   ├── __init__.py
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL routing
│   ├── wsgi.py                    # WSGI deployment config
│   └── asgi.py                    # ASGI deployment config
│
└── notes/                         # Notes application
    ├── __init__.py
    ├── models.py                  # Note model definition
    ├── views.py                   # View functions (CRUD logic)
    ├── urls.py                    # App URL patterns
    ├── forms.py                   # NoteForm definition
    ├── admin.py                   # Admin panel configuration
    ├── apps.py                    # App configuration
    ├── tests.py                   # Unit tests (27 tests)
    │
    ├── migrations/                # Database migrations
    │   ├── __init__.py
    │   └── 0001_initial.py
    │
    ├── static/                    # Static files
    │   └── notes/
    │       └── custom.css         # Custom styling
    │
    └── templates/                 # HTML templates
        └── notes/
            ├── base.html          # Base template
            ├── note_list.html     # List view
            ├── note_detail.html   # Detail view
            ├── note_form.html     # Create/Edit form
            └── note_confirm_delete.html  # Delete confirmation
```

## 🎨 Architecture

### Model-View-Template (MVT)

**Model (`models.py`)**
- Defines the Note data structure
- Fields: title, content, created_at, updated_at
- Automatic timestamp management
- Ordered by newest first

**Views (`views.py`)**
- `note_list()` - Display all notes
- `note_detail()` - Show individual note
- `note_create()` - Create new note
- `note_update()` - Edit existing note
- `note_delete()` - Delete note with confirmation

**Templates (`templates/notes/`)**
- Bootstrap 5 for responsive design
- Consistent layout via base template
- User-friendly forms and messages
- Empty state handling

### URL Structure

| URL Pattern | View | Purpose |
|-------------|------|---------|
| `/notes/` | note_list | Display all notes |
| `/notes/<pk>/` | note_detail | View single note |
| `/notes/new/` | note_create | Create new note |
| `/notes/<pk>/edit/` | note_update | Edit note |
| `/notes/<pk>/delete/` | note_delete | Delete note |
| `/admin/` | Django Admin | Admin interface |

## 🛠️ Technologies Used

- **Backend Framework**: Django 5.0+
- **Database**: SQLite3 (development)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome 6
- **Testing**: Django TestCase
- **Version Control**: Git

## 📝 Design Documentation

This project includes comprehensive design documentation:

- **Use Case Diagram** - System actors and interactions
- **Sequence Diagrams** - All CRUD operation flows
- **Class Diagram** - Note model structure
- **MVC Architecture** - Separation of concerns
- **CRUD Matrix** - Operation documentation

All design documents are available in the project repository.

## 🎓 Key Learning Outcomes

Through building this application, the following concepts were mastered:

- Django project and app structure
- Model definition with automatic fields
- Form creation and validation
- View functions and request handling
- Template inheritance and rendering
- URL routing and reverse lookups
- Unit testing with TestCase
- CRUD operation implementation
- Bootstrap integration
- Code quality and best practices

## 🐛 Known Issues

None currently. All tests passing.

## 🔮 Future Enhancements

Potential features for future development:

- [ ] User authentication and authorization
- [ ] Note categories and tags
- [ ] Search functionality
- [ ] Color-coded notes
- [ ] Rich text editor
- [ ] Note sharing capabilities
- [ ] Export notes to PDF/TXT
- [ ] Archive functionality
- [ ] Pagination for large note collections
- [ ] REST API for mobile apps

## 🤝 Contributing

This is an educational project, but feedback and suggestions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project was created for educational purposes as part of a software engineering bootcamp.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- HyperionDev for the project specifications
- Django documentation and community
- Bootstrap team for the UI framework
- Font Awesome for icons

## 📞 Support

If you have any questions or run into issues:

1. Check the documentation in this README
2. Review the inline code comments
3. Examine the test file for usage examples
4. Open an issue on GitHub

---

**Built with ❤️ using Django**

*Last Updated: February 2026*
