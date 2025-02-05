{
    'name': 'PostItOdoo',
    'version': '0.1a',
    'summary': 'Post en redes sociales',
    'description': 'Programa los post en tus redes sociales!',
    'category': 'Tools',
    'author': 'Cheick Sow, David Villamor',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/social_data.xml',
        'views/social_account_views.xml',
        'views/social_campaign_views.xml',
        'views/social_comment_views.xml',
        'views/social_hashtag_views.xml',
        'views/social_metric_views.xml',
        'views/social_post_views.xml',
        'views/social_schedule_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}