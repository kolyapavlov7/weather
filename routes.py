from views import weather_view

def setup_routes(app):
    app.router.add_get('/weather', weather_view)
