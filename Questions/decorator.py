def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m >=75:
                print("Distinction")
        result_function(marks)
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m >= 35:
            pass
        else:
            print('Fail')
    else:
        print("PASS")

result([46,56,78,60,85])