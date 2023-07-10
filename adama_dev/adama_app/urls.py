from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signin, name="login_page"),
    path('login', views.signin, name="login"),
    path('create_user', views.create_user, name="create_user"),
    path('logout', views.signout, name="logout"),
    path('noaccess', views.no_access, name="no_access"),
    path('del_noti/<str:data>', views.delete_notification, name="delete_notification"),
    path('del_all_noti', views.delete_all_notification, name="delete_all_notification"),
    path('home/', views.home, name="home"),
    path('home_ajax/', views.home_ajax, name="home_ajax"),
    path('batchcard/', views.batchcard, name="batchcard"),
    path('viewbatchcard/<str:batchcardno>', views.viewbatchcard, name="view_batchcard"),
    path('editbatchcard/<str:batchcardno>', views.editbatchcard, name="edit_batchcard"),
    path('newbatchcard/', views.newbatchcard, name="newbatchcard"),
    path('viewreceipe/<str:batchcardno>', views.viewreceipe,name = "viewreceipe"),
    path('productrecipe/<str:batchcardno>', views.productrecipe, name="productrecipe"),
    path('viewchemical/<str:batchcardno>', views.viewchemical, name="viewchemical"),
    path('completebatchcard/<str:batchcardno>', views.completebatchcard, name="completebatchcard"),

    path('profile', views.profile, name="profile"),
    path('group', views.group, name="group"),

    path('reports', views.reports, name="reportspage"),

    path('view_sop', views.view_sop, name="view_sop"),
    path('create_sop', views.create_sop, name="create_sop"),
    path('detail_sop/<str:id>', views.detail_sop, name="detail_sop"),

    path('task', views.task, name="task page"),
    path('create_task', views.create_task, name="createtask"),
    path('edit_task/<int:id>', views.edit_task, name="edit_task"),

    path('alerts', views.alerts, name="alerts page"),

    path('groupsecur', views.group_sec, name="NIV DAS Group Security Page"),
    path('register', views.user_register, name="NIVDAS Register page"),

    path('sample', views.sample, name="sample page"),
    path('ajax_test', views.ajax_test, name="ajax_test"),

    path('packaging', views.packaging, name="packaging"),
    path('newplanpackaging', views.newplanpackaging, name="newplanpackaging"),
    path('directpackaging', views.directpackaging, name="directpackaging"),
    path('newproduction/<str:packagecardno>', views.newproduction, name="newproduction"),
    path('newpackaging/<str:packagecardno>', views.newpackaging, name="newpackaging"),
    path('editpackaging/<str:packagecardno>', views.editpackaging, name="editpackaging"),
    path('viewpackaging/<str:packagecardno>', views.viewpackaging, name="viewpackaging"),
    path('completepackagecard/<str:packagecardno>', views.completepackagecard, name="completepackagecard"),

    path('maintenance', views.maintenance, name="maintenance page"),
    path('planmaintenance', views.planmaintenance, name="planmaintenance"),
    path('editmaintenance/<int:id>', views.editmaintenance, name="editmaintenance"),
    path('deletemaintenance/<int:id>',views.deletemaintenance, name="deletemaintenance"),
    path('pdf/',views.editpackaging),
    path('newmanpowerplanning', views.newmanpowerplanning, name="newmanpowerplanning"),
    path('manpowerplanning', views.manpowerplanning, name="manpowerplanning"),

    path('newproductionplanning', views.newproductionplanning, name="newproductionplanning"),
    path('productionplanning', views.productionplanning, name="productionplanning"),

    path('productionreport', views.productionreport, name="productionreport"),

    path('printbatchcard', views.printbatchcard, name="printbatchcard"),

    path('linenumber', views.linenumber, name="linenumber"),
]

if settings.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
