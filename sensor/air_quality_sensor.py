class AirQualitySensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.air_quality_data = None

    def read_sensor(self):
        # Code to interact with air quality sensor hardware
        pass

    def get_air_quality(self):
        self.air_quality_data = self.read_sensor()
        return self.air_quality_data

    def display_air_quality(self):
        if self.air_quality_data:
            print(f"Air Quality Data for Sensor {self.sensor_id}: {self.air_quality_data}")
        else:
            print("No data available. Please read the sensor first.")