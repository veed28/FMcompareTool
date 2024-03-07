import json, operator
import psycopg2
from striprtf.striprtf import rtf_to_text
from roles import Role
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, URL
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import csv, os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)


class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI",'sqlite:///users.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000), unique=True)


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


class UploadForm(FlaskForm):
    file = FileField()


@app.route("/", methods=['GET', 'POST'])
def home():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save(f'/opt/render/project/src/src/uploads/{current_user.name}/' + filename)
        return redirect(url_for('home'))

    return render_template("index.html", form=form, logged_in=current_user.is_authenticated)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))

        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))


        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=request.form.get('email'),
            password=hash_and_salted_password,
            name=request.form.get('name')
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        path = '/opt/render/project/src/src/uploads/' + new_user.name
        os.mkdir(path)
        return redirect(url_for("home"))

    return render_template("register.html", logged_in=current_user.is_authenticated)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))

    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/role/<selected_role>", methods=['GET', 'POST'])
def role(selected_role):
    first_dict = {}
    final_list = []
    user_name = current_user.name
    file = open(f"/opt/render/project/src/src/uploads/{user_name}/Untitled.rtf", encoding="utf-8")
    content = file.read()
    text = rtf_to_text(content)
    text2 = text.replace(" ", "")
    text = text2.replace("-", "")
    text2 = text.replace("||", "|")
    text = text2.replace("||", "|")
    text2 = text.replace("||", "|")
    final_list = text2.split("|")
    del final_list[0:38]
    del final_list[-1]
    player_count = int(len(final_list) / 37)
    file.close()
    for player in range(player_count):
        role = Role(player, final_list)
        if selected_role == 'inverted_wing_back_s': #IWB-S
            score = role.inverted_wing_back_s()
            display_role = "Inverted Wing Back - Support"
        elif selected_role == 'inverted_wing_back_d': #IWB-D
            score = role.inverted_wing_back_d()
            display_role = "Inverted Wing Back - Defend"
        elif selected_role == 'inverted_wing_back_a': #IWB-A
            score = role.inverted_wing_back_a()
            display_role = "Inverted Wing Back - Attack"
        elif selected_role == 'inverted_full_back': #IFB
            score = role.inverted_full_back()
            display_role = "Inverted Full Back"
        elif selected_role == 'complete_wing_back_a': #CWB-A
            score = role.complete_wing_back_a()
            display_role = "Complete Wing Back - Attack"
        elif selected_role == 'complete_wing_back_s': #CWB-S
            score = role.complete_wing_back_s()
            display_role = "Complete Wing Back - Support"
        elif selected_role == 'wing_back_s': #WB-S
            score = role.wing_back_s()
            display_role = "Wing Back - Support"
        elif selected_role == 'wing_back_a': #WB-A
            score = role.wing_back_a()
            display_role = "Wing Back - Attack"
        elif selected_role == 'wing_back_d': #WB-D
            score = role.wing_back_d()
            display_role = "Wing Back - Defend"
        elif selected_role == 'central_defender_d': #CD-D
            score = role.central_defender_d()
            display_role = "Central Defender - Defend"
        elif selected_role == 'central_defender_s': #CD-S
            score = role.central_defender_s()
            display_role = "Central Defender - Stopper"
        elif selected_role == 'central_defender_c': #CD-C
            score = role.central_defender_c()
            display_role = "Central Defender - Cover"
        elif selected_role == 'ball_playing_defender_d': #BPD-D
            score = role.ball_playing_defender_d()
            display_role = "Ball Playing Defender - Defend"
        elif selected_role == 'ball_playing_defender_s': #BPD-S
            score = role.ball_playing_defender_s()
            display_role = "Ball Playing Defender - Stopper"
        elif selected_role == 'ball_playing_defender_c': #BPD-C
            score = role.ball_playing_defender_c()
            display_role = "Ball Playing Defender - Cover"
        elif selected_role == 'wide_center_back_d': #WCB-D
            score = role.wide_center_back_d()
            display_role = "Wide Center Back - Defend"
        elif selected_role == 'wide_center_back_s': #WCB-S
            score = role.wide_center_back_s()
            display_role = "Wide Center Back - Support"
        elif selected_role == 'wide_center_back_a': #WCB-A
            score = role.wide_center_back_a()
            display_role = "Wide Center Back - Attack"
        elif selected_role == 'libero_d': #L-D
            score = role.libero_d()
            display_role = "Libero - Defend"
        elif selected_role == 'libero_s': #L-S
            score = role.libero_s()
            display_role = "Libero - Support"
        elif selected_role == 'ball_winning_midfielder_d': #BWM-D
            score = role.ball_winning_midfielder_d()
            display_role = "Ball Winning Midfielder - Defend"
        elif selected_role == 'ball_winning_midfielder_s': #BWM-S
            score = role.ball_winning_midfielder_s()
            display_role = "Ball Winning Midfielder - Support"
        elif selected_role == 'defensive_midfielder_d': #DM-D
            score = role.defensive_midfielder_d()
            display_role = "Defensive Midfielder - Defend"
        elif selected_role == 'defensive_midfielder_s': #DM-S
            score = role.defensive_midfielder_s()
            display_role = "Defensive Midfielder - Support"
        elif selected_role == 'segundo_volante_s': #SV-S
            score = role.segundo_volante_s()
            display_role = "Segundo Volante - Support"
        elif selected_role == 'segundo_volante_a': #SV-A
            score = role.segundo_volante_a()
            display_role = "Segundo Volante - Attack"
        elif selected_role == 'half_back': #HB
            score = role.half_back()
            display_role = "Half Back"
        elif selected_role == 'anchor': #Anc
            score = role.anchor()
            display_role = "Anchor"
        elif selected_role == 'deep_lying_playmaker_d': #DLP-D
            score = role.deep_lying_playmaker_d()
            display_role = "Deep Lying Playmaker - Defend"
        elif selected_role == 'deep_lying_playmaker_s': #DLP-S
            score = role.deep_lying_playmaker_s()
            display_role = "Deep Lying Playmaker - Support"
        elif selected_role == 'roaming_playmaker': #RPM
            score = role.roaming_playmaker()
            display_role = "Roaming Playmaker"
        elif selected_role == 'regista': #Reg
            score = role.regista()
            display_role = "Regista"
        elif selected_role == 'mezzala_s': #Mez-S
            score = role.mezzala_s()
            display_role = "Mezzala - Support"
        elif selected_role == 'mezzala_a': #Mez-A
            score = role.mezzala_a()
            display_role = "Mezzala - Attack"
        elif selected_role == 'central_midfielder_d': #CM-D
            score = role.central_midfielder_d()
            display_role = "Central Midfielder - Defend"
        elif selected_role == 'central_midfielder_s': #CM-S
            score = role.central_midfielder_s()
            display_role = "Central Midfielder - Support"
        elif selected_role == 'central_midfielder_a': #CM-A
            score = role.central_midfielder_a()
            display_role = "Central Midfielder - Attack"
        elif selected_role == 'box_to_box_midfielder': #BBM
            score = role.box_to_box_midfielder()
            display_role = "Box to Box Midfielder"
        elif selected_role == 'carrilero': #Car
            score = role.carrilero()
            display_role = "Carrilero"
        elif selected_role == 'winger_s': #W-S
            score = role.winger_s()
            display_role = "Winger - Support"
        elif selected_role == 'winger_a': #W_A
            score = role.winger_a()
            display_role = "Winger - Attack"
        elif selected_role == 'inverted_winger_s': #IW-S
            score = role.inverted_winger_s()
            display_role = "Inverted Winger - Support"
        elif selected_role == 'inverted_winger_a': #IW-A
            score = role.inverted_winger_a()
            display_role = "Inverted Winger - Attack"
        elif selected_role == 'inside_forward_s': #IF-S
            score = role.inside_forward_s()
            display_role = "Inside Forward - Support"
        elif selected_role == 'inside_forward_a': #IF-A
            score = role.inside_forward_a()
            display_role = "Inside Forward - Attack"
        elif selected_role == 'wide_playmaker_s': #WP-S
            score = role.wide_playmaker_s()
            display_role = "Wide Playmaker - Support"
        elif selected_role == 'wide_playmaker_a': #WP-A
            score = role.wide_playmaker_a()
            display_role = "Wide Playmaker - Attack"
        elif selected_role == 'defensive_winger_d': #DW-D
            score = role.defensive_winger_d()
            display_role = "Defensive Winger - Defend"
        elif selected_role == 'defensive_winger_s': #DW-S
            score = role.defensive_winger_s()
            display_role = "Defensive Winger - Support"
        elif selected_role == 'advanced_playmaker_s': #AP-S
            score = role.advanced_playmaker_s()
            display_role = "Advanced Playmaker - Support"
        elif selected_role == 'advanced_playmaker_a': #AP-A
            score = role.advanced_playmaker_a()
            display_role = "Advanced Playmaker - Attack"
        elif selected_role == 'attacking_midfielder_s':  # AM-S
            score = role.attacking_midfielder_s()
            display_role = "Attacking Midfielder - Support"
        elif selected_role == 'attacking_midfielder_a':  # AM-A
            score = role.attacking_midfielder_a()
            display_role = "Attacking Midfielder - Attack"
        elif selected_role == 'shadow_striker':  # SS
            score = role.shadow_striker()
            display_role = "Shadow Striker"
        elif selected_role == 'enganche':  # ENG
            score = role.enganche()
            display_role = "Enganche"
        elif selected_role == 'trequartista':  # TREQ
            score = role.trequartista()
            display_role = "Trequartista. FUCK YEAH!"
        first_dict[role.player] = "{:.2f}".format(score)
    final_list = []
    dict_sorted = dict(sorted(first_dict.items(), key=operator.itemgetter(1), reverse=True))
    return render_template("roles.html", role=display_role, dict=dict_sorted)

# with open(f"uploads/{current_user.name}/Untitled.rtf", encoding="utf-8") as file:
#     content = file.read()
#     text = rtf_to_text(content)
#     text2 = text.replace(" ", "")
#     text = text2.replace("-", "")
#     text2 = text.replace("||", "|")
#     text = text2.replace("||", "|")
#     text2 = text.replace("||","|")
#     list = text2.split("|")
#     del list[0:38]
#     del list[-1]
#     player_count = int(len(list) / 37)



# print(list)
# print(list[37]) <-- player names are at 0,37,74 etc.

# find the technique value for every player
# for player in range(player_count):
#     role = Role(player, list)
#     score = role.shadow_striker()
#     first_dict[role.player] = "{:.2f}".format(score)

# dict_sorted = dict(sorted(first_dict.items(), key=operator.itemgetter(1), reverse=True))
# print(next(iter(dict_sorted)))
# print(json.dumps(dict_sorted, indent=4))


if __name__ == '__main__':
    app.run(debug=True)