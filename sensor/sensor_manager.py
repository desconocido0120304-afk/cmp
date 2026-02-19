# IoT Sensor Management

class SensorManager:
    def __init__(self):
        self.sensors = {}

    def add_sensor(self, sensor_id, sensor_data):
        self.sensors[sensor_id] = sensor_data
        print(f'Sensor {sensor_id} added.')

    def remove_sensor(self, sensor_id):
        if sensor_id in self.sensors:
            del self.sensors[sensor_id]
            print(f'Sensor {sensor_id} removed.')
        else:
            print(f'Sensor {sensor_id} not found.')

    def get_sensor_data(self, sensor_id):
        return self.sensors.get(sensor_id, 'Sensor not found.')

    def list_sensors(self):
        return self.sensors.keys()