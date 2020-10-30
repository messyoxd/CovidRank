import random
import time


class Shell:

    @staticmethod
    def adapted_decrescent_insertion_sort(sortable_list, size, h) -> list:
        for i in range(h, size):
            pivo = sortable_list[i]
            j = i - h
            while j >= 0 and sortable_list[j][1] < pivo[1]:
                sortable_list[j+h] = sortable_list[j]
                j -= h
            sortable_list[j+h] = pivo
        return sortable_list

    @staticmethod
    def decrescent_shell(sortable_list, size) -> list:
        """
        Parameter: A list "sortable_list" with elements that have the same type
            and a int "size" with the number of elements of the list
        Return: A crescent sorted list 
        Brief: 

        """
        ##### sequencia de Knuth (1973) #####
        h = 1
        while h < size:
            h = 3 * h + 1
        h = int(h/3)
        #####################################
        # insertion adaptado para shell sort
        sortable_list = Shell.adapted_decrescent_insertion_sort(sortable_list, size, h)
        while h > 1:
            h = int(h/3)
            # insertion adaptado para shell sort
            sortable_list = Shell.adapted_decrescent_insertion_sort(
                sortable_list, size, h)
        return sortable_list

    @staticmethod
    def decrescent_shell_ciura(sortable_list, size) -> list:
        """
        Parameter: A list "sortable_list" with elements that have the same type
            and a int "size" with the number of elements of the list
        Return: A crescent sorted list 
        Brief: 

        """
        if size < 1751:
            ciura_sequence = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
            counter = 0
            h = 1
            while h < size:
                counter += 1
                h = ciura_sequence[counter]
            counter -= 1
            h = ciura_sequence[counter]
            # insertion adaptado para shell sort
            sortable_list = Shell.adapted_decrescent_insertion_sort(
                sortable_list, size, h)
            while h > 1:
                counter -= 1
                h = ciura_sequence[counter]
                # insertion adaptado para shell sort
                sortable_list = Shell.adapted_decrescent_insertion_sort(
                    sortable_list, size, h)
            return sortable_list
        else:
            raise Exception(
                "Only lists lower than 1750 elements can use this!")

    @staticmethod
    def worst_case(size):
        """
            Depende da sequencia de gaps. Para a sequencia de Knuth(1973) a complexidade
            temporal fica em Θ(n^1.5), com n sendo o numero de elementos da lista.
        """
        return random.shuffle(list(range(size)))


if __name__ == "__main__":
    s = 1000
    x = list(range(s))
    random.shuffle(x)
    # print(x)
    # print(Shell.crescent_shell(x, s))
    start = time.time()
    a=Shell.decrescent_shell(x, s)
    end = time.time()
    print(end - start)
    print(a)
    # print(Shell.crescent_shell_ciura(x, s))
