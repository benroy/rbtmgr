class RallyTeam(object):
    """docstring for RallyTeam"""
    def __init__(self, rally, memberEmails):
        super(RallyTeam, self).__init__()
        self.__rally = rally
        self.__members = []

        if memberEmails is None:
            raise "Must specify members"

        for memberEmail in memberEmails:
            self.addMember(memberEmail)

    def addMember(self, memberEmail):
        users = self.__rally.getUserInfo(username=memberEmail)

        if len(users) == 1:
            self.__members.append(users[0])
        else:
            raise "something's not right"

    def members(self):
        return self.__members
