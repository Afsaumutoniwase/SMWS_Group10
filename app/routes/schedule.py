from flask import request
from flask_restful import Resource, reqparse
from app import api
from app.models import Schedule
from datetime import datetime

# Mock data for scheduling (replace with your actual scheduling logic)
schedules = [
    {
        'id': 1,
        'bin_id': 1,
        'collection_date': '2024-06-25T10:00:00',
        'collection_frequency': 'Weekly',
        'collection_status': 'Scheduled',
        'responsible_user_id': 1
    },
    {
        'id': 2,
        'bin_id': 2,
        'collection_date': '2024-06-26T11:00:00',
        'collection_frequency': 'Monthly',
        'collection_status': 'Scheduled',
        'responsible_user_id': 2
    }
]

parser = reqparse.RequestParser()
parser.add_argument('bin_id', type=int, required=True, help='Bin ID is required')
parser.add_argument('collection_date', type=str, required=True, help='Collection date is required')
parser.add_argument('collection_frequency', type=str, required=True, help='Collection frequency is required')
parser.add_argument('responsible_user_id', type=int, required=True, help='Responsible user ID is required')

class ScheduleResource(Resource):
    def get(self, schedule_id):
        for schedule in schedules:
            if schedule['id'] == schedule_id:
                return schedule, 200
        return {'message': 'Schedule not found'}, 404

    def post(self):
        args = parser.parse_args()
        new_schedule = {
            'id': len(schedules) + 1,
            'bin_id': args['bin_id'],
            'collection_date': args['collection_date'],
            'collection_frequency': args['collection_frequency'],
            'collection_status': 'Scheduled',
            'responsible_user_id': args['responsible_user_id']
        }
        schedules.append(new_schedule)
        return new_schedule, 201

api.add_resource(ScheduleResource, '/api/schedule', '/api/schedule/<int:schedule_id>')
