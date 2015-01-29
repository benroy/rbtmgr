class RallyTeam(object):
	"""docstring for RallyTeam"""
	def __init__(self, rally, projects=None, memberEmails=None):
		super(RallyTeam, self).__init__()
		self.rally = rally
		self.members = []

		if projects == None and memberEmails == None:
			raise "Must specify either projects or members"

		if memberEmails != None:
			for memberEmail in memberEmails:
				response = rally.get('User', username=memberEmail)
				user = response.next()
				if user:
					self.members.append(user)
				else:
					raise "something's not right"
					
				

		if projects != None:
			raise "Uh...heh... someone should add support for getting users from projects"


	def members(self):
		return self.members

	def stories(self, members=None, iteration=None, state=None):
		return []

	def points(self, members=None, iteration=None, state=None):
		return 0

	def blockedStories(self, members=None, iteration=None):
		return []	