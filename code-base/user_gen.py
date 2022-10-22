from app.models import User
from app import db, create_app
from datetime import datetime
from werkzeug.security import generate_password_hash


with create_app().app_context():
    first_name = 'Lenny'
    last_name = "Ng'ang'a"
    phone1 = '0791485681'
    email = 'lennylen254@gmail.com'

    user = User(
        first_name=first_name,
        last_name=last_name,
        phone1=phone1,
        # phone2 = phone2,
        email=email,
        pword=generate_password_hash(phone1, method='sha256'),
        is_verified=1
    )

    db.session.add(user)
    db.session.commit()

    print(f'User Added: {first_name}')
