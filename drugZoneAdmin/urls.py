from rest_framework import routers
from django.urls import path, include
from drugZoneAdmin import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login', views.LoginFormView, name='login'),
    path('logout', views.LogOutView, name='logout'),
    # path('forgot_password', views.forgotPassword, name='forgot_password'),      # newly made view
    # path('recover_password', views.recoverPassword, name='recover_password'),      # newly made view
    # path('reset-password', views.ResetPassword, name='reset_password'),
    path('dashbord', views.dashbord, name = 'dashbord'),

    path('employee-add', views.employeeAdd, name='employee-add'),
    path('employee-list', views.employeeList, name='employee-list'),
    # path('get-vehicle/<int:pk>', views.GetAmbulanceView, name='get_vehicle'),
    # path('edit-vehicle', views.UpdateAmbulanceView, name='edit_vehicle'),
    # path('remove-crew-from-vehicle/<int:pk>', views.RemoveCrewAmbulanceAssosiation, name='remove_crew_from_vehicle'),


    # path('add-user', views.addCrewView, name='add_crew'),


    # path('edit-user/<int:pk>', views.GetUserById, name='edit_user'),
    # path('update-user', views.UpdateUser, name='update_user'),
    # path('user-list', views.GetUserListView, name='user_list'),
    # path('user-activation/<int:pk>', views.ActivateDeactivateCrewStatusView, name='user_activation'),

    # path('form-builder', views.formBuilder, name='form_builder'),
    # path('update-form/<int:pk>', views.updateDynamicFormView, name='update_form'),
    # path('delete-form/<int:pk>', views.DeleteFormView, name='delete_form'),
    # path('form-table', views.GetFormView, name='form_table'),

    # path('submitted-incident-list', views.GetSubmitedIncidentView, name='submitted_incident_list'),
    # path('pending-incident-list', views.GetPendingIncidentView, name='pending_incident_list'),
    # path('inprogress-calls-list', views.GetInProgressCallsView, name='inprogress_calls_list'),
    # path('pending-incident-detail/<int:pk>', views.GetPendingIncidentDetails, name='pending_incident_detail'),

    # path('add-incident', views.addIncidentView, name= 'add_incident'),
    # path('incident-detail/<int:pk>', views.GetIncidentDetailView, name='incident_detail'),
    # path('edit-incident/<int:pk>', views.EditIncidentView, name='edit_incident'),
    # path('delete-incident/<int:pk>', views.DeleteIncidentView, name='delete_incident'),
    # path('delete-submitted-call/<int:pk>', views.DeleteSubmitedCallView, name='delete_submitted_call'),
    # path('call-default-setting', views.CallDefaultSetting, name= 'call_default_setting'),


    # path('equipment-checklist/<int:pk>', views.EquipmentChecklistView, name='equipment_checklist'),
    # path('equipment-checklist-details/<int:pk>', views.GetEquipmentCheckDetailByDateView, name='equipment_checklist_details'),
    # path('vehicle-checklist/<int:pk>', views.VehicleChecklistView, name='vehicle_checklist'),
    # path('vehicle-checklist-details/<int:pk>', views.GetVehicleCheckDetailByDateView, name='vehicle_checklist_details'),

    # path('reported-incident-list',views.ReportedIncidentListView, name='reported_incident_list'),
    # path('delete-reported-incident/<int:pk>', views.DeleteReportedIncidentViev, name='delete_reported_incident'),
    # path('reported-incident-details/<int:pk>', views.ReportedIncidentDetailsViev, name='reported_incident_details'),


    # path('upload_static_files', views.UploadStaticFiles, name='upload_static_files'),
    # path('update_static_files/<int:pk>', views.updateStaticFileView, name='update_static_files'),
    # path('filestatic_list', views.StaticFilesList, name='filestatic_list'),
    # path('submitted-forms',views.SubmittedForms,name='submitted-forms'),
    # path('all-app-versions',views.all_api_versions,name = 'all-app-versions'),
    # path('add-app-versions',views.add_api_version,name = 'add-app-versions'),
    # path('delete-app/<int:pk>',views.delete_app,name = 'delete-app'),
    # path('edit-app/<int:pk>',views.update_app,name = 'edit-app')


    # path('logout', auth_views.auth_login, name='logout'),


]
