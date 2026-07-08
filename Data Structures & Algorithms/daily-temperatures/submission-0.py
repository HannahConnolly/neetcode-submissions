class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp_stack = []
        output = [0] * len(temperatures)

        for id_temp, temp in enumerate(temperatures):

            if not temp_stack:
                temp_stack.append({'temp': temp, 'id_temp': id_temp})

            else:
                # destroy stack finding lower temps & setting in output
                while(temp_stack and temp_stack[-1]['temp'] < temp):
                    # set output temp days as difference in days in stack vs current
                    output[temp_stack[-1]['id_temp']] = id_temp - temp_stack[-1]['id_temp'] 
                    temp_stack.pop()
            
            temp_stack.append({'temp': temp, 'id_temp': id_temp})
                
        print(temp_stack)
        return output