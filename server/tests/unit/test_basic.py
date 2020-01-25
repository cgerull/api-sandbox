
def test_SECRET(test_app):
    assert test_app.config['SECRET_KEY'] == 'Only_the_default_secret_key'

def test_SECRET_FILE(test_app):
    assert test_app.config['SECRET_FILE'] == '/run/secrets/my_secret_key'
    
# def test_SECRET_with_env(monkeypatch):
#     monkeypatch.setenv("SECRET_KEY", "MonkeySecret")
#     print("KEY: {}".format(os.getenv('SECRET_KEY')))
#     assert Config.get_secret_key() == 'MonkeySecret'