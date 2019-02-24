from flask import Blueprint
from flask_restplus import Api

from .main.controller.auth_controller import api as auth_ns
from .main.controller.report_controller import api as report_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__, url_prefix='/api/v1.0')

api = Api(blueprint,
          title='TRACE-API',
          version='1.0',
          description='a service to replace MyTrace'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(report_ns, path='/')


@api.errorhandler(BaseException)
def base_exception_handler(error):
    return {'message': f'An unknown error has occurred. Error: {str(error)}'}, getattr(error, 'code', 500)
