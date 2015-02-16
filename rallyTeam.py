"""docstring for rallyTeam module."""


class RallyTeam(object):

    """docstring for RallyTeam class."""

    def __init__(self, rally, member_emails):
        """docstring for __init__."""
        super(RallyTeam, self).__init__()
        self.__rally = rally
        self.__members = []

        if member_emails is None:
            raise "Must specify members"

        for member_email in member_emails:
            self.add_member(member_email)

    def add_member(self, member_email):
        """docstring for add_member method."""
        users = self.__rally.getUserInfo(username=member_email)

        if len(users) == 1:
            self.__members.append(users[0])
        else:
            raise "something's not right"

    def members(self):
        """docstring for members method."""
        return self.__members
