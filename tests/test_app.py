import app
def test_lambda_handler():
    response = app.lambda_handler({}, {})
    assert response["statusCode"] == 200
