title = [
    {'title': 'UBT', 'url_name': 'buildings:index'}
]


class BuildingDataMixin:
    template_name = 'buildings/building.html'
    paginate_by = 10
    title_page = None
    category_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.category_selected is not None:
            self.extra_context['category_selected'] = self.category_selected

    def get_mixin_context(self, context, **kwargs):
        context['menu'] = title
        context.update(kwargs)
        return context
