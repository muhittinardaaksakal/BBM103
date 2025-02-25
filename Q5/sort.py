import sys
def is_already_sorted_insertion(unsorted_list ):
    # Check if the list is already sorted
    if all(unsorted_list[i] <= unsorted_list[i + 1] for i in range(len(unsorted_list) - 1)):
        return True



def is_already_sorted_bubble(unsorted_list ):
    # Check if the list is already sorted
    if all(unsorted_list[i] <= unsorted_list[i + 1] for i in range(len(unsorted_list) - 1)):
        return True
def bubblesort(unsorted_list, output_bubble_file):
    step = 0
    for pass_counter in range(len(unsorted_list) - 1, 0, -1):
        check = True
        for i in range(pass_counter):
            if unsorted_list[i] > unsorted_list[i + 1]:
                # Swap the elements if they are in the wrong order
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                check = False
        step += 1
        if check:
            break

        # Write the situation of the list after each pass to the bubble output file
        output_bubble_file.write("Pass {}: ".format(step))
        for j in unsorted_list:
            if unsorted_list.index(j) == len(unsorted_list) - 1:
                output_bubble_file.write(str(j))
            else:
                output_bubble_file.write(str(j) + " ")
        if all(unsorted_list[i] <= unsorted_list[i + 1] for i in range(len(unsorted_list) - 1)):
            break
        else:
            output_bubble_file.write("\n")




def insertion_sort(copied_unsorted_list, output_insertion_file):
    for index in range(1, len(copied_unsorted_list)):
        step = index
        current_value = copied_unsorted_list[index]
        current_index = index
        while current_index > 0 and copied_unsorted_list[current_index - 1] > current_value:
            # Shift elements to the right to make space for the current value
            copied_unsorted_list[current_index] = copied_unsorted_list[current_index - 1]
            current_index -= 1
        copied_unsorted_list[current_index] = current_value


        # Write the situtation of the list after each pass to the insertion output file
        output_insertion_file.write("Pass {}: ".format(step))

        for j in copied_unsorted_list:
            if copied_unsorted_list.index(j) == len(copied_unsorted_list) - 1:
                output_insertion_file.write(str(j))
            else:
                output_insertion_file.write(str(j) + " ")

        if all(copied_unsorted_list[i] <= copied_unsorted_list[i + 1] for i in range(len(copied_unsorted_list) - 1)):
            break
        else:
            output_insertion_file.write("\n")


def main():
    input_file = open(sys.argv[1], "r")
    output_bubble_file = open(sys.argv[2], "w")
    output_insertion_file = open(sys.argv[3], "w")
    # Read input file and convert the string values to integers
    unsorted_list_string = input_file.read().split()
    unsorted_list = []
    for i in unsorted_list_string:
        j = int(i)
        unsorted_list.append(j)
    coppied_unsorted_list = unsorted_list.copy()
    # Check if the list is already sorted or has only one element
    if is_already_sorted_bubble(unsorted_list) or len(unsorted_list)<=1:
        output_bubble_file.write("Already sorted!")
        output_bubble_file.flush()
        output_bubble_file.close()
    else:
        bubblesort(unsorted_list, output_bubble_file)
        output_bubble_file.flush()
        output_bubble_file.close()
    # Check if the list is already sorted or has only one element
    if len(unsorted_list) <=1:
        output_insertion_file.write("Already sorted!")
        output_insertion_file.flush()
        output_insertion_file.close()
    else:
        insertion_sort(coppied_unsorted_list, output_insertion_file)
        output_insertion_file.flush()
        output_insertion_file.close()



if __name__ == "__main__":
    main()