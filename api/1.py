import json


class ReportBean:
    def __init__(self, channel, version, result):
        self.channel = channel
        self.version = version
        self.result = result


    def __init__(self, success, fail, total, startType, detail):
        self.success = success
        self.fail = fail
        self.total = total
        self.startType = startType
        self.detail = detail


class ReportResultDetailBean:
    def __init__(self, component, success):
        self.component = component
        self.success = success

bean = ReportResultDetailBean("com.onexzgj.Activity1", True).__dict__
bean1 = ReportResultDetailBean("com.onexzgj.Activity2", False).__dict__

details = []
details.append(bean)
details.append(bean1)
print(details)
resultBean = ReportResultBean(100, 50, 150, "上架", details).__dict__

data2 = json.dumps(resultBean)

print(data2)

