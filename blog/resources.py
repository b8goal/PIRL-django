from import_export import resources
from .models import M1_Train_data


class TrainResource(resources.ModelResource):
    class Meta:
        model = M1_Train_data