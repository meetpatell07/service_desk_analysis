import pandas as pd
import numpy as np
from faker import Faker
import os


# Create the 'data' folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

fake = Faker()

data = []
for _ in range(1000):
    ticket_id = fake.uuid4()
    priority = np.random.choice(['Low', 'Medium', 'High'])
    issue_type = np.random.choice(['Software', 'Hardware', 'Network'])
    creation_date = fake.date_this_decade()
    resolution_time = np.random.randint(1, 100)
    status = np.random.choice(['Open', 'In Progress', 'Closed'])
    assigned_team = np.random.choice(['Team A', 'Team B', 'Team C'])

    data.append([ticket_id, priority, issue_type, creation_date, resolution_time, status, assigned_team])

df = pd.DataFrame(data, columns=['Ticket ID', 'Priority', 'Issue Type', 'Creation Date', 'Resolution Time', 'Status', 'Assigned Team'])
df.to_csv('data/service_desk_data.csv', index=False)
