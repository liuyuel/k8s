import requests
import json

if __name__ == '__main__':
    pageNum = 1
    pageSize = 300
    param = {
        "query": "query queryTraces($condition: TraceQueryCondition) {\n  data: queryBasicTraces(condition: $condition) {\n    traces {\n      key: segmentId\n      endpointNames\n      duration\n      start\n      isError\n      traceIds\n    }\n    total\n  }}",
        "variables": {"condition": {"queryDuration": {"start": "2022-09-26 10", "end": "2022-09-27 10", "step": "HOUR"},
                                    "traceState": "ERROR",
                                    "paging": {"pageNum": pageNum, "pageSize": pageSize, "needTotal": True},
                                    "queryOrder": "BY_START_TIME",
                                    "serviceId": "Mzflj4LlsZXllYbnjq/looM6OkV4aGliaXRpb25TZWF0QXJyYW5nZU1T.1"}}}
headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "keep-alive", "Content-Length": "538",
           "Content-Type": "application/json;charset=UTF-8", "Host": "10.32.37.50:8080",
           "Origin": "chrome-extension://cgpnoendcibcgokcokfgcklbemlcbgih",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"}
api = set()
while True:
    data = requests.post("http://10.32.37.50:8080/graphql", json=param, headers=headers)
    res = json.loads(data.text).get('data').get('data')
    # print(res.get('traces'))
    api = set.union(api, set(item.get('endpointNames')[0] for item in res.get('traces')))
    if res.get('total') <= pageNum * pageSize:
        break
    pageNum = pageNum + 1
print(api)
print(pageNum)
# {'/api/ordinaryCompanyDemandRecord/getListPage', '/api/ordinaryArrange/getOrdinaryArrangeCompanyRecord',
#  '/api/numforOnlineService/getOrdinaryArrangeCompanyResult', '/api/newthemePublish/publish/add'}


'''
/**
 * Java 类作用描述 服务申请明细
 *
 * @author :    yueliuk 170115
 * @version :   1.0
 * @apiNote :   ServiceApplyDetailDTO 类作用描述
 * @date :      2021/1/11 15:25
 * @see ServiceApplyDetailDTO
 * @since :     2021/1/11 15:25
 */

/ **
*字段含义说明
服务项目名id
*
* @ date
2020 / 4 / 17
15: 05
* /
/**
   * 方法实现说明  计算押金金额和服务费用金额
   *
   * @param
   * @return "def result=''; 	def params=\"${_1}\".replaceAll('[\\\\[|\\\\]|\\\\s]', '').split(',').toList(); 	for(i = 0; i < params.size(); i++) {if(params[i] != '')result+='* @param ' + params[i] + ': ' + ((i < params.size() - 1) ? '\\n ' : '')};  	return result == '' ? null : '\\r\\n ' + result"
   * @throws
   * @author yueliuk 170115
   * @date 2020/5/21 15:30
   */
'''