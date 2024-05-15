from bills.forms import BillsForm, UploadFileBillForm
from bills.models import Bill, BillType
from buildings.models import Building


title = [{"title": "UBT", "url_name": "buildings:index"}]


class BuildingDataMixin:
    template_name = "buildings/building.html"
    paginate_by = 10
    title_page = None
    category_selected = None
    extra_context = {}

    def __init__(self):
        self.kwargs = None
        if self.title_page:
            self.extra_context["title"] = self.title_page

        if self.category_selected is not None:
            self.extra_context["category_selected"] = self.category_selected

    def get_mixin_context(self, context, **kwargs):
        context["menu"] = title
        context.update(kwargs)
        return context

    def get_building(self):
        building_slug = self.kwargs["building_slug"]
        return Building.objects.get(slug=building_slug)

    def get_common_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        building = self.get_building()
        context["building"] = building
        context["bill_types"] = BillType.objects.all()
        context["total_sum"] = Bill.total_sum(
            building_slug=self.get_building().slug
        )
        context["form"] = BillsForm()
        context["file_form"] = UploadFileBillForm()
        return context
