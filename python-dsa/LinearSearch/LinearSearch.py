from jovian.pythondsa import evaluate_test_cases #to test multiple test cases
from jovian.pythondsa import evaluate_test_case 

#linear search 
def search(cards, query):
    position = 0;
    for position in range(len(cards)):
        if cards[position] == query:
            return position
    return -1

def main():
    test = {
            'input' : {
                'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
                'query' : 7
                },
            'output' : 3
            }
    tests = []
    tests.append(test)
    tests.append({'input' : {'cards' : [], 'query' : 7}, 'output' : -1})
    evaluate_test_cases(search, tests)
    #evaluate_test_case(search,test)

if __name__ == "__main__":
    main()
