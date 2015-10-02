import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
import logging

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator('ignore_empty')

class IframeviewPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IResourceView, inherit=True)
    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'iframeview')


    def info(self):
        return {'name': 'iframeview',
                'title': 'iframe',
                'icon': 'picture',
                'schema': {'image_url': [ignore_empty, unicode]},
                'always_available': True,
                'default_title': 'iframe',
                }

    def can_view(self, data_dict):
        #return (data_dict['resource'].get('format', '').lower()
        #        in DEFAULT_IMAGE_FORMATS)
        return True

    def view_template(self, context, data_dict):
        return 'iframe_view.html'

    def form_template(self, context, data_dict):
        return 'iframe_form.html'
