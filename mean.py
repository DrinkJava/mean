def mean(num_list):
    if(type(num_list) != type([])):
        print("Fail")
        raise Exception("Type of num_list is not a list")
    for num in num_list:
        if(complex(num)):
            return NotImplemented
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return Infinity
    except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined. Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
# your except clause here:
                                            
