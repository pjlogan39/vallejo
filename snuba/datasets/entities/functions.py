from snuba.datasets.entity import Entity
from snuba.datasets.plans.single_storage import SingleStorageQueryPlanBuilder
from snuba.datasets.storages import StorageKey
from snuba.datasets.storages.factory import get_writable_storage
from snuba.pipeline.simple_pipeline import SimplePipelineBuilder
from snuba.query.validation.validators import EntityRequiredColumnValidator


class FunctionsEntity(Entity):
    def __init__(self) -> None:
        functions_storage = get_writable_storage(StorageKey.FUNCTIONS)
        schema = functions_storage.get_table_writer().get_schema()

        super().__init__(
            storages=[functions_storage],
            query_pipeline_builder=SimplePipelineBuilder(
                query_plan_builder=SingleStorageQueryPlanBuilder(
                    storage=functions_storage
                )
            ),
            abstract_column_set=schema.get_columns(),
            join_relationships={},
            writable_storage=functions_storage,
            validators=[
                EntityRequiredColumnValidator({"org_id", "project_id"}),
            ],
            required_time_column="received",
        )
