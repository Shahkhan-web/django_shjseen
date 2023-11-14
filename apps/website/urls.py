from django.urls import path

from apps.website import views

urlpatterns = [
    path(
        '',
        views.LandingPageView.as_view(),
        name='landing_page'
    ),
    path(
        'aboutUs',
        views.aboutUs.as_view(),
        name='aboutUs'
    ), 
    path(
        'contact',
        views.contact.as_view(),
        name='contact'
    ), 
    path(
        'media',
        views.media.as_view(),
        name='media'
    ),path(
        'award',
        views.award.as_view(),
        name='award'
    ),path(
        'terms',
        views.terms.as_view(),
        name='terms'
    ),
    path(
        'participate',
        views.ParticipatePageView.as_view(),
        name='participate_page'
    ),
    path(
        'register-participant',
        views.register_participant,
        name='register_participant'
    ),
    path(
        'participate-confirmation',
        views.ParticipateConfirmationPageView.as_view(),
        name='participate_confirmation_page'
    )
]
