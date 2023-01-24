from flask import Blueprint,url_for,request,jsonify,g
from flask_admin import Admin
from .UserAdmin import UserAdmin
from .DomainAdmin import DomainAdmin
from .ConfigAdmin import ConfigAdmin
from hiddifypanel.models import  StrConfig,ConfigEnum
# from .resources import ProductItemResource, ProductResource
from hiddifypanel.panel.database import db
from hiddifypanel.models import User,Domain,BoolConfig,StrConfig
from .dashboard import Dashboard
from .actions import Actions
from flask_admin.menu import MenuLink
from . import actions 
import uuid
from flask_adminlte3 import AdminLTE3
# bp = Blueprint("admin", __name__, url_prefix=f"/<proxy_path>/<user_secret>/",template_folder="templates")



def init_app(app):
    # admin_secret=StrConfig.query.filter(StrConfig.key==ConfigEnum.admin_secret).first()
    # 
    # return
    # admin = Admin(endpoint="admin",index_view=Dashboard(),base_template='lte-master.html',static_url_path="/static/")    
    AdminLTE3(app,)
    admin = Admin(endpoint="admin",index_view=Dashboard(url=f"/admin/"),url=f"/<proxy_path>/<user_secret>/admin/",
                base_template='lte-master.html')    

    admin.template_mode = app.config.FLASK_ADMIN_TEMPLATE_MODE
    # bp.add_url_rule("/actions/reverselog/<logfile>", view_func=actions.reverselog)
    # bp.add_url_rule("/actions/apply_configs", view_func=actions.apply_configs)
    # bp.add_url_rule("/actions/change", view_func=actions.change)
    # bp.add_url_rule("/actions/reinstall", view_func=actions.reinstall)
    # bp.add_url_rule("/actions/status", view_func=actions.status)
    # bp.add_url_rule("/actions/update", view_func=actions.update)
    # bp.add_url_rule("/actions/config", view_func=actions.config)

    
    admin.init_app(app)
    
    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(DomainAdmin(Domain, db.session))
    admin.add_view(ConfigAdmin(BoolConfig, db.session))
    admin.add_view(ConfigAdmin(StrConfig, db.session))
    # admin.add_view(Actions(name="Dashboard",endpoint="home",url="/<proxy_path>/<user_secret>/admin/",))
    admin.add_view(Actions(name="Actions",endpoint="actions",))
    
    # admin.add_link(MenuLink(name='Apply Changes', category='', url=f"/{g.proxy_path}/{g.user_secret}/actions/apply_configs"))
    # admin.
    # admin.init_app(bp)
    # app.register_blueprint(bp)
    print(app.url_map)    
    
    