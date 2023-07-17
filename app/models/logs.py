from app.services.application.query.logs_query import LogsQuery
from app.types.logs import LogInfo

class Logs():
	def __init__(self, user_id, problem_cd):
		self.user_id = user_id
		self.problem_cd = problem_cd

		self.adding = []
		self.removing = []

	def add_log(self, log_info:LogInfo):
		self.adding.append(log_info)

	def get_adding(self):
		return self.adding

	def get_logs(self, param, session):
		pass

class FrontEndLogs(Logs):
	def get_logs(self, param, session):
		return LogsQuery.get_front_end_logs(param, session)

class BackEndLogs(Logs):
	def get_logs(self, param, session):
		return LogsQuery.get_back_end_logs(param, session)
