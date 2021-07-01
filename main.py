
import time
start_time = time.time()
import json

#open and read json file
f = open('run_results.json',)
data = json.load(f)
f.close()

passed = []
failed = []
num = 0


#output individual json files for each test
for i in data['results']:
    #prints/log outupt for successful tests
    test_i = json.dumps(i, indent=len(i))
    if i['status'] == 'pass':
        print(num, '=', test_i)
        passed.append(1)
    #if a fail adds one to keep count
    else:
        failed.append(1)
    num = num + 1
    #create json file for all individual outputs
    filename = "test" + str(num) + ".json"
    with open(filename, "w") as outfile:
        json.dump(i, outfile)

print('change')
print(len(passed), 'tests passed and', len(failed), 'failed, so there were', len(passed) + len(failed), 'tests in total!')


executionTime = (time.time() - start_time)
print('This took', executionTime, 'seconds to run!')
