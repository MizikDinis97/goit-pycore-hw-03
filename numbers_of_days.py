from datetime import datetime

def get_days_from_today(date):
	input_data = datetime.strptime(date, "%Y-%m-%d").date()
	today = datetime.today().date()
	the_delta = today - input_data
	return (the_delta.days)
print(get_days_from_today("2026-10-14"))