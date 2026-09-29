def generate_continous_array(max_len):
    return range(0, max_len)



if __name__ == "__main__":
    ### options
    
    I_facings = 32
    I_sequnce_array = generate_continous_array(I_facings)
    #sequnce_array = [2,4,6,7]

    I_sub_sequence_length = 5
    I_need_reverse = True
    use_reverse = False

    I_start_sequence_index = 30



    ### program
    result_array = []
    facing_array = []
    current_index = I_start_sequence_index
    iter_counter = 0
    sub_sequence_counter = 0

    if I_start_sequence_index >= len(I_sequnce_array):
        print("start_sequence_index larger than overall sequence length!!!")
    else:
        while iter_counter < I_facings:
            
            while sub_sequence_counter < I_sub_sequence_length:
                facing_array.append(I_sequnce_array[current_index])
                if not use_reverse:
                    current_index = (current_index + 1 + len(I_sequnce_array)) % len(I_sequnce_array)
                else:
                    current_index = (current_index - 1 + len(I_sequnce_array)) % len(I_sequnce_array)
                sub_sequence_counter+=1

            if I_need_reverse:
                if not use_reverse:
                    current_index = (current_index - 2 + len(I_sequnce_array)) % len(I_sequnce_array)
                else:
                    current_index = (current_index + 2 + len(I_sequnce_array)) % len(I_sequnce_array)
                    
                while sub_sequence_counter < I_sub_sequence_length * 2 - 2:
                    facing_array.append(I_sequnce_array[current_index])
                    if not use_reverse:
                        current_index = (current_index - 1 + len(I_sequnce_array)) % len(I_sequnce_array)
                    else:
                        current_index = (current_index + 1 + len(I_sequnce_array)) % len(I_sequnce_array)                        
                    sub_sequence_counter+=1

            sub_sequence_counter = 0
            iter_counter+=1
            current_index = (I_start_sequence_index + iter_counter) % len(I_sequnce_array)
            result_array += facing_array
            facing_array.clear()
            #result_array.append('<>')## -- debug

        print(result_array)
        print(len(result_array))
        #print('and its reverse(): \n')
        #result_array.reverse()
        #print(result_array)


    
