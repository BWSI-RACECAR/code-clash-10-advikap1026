import itertools
 
class Solution:
    def create_action_dict(self, num_players, num_actions):
            #type num: two integer values
            #return type: int dictionary
            
            #TODO: Write code below to return a dictionary with the solution to the prompt.
            dict = {}
           # count = 0 
            for i in range(num_actions**num_players):
                dict[i] = ()
                for j in range(num_players):
                     dict[i] += (i//(num_actions**j)%num_actions,)
                dict[dict[i]] = i
            return dict 

            # originalTup = ()
            # for i in range(0,num_actions):
            #      originalTup.append(i)
            # comb = list(itertools.combinations_with_replacement(originalTup,num_actions))
            # for i in range(len(comb)):
            #      dict[i] = comb[i]
            #      dict[comb[i]] = i
            # return dict 
            # pass
    
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