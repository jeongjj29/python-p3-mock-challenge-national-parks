import re


def is_valid_date_format(date):
    pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December) [1-9]|[12][0-9]|3[01](st|nd|rd|th)$"
    match = re.match(pattern, date)
    return bool(match)


class NationalPark:

    all = []

    def __init__(self, name):
        self._name = name
        NationalPark.all.append(self)

    @classmethod
    def most_visited(cls):
        visits = {}
        for national_park in NationalPark.all:
            visits[national_park] = len(national_park.trips())
        return max(visits, key=visits.get)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        else:
            # raise Exception
            return

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        if self.total_visits() == 0:
            return 0
        visits = {}
        for visitor in self.visitors():
            visits[visitor] = len(
                [trip for trip in visitor.trips() if trip.national_park == self]
            )
        return max(visits, key=visits.get)


class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            # raise Exception
            return

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            # raise Exception
            return

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if (
            isinstance(start_date, str)
            and len(start_date) >= 7
            and is_valid_date_format(start_date)
        ):
            self._start_date = start_date
        else:
            # raise Exception
            return

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if (
            isinstance(end_date, str)
            and len(end_date) >= 7
            and is_valid_date_format(end_date)
        ):
            self._end_date = end_date
        else:
            # raise Exception
            return


class Visitor:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            # raise Exception
            return

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])
