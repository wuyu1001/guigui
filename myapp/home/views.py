from flask import render_template, flash, abort
from flask_login import login_required, current_user

from . import home
from .forms import CurrentWeatherForm

from .apixu.client import ApixuClient, ApixuException
api_key = 'dfee37deb4264b578a1132834172608'
client = ApixuClient(api_key)



@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard', methods=['GET', 'POST'])
@login_required # users must be logged in to access it
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    form = CurrentWeatherForm()
    while True:
        if form.validate_on_submit():
            q = form.city.data
            try:
                current = client.getCurrentWeather(q)
                localtime = current['location']['localtime']
                country = current['location']['country']
                region = current['location']['region']
                name = current['location']['name']
                temperature = current['current']['temp_c']
                text = current['current']['condition']['text']
                icon = 'http:' + str(current['current']['condition']['icon'])

                return render_template('home/dashboard.html', form=form, 
                                   localtime = localtime,
                                   country = country,
                                   region = region,
                                   name = name,
                                   temperature = temperature,
                                   text = text,
                                   icon = icon,
                                  )
            except:
                flash('您输入有误，请重新输入') # 有待解决的问题？
                

        return render_template('home/dashboard.html', form=form, title="Dashboard")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")
