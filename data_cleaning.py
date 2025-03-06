"""
COMP 614
Homework 2: Statistics
"""

import math

def arithmetic_mean(data):
    """
    Given a list of numbers representing a data set, computes and returns 
    the arithmetic mean of the data set.
    
    Input: data - a list of number
    
    Output: mean - average of the numbers
    """
    total = 0.0
    count = 0
    mean = 0
    
    for index in range(len(data)):
        if data[index] is not None and not isinstance(data[index], str) :
            total += data[index]
            count += 1
            
    if len(data) > 0 and count > 0:
        mean = total/count
        return mean
    else:
        return None


def pop_variance(data):
    """
    Given a list of numbers representing a data set, computes and returns 
    the population variance of the data set.
    
    Input: data - a list of number
    
    Output: var - variance of data set
    """
    count = 0
    mean = arithmetic_mean(data)
    var = 0.0
    total = 0.0
    
    for index in range(len(data)):
        square = math.pow(data[index] - mean, 2)
        total += square
        count += 1
    
    if count>0:
        var = total/count
        return var
    
    return None


def std_deviation(data):
    """
    Given a list of numbers representing a data set, computes and returns 
    the standard deviation of the data set.
    
    Input: data - a list of number
    
    Output: std - standard variance of data set
    """
    if len(data) == 0:
        return None
    else:
        std = math.sqrt(pop_variance(data))
        return std


def moving_avg(data, num_days):
    """
    Given a list of numbers representing a data set and an integer representing
    a number of days, builds and returns a new list where the i-th element is 
    the average of the data over the input number of days starting at position
    i in the data list.
    
    Input:  data - a list of number
            num_days - number of days to average
    
    Output: avg - list of averages
    """
    avg = []
    
    if num_days > len(data):
        avg.append ( arithmetic_mean(data) )
        return avg
    elif num_days <= len(data) and num_days > 0:
    
        for index in range(len(data)):
            #len(data) - index limits the maximum index or else you will get out of range error
            if (len(data) - index) >= num_days:
                total = 0.0
                for day in range(num_days):
                    total += data[index+day]
                current_avg = total/num_days
                avg.append(current_avg)
        return avg
    else:
        return None

      
def clean_with_deletion(data):
    """
    Given a list of lists representing a data set, cleans the data by creating
    and returning a new list of lists that contains the same data, minus any 
    rows that were originally missing values (denoted by None). Should not 
    mutate the original list.
    
    Input: data - a list of lists of numbers
    
    Output: clean - a shorter or equal list of lists of numbers 
    """
    #start before first item
    new_row_num = -1
    clean = []
    print(data, 'eof')
    for row_index in range(len(data)):
        remove = False
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] is None:
                remove = True
        #create lst then append this lst to clean
        if remove == False:
            lst = []
            #assign values to this lst
            clean.append(lst)
            #new row index for list clean
            new_row_num += 1
            #append both column's values
            for col_index in range(len(data[row_index])):
                clean[new_row_num].append( data[row_index][col_index] )   
    return clean


def column_avgs(data):
    """
    Given a list of lists representing a data set, returns a new list where the
    i-th element is the arithmetic mean of the i-th column in the data set.
    
    Input: data - a list of lists of numbers
    
    Output: col_avgs - a list of column's averages 
    """
    col_avgs = []
    
    for col_index in range (len (data[0]) ):
        lst = []
        for row_index in range(len (data) ):
            lst.append ( data[row_index][col_index] )
        
        col_avgs.append( arithmetic_mean(lst) )
    return col_avgs


def clean_with_mean(data):
    """
    Given a list of lists representing a data set, cleans the data by creating
    and returning a new list of lists that contains the same data, but with
    any values that were originally missing (denoted by None) filled in with 
    the arithmetic mean of the corresponding column.
    
    Input: data - a list of lists of numbers
    
    Output: clean - a list of lists of numbers where the mean of column replaces None
    """
    clean = []
    for row_index in range(len(data)):
        #append new lists as rows for list clean
        lst = []
        clean.append(lst)
        
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] is None:
                list_avgs = column_avgs(data)
                print(list_avgs)
                clean[row_index].append( list_avgs[col_index]) 
            else:
                clean[row_index].append( data[row_index][col_index] )   
    return clean

