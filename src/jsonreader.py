
import time
start_time = time.time()
import json


def read_jsonfile(filename):
    f = open(filename, "r")
    data = json.load(f)
    f.close()
    return data

if __name__ == "__main__":
    pass
# open and read json file


    #passed = []
    #failed = []
    # num = 0
    #
    #
    # #output individual json files for each test
    # for i, r in enumerate(data['results'], start = 1):
    #     #prints/log outupt for successful tests
    #     test_r = json.dumps(r, indent=len(r))
    #     if r['status'] == 'pass':
    #         print(i, '=', test_r)
    #         passed.append(1)
    #     #if a fail adds one to keep count
    #     else:
    #         failed.append(1)
    #     #create json file for all individual outputs
    #     filename = f"./output_jsonfiles/test{i}.json"
    #     with open(filename, "w") as outfile:
    #         json.dump(r, outfile)
    #
    # print('change')
    # print(len(passed), 'tests passed and', len(failed), 'failed, so there were', len(passed) + len(failed), 'tests in total!')
    #
    #
    # executionTime = (time.time() - start_time)
    # print('This took', executionTime, 'seconds to run!')
