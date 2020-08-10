from locust import TaskSet, HttpUser, task, between


class TravelCalendar(TaskSet):
    """Task set class for testing functionality related to travel calendar"""

    @task(2)
    class BrowseCalendar(TaskSet):

        @task(2)
        def filters_setup(self):
            self.client.get("/")
            print("Setting up filters on calendar")

        @task(5)
        def check_existing_events(self):
            print("Browsing existing entries in the calendar")

        @task(1)
        def stop(self):
            self.interrupt(True)
            print("Stopping to browse calendar")

    @task(1)
    class UpdateCalendar(TaskSet):

        @task(4)
        def create_event(self):
            print("Creating calendar entry as user could not find existing")

        @task(2)
        def edit_event(self):
            print("Editing my own calendar entry")

        @task(1)
        def stop(self):
            self.interrupt(True)
            print("Stopping to edit calendar")


class DeviOnWheelsWebUser(HttpUser):
    """Web user to simulate load of web based user"""

    wait_time = between(2, 3)
    host = "https://devilonwheels.com"

    # use tasks attribute to define tasks as a list of defined functions or Taskset classes
    tasks = [TravelCalendar]

    # use dictionary based tasks attribute to specify weights
    # tasks = {browse_homepage: 8, create_calendar_event: 1}
