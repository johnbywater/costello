from eventsourcing.domain.model.aggregate import BaseAggregateRoot


class Disease(BaseAggregateRoot):
    def __init__(self, *, name, **kwargs):
        super(Disease, self).__init__(**kwargs)
        self.name = name

    def set_earliest_infectiousness_onset(self, days):
        pass

    def set_latest_symptom_onset(self, days):
        pass
