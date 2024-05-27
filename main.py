import json, unittest, datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    l = jsonData1["location"].split("/")
    location = {}
    location["country"] = l[0]
    location["city"] = l[1]
    location["area"] = l[2]
    location["factory"] = l[3]
    location["section"] = l[4]
    jsonData1["location"] = location

    jsonData1["data"] = {
        "status": jsonData1["operationStatus"],
        "temperature": jsonData1["temp"]
    }
    jsonData1.pop("operationStatus")
    jsonData1.pop("temp")
    # print(jsonData1)
    return jsonData1
    # return NotImplemented


def convertFromFormat2(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    id = jsonData2["device"]["id"]
    deviceType = jsonData2["device"]["type"]
    jsonData2.pop("device")
    timestamp = jsonData2["timestamp"]
    date = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    timestamp = ((date - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
    # timestamp = timestamp[:-2]
    data = jsonData2["data"]
    location = {
        "country": jsonData2["country"],
        "city": jsonData2["city"],
        "area": jsonData2["area"],
        "factory": jsonData2["factory"],
        "section": jsonData2["section"]
    }
    jsonDatax = {
        "deviceID": id,
        "deviceType": deviceType,
        "timestamp": timestamp,
        "location": location,
        "data": data
    }
    return jsonDatax
    # return NotImplemented


def main(jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):

        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 1 failed')

    def test_dataType2(self):

        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 2 failed')


if __name__ == '__main__':
    unittest.main()
