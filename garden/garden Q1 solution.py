import json
class Solution:
    def read_json(self):
        filename=input('Enter your json file name:')
        with open(filename, 'r',encoding='utf8') as rf:
            data = json.load(rf)
        Input_list=[]
        def Input(data):

            for i in data:
                if 'items' in i:
                    for a in i['items']:
                        if 'items' not in a:
                            Input(i['items'])
                #else:
                    #Input_list.append({"id":i['id'],"title":i['title']})
            return Input_list
        return Input(data)
    def output_answer(self):
        dict=self.read_json()

        l=[]
        for i in dict:
            print(i)

#AttributeError: 'Solution' object has no attribute 'Input'
#while又return一旦有'items'他就一直往內跑，回不去繼續i迭代了

if __name__=='__main__':
    print(Solution().read_json())
#print(Solution().Input("[{'id': '1', 'title': '領導力', 'items': [{'id': '1.1', 'title': '溝通能力'}, {'id': '1.2', 'title': '判斷能力', 'items': [{'id': '1.2.1', 'title': '分析能力'}, {'id': '1.2.2', 'title': '應變能力'}, {'id': '1.2.3', 'title': '觀察力'}]}]}, {'id': '2', 'title': '創作力', 'items': [{'id': '2.1', 'title': '創意'}, {'id': '2.2', 'title': '計畫', 'items': [{'id': '2.2.1', 'title': '資料收集'}, {'id': '2.2.2', 'title': '企劃', 'items': [{'id': '2.2.2.1', 'title': '企劃書'}, {'id': '2.2.2.2', 'title': '簡報'}]}]}, {'id': '2.3', 'title': '實作能力'}]}]')"))