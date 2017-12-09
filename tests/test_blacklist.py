from fence import keys
from fence.blacklist import (
    blacklist_token,
    is_blacklisted,
    is_token_blacklisted,
)


def test_jti_not_blacklisted(app, jti):
    """
    Test checking a ``jti`` which has not been blacklisted.
    """
    assert not is_blacklisted(jti)


def test_blacklist(app, jti, iat_and_exp):
    """
    Test blacklisting a ``jti`` directly.
    """
    _, exp = iat_and_exp
    blacklist_token(jti, exp)
    assert is_blacklisted(jti)


def test_normal_token_not_blacklisted(app, encoded_jwt_refresh_token):
    """
    Test that a (refresh) token which was not blacklisted returns not
    blacklisted.
    """
    print keys.default_public_key()
    assert not is_token_blacklisted(encoded_jwt_refresh_token)


def test_blacklisted_token(client, encoded_jwt_refresh_token):
    """
    Revoke a JWT and test that it registers as blacklisted.
    """
    data = {'token': encoded_jwt_refresh_token}
    response = client.post('/oauth2/revoke', data=data)
    assert response.status_code == 204, response.data
    assert is_token_blacklisted(encoded_jwt_refresh_token)


def test_cannot_revoke_access_token(client, encoded_jwt):
    """
    Test that attempting to revoke an access token fails and returns 400.
    """
    data = {'token': encoded_jwt}
    response = client.post('/oauth2/revoke', data=data)
    assert response.status_code == 400, response.data
