class BaseDistanceService:
    @app.route('/')
    def hello_world():
        return 'Distance Controller Module'