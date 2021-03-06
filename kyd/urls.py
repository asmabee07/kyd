"""kyd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.conf.urls import url
from dashboard.views import DashboardView
from kyd_dashboard.views import KYDDashboardView, FeatureOne, FeatureTwo, FeatureThree, FeatureFour, FeatureSix
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='home'),
    url(r'^kyd_dashboard$', KYDDashboardView.as_view(), name='kyd_dashboard'),
    url(r'^kyd_dashboard/feature1$', FeatureOne.as_view(), name='feat1'),
    url(r'^kyd_dashboard/feature2$', FeatureTwo.as_view(), name='feat2'),
    url(r'^kyd_dashboard/feature3$', FeatureThree.as_view(), name='feat3'),
    url(r'^kyd_dashboard/feature4$', FeatureFour.as_view(), name='feat4'),
    url(r'^kyd_dashboard/feature5$', FeatureSix.as_view(), name='feat5'),

    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login_request, name='login'),
    url(r'^logout/', views.logout_request, name='logout'),


    # url(r'logout', views.logout_request, name="logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
