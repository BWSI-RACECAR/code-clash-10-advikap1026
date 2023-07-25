import itertools 
 
class Solution:
    def create_action_dict(self, num_players, num_actions):
            #type num: two integer values
            #return type: int dictionary
            
            #TODO: Write code below to return a dictionary with the solution to the prompt.
            dict = {}
            count = 0 
            comb = [i for i in product(range(0,num_actions), repeat = num_actions)]
            for i in range(len(comb)):
                 dict[i].append(comb[i])
            return dict 
            pass
    
def main():
    input1 = input()
    input1= int(input1)
    input2= input()
    input2=int (input2)
    tc1 = Solution()
    ans = tc1.create_action_dict(input1, input2)
    print(ans)

if __name__ == "__main__":
    main()