from datetime import datetime, timedelta
import random

measurements = [
    (28, [(0, 4)]),
    (1, [(1, 5)]),
    (1, [(1, 5)]),
    (1, [(0, 600)]),
    (7, [
        (1, 5),
        (1, 5),
        (1, 5),
        (1, 5),
        (1, 5),
        (0, 100)
    ])
]

startDate = datetime(2020, 10, 1)

measurementRecordText = ''
dataPointRecordText = ''

nextMeasurementRecordId = 1

for measurementId, (frequency, dataPoints) in enumerate(measurements):
    measurementId += 1

    nextDate = startDate

    while nextDate < datetime.today():
        measurementRecordText += "('{0:04d}-{1:02d}-{2:02d}', {3}, 1, '123456789'),\n".format(nextDate.year, nextDate.month, nextDate.day, measurementId)

        for dataPointId, (minimum, maximum) in enumerate(dataPoints):
            dataPointId += 1

            dataPointRecordText += "({}, {}, {}.0, {}),\n".format(measurementId, dataPointId, random.randint(minimum, maximum), nextMeasurementRecordId)

        nextMeasurementRecordId += 1
        nextDate += timedelta(days=frequency)

print(measurementRecordText)

print()
print()

print(dataPointRecordText)