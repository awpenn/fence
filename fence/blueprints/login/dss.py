import flask

from fence.models import IdentityProvider
from fence.config import config
from fence.blueprints.login.base import DefaultOAuth2Login, DefaultOAuth2Callback


class DSSLogin(DefaultOAuth2Login):
    def __init__(self):
        super(DSSLogin, self).__init__(
            idp_name=IdentityProvider.dss, client=flask.current_app.dss_client
        )


class DSSCallback(DefaultOAuth2Callback):
    def __init__(self):
        super(DSSCallback, self).__init__(
            idp_name=IdentityProvider.dss, client=flask.current_app.dss_client
        )
